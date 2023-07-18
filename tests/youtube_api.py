import json

with open('../api.json','r') as f:
    config = json.load(f)
aip_key = config['api_key']