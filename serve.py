#!/usr/bin/env python3
"""Local preview server. Sends no-store so edits always show up on reload —
python -m http.server sends no Cache-Control at all, which lets browsers apply
heuristic caching and quietly serve a stale stylesheet."""
import http.server, socketserver, sys

class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()
    def send_header(self, k, v):
        if k == "Last-Modified":
            return
        super().send_header(k, v)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8788
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", port), H) as httpd:
    print(f"serving on http://127.0.0.1:{port}")
    httpd.serve_forever()
