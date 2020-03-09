import dash

from mypackage.core.callbacks import decorate_app
from mypackage.core.layout import get_layout_frame

EXTERNAL_STYLESHEETS = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


def get_app(some_arg: str) -> dash.Dash:

    app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
    app.config["suppress_callback_exceptions"] = True
    app.title = "My app"

    app.layout = get_layout_frame(some_arg)

    decorate_app(app)

    return app
