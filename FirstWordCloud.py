# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba

'''利用jieba分词后，制作词云，并画成图，保存到本地'''

with open('19Da.txt', 'r', encoding='utf-8') as f:
    mytext = f.read()
mytext = " ".join(jieba.cut(mytext))
font = r'C:\Windows\Fonts\simfang.ttf'
backgroud_Image = plt.imread('tree.jpg')
wc = WordCloud(
    collocations=False,
    background_color='white',
    mask=backgroud_Image,
    font_path=font,
    width=2400,
    height=2400,
    margin=3).generate(
        mytext.lower())
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('19DaTree.png')
