#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class read_data_to_plot:
    def __init__(self, if_debug):
        self.origin_data = []
        self.debug_status = if_debug

    def read_data_from_xls(self, data_file_path, data_file_name):
        """
        读取一个.xls文件的数据，保存至类的origin_data成员
        :param data_file_path: 文件所在目录
        :param data_file_name: 文件名
        :return: True/False代表是否成功读取
        """
        try:
            print("读取数据中") if self.debug_status else 0
            self.origin_data = pd.read_excel(data_file_path + data_file_name)
            print("读取数据完成") if self.debug_status else 0
        except:
            return False
        return True


class seaborn_box_plot:
    """
    seaborn的箱线图绘图常用封装
    """
    def __init__(self, data, x_label, y_label, title):
        """
        构造函数
        """
        self.origin_data = data
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        sns.set(font='SimHei')  # 解决Seaborn中文显示问题

    def plot(self):
        f, ax = plt.subplots()
        # ax = plt.subplot(2, 1, 1)
        sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data)
        ax.set_title(self.title, fontsize=15)

        ax.set_xlabel(self.x_label, fontsize=15)
        ax.set_ylabel(self.y_label, fontsize=15)
        # plt.ylim((-18, 80.0))
        plt.yticks(fontproperties='Times New Roman', size=15)
        plt.xticks(fontproperties='Times New Roman', size=15)

        plt.show()

