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
        init_res = requests.get('https://api.predicthq.com/v1/events/', headers=headers, allow_redirects=False)
        if init_res.status_code == 307:
            api_response = requests.get(init_res.headers['Location'], headers=headers, allow_redirects=False)
            if  api_response.status_code == 200:
                return api_response.json()
        elif init_res.status_code == 200:
            return init_res.json()
    except Exception as ce:
        print(ce)



print(get_nest_data(ACCESS_TOKEN))