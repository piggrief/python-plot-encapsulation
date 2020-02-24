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
    def __init__(self, data, x_label, y_label, title, hue_label=[], font_size=18,
                 x_range=[], y_range=[], palette=[], background_style=[]):
        """
        构造函数
        """
        self.origin_data = data
        self.x_label = x_label
        self.y_label = y_label
        self.hue_label = hue_label
        self.font_size = font_size
        self.title = title
        self.x_range = x_range
        self.y_range = y_range
        self.palette = palette

        if [] != background_style:
            sns.set(style=background_style, font='SimHei')

    def plot(self):
        f, ax = plt.subplots()
        # ax = plt.subplot(2, 1, 1)
        if not self.hue_label:
            if [] == self.palette:
                sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data)
            else:
                sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                            palette=self.palette)
        else:
            if [] == self.palette:
                sns.boxplot(x=self.x_label, y=self.y_label, hue=self.hue_label
                            , data=self.origin_data)
            else:
                sns.boxplot(x=self.x_label, y=self.y_label, hue=self.hue_label
                            , data=self.origin_data, palette=self.palette)
        ax.set_title(self.title, fontsize=self.font_size)

        ax.set_xlabel(self.x_label, fontsize=self.font_size)
        ax.set_ylabel(self.y_label, fontsize=self.font_size)
        if self.x_range:
            plt.xlim(self.x_range)
        if self.y_range:
            plt.ylim(self.y_range)

        plt.yticks(fontproperties='Times New Roman', size=self.font_size)
        plt.xticks(fontproperties='Times New Roman', size=self.font_size)

        plt.show()

