import json
import os

from shutil import copy  # shutil 是用来复制黏贴文件的

sd_store = ".DS_Store"
origin_git_dir = "/Volumes/CK/Githubbbb/"
# ⭐ ☆
origin_dir_s = os.listdir(origin_git_dir)
print(origin_dir_s)

new_git_dir = "/Volumes/CK/newGIthubbbbb/"
# ⭐ ☆
new_dir_s = os.listdir(new_git_dir)
print(new_dir_s)

repo_json_dir = "/Volumes/CK/stars_repo_json/"
json_dir_s = os.listdir(repo_json_dir)
print(json_dir_s)

fail_dirs = []
current_dir = ""

os.chdir(new_git_dir)

big_size_repo = []
# 获取仓库信息

white = ["aws丨aws-sdk-go",
         "aws丨aws-sdk-js",
         "bannedbook丨fanqiang",
         "bminor丨binutils-gdb",
         "cockroachdb丨cockroach",
         "mozilla丨gecko-dev",
         "gatsbyjs丨gatsby",
         "nestjs丨nest",
         "nndl丨nndl.github.io",
         "o2oa丨o2oa",
         "papers-we-love丨papers-we-love",
         "paritytech丨substrate",
         "",
         "",
         "",
         "",
         "",
         "",
         "", ]
black = []
for json_item in json_dir_s:
    json_name_without_json = json_item.split(".json")[0]
    if white.__contains__(json_name_without_json):
        print("白名单：", json_name_without_json)
        continue
    if origin_git_dir.__contains__(json_name_without_json) \
            or new_dir_s.__contains__(json_name_without_json):
        print("已经下载过：", json_name_without_json)

        j_dir = repo_json_dir + json_item
        with open(j_dir, 'r') as load_f:
            j_content = json.load(load_f)
        full_name = j_content["full_name"]
        description = j_content["description"]
        clone_url = j_content["clone_url"]
        size = j_content["size"]  # kb
        stargazers_count = j_content["stargazers_count"]
        language = j_content["language"]  # 可能为null

        source = new_git_dir + json_name_without_json
        new_des=str(description).replace("/","+")
        result = new_git_dir + str(language) + "丨" + json_name_without_json + "丨" + str(new_des)
        print(source)
        print(result)
        # os.rename(source, result)

    elif not json_name_without_json == ".DS_Store":
        j_dir = repo_json_dir + json_item
        # print(j_dir)
        with open(j_dir, 'r') as load_f:
            j_content = json.load(load_f)
        full_name = j_content["full_name"]
        description = j_content["description"]
        clone_url = j_content["clone_url"]
        size = j_content["size"]  # kb
        stargazers_count = j_content["stargazers_count"]
        language = j_content["language"]  # 可能为null



        print("开始下载：", json_name_without_json, "  size:", size, " language:", language)

        # print(full_name)
        # print(description)
        # print(clone_url)
        # print(size)
        # print(stargazers_count)
        # print(language)

        dns_git_clone = "https://hub.fastgit.org/" + full_name + ".git"

        if size > 1024000000000:  # 大于10M
            repo_url = "http://github.com/" + j_content["full_name"]
            print("仓库过大: ", repo_url)
            big_size_repo.append(repo_url)
        else:
            file_name = full_name.replace("/", "丨")
            command = "git clone " + dns_git_clone + " " + file_name
            print(command)
            result = os.popen(command).read()
            print(result)

print(str(len(big_size_repo)), "  ", big_size_repo)
with open("/Users/chengkun02/Downloads/awesome-cs/BE/Python/Python基础/爬虫/github相关爬虫和脚本/big_size_repo.txt", 'w+') as fout:
    for item in big_size_repo:
        fout.write(item + "\n")
    fout.close()
