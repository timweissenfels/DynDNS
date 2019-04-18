import urllib
import json
import requests

response = requests.get("https://api.myip.com")
json_data = json.loads(response.text)

ip = json_data['ip']

hostname = "test-pcs.dynv6.net"
account = "t1wSt5VvuxTY2x-gniA1PAyuHxe4E-"
parameters = {'hostname': hostname, 'token': account, 'ipv6': ip}

response = requests.get('https://dynv6.com/api/update?{}'.format(
urllib.urlencode(parameters)))

print(response)

#url = 'https://dynv6.com/api/update?token='.account.'&hostname='.hostname.'&ipv6='.ip;
