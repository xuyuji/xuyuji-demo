import datetime
import os

from wand.image import Image  # pip install Wand

PDF_SOURCE = 'TuringCalendar2018.pdf[{}]'  # 下载的PDF日历路径
BACKGROUND_SOURCE = 'background.jpg'  # 使用的壁纸
OUTPUT = 'backgrounds/turing_day{}.jpg'  # 生成的壁纸路径
OUTPUT_FLODER = 'backgrounds';  # 生成壁纸目录

if not os.path.exists(OUTPUT_FLODER):
    os.makedirs(OUTPUT_FLODER)

PAGE_OFFSET = 6  # 周历从PDF文档的第7页开始
MARGIN_RIGHT = 1200  # 周历的右边距
MARGIN_TOP = 200  # 周历的上边距

for week in range(1, 54):
    with Image(filename=PDF_SOURCE.format(week + PAGE_OFFSET), resolution=200) as calendar:
        with Image(filename=BACKGROUND_SOURCE) as background:
            for week_day in range(1, 7):
                day = (week - 1) * 7 + week_day;
                background.composite_channel('default_channels', calendar, 'blend',
                                             background.page_width - MARGIN_RIGHT, MARGIN_TOP)
                background.save(filename=OUTPUT.format(day))
