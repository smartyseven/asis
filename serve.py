import http.server
import os
import sys

os.chdir('/Users/marcelo/Desktop/esc-asistencia')
port = int(os.environ.get('PORT', 7789))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('127.0.0.1', port), handler)
print(f'Serving on http://127.0.0.1:{port}', flush=True)
httpd.serve_forever()
