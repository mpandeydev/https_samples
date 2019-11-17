import http.client
import ssl
import json
import base64
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
FORMAT = '%(asctime)-15s [ %(message)s ]'
fmt = logging.Formatter(FORMAT)
console = logging.StreamHandler()
console.setFormatter(fmt)
logger.addHandler(console)


hostname = '127.0.0.1'
portnum = 4000
timeout_secs = 15
usid = 'admin@admin.com'
passwd = 'admin95070'

#Create b64 encoding of username + password
usidpasswd = usid + ':' + passwd
b64Val = base64.b64encode(bytes(usidpasswd, 'utf-8'))
b64str = str(b64Val, "utf-8")

conn = http.client.HTTPConnection(host=hostname, port=portnum, timeout=timeout_secs)
headers = {'Authorization':'Basic %s' % b64str}

'''
#1. Login request
try:
    conn.request(method='GET', url='/login', body=None, headers=headers)
    #conn.endheaders()
    r = conn.getresponse()
    logger.info("LOGIN REQUEST RESPONSE =%s"% r.read().decode('utf-8'))
except http.client.HTTPException:
    logger.info("Failed connection")

#2. Logout request
try:
    conn.request(method='GET', url='/logout', body=None, headers=headers)
    r = conn.getresponse()
    logger.info("LOGOUT REQUEST RESPONSE = %s"% r.read().decode('utf-8'))
except http.client.HTTPException:
    logger.info("Failed connection")
'''
count = 2
for i in range(count):
    #3. Answers request
    try:
        urlval = ('/related?question=g=how+to+dedupe+%d?' % i)
        conn.request(method='GET', url=urlval, body=None, headers=headers)
        r = conn.getresponse()
        response_str = r.read().decode('utf-8')
        logger.info("ANSWERS RESPONSE =%s"% response_str)
    except http.client.HTTPException:
        logger.error("Failed connection")


