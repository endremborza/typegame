import json
from typegame.core.question_class import Question


def handle_error(e, line, explanation):
    explanation.append("error in line: {}".format(line.strip()))
    explanation.append("{} -> {}".format(type(e).__name__, e))


def parse_snippet(snippet):
    code = []
    explanation = []
    alternates = ["error"]
    alt_line = "ALTERNATES = []"
    line = "None"
    has_error = False
    for line in snippet:
        if "ALTERNATES" in line:
            alt_line = line
        else:
            code.append(line)

    try:
        exec("".join(code), locals())
    except Exception as e:
        handle_error(
            e, code[e.__traceback__.tb_next.tb_lineno - 1], explanation
        )
        has_error = True

    exec(alt_line, locals())
    atypes = eval("[type(x).__name__ for x in ALTERNATES]", locals())
    alternates += atypes

    try:
        answer = eval("type({}).__name__".format(line.strip()), locals())
        answer_value = str(eval(line.strip(), locals()))
    except Exception as e:
        answer = "error"
        answer_value = "error"
        handle_error(e, line, explanation)

    if has_error:
        answer = "error"

    explanation.append("%s --> %s" % (line, answer_value))

    return Question(
        answer=answer,
        answer_value=answer_value,
        alternates=set(alternates + [answer]),
        _code_lines=code,
        _explanation_lines=explanation,
    )


def parse_notebook(nb_loc):
    return list(
        map(
            parse_snippet,
            [
                c["source"]
                for c in json.load(open(nb_loc, "r"))["cells"]
                if (c["cell_type"] == "code") and (len(c["source"]) > 0)
            ],
        )
    )
