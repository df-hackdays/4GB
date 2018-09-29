import requests
from requests.auth import HTTPBasicAuth
import json

url="https://api.powerbi.com/beta/8ff33436-4701-4dad-b7d3-3462e99c6889/datasets/ca347d43-d161-42fd-8686-fdcde6e155c3/rows?key=vimhQpghVcuW5dsaMoDOQd%2F15magtrzPuIuGl2GPhwq7tQP3%2F1FQ473ANr7M4PfZ%2BGHBl%2FTlB%2BMI0Wrzy6zuLw%3D%3D"

data = [{
    "name":"Learner3",
    "question": "Do you like CLC course?",
    "answer": 1,
    "submittedtime" :"2018-09-29T16:17:22.752Z"
}]
proxy={"https":"https://proxyprd.scotia-capital.com:8080"}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers,proxies=proxy)
print(r.status_code)


