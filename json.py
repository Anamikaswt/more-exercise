import json
dic={"anamika":"1" ,"singh":"2"}
# print(type(dic))
with open("dic.json","w") as my_data:
    json.loads(dic,my_data,indent=4)
