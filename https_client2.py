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
portnum = 8000
timeout_secs = 12
usid = 'admin@admin.com'
passwd = 'admin95070'

#Create b64 encoding of username + password
usidpasswd = usid + ':' + passwd
b64Val = base64.b64encode(bytes(usidpasswd, 'utf-8'))
b64str = str(b64Val, "utf-8")

conn = http.client.HTTPSConnection(host=hostname, port=portnum, context=ssl._create_unverified_context(), timeout=timeout_secs)
headers = {'Authorization':'Basic %s' % b64str}


count = 5
for i in range(count):
    
    try:
        conn.request(method='GET', url='/logout', body=None, headers=headers)
        r = conn.getresponse()
        logger.info("LOGOUT REQUEST RESPONSE = %s"% r.read().decode('utf-8'))
    except http.client.HTTPException:
        logger.info("Failed connection")




