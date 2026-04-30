# Summarized comparison table
## 1. Conventional machine learning models
### 1.1 Feature construction
- phys: 
  `length,n,m,diameter,Ti_count,FG_C=O,FG_NH2,FG_SO3H,FG_none,TiType_1Ti_substitution,TiType_1Ti_surface,TiType_2Ti_substitution,TiType_2Ti_surface,TiType_none`
- T,P: 
  `Temperature,Pressure,`
- TDA: 
  `TDA_H0_max,TDA_H0_min,TDA_H0_mean,TDA_H0_std,TDA_H0_sum,TDA_H1_max,TDA_H1_min,TDA_H1_mean,TDA_H1_std,TDA_H1_sum,TDA_H2_max,TDA_H2_min,TDA_H2_mean,TDA_H2_std,TDA_H2_sum`
- **target**: 
  `theta`

### 1.2 Summary table
| Model | phys_T,P_TDA | phys_TDA | phys_T,P | only_phys | only_TDA | only_T,P |
| --- | --- | --- | --- | --- | --- | --- |
| Linger Regression | 0.712 | -28.917 | 0.365 | -3.380 | 0.195 | 0.107 |
| XGBoost | 0.998 | -0.416 | 0.812 | -0.186 | 0.698 | 0.109 |
| SVR | 0.998 | -0.298 | 0.724 |  -0.152 | 0.677 | 0.101 |
| Random Forest | 0.994 | 0.075 | 0.779 | -0.026 | 0.700 | 0.105 |

## 2. Graph neural networks
### 2.1 Feature construction
### 2.2 Summary table
| Model | graph+T,P+TDA | graph+T,P | graph+TDA | only graph |  only T,P (MLP) | only TDA (MLP) |
| --- | --- | --- | --- | --- | --- | --- |
| Deepchem GNN | 0.936 | 0.883 | 0.823 | -0.003 | 0.131 | 0.539 |

