# Summary of the ZH-1 project: Interpretable ML predict adsorption of $H_2$ by SWCNT

## Conventional machine learning models
### Summary Table ($R^2$)
| Model | All features | no (T,P) | no (TDA) | no (T,P) and (TDA) |
| --- | --- | --- | --- | --- |
| Linger Regression | 0.712 | -28.917 | 0.365 | -3.380 |
| XGBoost | 0.998 | -0.416 | 0.812 | -0.186 |
| SVR | 0.998 | -0.298 | 0.724 |  -0.152 |
| Random Forest | 0.994 | 0.075 | 0.779 | -0.026 |

*For `All features, no (TDA)`, the dataset is `1760 data with T,P`; for `no (T,P), no (T,P) and (TDA)`, the dataset is `44 data without T,P`.*

### Result and analysis
**Limition of dataset:** For model training without T and P, only 44 SWCNT structure can not be used for machine learning training.

**Non-linear relationship:** Due to the poor performance of LR, it means that the relationship among $\theta$, $\Delta G$ and strutral features is non-linear.

**High importance of P:** That indicates the models such as RF, XGBoost and SVR have the ability to capture non-linear relationship based on Langmuir Equation.

**High importance of TDA_H0 and TDA_H1 series:** The TDA_H0 and TDA_H1 represent atomic distance (atom density in atomic scale) and rings, respectively. According to the SHAP analysis of RF, XGBoost and SVR, the density of carbon atoms and minimum size of rings have significant influence to the result. **Additionally, integrating TDA descriptors have obviously improved the prediction**
![fig](/Sum_ML_all/Random_Forest_shap_beeswarm.png)
![fig](/Sum_ML_all/SVR_shap_beeswarm.png)
![fig](/Sum_ML_all/XGBoost_shap_beeswarm.png)


## Deepchem based GNN
### Summary Table ($R^2$)
| Model | Only graph | with (TDA) and (T,P) | with (T,P) | 
| --- | --- | --- | --- | 
| simple GNN | -0.01 | 0.606 | 0.687 |
| deepchem GNN | -0.086 | 0.936 | 0.883 |
| deepchem GNN + GNNExplainer | none | none | none |
| deepchem GNN + Integrated Gradient | done | done | done |

*For `Only graph`, the dataset contains of only 44 SWCNT structures; for `with (TDA) and (T,P)` and `with (T,P)`, the dataset contains of full 1760 datapoints*
### Explainer (based on deepchem GNN)
#### GNNExplainer
Need to be integrated and tested.
#### Integrated Gradient
*Reference:*
- Blog (Chinese, need translator): http://home.ustc.edu.cn/~liujunyan/blog/Integrated-Gradients-IG/ 
- Paper: https://arxiv.org/abs/1611.02639

There are 44 molecular structures with coolwarm color extracted from IG explainer. The figures show that the deepchem GNN have the ability to understand different dopant or functional groups in the complex, according to the specific patterns with darker color.
For example, the explainer shows that Ti obtains the most important score in the `Ti` doped SWCNT, and the atoms surrounding Ti have been influenced as well:
![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_20.png)

### Result and analysis
**Importance of integrating T,P as features:** Compared with the result of `only graph` and `with (T,P`, the $R^2$ has been improved significantly from -0.086 to 0.883. That's because the $\theta$ is greatly dependent on tempreature and pressure. Hence, only the graph can not capture sufficient features of SWCNTs.
*Note: in this case, each $\theta$ was created by frequency DFT calculation (with 7 temperature) and Langmuir equation (with 5 pressure).*

**Efficiency of deepchem architecture:** According to the results between simple GNN and deepchem one, the deepchem architecture can capture more structural information to get better performance.

**Influence of TDA descriptors:** Compared with deepchem GNN + TDA and deepchem GNN + only T,P, the result shows the enhancement made by TDA descriptors.

## Appendix
Code files and dataset: `Zhonghua Tian ZH-1/Python codes/0330deepchem`

Deepchem GNN (only graph): `dc_gnnv4_onlygraph.py`
Deepchem GNN (with T,P): `dc_gnnv4_ig.py`
Deepchem GNN (with T,P and TDA): `dc_gnnv3_tda.py`
Simple GNN (onlygraph/with T,P): `s_gnn.py`
Simple GNN (with TDA): `s_gnn_tda.py`
1760 dataset: `dataset_form.csv`
44 dataset: `dataset_form_noTP.csv`
Environment: `requirement.txt`