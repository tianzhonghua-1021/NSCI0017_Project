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
**with $\Delta G$ version**
```
X = df.drop(['E', 'theta','FileID'], axis=1)
y = df['theta']
```
**without $\Delta G$ version**
```
X = df.drop(['G','E', 'theta','FileID'], axis=1)
y = df['theta']
```
### Pearson correlation analysis
![figure17](/MLs_without_G/Feature_Analysis_correlation_matrix.png)
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
### Metrics (with $\Delta G$)
The comparison of scatter plots with 4 ML models:
![figure.1](/MLs_with_G/model_comparison.png)
The SHAP analysis for feature importance:<br>
| <div style="width:50px">Model</div> | Beeswarm | Bar |
| --- | --- | --- |
| **RF** |![figure.2](/MLs_with_G/Random_Forest_shap_beeswarm.png)|![figure.3](/MLs_with_G/Random_Forest_shap_bar.png)|
| **LR** | ![figure.4](/MLs_with_G/Linear_Regression_shap_beeswarm.png) | ![figure.5](/MLs_with_G/Linear_Regression_shap_bar.png) |
| **SVR** | ![figure.6](/MLs_with_G/SVR_shap_beeswarm.png) | ![figure.7](/MLs_with_G/SVR_shap_bar.png) |
| **XGBoost** | ![figure.8](/MLs_with_G/XGBoost_shap_beeswarm.png) | ![figure.9](/MLs_with_G/XGBoost_shap_bar.png) |


### Metrics (without $\Delta G$)
The comparison of scatter plots with 4 ML models:
![figure.1](/MLs_without_G/model_comparison.png)
The SHAP analysis for feature importance:<br>
| <div style="width:50px">Model</div> | Beeswarm | Bar |
| --- | --- | --- |
| **RF** |![figure.2](/MLs_without_G/Random_Forest_shap_beeswarm.png)|![figure.3](/MLs_without_G/Random_Forest_shap_bar.png)|
| **LR** | ![figure.4](/MLs_without_G/Linear_Regression_shap_beeswarm.png) | ![figure.5](/MLs_without_G/Linear_Regression_shap_bar.png) |
| **SVR** | ![figure.6](/MLs_without_G/SVR_shap_beeswarm.png) | ![figure.7](/MLs_without_G/SVR_shap_bar.png) |
| **XGBoost** | ![figure.8](/MLs_without_G/XGBoost_shap_beeswarm.png) | ![figure.9](/MLs_without_G/XGBoost_shap_bar.png) |

### Metrics (file id split without $\Delta G$)
The comparison of scatter plots with 4 ML models:
![figure.1](/MLs_fileid/model_comparison.png)
The SHAP analysis for feature importance:<br>
| <div style="width:50px">Model</div> | Beeswarm | Bar |
| --- | --- | --- |
| **RF** |![figure.2](/MLs_fileid/Random_Forest_shap_beeswarm.png)|![figure.3](/MLs_without_G/Random_Forest_shap_bar.png)|
| **LR** | ![figure.4](/MLs_fileid/Linear_Regression_shap_beeswarm.png) | ![figure.5](/MLs_fileid/Linear_Regression_shap_bar.png) |
| **SVR** | ![figure.6](/MLs_fileid/SVR_shap_beeswarm.png) | ![figure.7](/MLs_fileid/SVR_shap_bar.png) |
| **XGBoost** | ![figure.8](/MLs_fileid/XGBoost_shap_beeswarm.png) | ![figure.9](/MLs_fileid/XGBoost_shap_bar.png) |

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

## Discussion
- TDA descriptors are efficient to capture the structural information
- The scaffold is important for diversity of CNTs, and there is a need for more data but with new automated process or smarter algorithm to decide which will be included experiment.
- **Next steps: which way shoud to be selected**: (1) imporve the optimization of hyperparameters (2) inegrated active learning try (3) create more data automately.


<br>

