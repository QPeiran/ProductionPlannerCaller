import json
import requests

planUrl = 'https://kittingline.azurewebsites.net/api/planning/PlanHistoryDate'

localUrl = 'http://localhost:62805/api/planning/PlanHistoryDate'

testUrl = 'https://httpbin.org/post'

sampleDict = {
    "id": 1,
    "name":"Jessa"
}
sampleJsonData = json.dumps(sampleDict)
# solution 1:
# response = requests.post(testUrl, json=sampleJsonData)
# print("Status code: ", response.status_code)
# print("Printing Entire Post Request")
# print(response.json())

# solution 2:
newHeaders = {'Content-type': 'application/json'}

# response = requests.post(testUrl,
#                          data=jsonData,
#                          headers=newHeaders)

with open(r'./template input.json') as f:
    jsonData = json.load(f)

response = requests.post(url = localUrl, 
                         json = jsonData, 
                         headers=newHeaders)


print("Status code: ", response.status_code)

# response_Json = response.json()
# print("Printing Post JSON data")
# print(response_Json['data'])

# print("Content-Type is ", response_Json['headers']['Content-Type'])