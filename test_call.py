import requests
import json
ACCESS_TOKEN = "m1wq_i9NiwEW4jym3s_MX6mpJgFLND2bERLtsf-8"



def get_nest_data(token):
    url = "https://api.predicthq.com/v1/events/"
    auth_t = token#.encode("ascii", "ignore")
    headers = {
        'authorization': "Bearer " + auth_t,
        'content-type': "application/json",
    }

    try:
        init_res = requests.get('https://api.predicthq.com/v1/events/', headers=headers)
        if init_res.status_code == 200:
            return init_res.json()
    except Exception as ce:
        print(ce)

print(get_nest_data(ACCESS_TOKEN))


# response = requests.get(
#     url="https://api.predicthq.com/v1/events/",
#     headers={"authorization": "Bearer $ACCESS_TOKEN"},
#     params={"q": "jazz"},
#     allow_redirects=False
# )

# print(response.json())