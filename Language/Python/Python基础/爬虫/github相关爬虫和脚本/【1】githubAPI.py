# https://gist.github.com/derhuerst/19e0844796fa3b62e1e9567a1dc0b5a3
# https://github.community/t/how-can-i-know-the-number-of-repository-by-user-name/13767/3
# curl -i -u ck76: https://api.github.com/users/ck76/starred
# curl -i -u ck76: https://api.github.com/users/ck76/starred?per_page=20&page=20
import json
import os

repo_json_dir = "/Volumes/CK/stars_repo_json_new/"
json_dir_s = os.listdir(repo_json_dir)
print(json_dir_s)


original_repo_json_dir = "/Volumes/CK/stars_repo_json/"
original_json_dir_s = os.listdir(original_repo_json_dir)
print(original_json_dir_s)

# 30 总共77页
# 100 24页
per_page = 40
page_count = 77

count = 1

for i in range(1, 3):
    # TODO 加密码
    url = "curl -u ck76: https://api.github.com/users/ck76/starred?page=" + str(i)
    print(url)
    result = os.popen(url).read()
    print(result)
    json_result = json.loads(result)
    for index in range(0, len(json_result)):
        j_item = json_result[index]
        full_name = j_item["full_name"]
        file_name = full_name.replace("/", "丨") + ".json"

        if not original_json_dir_s.__contains__(file_name):
            j_item_result_string = json.dumps(j_item)
            with open(repo_json_dir + file_name, "w+") as fout:
                fout.write(j_item_result_string)
                fout.close()

            print(count)
            count = count + 1
        else:
            print("已经下载过了",)