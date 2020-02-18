from snownlp import SnowNLP
import pandas as pd
import re
import jieba
import os

# 定义词云图函数变量
csv_file = "我不是药神"
stopwords_path = "stopwords_cn.txt"
pic_path = "我不是药神.jpg"

print("正在获取专业影评库和观众影评库的六维数值...")
# 获取两个txt文件中的值，提取后为字符串类型
with open("Da.txt", 'r', encoding="utf-8") as fa:
    Da = fa.readlines()  # 获取Da.txt中的六行，Da[0]-Da[5]分别对应观众影评在该维度的值
    Da = [x.strip() for x in Da if x.strip() != '']  # 去掉每一行末尾的换行符
fa.close()
# os.remove(Da.txt)  # 读取完数据后删除文件

with open("Dv.txt", 'r', encoding="utf-8") as fv:
    Dv = fv.readlines()
    Dv = [x.strip() for x in Dv if x.strip() != '']
fv.close()
# os.remove(Dv.txt)  # 读取完数据后删除文件

# 六维计算过程

# 数学公式系数的初始化
p = 0.7
q = 0.3
# 利用建模公式1得出各维度临时结果
plot_temp = float(Dv[0]) * p + float(Da[0]) * q
audio_visual_temp = float(Dv[1]) * p + float(Da[1]) * q
character_temp = float(Dv[2]) * p + float(Da[2]) * q
fan_temp = float(Dv[3]) * p + float(Da[3]) * q
commercial_temp = float(Dv[4]) * p + float(Da[4]) * q
conception_temp = float(Dv[5]) * p + float(Da[5]) * q
temp = [plot_temp, audio_visual_temp, character_temp, fan_temp, commercial_temp, conception_temp]
# 利用Z-Score模型变式3得出各维度结果
length = len(temp)
total = sum(temp)
ave = float(total) / length
temp_sum = sum([pow(temp[i] - ave, 2) for i in range(length)])
temp_sum = pow(float(temp_sum) / length, 0.5)
for i in range(length):
    temp[i] = (temp[i] - ave) / temp_sum
# 得出六个维度的最终数值
plot = (temp[0] + 2.58) * (100 / 5.16)
audio_visual = (temp[1] + 2.58) * (100 / 5.16)
character = (temp[2] + 2.58) * (100 / 5.16)
fan = (temp[3] + 2.58) * (100 / 5.16)
commercial = (temp[4] + 2.58) * (100 / 5.16)
conception = (temp[5] + 2.58) * (100 / 5.16)

if __name__ == "__main__":
    # 绘制六维雷达图
    from pyecharts import Page, Radar

    page = Page(csv_file + "-可视化分析")
    print("正在绘制六维雷达图和饼图...")
    value = [[plot, audio_visual, character, fan, commercial, conception]]

    # 用于调整雷达各维度的范围大小
    c_schema = [{"name": "Plot", "max": 100, "min": 0},
                {"name": "Audio-visual", "max": 100, "min": 0},
                {"name": "Character", "max": 100, "min": 0},
                {"name": "Fan Effect", "max": 100, "min": 0},
                {"name": "Business Value", "max": 100, "min": 0},
                {"name": "Theme", "max": 100, "min": 0}]
    radar = Radar(" ", title_pos='left')
    radar.config(c_schema=c_schema, radar_text_size=20)
    radar.add('我不是药神', value, item_color="#5CACEE",
              symbol=None, area_color="#5CACEE", area_opacity=0.3,
              legend_top='right', line_width=3)

    radar.render("Radar.html")

    # 绘制六维饼图
    from pyecharts import Pie

    attr = ['Music', 'Impression', 'Performance', 'Plot', 'Director', 'Frames']
    val = [plot, audio_visual, character, fan, commercial, conception]

    pie = Pie(" ", title_pos="left", width=1200, height=600)
    pie.add("", attr, val, radius=[20, 50], label_text_color=None, is_label_show=True,
            label_text_size=18, legend_text_size=18)
    pie.render("Pie.html")

    # # 绘制情感分析柱形图
    # from pyecharts import Bar
    #
    # print("正在绘制所有影评的情感分析柱形图...")
    #
    #
    # def count_sentiment(csv_file):
    #     path = os.path.abspath(os.curdir)
    #     csv_file = path + "\\" + csv_file + ".csv"
    #     csv_file = csv_file.replace('\\', '\\\\')
    #     d = pd.read_csv(csv_file, engine='python', encoding='utf-8')
    #     motion_list = []
    #     for i in d['content']:
    #         try:
    #             s = round(SnowNLP(i).sentiments, 2)
    #             motion_list.append(s)
    #         except TypeError:
    #             continue
    #     result = {}
    #     for i in set(motion_list):
    #         result[i] = motion_list.count(i)
    #     return result
    #
    #
    # def draw_sentiment_pic(csv_file):
    #     attr, val = [], []
    #     info = count_sentiment(csv_file)
    #     info = sorted(info.items(), key=lambda x: x[0], reverse=False)  # dict的排序方法
    #     for each in info[:-1]:
    #         attr.append(each[0])
    #         val.append(each[1])
    #     global bar
    #     bar = Bar(csv_file + "-影评情感分析", width=960, height=480)
    #     bar.add("", attr, val, is_smooth=True, is_more_utils=True)
    #     bar.render(csv_file + "_情感分析柱形图.html")
    #
    #
    # draw_sentiment_pic(csv_file)
    #
    # # 绘制词云图
    # import matplotlib.pyplot as plt
    # from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    #
    # print("正在绘制词云图...")
    #
    #
    # # 过滤字符串只保留中文
    # def translate(str):
    #     line = str.strip()
    #     p2 = re.compile('[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    #     zh = " ".join(p2.split(line)).strip()
    #     zh = ",".join(zh.split())
    #     str = re.sub("[A-Za-z0-9!！，%[],。]", "", zh)
    #     return str
    #
    #
    # pic_name = csv_file + "_词云图.png"
    # path = os.path.abspath(os.curdir)
    # csv_file1 = path + '/' + csv_file + "（总）.csv"
    # csv_file1 = csv_file1.replace('\\', '\\\\')
    # d = pd.read_csv(csv_file1, engine='python', encoding='utf-8')
    # content = []
    # for i in d['content']:
    #     try:
    #         i = translate(i)
    #     except AttributeError as e:
    #         continue
    #     else:
    #         content.append(i)
    # comment_after_split = jieba.cut(str(content), cut_all=False)
    # wl_space_split = " ".join(comment_after_split)
    # backgroud_Image = plt.imread(pic_path)
    # stopwords = STOPWORDS.copy()
    # with open(stopwords_path, 'r', encoding='utf-8') as f:
    #     for i in f.readlines():
    #         stopwords.add(i.strip('\n'))
    #     f.close()
    #
    # wc = WordCloud(width=1024, height=768, background_color='white',
    #                mask=backgroud_Image, font_path="simhei.ttf",
    #                stopwords=stopwords, max_font_size=400,
    #                random_state=50)
    # wc.generate_from_text(wl_space_split)
    # img_colors = ImageColorGenerator(backgroud_Image)
    # wc.recolor(color_func=img_colors)
    # plt.imshow(wc)
    # plt.axis('off')
    # plt.show()
    # wc.to_file(pic_name)
    #
    # page.add_chart(radar)
    # page.add_chart(pie)
    # page.add_chart(bar)
    # page.render(csv_file + "-可视化分析.html")
    #
    # print("绘图完成！")
