from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import sys

text = open(sys.argv[1],'r').read()
bg_pic = imread('bg.png')

wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(text)

image_colors = ImageColorGenerator(bg_pic)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file(sys.argv[1][:sys.argv[1].find('.')] + '.png')
