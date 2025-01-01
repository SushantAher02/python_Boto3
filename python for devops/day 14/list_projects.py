import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://***********.atlassian.net/rest/api/3/project"
API_TOKEN ="********************"
auth = HTTPBasicAuth("************@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

