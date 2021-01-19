import requests
import json
ACCESS_TOKEN = "m1wq_i9NiwEW4jym3s_MX6mpJgFLND2bERLtsf-8"
URL = "https://api.predicthq.com/v1/events/"
params={
        "q": "jazz",
        "country": "NZ"
        }

def get_data(token,url,params):
    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
        }
    try:
        init_res = requests.get(URL, headers=headers, params=params)
        if init_res.status_code == 200:
            return init_res.json()
    except Exception as ce:
        print(ce)

print(get_data(ACCESS_TOKEN, URL, params))


# response = requests.get(
#     url="https://api.predicthq.com/v1/events/",
#     headers={"Authorization": "Bearer $ACCESS_TOKEN"}
# )

# print(response.json())