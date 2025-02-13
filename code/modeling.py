import data_processing as dp
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from Correlation_Analysis import correlation_analysis

def regression_model(data):
    """
    使用随机森林回归分析影响因素，输出全面评估参数
    """
    # 特征和目标值划分
    features = ['Household_Size', 'Cost_Savings_USD', 'Years_Since_Adoption', 'Subsidy_Received','Income_Level', 'Region']
    target = 'Monthly_Usage_kWh'
    X = data[features]
    y = data[target]
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 模型训练
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 模型预测
    y_pred = model.predict(X_test)
    
    # 模型评估
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # 交叉验证得分
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"R² Score: {r2}")
    print(f"Cross-Validation R² Scores: {cv_scores}")
    print(f"Mean CV R² Score: {np.mean(cv_scores)}")
    
    # 特征重要性
    feature_importances = model.feature_importances_
    feature_names = features
    plt.figure(figsize=(8, 5))
    sns.barplot(x=feature_importances, y=feature_names)
    plt.title("Feature Importance")
    plt.show()

    # 残差分析
    residuals = y_test - y_pred
    plt.figure(figsize=(8, 5))
    sns.histplot(residuals, kde=True)
    plt.title("Residual Distribution")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.show()

    return model, mse, mae, r2, cv_scores


# 执行回归模型分析
if __name__ == "__main__":
    path="d:\Desktop\stuDOC\BigData\MasterHomework\Renewable_Energy_Usage_Sampled.csv"
    data=dp.load_data(path)
    correlation_analysis(data)
    model, mse, mae, r2, cv_scores = regression_model(data)