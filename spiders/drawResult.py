#!usr/bin/python
# -*- coding: utf-8 -*-
from pyecharts import charts

city_nums_top = ['北京', '上海', '深圳', '成都', '武汉']
city_nums_top10 = [149, 95, 77, 22]
bar = charts.Bar("数据产品经理岗位", "各城市数量")
bar.add("数据产品经理岗位", city_nums_top, city_nums_top10)
bar.render('数据产品经理岗位.html')