---
## The result of Deepchem GNN with only T, P (no $\Delta G$)
The model was trained with only T, P for the global features because there is a high dependent on T and P for the $\theta$. <br>
![figurea1](/no_global_with_T_P/learning_curve.png)
![figurea2](/no_global_with_T_P/result.png)
![figurea3](/no_global_with_T_P/shap_importance_bar.png)
![figurea4](/no_global_with_T_P/shap_summary.png)

## The bar code for 44 SWCNTs' structures
| No | Bar code plot |
| --- | --- |
| 1 | ![figure](./tda_barcodes/1_barcode.png) |
| 2 | ![figure](./tda_barcodes/2_barcode.png) |
| 3 | ![figure](./tda_barcodes/3_barcode.png) |
| 4 | ![figure](./tda_barcodes/4_barcode.png) |
| 5 | ![figure](./tda_barcodes/5_barcode.png) |
| 6 | ![figure](./tda_barcodes/6_barcode.png) |
| 7 | ![figure](./tda_barcodes/7_barcode.png) |
| 8 | ![figure](./tda_barcodes/8_barcode.png) |
| 9 | ![figure](./tda_barcodes/9_barcode.png) |
| 10 | ![figure](./tda_barcodes/10_barcode.png) |
| 11 | ![figure](./tda_barcodes/11_barcode.png) |
| 12 | ![figure](./tda_barcodes/12_barcode.png) |
| 13 | ![figure](./tda_barcodes/13_barcode.png) |
| 14 | ![figure](./tda_barcodes/14_barcode.png) |
| 15 | ![figure](./tda_barcodes/15_barcode.png) |
| 16 | ![figure](./tda_barcodes/16_barcode.png) |
| 17 | ![figure](./tda_barcodes/17_barcode.png) |
| 18 | ![figure](./tda_barcodes/18_barcode.png) |
| 19 | ![figure](./tda_barcodes/19_barcode.png) |
| 20 | ![figure](./tda_barcodes/20_barcode.png) |
| 21 | ![figure](./tda_barcodes/21_barcode.png) |
| 22 | ![figure](./tda_barcodes/22_barcode.png) |
| 23 | ![figure](./tda_barcodes/23_barcode.png) |
| 24 | ![figure](./tda_barcodes/24_barcode.png) |
| 25 | ![figure](./tda_barcodes/25_barcode.png) |
| 26 | ![figure](./tda_barcodes/26_barcode.png) |
| 27 | ![figure](./tda_barcodes/27_barcode.png) |
| 28 | ![figure](./tda_barcodes/28_barcode.png) |
| 29 | ![figure](./tda_barcodes/29_barcode.png) |
| 30 | ![figure](./tda_barcodes/30_barcode.png) |
| 31 | ![figure](./tda_barcodes/31_barcode.png) |
| 32 | ![figure](./tda_barcodes/32_barcode.png) |
| 33 | ![figure](./tda_barcodes/33_barcode.png) |
| 34 | ![figure](./tda_barcodes/34_barcode.png) |
| 35 | ![figure](./tda_barcodes/35_barcode.png) |
| 36 | ![figure](./tda_barcodes/36_barcode.png) |
| 37 | ![figure](./tda_barcodes/37_barcode.png) |
| 38 | ![figure](./tda_barcodes/38_barcode.png) |
| 39 | ![figure](./tda_barcodes/39_barcode.png) |
| 40 | ![figure](./tda_barcodes/40_barcode.png) |
| 41 | ![figure](./tda_barcodes/41_barcode.png) |
| 42 | ![figure](./tda_barcodes/42_barcode.png) |
| 43 | ![figure](./tda_barcodes/43_barcode.png) |
| 44 | ![figure](./tda_barcodes/44_barcode.png) |

## Discussion
- what about the closed loop and story (the most worry is FILE ID)? how far it will be a publication for publication?
- what format is best recommended to display clearly for the whole project ($Gaussian \rightarrow Model \rightarrow Results$)
- should I pay more effort on active learning based on this project or the next one?