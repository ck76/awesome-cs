import json
jjjjj = ""
# /Volumes/CK/stars_repo_json/0voice丨campus_recruitmen_questions.json
# json_str = open("json_result_sample.json",mode = "r")
json_str = open("/Volumes/CK/stars_repo_json/0voice丨campus_recruitmen_questions.json",mode = "r")
for item in json_str.readlines():
    # item=item.replace("\n","")
    jjjjj=jjjjj+item
j= json.loads(jjjjj)
print(j)
# print(j[0]["description"])