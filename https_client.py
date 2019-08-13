import http.client
import ssl

hostname = '127.0.0.1'
portnum = 4443
timeout_secs = 1

try:
    conn = http.client.HTTPSConnection(host=hostname, port=portnum, context=ssl._create_unverified_context(), timeout=timeout_secs)
    conn.putrequest('GET', '/?arg1=foo+bar')
    conn.endheaders() # <---
    r = conn.getresponse()
    print(r.read())
except http.client.HTTPException:
    print("Failed connection")

