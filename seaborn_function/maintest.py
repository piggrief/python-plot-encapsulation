#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import seaborn_function.seaborn_plot as sp
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    DataFilePath = "G:\\Program\\python-plot-encapsulation\\seaborn_function\\"
    FileName = "test_data1.xls"

    rd = sp.read_data_to_plot(True)
    rd.read_data_from_xls(DataFilePath, FileName)

    seaborn_plot = sp.plot_with_seaborn(
        rd.origin_data, x_label='开始小时', y_label='收益',
        title='在机场内一小时的平均收益随时间段变化图',
        hue_label='机场单', y_range=(0, 65)
        , background_style="whitegrid", order=[1.0, 2.0])
    seaborn_plot.stripplot(if_show=False, if_jitter=True, split=False).show()

    input()
