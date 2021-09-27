# 生成2021-2091年的日记和模板

# 闰年
import os

path = "/Users/chengkun/Documents/Blog/生活/Daily/"
os.chdir(path)
year = 2021

# 总共10辈子
lifetime = 10

# 1、3、5、7、8、10、11  2月闰年29天普通28天
month_31 = [1,3, 5, 7, 8, 10, 12]

enter_command = "\n"
#
# for lifetime in range(1,lifetime+1):
#     os.mkdir("")

# 生成年份目录和年终总结
def create_year_end_summary_template(start, end):
    for year in range(start, end):
        year_path = path + str(year)
        os.mkdir(year_path)
        os.chdir(year_path)
        with open("年末のまとめ.md", "w") as f:
            f.writelines("[TOC]" + enter_command)
            f.writelines("### キーワード：" + enter_command)
            f.writelines("- " + enter_command)

        for month in range(1, 13):
            # month_path = year_path + "/" + str(month) + "月/"
            # os.mkdir(month_path)
            # os.chdir(month_path)
            day_count = 30
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day_count = 29
            elif month == 2:
                day_count = 28
            if month in month_31:
                day_count = 31

            print("year:" + str(year) + " month:" + str(month) + " day:" + str(day_count))

            with open(str(month) + "月.md", "w") as f:
                f.writelines("[TOC]" + enter_command)
                f.writelines("### **" + str(month) + "：" + "**" + enter_command)
                for day in range(1, day_count + 1):
                    f.writelines("#### " + str(month) + "." + str(day) + enter_command)
                    f.writelines("```c" + enter_command)
                    f.writelines(" " + enter_command)
                    f.writelines("```" + enter_command)
                    f.writelines(enter_command)
            with open(str(month) + "月の時間手帳.md", "w") as f:
                f.writelines("[TOC]" + enter_command)
                f.writelines("### **" + str(month) + "：" + "**" + enter_command)
                for day in range(1, day_count + 1):
                    f.writelines("#### " + str(month) + "." + str(day) + enter_command)
                    f.writelines("```c" + enter_command)
                    f.writelines("起床" + enter_command)
                    f.writelines(" " + enter_command)
                    f.writelines("睡觉" + enter_command)
                    f.writelines("```" + enter_command)

    return


create_year_end_summary_template(2021, 2092)
