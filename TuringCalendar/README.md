# 图灵编程日历壁纸生成工具

## 来历

图灵社区2018年初推出了一款[编程日历](http://www.ituring.com.cn/book/2625)，限量1000份，很多人没买到，于是给出了电子版，看到一篇[博客](https://www.jianshu.com/p/912ce01d4752)，博主利用这个电子版日历生成壁纸。

稍微改了改，当做笔记，以后有新日历的时候还能派上用场。

## 介绍

1. TodayCalendar：博主的代码，生成嵌入当前周日历的壁纸。把日历位置改为靠右。
2. WeekCalendar：生成每周的日历壁纸。
3. DayOfYearCalendar：生成每天的日历壁纸。一周的都是一样的，这么做是为了使用win10的幻灯片壁纸，这个功能最大值是一天，不能设成一周。

## 我的环境

win10

python3.7.0 x86

wand 0.4.4

[ImageMagick-6.9.6-8-Q8-x86-dll](https://ftp.icm.edu.pl/packages/ImageMagick/binaries/)

[Ghostscript 9.23 for Windows (32 bit)](https://www.ghostscript.com/download/gsdnld.html)