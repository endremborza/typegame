import dash
from dash.dependencies import Input, Output


def decorate_app(app: dash.Dash) -> None:
    @app.callback(
        Output("out-h4", "children"), [Input("selector-dd", "value")],
    )
    def update_leaderboard(val):
        return val
