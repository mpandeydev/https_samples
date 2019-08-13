import http
import ssl
import time

from urllib.parse import urlparse, parse_qs
from io import BytesIO

from http.server import HTTPServer, BaseHTTPRequestHandler




class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        path = bytes('path=%s\n'%self.path, 'utf-8')
        self.wfile.write(path)
        
        query_components = parse_qs(urlparse(self.path).query)
        path_args = bytes('query components=%s\n'%query_components, 'utf-8')
        
        self.wfile.write(path_args)
        self.wfile.write(b'Hello, world!\n')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="keys/key.pem", 
        certfile='keys/cert.pem', server_side=True)

httpd.serve_forever()

        

