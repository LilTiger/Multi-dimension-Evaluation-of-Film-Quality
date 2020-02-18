import re
from snownlp import SnowNLP

# 定义六个维度的变量，存放每个维度的情感极性数值
global plot  # 故事情节
global audio_visual  # 视听体验
global character  # 人物塑造
global fan  # 粉丝基础
global commercial  # 商业价值
global conception  # 主题文化

# 以下分别读入六个维度的近义词文件，组成列表，并在影评当中查找到，计算情感极性分值，放入一个float变量中
print("正在计算观众影评库六个维度的对应数值...")

# 故事情节
# 将txt中的内容读进一个列表
with open('故事情节.txt', 'r', encoding="utf-8") as f:
    contents = f.read().splitlines()
# 读取影评文件
with open("我不是药神 Da.csv", 'r', encoding="utf-8") as fs:
    st = fs.read()
plot_list = []  # 存放检索到的句子
plot = 0.0  # 存放情感极性数值
for kw in contents:
    pattern = re.compile('[，,。.！？；…（\n]+[^，,。.！？；…（\n]*' + kw
                         + '[^，。.！？；…）\n]*[，！.。？；…）\n]+')
    pattern = re.compile('[^，,。.！？；…（\n]*' + kw
                         + '[^，.。！？；…）\n]*[，！.。？；…）\n]+')
    plot_temp = re.findall(pattern, st)
    plot_list = plot_list + plot_temp
# print(plot_list)

# 打印定位句的情感极性并累加
for i in range(len(plot_list)):
    plot_list[i] = re.sub('[，；…）\n]+', '', plot_list[i])
    # 处理掉句末的逗号、分号、省略号、括号和换行符，保留句号、感叹号和问号
    s = SnowNLP(plot_list[i])
    # print(plot_list[i], s.sentiments)
    plot += s.sentiments
print("plot=", plot)

# 视听体验
audio_visual = 0.0
with open('视听体验.txt', 'r', encoding="utf-8") as f:
    contents = f.read().splitlines()
with open("我不是药神 Da.csv", 'r', encoding="utf-8") as fs:
    st = fs.read()
audio_visual_list = []
audio_visual = 0.0
for kw in contents:
    pattern = re.compile('[，,。.！？；…（\n]+[^，,。.！？；…（\n]*' + kw
                         + '[^，。.！？；…）\n]*[，！.。？；…）\n]+')
    pattern = re.compile('[^，,。.！？；…（\n]*' + kw
                         + '[^，.。！？；…）\n]*[，！.。？；…）\n]+')
    audio_visual_temp = re.findall(pattern, st)
    audio_visual_list = audio_visual_list + audio_visual_temp
# print(audio_visual_list)

for i in range(len(audio_visual_list)):
    audio_visual_list[i] = re.sub('[，；…）\n]+', '', audio_visual_list[i])
    s = SnowNLP(audio_visual_list[i])
    # print(audio_visual_list[i], s.sentiments)
    audio_visual += s.sentiments
print("audio_visual=", audio_visual)

# 人物塑造
with open('人物塑造.txt', 'r', encoding="utf-8") as f:
    contents = f.read().splitlines()
with open("我不是药神 Da.csv", 'r', encoding="utf-8") as fs:
    st = fs.read()
character_list = []
character = 0.0
for kw in contents:
    pattern = re.compile('[，,。.！？；…（\n]+[^，,。.！？；…（\n]*' + kw
                         + '[^，。.！？；…）\n]*[，！.。？；…）\n]+')
    pattern = re.compile('[^，,。.！？；…（\n]*' + kw
                         + '[^，.。！？；…）\n]*[，！.。？；…）\n]+')
    character_temp = re.findall(pattern, st)
    character_list = character_list + character_temp
# print(character_list)

for i in range(len(character_list)):
    character_list[i] = re.sub('[，；…）\n]+', '', character_list[i])
    s = SnowNLP(character_list[i])
    # print(character_list[i], s.sentiments)
    character += s.sentiments
print("character=", character)

# 粉丝基础
with open('粉丝基础.txt', 'r', encoding="utf-8") as f:
    contents = f.read().splitlines()
with open("我不是药神 Da.csv", 'r', encoding="utf-8") as fs:
    st = fs.read()
fan_list = []
fan = 0.0
for kw in contents:
    pattern = re.compile('[，,。.！？；…（\n]+[^，,。.！？；…（\n]*' + kw
                         + '[^，。.！？；…）\n]*[，！.。？；…）\n]+')
    pattern = re.compile('[^，,。.！？；…（\n]*' + kw
                         + '[^，.。！？；…）\n]*[，！.。？；…）\n]+')
    fan_temp = re.findall(pattern, st)
    fan_list = fan_list + fan_temp
# print(fan_list)

for i in range(len(fan_list)):
    fan_list[i] = re.sub('[，；…）\n]+', '', fan_list[i])
    s = SnowNLP(fan_list[i])
    # print(fan_list[i], s.sentiments)
    fan += s.sentiments
print("fan=", fan)

# 商业价值
with open('商业价值.txt', 'r', encoding="utf-8") as f:
    contents = f.read().splitlines()
with open("我不是药神 Da.csv", 'r', encoding="utf-8") as fs:
    st = fs.read()
commercial_list = []
commercial = 0.0
for kw in contents:
    pattern = re.compile('[，,。.！？；…（\n]+[^，,。.！？；…（\n]*' + kw
                         + '[^，。.！？；…）\n]*[，！.。？；…）\n]+')
    pattern = re.compile('[^，,。.！？；…（\n]*' + kw
                         + '[^，.。！？；…）\n]*[，！.。？；…）\n]+')
    commercial_temp = re.findall(pattern, st)
    commercial_list = commercial_list + commercial_temp
# print(commercial_list)

for i in range(len(commercial_list)):
    commercial_list[i] = re.sub('[，；…）\n]+', '', commercial_list[i])
    s = SnowNLP(commercial_list[i])
    # print(commercial_list[i], s.sentiments)
    commercial += s.sentiments
print("commercial=", commercial)

# 主题文化
with open('主题文化.txt', 'r', encoding="utf-8") as f:
    contents = f.read().splitlines()
with open("我不是药神 Da.csv", 'r', encoding="utf-8") as fs:
    st = fs.read()
conception_list = []
conception = 0.0
for kw in contents:
    pattern = re.compile('[，,。.！？；…（\n]+[^，,。.！？；…（\n]*' + kw
                         + '[^，。.！？；…）\n]*[，！.。？；…）\n]+')
    pattern = re.compile('[^，,。.！？；…（\n]*' + kw
                         + '[^，.。！？；…）\n]*[，！.。？；…）\n]+')
    conception_temp = re.findall(pattern, st)
    conception_list = conception_list + conception_temp
# print(conception_list)

for i in range(len(conception_list)):
    conception_list[i] = re.sub('[，；…）\n]+', '', conception_list[i])
    s = SnowNLP(conception_list[i])
    # print(conception_list[i], s.sentiments)
    conception += s.sentiments
print("conception=", conception)

print("观众影评库六个维度的数值计算成功！")

# 将六个维度数值转换为字符串后写入文件
with open("Da.txt", 'w', encoding="utf-8") as fa:
    fa.write(str(plot) + '\n' + str(audio_visual) + '\n' + str(character) + '\n'
             + str(fan) + '\n' + str(commercial) + '\n' + str(conception))
fa.close()
