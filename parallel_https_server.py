import http
import ssl
import time
import json
import base64
from urllib.parse import urlparse, parse_qs
from io import BytesIO
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import threading
from socketserver import ThreadingMixIn
#https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python
USE_HTTPS = True

logger = logging.getLogger()
logger.setLevel(logging.INFO)
FORMAT = '%(asctime)-15s [ %(message)s ]'
fmt = logging.Formatter(FORMAT)
console = logging.StreamHandler()
console.setFormatter(fmt)
logger.addHandler(console)


#Basic authentication 
# UID + Password b64
usid = 'admin@admin.com'
passwd = 'admin95070'
usidpasswd = usid + ':' + passwd
b64str = str(base64.b64encode(bytes(usidpasswd, 'utf-8')), "utf-8")


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    #https://gist.github.com/fxsjy/5465353
    def do_AUTHHEAD(self):
        logger.info("--------------------- send Auth Request ------------------")
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        
    def do_GET(self):
        #content_length = int(self.headers['Content-Length'])
        #body = self.rfile.read(content_length)
        #print("Post Header = [%s]"%str(self.headers))
        #print("Post Body = [%s]"%str(body))

        logger.info("--------- GET Path = %s -----------"% self.path)

        if self.headers.get('Authorization') == None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'utf-8'))
            return
        else:
            #verify that correct username password has been provided
            headerb64str = self.headers.get('Authorization')[6:]
            if(b64str != headerb64str):
                logger.error("Password mismatch")
                self.do_AUTHHEAD()
                self.wfile.write(bytes('incorrect authentication', 'utf-8'))
                return

        
        #Response will be successful at this point        
        if(self.path == '/login'):
            self.send_response(200)
            self.end_headers()
            response_str = 'login successful'
            response = bytes(response_str, 'utf-8')
            self.wfile.write(response)
            logger.info(response_str)
            #return

        if(self.path == '/logout'):
            self.send_response(200)
            self.end_headers()
            response_str = 'logout successful'
            response = bytes(response_str, 'utf-8')
            self.wfile.write(response)
            logger.info(response_str)
            #return

        if(urlparse(self.path).path == '/answers'):
            time.sleep(10)
            self.send_response(200)
            self.end_headers()
            
            #path = urlparse(self.path).path
            #query_components = parse_qs(urlparse(self.path).query)
            #response_str = 'path=%s query components=%s\n'%(path, query_components)
            
            with open('answer_docs_sample.json', 'r') as content_file:
                json_content = content_file.read()
                response = bytes(json_content, 'utf-8')
                self.wfile.write(response)
                logger.info("Sending response ... %s"% self.path)                                 
            

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


def run():
    server = ThreadingSimpleServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    if USE_HTTPS:
        import ssl
        server.socket = ssl.wrap_socket(server.socket,
                                        keyfile='keys/key.pem',
                                        certfile='keys/cert.pem',
                                        server_side=True)
    server.serve_forever()


if __name__ == '__main__':
    run()

                
        

