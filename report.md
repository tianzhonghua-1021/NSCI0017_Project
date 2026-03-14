# Comparison with DeepChemGNN and MLs
## Machine learning models
### Dataset structure
```
colnames = [
    'FileID', 
    'Temperature', 
    'E', 
    'G', 
    'Pressure' , 
    'length', 
    'n', 
    'm', 
    'diameter', 
    'Ti_count', 
    'FG_C=O', 
    'FG_NH2', 
    'FG_SO3H', 
    'FG_none', 
    'TiType_1Ti_substitution', 
    'TiType_1Ti_surface', 
    'TiType_2Ti_substitution', 
    'TiType_2Ti_surface', 
    'TiType_none', 
    'TDA_H0_max', 
    'TDA_H0_min', 
    'TDA_H0_mean', 
    'TDA_H0_std', 
    'TDA_H0_sum', 
    'TDA_H1_max', 
    'TDA_H1_min', 
    'TDA_H1_mean', 
    'TDA_H1_std', 
    'TDA_H1_sum', 
    'TDA_H2_max', 
    'TDA_H2_min', 
    'TDA_H2_mean', 
    'TDA_H2_std', 
    'TDA_H2_sum', 
    'theta'
    ]
shape is: (1760, 31)
```
### Input features
```
X = df.drop(['G','E', 'theta','FileID'], axis=1)
y = df['theta']
```
### Model selection
```
rf = RandomForestRegressor(random_state=42)
svr = SVR()
lr = LinearRegression()
xgb = XGBRegressor(random_state=42, objective='reg:squarederror')
```
### Parameter setting
```
rf_param_grid = {
    'n_estimators': [50, 100, 200], 
    'max_depth': [5, 10, 15]
}
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
grid_rf = GridSearchCV(rf, rf_param_grid, cv=5)
grid_svr = GridSearchCV(svr, svr_param_grid, cv=5)
grid_xgb = GridSearchCV(xgb, xgb_param_grid, cv=5)
```
### Metrics (without $\Delta G$)
The comparison of scatter plots with 4 ML models:
![figure.1](/model_comparison.png)
The SHAP analysis for feature importance:<br>
| <div style="width:50px">Model</div> | Beeswarm | Bar |
| --- | --- | --- |
| **RF** |![figure.2](/Random_Forest_shap_beeswarm.png)|![figure.3](/Random_Forest_shap_bar.png)|
| **LR** | ![figure.4](/Linear_Regression_shap_beeswarm.png) | ![figure.5](/Linear_Regression_shap_bar.png) |
| **SVR** | ![figure.6](/SVR_shap_beeswarm.png) | ![figure.7](/SVR_shap_bar.png) |
| **XGBoost** | ![figure.8](/XGBoost_shap_beeswarm.png) | ![figure.9](/XGBoost_shap_bar.png) |
## DeepChem GNN model
### Dataset structure
### Input features
### Metrics