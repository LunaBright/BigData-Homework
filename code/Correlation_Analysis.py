import data_processing as dp
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis(data):
    """
    计算数值型变量的相关性并可视化，同时输出重要信息
    """
    # 选择数值型变量
    numeric_columns = ['Monthly_Usage_kWh', 'Household_Size', 'Cost_Savings_USD']
    
    # 增加一些离散特征处理（如 'Subsidy_Received' 转换为 0/1）
    data['Subsidy_Received'] = data['Subsidy_Received'].map({'Yes': 1, 'No': 0})
    data['Income_Level'] = data['Income_Level'].map({'Low': 0, 'Middle': 1, 'High': 2})
    data['Region'] = data['Region'].map({'Africa': 0, 'South America': 1, 'Australia': 2, \
                                         'Asia': 3,'Europe': 4, 'North America': 5})
    
    # 增加年限计算
    data['Years_Since_Adoption'] = data['Year'] - data['Adoption_Year']

    # 更新数值型变量
    numeric_columns += ['Years_Since_Adoption', 'Subsidy_Received','Income_Level', 'Region']
    
    # 计算相关性矩阵
    correlation_matrix = data[numeric_columns].corr()

    # 打印相关性矩阵并绘制热力图
    print("\n相关性矩阵：")
    print(correlation_matrix)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

    return correlation_matrix

def scatter_and_box_plots(data):
    """
    绘制散点图和分类变量的箱线图，结合数值型和分类特征
    """
    # 1. 散点图 - Household_Size vs Monthly_Usage_kWh
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Household_Size', y='Monthly_Usage_kWh', hue='Region', data=data)
    plt.title("Household Size vs Monthly Usage (kWh)")
    plt.xlabel("Household Size")
    plt.ylabel("Monthly Usage (kWh)")
    plt.show()

    # 2. 散点图 - Years_Since_Adoption vs Monthly_Usage_kWh
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Years_Since_Adoption', y='Monthly_Usage_kWh', hue='Energy_Source', data=data)
    plt.title("Years Since Adoption vs Monthly Usage (kWh)")
    plt.xlabel("Years Since Adoption")
    plt.ylabel("Monthly Usage (kWh)")
    plt.show()

    # 3. 分类变量箱线图 - Income_Level vs Monthly_Usage_kWh
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Income_Level', y='Monthly_Usage_kWh', data=data)
    plt.title("Income Level vs Monthly Usage (kWh)")
    plt.xlabel("Income Level")
    plt.ylabel("Monthly Usage (kWh)")
    plt.show()



# 执行相关性分析
if __name__ == "__main__":
    path="d:\Desktop\stuDOC\BigData\MasterHomework\Renewable_Energy_Usage_Sampled.csv"
    data=dp.load_data(path)
    correlation_matrix = correlation_analysis(data)
    scatter_and_box_plots(data)