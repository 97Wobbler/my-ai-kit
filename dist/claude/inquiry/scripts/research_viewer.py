#!/usr/bin/env python3
"""Serve only the packaged viewer on loopback; research files stay client-side."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import urllib.parse
import webbrowser

ASSETS = Path(__file__).resolve().parent.parent / "assets" / "research-viewer"
ALLOWED = {"/", "/index.html", "/app.js", "/styles.css", "/demo.json", "/build.json"}


class ViewerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        name = urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
        if name not in ALLOWED or not (ASSETS / ("index.html" if name == "/" else name[1:])).is_file():
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        name = urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
        if name not in ALLOWED:
            self.send_error(404)
            return
        super().do_HEAD()

    def end_headers(self):
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404)
        return None


def create_server(port=0):
    return ThreadingHTTPServer(("127.0.0.1", port), partial(ViewerHandler, directory=str(ASSETS)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--open", action="store_true", help="open in the system browser")
    args = parser.parse_args()
    with create_server(args.port) as server:
        url = f"http://127.0.0.1:{server.server_port}/"
        print(url, flush=True)
        print("Stop with Ctrl-C. Open a research JSON using the viewer's file picker.", flush=True)
        if args.open:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
