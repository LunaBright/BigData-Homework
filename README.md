# 代码使用说明

## 主要工作
通过数据特征的相关性分析和建立随机森林回归模型分析，探讨影响家庭可再生能源使用量的主要因素。

## 基于数据集[“Global Renewable Energy Usage（2020-2024）”](https://www.kaggle.com/datasets/hajraamir21/global-renewable-energy-usage-2020-2024)

## 代码结构
`data_processing.py` 数据读入和可视化（数据分布直方图）

`Correlation_Analysis.py` 相关性分析与可视化

`modeling.py` 随机森林回归建模

## 代码使用方法
1.下载依赖包  
2.下载数据集（通过官网下载/直接从本仓库下载）  
3.依次运行三个.py文件：`data_processing.py`、`Correlation_Analysis.py`、`modeling.py`