#!/usr/bin/env python3
"""Serve the site locally for testing, exactly as GitHub Pages serves /docs.

Usage:
    python3 serve.py [port]

Defaults to port 8000. Open http://localhost:<port>/ in a browser.
"""
import http.server
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent / "docs"


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

    handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(
        *args, directory=str(DOCS_DIR), **kwargs
    )

    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        url = f"http://localhost:{port}/"
        print(f"Serving {DOCS_DIR} at {url}  (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")


if __name__ == "__main__":
    main()
