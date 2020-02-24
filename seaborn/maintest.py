#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    rd = read_data_to_plot()
    DataFilePath = "G:\\Program\\python-plot-encapsulation\\seaborn\\"
    FileName = "test_data1.xls"
    print("读取数据中")
    Data = pd.read_excel(DataFilePath + FileName)
    print("读取数据完成")

    sns.set(font='SimHei')  # 解决Seaborn中文显示问题

    # f, ax = plt.subplots()
    ax = plt.subplot(2, 1, 1)
    sns.boxplot(x='开始小时', y='收益', data=Data)
    ax.set_title('在机场内一小时的平均收益随时间段变化图', fontsize=15)

    ax.set_xlabel('', fontsize=15)
    ax.set_ylabel('在机场内一小时的平均收益', fontsize=15)
    plt.ylim((-18, 80.0))
    plt.yticks(fontproperties='Times New Roman', size=15)
    plt.xticks(fontproperties='Times New Roman', size=15)
    plt.show()
    input()
