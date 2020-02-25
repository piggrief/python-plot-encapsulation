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


class plot_with_seaborn:
    """
    seaborn的箱线图绘图常用封装
    """
    def __init__(self, data, x_label, y_label, title, hue_label=[], font_size=18,
                 x_range=[], y_range=[], palette=[], background_style=[], order=[]):
        """
        boxplot构造函数，用来配置一些绘图参数
        sample:
        seaborn_plot = sp.plot_with_seaborn(rd.origin_data,
                               x_label='开始小时', y_label='收益',
                              title='在机场内一小时的平均收益随时间段变化图',
                              hue_label='机场单', y_range=(0, 65)
                              , background_style="whitegrid", order=[1.0, 2.0])

        :param data:用于绘图的原始数据
        :param x_label:x轴标签
        :param y_label:y轴标签
        :param title:图表标题
        :param hue_label:划分标签
        :param font_size:字体大小
        :param x_range:x轴范围，如(0, 10.5)
        :param y_range:y轴范围，如(0, 10.5)
        :param palette:调色板，如“Set3”
        :param background_style:背景样式，如"whitegrid"
        :param order:显示的x轴的取值范围，也可理解为约束，如[1.0, 2.0]
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
        self.order = order
        if [] != background_style:
            sns.set(style=background_style, font='SimHei')

    def boxplot(self, if_show):
        """
        根据定义的参数绘制箱线图
        :param if_show:是否直接显示，True的话会直接调用plt.show()，
                                     False的话会返回plt句柄
        :return:plt句柄，可用于后续对图表的自定义修改
        """
        f, ax = plt.subplots()
        # ax = plt.subplot(2, 1, 1)
        if not self.hue_label:
            if [] == self.palette:
                if [] == self.order:
                    sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data)
                else:
                    sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                                order=self.order)
            else:
                if [] == self.order:
                    sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                                palette=self.palette)
                else:
                    sns.boxplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                                palette=self.palette, order=self.order)
        else:
            if [] == self.palette:
                if [] == self.order:
                    sns.boxplot(x=self.x_label, y=self.y_label, hue=self.hue_label
                                , data=self.origin_data)
                else:
                    sns.boxplot(x=self.x_label, y=self.y_label, hue=self.hue_label
                                , data=self.origin_data, order=self.order)
            else:
                if [] == self.order:
                    sns.boxplot(x=self.x_label, y=self.y_label, hue=self.hue_label
                                , data=self.origin_data, palette=self.palette)
                else:
                    sns.boxplot(x=self.x_label, y=self.y_label, hue=self.hue_label
                                , data=self.origin_data, palette=self.palette, order=self.order)
        ax.set_title(self.title, fontsize=self.font_size)

        ax.set_xlabel(self.x_label, fontsize=self.font_size)
        ax.set_ylabel(self.y_label, fontsize=self.font_size)
        if self.x_range:
            plt.xlim(self.x_range)
        if self.y_range:
            plt.ylim(self.y_range)

        plt.yticks(fontproperties='Times New Roman', size=self.font_size)
        plt.xticks(fontproperties='Times New Roman', size=self.font_size)

        if if_show:
            plt.show()
            return []
        else:
            return plt

    def violinplot(self, if_show, split=True):
        """
        根据定义的参数绘制箱线图
        :param if_show:是否直接显示，True的话会直接调用plt.show()，
                                     False的话会返回plt句柄
        :param split:如果有分组的话是否对半拼接显示
        :return:plt句柄，可用于后续对图表的自定义修改
        """
        f, ax = plt.subplots()
        # ax = plt.subplot(2, 1, 1)
        if not self.hue_label:
            if [] == self.palette:
                if [] == self.order:
                    sns.violinplot(x=self.x_label, y=self.y_label, data=self.origin_data)
                else:
                    sns.violinplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                                   order=self.order)
            else:
                if [] == self.order:
                    sns.violinplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                                   palette=self.palette)
                else:
                    sns.violinplot(x=self.x_label, y=self.y_label, data=self.origin_data,
                                   palette=self.palette, order=self.order)
        else:
            if [] == self.palette:
                if [] == self.order:
                    sns.violinplot(x=self.x_label, y=self.y_label, hue=self.hue_label,
                                   data=self.origin_data, split=split)
                else:
                    sns.violinplot(x=self.x_label, y=self.y_label, hue=self.hue_label,
                                   data=self.origin_data, order=self.order, split=split)
            else:
                if [] == self.order:
                    sns.violinplot(x=self.x_label, y=self.y_label, hue=self.hue_label,
                                   data=self.origin_data, palette=self.palette, split=split)
                else:
                    sns.violinplot(x=self.x_label, y=self.y_label, hue=self.hue_label, split=split,
                                   data=self.origin_data, palette=self.palette, order=self.order)
        ax.set_title(self.title, fontsize=self.font_size)

        ax.set_xlabel(self.x_label, fontsize=self.font_size)
        ax.set_ylabel(self.y_label, fontsize=self.font_size)
        if self.x_range:
            plt.xlim(self.x_range)
        if self.y_range:
            plt.ylim(self.y_range)

        plt.yticks(fontproperties='Times New Roman', size=self.font_size)
        plt.xticks(fontproperties='Times New Roman', size=self.font_size)

        if if_show:
            plt.show()
            return []
        else:
            return plt

