# Summarized comparison table
## Conventional machine learning models
| Model | all features | no T,P | no TDA | no T,P and TDA | only TDA | only T,P |
| --- | --- | --- | --- | --- | --- | --- |
| Linger Regression | 0.712 | -28.917 | 0.365 | -3.380 | 0.195 | 0.107 |
| XGBoost | 0.998 | -0.416 | 0.812 | -0.186 | 0.698 | 0.109 |
| SVR | 0.998 | -0.298 | 0.724 |  -0.152 | 0.677 | 0.101 |
| Random Forest | 0.994 | 0.075 | 0.779 | -0.026 | 0.700 | 0.105 |
## Graph neural networks
| Model | graph+T,P+TDA | graph+T,P | graph+TDA | only graph |  only T,P (MLP) | only TDA (MLP) |
| --- | --- | --- | --- | --- | --- | --- |
| Deepchem GNN | 0.936 | 0.883 | 0.823 | -0.003 | 0.131 | 0.539 |