import requests
import subprocess

"""
for windows:
192.168.99.100 = docker-machine ip default
curl 192.168.99.100:5000/ -d "{\"foo\": \"bar\"}" -H 'Content-Type:application/json'
"""

def test_server_request():
    """
    Tests that server is able to receive curl request.
    Does not care about schema of response
    :return:
    """

    url = subprocess.check_output(["docker-machine", "ip", "default"]).decode().strip()
    host = "http://" + url + ":5000"
    payload = '{"X1":0.0}'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    try:
        r = requests.post(host, data=payload, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print("unable to connect to server on {}".format(host))
        print(e)
        return
    assert r.status_code == 200, "Unable to connect to server on {}".format(host)


if __name__=="__main__":
    test_server_request()