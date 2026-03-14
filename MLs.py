import pandas as pd
import numpy as np
import shap
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor # RF
from sklearn.linear_model import LinearRegression # LR
from sklearn.svm import SVR # SVR
from xgboost import XGBRegressor # XGBoost
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt



# shap with visualization
def run_shap_analysis(model, X_test_scaled, feature_names, model_name="Model"):
    X_df = pd.DataFrame(X_test_scaled, columns=feature_names)
    print(f"Calculating {model_name} for SHAP values")
    
    if "RandomForest" in str(type(model)):
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_df)
    else:
        X_summary = shap.sample(X_df, 50) 
        explainer = shap.KernelExplainer(model.predict, X_summary)
        shap_values = explainer.shap_values(X_summary)
        X_df = X_summary
    # 1. Beeswarm Plot
    plt.figure(figsize=(5, 5),dpi=300)
    shap.summary_plot(shap_values, X_df, plot_type="dot", show=False)
    plt.title(f"SHAP Beeswarm Plot: {model_name}")
    plt.tight_layout()
    plt.savefig(f'{model_name}_shap_beeswarm.png', bbox_inches='tight')
    # 2. Bar Plot
    plt.figure(figsize=(5, 5),dpi=300)
    shap.summary_plot(shap_values, X_df, plot_type="bar", show=False)
    plt.title(f"SHAP Feature Importance: {model_name}")
    plt.tight_layout()
    plt.savefig(f'{model_name}_shap_bar.png', bbox_inches='tight')
    return shap_values



csv_dir = r"D:\UCL Courses\NSCI0016 Literature Report\dataset and models\deepchem\0314analysis\dataset_full_feat.csv"
colnames = ['FileID', 'Temperature', 'E', 'G', 'Pressure' , 'length', 'n', 'm', 'diameter', 'Ti_count', 'FG_C=O', 'FG_NH2', 'FG_SO3H', 'FG_none', 'TiType_1Ti_substitution', 'TiType_1Ti_surface', 'TiType_2Ti_substitution', 'TiType_2Ti_surface', 'TiType_none', 'TDA_H0_max', 'TDA_H0_min', 'TDA_H0_mean', 'TDA_H0_std', 'TDA_H0_sum', 'TDA_H1_max', 'TDA_H1_min', 'TDA_H1_mean', 'TDA_H1_std', 'TDA_H1_sum', 'TDA_H2_max', 'TDA_H2_min', 'TDA_H2_mean', 'TDA_H2_std', 'TDA_H2_sum', 'theta']
df = pd.read_csv(csv_dir)
df.columns = df.columns.str.strip()
# transfer to numeric variables
df = pd.get_dummies(df)
# data splitting (change for "with G" and "without G")
X = df.drop(['G','E', 'theta','FileID'], axis=1)
y = df['theta']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
scaler_X = StandardScaler()
X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled = scaler_X.transform(X_test)

# load model
rf = RandomForestRegressor(random_state=42)
svr = SVR()
lr = LinearRegression()
xgb = XGBRegressor(random_state=42, objective='reg:squarederror')
# define the parameter grid
rf_param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [5, 10, 15]}
svr_param_grid = {
    'C': [0.1, 1, 10, 100],
    'epsilon': [0.01, 0.1, 0.2],
    'kernel': ['rbf']
}
xgb_param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 6],
    'subsample': [0.8, 1.0]
}
# initialize the grid search object
grid_rf = GridSearchCV(rf, rf_param_grid, cv=5)
grid_rf.fit(X_train_scaled, y_train)
grid_svr = GridSearchCV(svr, svr_param_grid, cv=5)
grid_svr.fit(X_train_scaled, y_train)
grid_xgb = GridSearchCV(xgb, xgb_param_grid, cv=5)
grid_xgb.fit(X_train_scaled, y_train)
lr.fit(X_train_scaled, y_train) 

# make predictions on the test set
best_rf = grid_rf.best_estimator_
best_svr = grid_svr.best_estimator_
best_xgb = grid_xgb.best_estimator_

y_pred_rf = best_rf.predict(X_test_scaled)
y_pred_svr = best_svr.predict(X_test_scaled)
y_pred_lr = lr.predict(X_test_scaled)
y_pred_xgb = best_xgb.predict(X_test_scaled)

# get performance
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
r2_svr = r2_score(y_test, y_pred_svr)
rmse_svr = np.sqrt(mean_squared_error(y_test, y_pred_svr))
r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
r2_xgb = r2_score(y_test, y_pred_xgb)
rmse_xgb = np.sqrt(mean_squared_error(y_test, y_pred_xgb))

# visualization
plt.figure(figsize=(15, 15), dpi=300)

# RF
plt.subplot(2, 2, 1)
plt.scatter(y_test, y_pred_rf, alpha=0.6, edgecolors='k', color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.title(f'Random Forest (R2={r2_rf:.3f} RMSE= {rmse_rf:.4f})')
plt.xlabel('Measured Theta')
plt.ylabel('Predicted Theta')

# SVR
plt.subplot(2, 2, 2)
plt.scatter(y_test, y_pred_svr, alpha=0.6, edgecolors='k', color='green')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.title(f'SVR (R2={r2_svr:.3f} RMSE= {rmse_svr:.4f})')
plt.xlabel('Measured Theta')
plt.ylabel('Predicted Theta')

# LR
plt.subplot(2, 2, 3)
plt.scatter(y_test, y_pred_lr, alpha=0.6, edgecolors='k', color='orange')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.title(f'Linear Regression\n(R2={r2_lr:.3f} RMSE={rmse_lr:.4f})')
plt.xlabel('Measured Theta')
plt.ylabel('Predicted Theta')
plt.tight_layout()
plt.savefig('model_comparison.png')

# XGBoost
plt.subplot(2, 2, 4)
plt.scatter(y_test, y_pred_xgb, alpha=0.6, edgecolors='k', color='royalblue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.title(f'XGBoost\n(R2={r2_xgb:.3f} RMSE={rmse_xgb:.4f})')
plt.xlabel('Measured Theta')
plt.ylabel('Predicted Theta')

plt.tight_layout()
plt.savefig('model_comparison.png')


# shap
shap_values_rf = run_shap_analysis(best_rf, X_test_scaled, X.columns, model_name="Random_Forest")
shap_values_svr = run_shap_analysis(best_svr, X_test_scaled, X.columns, model_name="SVR")
shap_values_lr = run_shap_analysis(lr, X_test_scaled, X.columns, model_name="Linear_Regression")
shap_values_xgb = run_shap_analysis(best_xgb, X_test_scaled, X.columns, model_name="XGBoost")