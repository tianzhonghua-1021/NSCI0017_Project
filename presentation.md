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
### Pearson correlation analysis
![figure17](/Feature_Analysis_correlation_matrix.png)
Based on the plot of Pearson correlation, the next experiment is to remove the features which have the highest correlationship with others (threshold of coefficient is 0.9)
```
def remove_high_correlation_features(X, threshold=0.9):
    corr_matrix = X.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    
    print(f"There are {len(to_drop)} features (r > {threshold}):")
    print(to_drop)
    X_dropped = X.drop(columns=to_drop)
    return X_dropped, to_drop
```
And the output following the drop of features
```
There are 8 features (r > 0.9):
['m', 'diameter', 'TiType_none', 'TDA_H1_sum', 'TDA_H2_max', 'TDA_H2_mean', 'TDA_H2_std', 'TDA_H2_sum']
```
**Drop the high corelated features**
```
X, dropped_cols = remove_high_correlation_features(X, threshold=0.9)
```
**Stratify the dataset based on label ($\theta$)**
```
y_bins = pd.cut(y, bins=5, labels=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y_bins, shuffle=True)
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
```
[File ID, Temperature (K), G, Pressure (bar), theta]
dataset shape: 1760x5
```
### Input features
```
data[0] structure:
Node Feats: (132, 133)
Edge Index: (2, 348)
Edge Feats: (348, 14)
Global Feats: (19) # T,P,G (or without G),1/T,lnP+15*TDA
y: [0.513297]
```
### Model structure
```
num_epochs = 500
model = dc.models.torch_models.DMPNNModel(
    mode='regression',
    n_tasks=1,
    batch_size=64,
    global_features_size=19 (or 20),  #T,P,G (or without G),1/T,lnP+15*TDA
    enc_hidden=32,  # Size of hidden layer in the encoder layer
    ffn_hidden=32,  # Size of hidden layer in the feed-forward network layer
    ffn_layers=3,    # Number of layers in the feed-forward network layer
    # learning_rate=1e-4,
    ffn_dropout_p = 0.3,
    learning_rate=dc.models.optimizers.ExponentialDecay(5e-4, 0.9, 1000)
)
```
### Metrics
| with $\Delta G$ | without $\Delta G$ |
| --- | --- |
|![figure10](/TDA%20with%20G/learning_curve.png) | ![figure11](/TDA%20without%20G/learning_curve.png)|
|![figure12](/TDA%20with%20G/result.png)|![figure13](/TDA%20without%20G/result.png)|
|![figure14](/TDA%20with%20G/shap_importance_bar.png)|![figure15](/TDA%20without%20G/shap_importance_bar.png)|
|![figure16](/TDA%20with%20G/shap_summary.png)| ![figure17](/TDA%20without%20G/shap_summary.png)|


