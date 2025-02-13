import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    data=pd.read_csv(path)
    # print(data)
    # print(data.columns)
    # print(data.info())
    # print(data.describe())
    return data


def plot_initial_distributions(data):
    """
    绘制数据初始分布图
    """
    # 数值型变量分布
    numeric_columns = ['Monthly_Usage_kWh', 'Household_Size', 'Cost_Savings_USD']
    for column in numeric_columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(data[column], kde=True, bins=30)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    # 分类变量分布
    categorical_columns = ['Region', 'Country', 'Energy_Source', 'Urban_Rural', 'Income_Level', 'Subsidy_Received']
    for column in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(y=column, data=data, order=data[column].value_counts().index)
        plt.title(f"Count of {column}")
        plt.xlabel("Count")
        plt.ylabel(column)
        plt.show()


if __name__=="__main__":
    path="d:\Desktop\stuDOC\BigData\MasterHomework\Renewable_Energy_Usage_Sampled.csv"
    data=load_data(path)

    # features_set=features_set(data)
    # print(features_set)
    # features_list=list(features_set.keys())
    # print(features_set[features_list[2]])

    plot_initial_distributions(data)