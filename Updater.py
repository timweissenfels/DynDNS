import urllib
import json
import requests
import argparse
import sentry_sdk
sentry_sdk.init("https://5e1eb70302864954b3c653de2919c3b7@sentry.io/1457409")

response = requests.get("https://api.myip.com")
json_data = json.loads(response.text)

ip = json_data['ip']

parser = argparse.ArgumentParser(description='Update Skript fuer Dynv6')
parser.add_argument('-u',"--url",type=str,
help='Volle URL der Seite/Domain Beispiel: pcs-test.dynv6.net')
parser.add_argument('-t',"--token",type=str, help='\nToken zur Validierung des Updates der IP')

args = parser.parse_args()

hostname = args.url
account = args.token

parameters = {'hostname': hostname, 'token': account, 'ipv6': ip}

response = requests.get('https://dynv6.com/api/update?{}'.format(
urllib.urlencode(parameters)))

assert response.status_code == 200, response.content
print response.content
