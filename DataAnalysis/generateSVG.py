import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import sys

f_name = sys.argv[1]
f = open(f_name, "r")
d = eval(f.read())
del d['JavaScript']
del d['None']
# Line
my_style = 	LS('#336699', base_style = LCS)
copy_write = 'Created By Xiaoqiang Wang 2018.6\n' + 'A Naive Python Project in Pygal'
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = 'Most Popular Programming Language or topics in Github\n' + copy_write
chart_items = d.items()
chart_items = sorted(chart_items, key = lambda x: x[0], reverse = True)
chart.x_labels = [i[0] for i in chart_items]
chart.add('', [i[1] for i in chart_items])
chart.render_to_file(f_name[:f_name.find('.')] + '2.svg')