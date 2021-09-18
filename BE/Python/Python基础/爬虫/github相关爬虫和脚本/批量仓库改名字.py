import json

import os

from shutil import copy  # shutil 是用来复制黏贴文件的

sd_store = ".DS_Store"
git_dir = "/Volumes/CK/newGIthubbbbb/"
repo_json_dir = "/Volumes/CK/newGIthubbbbb/"
result_dir = ""
# ⭐ ☆
dir_s = os.listdir("/Volumes/CK/newGIthubbbbb/")
print(dir_s)
fail_dirs = []
fail_dirs_new = []
current_dir = ""

json_dir_s = os.listdir(repo_json_dir)
print(json_dir_s)

count = 0
# try:
#     for dir in dir_s:
#         ddddir = git_dir + dir
#         if os.path.isdir(ddddir):
#             current_dir = ddddir
#             print(current_dir)
#             os.chdir(current_dir)
#             result = os.popen("git remote -v").read()
#             print(result)
#             author = result.split("/")[3]
#             repo_name = result.split("/")[4].split(".git")[0]
#             # print(repo_name)
#             result_name = current_dir + "/" + author + "丨" + repo_name + ".json"
#
#             # json_result_name = result_name
#             # dir_json_result_name=current_dir+json_result_name
#             print(result_name)
#             # json_dir_json_result_name = current_dir + json_result_name
#             # print(json_dir_json_result_name)
#             # 读json
#             with open(result_name, "r") as fin:
#                 j_content = json.load(fin)
#                 fin.close()
#
#             full_name = j_content["full_name"]
#             description = j_content["description"]
#             clone_url = j_content["clone_url"]
#             size = j_content["size"]  # kb
#             stargazers_count = j_content["stargazers_count"]
#             language = j_content["language"]  # 可能为null
#             # 重命名
#             print(current_dir)
#             result_dir_name = git_dir  \
#                               + "【" + "🥑" + str(language) + "】" \
#                               + "丨" + "🍑" + str(author) \
#                               + "丨" + "🍉" + str(repo_name) \
#                               + "丨" + "" + "⭐️" + str(stargazers_count) + "" \
#                               + "丨" + "🌰" + str(description)
#             print(result_dir_name)
#             os.rename(current_dir, result_dir_name)
#
#             # if json_dir_s.__contains__(author + "丨" + repo_name + ".json"):
#             #     source_file = repo_json_dir + author + "丨" + repo_name + ".json"
#             #     dist_file = ddddir + "/" + author + "丨" + repo_name + ".json"
#             #     print(source_file)
#             #     print(dist_file)
#             #     # 复制文件
#             #     copy(source_file, dist_file)
#             #     count = count + 1
# except IndexError:
#     print("IndexError")
#     fail_dirs.append(current_dir)
#     fail_dirs_new.append(result_dir_name)
# except FileNotFoundError:
#     print("FileNotFoundError")
#     fail_dirs.append(current_dir)
#     fail_dirs_new.append(result_dir_name)
# except OSError:
#     print("IndexError")
#     fail_dirs.append(current_dir)
#     fail_dirs_new.append(result_dir_name)

print("fail：", fail_dirs)
print("count:", str(count))

for dir in dir_s:
    ddddir = git_dir + dir
    if os.path.isdir(ddddir):
        current_dir = ddddir
        print("dir:", dir)
        splite_res = dir.split("丨")
        if len(splite_res) > 4000:
            print("已经改过名字了:",current_dir)
        else:
            # print(current_dir)
            os.chdir(current_dir)
            result = os.popen("git remote -v").read()
            # print(result)
            author = result.split("/")[3]
            repo_name = result.split("/")[4].split(".git")[0]
            # print(repo_name)
            result_name = current_dir + "/" + author + "丨" + repo_name + ".json"

            # json_result_name = result_name
            # dir_json_result_name=current_dir+json_result_name
            # print(result_name)
            # json_dir_json_result_name = current_dir + json_result_name
            # print(json_dir_json_result_name)
            # 读json
            with open(result_name, "r") as fin:
                j_content = json.load(fin)
                fin.close()

            full_name = j_content["full_name"]
            description = j_content["description"]
            clone_url = j_content["clone_url"]
            size = j_content["size"]  # kb
            stargazers_count = j_content["stargazers_count"]
            language = j_content["language"]  # 可能为null

            new_des = str(description).replace("/", "+")
            # 重命名
            # print(current_dir)
            real_dir_name = "" + "🥑" + str(language) + "" \
                            + "丨" + "🍋" + str(author) \
                            + "丨" + "🍉" + str(repo_name) \
                            + "丨" + "" + "⭐️" + str(stargazers_count) + "" \
                            + "丨" + "🌰" + str(new_des)
            result_dir_name = git_dir + real_dir_name[0:200]

            # print(result_dir_name)
            print("count----------------------",count)
            count=count+1
            if os.path.exists(result_dir_name):
                print("已经重命名过")
            else:
                os.rename(current_dir, result_dir_name)

# 【🥑Vue】丨🍑chuzhixin丨🍉vue-admin-beautiful-pro丨⭐️10251丨🌰🚀🚀🚀vue3,vue3.0,vue,vue3.x,vue.js,vue后台管理,admin,vue-admin,vue-element-admin,ant-design，vue-admin-beautiful-pro,vab admin pro,vab admin plus主线版本基于element-plus、element-ui、ant-design-vue三者并行开发维护，同时支持电脑，

