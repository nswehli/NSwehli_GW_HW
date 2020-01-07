########### Python 2.7 #############
import urllib.error
import urllib.parse
import urllib.request
import http.client
import httplib
import urllib
import base64

headers = {
    # Request headers
    'api_key': '{subscription key}',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.wmata.com')
    conn.request(
        "GET", "/TrainPositions/TrainPositions?contentType={contentType}&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

########### Python 3.2 #############

headers = {
    # Request headers
    'api_key': '{subscription key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request(
        "GET", "/TrainPositions/TrainPositions?contentType={contentType}&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
