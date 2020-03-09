from mypackage.core.app import get_app
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--port", "-p", help="define port", default=6999, type=int)
parser.add_argument("--host", "-H", help="define host", default="0.0.0.0")
parser.add_argument("--some-arg", help="some argument", default="fing")


if __name__ == "__main__":
    args = parser.parse_args()
    app = get_app(some_arg=args.some_arg)
    app.run_server(port=args.port, host=args.host, debug=True)
