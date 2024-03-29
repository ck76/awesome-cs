import os

from shutil import copy  # shutil 是用来复制黏贴文件的

sd_store = ".DS_Store"
git_dir = "/Volumes/CK/newGIthubbbbb_new/"
repo_json_dir = "/Volumes/CK/stars_repo_json_new/"
dir_s = os.listdir(git_dir)
print(dir_s)
fail_dirs = []
current_dir = ""

json_dir_s = os.listdir(repo_json_dir)
print(json_dir_s)

count = 0
try:
    for dir in dir_s:
        ddddir = git_dir + dir
        if os.path.isdir(ddddir):
            current_dir = ddddir

            current_dir_list = os.listdir(current_dir)

            # print(ddddir)
            os.chdir(ddddir)
            result = os.popen("git remote -v").read()
            # print(result)
            author = result.split("/")[3]
            # print(author)
            repo_name = result.split("/")[4].split(".git")[0]
            # print(repo_name)
            result_name = git_dir + author + "丨" + repo_name
            json_result_name = result_name + ".json"
            # 重命名
            # os.rename(ddddir, result_name)

            name = author + "丨" + repo_name + ".json"
            if json_dir_s.__contains__(name):
                if current_dir_list.__contains__(name):
                    print("已经拷贝过了: ", name)
                else:
                    source_file = repo_json_dir + author + "丨" + repo_name + ".json"
                    dist_file_without_ = ddddir + "/" + author + "丨" + repo_name + ".json"
                    dist_file = ddddir + "/" + "【" + author + "丨" + repo_name + "】" + ".json"
                    print(source_file)
                    print(dist_file)
                    # 复制文件
                    copy(source_file, dist_file_without_)
                    copy(source_file, dist_file)
                    count = count + 1


except IndexError:
    print("IndexError")
    fail_dirs.append(current_dir)

except OSError:
    print("IndexError")
    fail_dirs.append(current_dir)
print("fail：", fail_dirs)
print("count:", str(count))
