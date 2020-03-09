import dash_html_components as html
import dash_core_components as dcc


def get_layout_frame(some_arg):

    return html.Div(
        [
            html.H2("My app!"),
            dcc.Dropdown(
                id="selector-dd",
                options=[
                    {"label": c.upper(), "value": c.lower()} for c in some_arg
                ],
            ),
            html.H4(id="out-h4"),
        ]
    )
