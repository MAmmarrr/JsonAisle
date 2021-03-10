import requests
import pprint

printer = pprint.PrettyPrinter()
URL = "https://www.signupanytime.com/plugins/links/admin/LinksAJAX.aspx?op=GetMeta&t=9761&fbclid=IwAR03xgA9Qri27pGlmhj60jw_tr7Wr5ug1nyXUX0KSMS_3H3m6UYeOY7Iw2I"
resp = requests.get(url=URL)
data = data.json()
keys = data.keys()

for key in keys:
    print("Key:", key)
    for idx, entry in enumerate(data[key]):
        print(f"DATA: {entry}")