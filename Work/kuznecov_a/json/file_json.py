import json

active, disabled = [], []

with open('upask.json', encoding='utf-8') as upask:
    upask_string = upask.read()
    parsed_upask_string = json.loads(upask_string)
    for cnt, el in enumerate(parsed_upask_string, 1):
        print(f"[3.{cnt:2}] {el['object'].upper()}")
        # for i in el['items']:
        #     if i['used_in_PA']:
        #         active.append(i['item_title'])
        #         print(f"\t{i['item_title']}")
        #     else:
        #         disabled.append(i['item_title'])
        #         print(f"\t{i['item_title']}")


