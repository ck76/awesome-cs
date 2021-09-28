import os

sd_store = ".DS_Store"
black_list= [".idea",
             ".DS_Store"]
git_dir = "/Volumes/CK/newGIthubbbbb/"
dir_s = os.listdir(git_dir)

# print(dir_s)

for item in dir_s:
    if black_list.__contains__(item):
        continue
    current_dir = git_dir + item
    if os.path.isdir(current_dir):
        os.chdir(current_dir)
        print(current_dir)
        result = os.popen("git remote -v").read()
        author = result.split("/")[3]
        repo_name = result.split("/")[4].split(".git")[0]
        result_github_url = "https://github.com/" + author + "/" + repo_name
        result_content = "githuburl = " + "\"" + result_github_url + "\""
        print(result_github_url)
        print(current_dir + "/【github地址】.py")
        with open( "【github地址】.py", "w+") as fout:
            fout.writelines(result_content)
            fout.close()
