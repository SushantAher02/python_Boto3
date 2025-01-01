
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://****.atlassian.net/rest/api/3/issue"
API_TOKEN= "******************"
auth = HTTPBasicAuth("*************@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    "issuetype": {
      "name": "Story"
    },
   
    "project": {
      "key": "*"
    },
    "summary": "First jira ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))