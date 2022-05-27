import requests
import json
from pprint import pprint

pc_req = requests.get("https://api.postcodes.io/postcodes/SK4 2QS")
# print(pc_req, type(pc_req))
# print(pc_req.status_code)

if pc_req.status_code == 200:
    # print(type(pc_req.headers))  # It's a dictionary
    # pprint(dict(pc_req.headers), sort_dicts=False)  # prints in order received not alphabetical

    # print(type(pc_req.content))  # Type is bytes string
    # pprint(pc_req.content)
    # print(pc_req.content["result"]["postcode"])  # Won't work because it's not a dictionary

    postcode = json.loads(pc_req.content)
    # print(type(postcode))  # Dictionary
    # pprint(postcode)  # View as a dictionary
    # print(postcode["result"]["postcode"])

    # Print admin district, eastings and northings, NUTS code
    # print(postcode.keys())
    result = postcode["result"] # we are working with the results key
    print(result["admin_district"])
    print(result["eastings"], result["northings"])
    print(result["codes"]["nuts"])
