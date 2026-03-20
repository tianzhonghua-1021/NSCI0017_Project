# Prediction of $H_2$ adsorption coverage of single-walled carbon nanotubes: A study based on structural characteristics described by topological descriptors and machine learning models

## Experiment design
### Doped metal atoms: Titanium (Ti)
**Experiments Reference**: [1] https://doi.org/10.1016/S0009-2614(00)01162-3
**DFT/MD Reference**: [2] https://doi.org/10.1038/s41598-025-26005-0 (*Nature-scientific report*)
**Found**: The **concentration**-capacity of adsorption of $H_2$ is nonlinear [2]
`Variables: (1) number (concentration) (2) position (surface or substitution)`
### Functional group:
**Experiment Reference**: [1] https://doi.org/10.1016/j.carbon.2020.10.038 ($NH_2$) [2] https://doi.org/10.1016/j.jssc.2007.12.017 ($-SO_3H$)
**DFT/MD Reference**: [3] https://doi.org/10.1016/j.cej.2024.158989
**Found**: The **sensitivity of $H_2$** follows: $-SO_3H > -C=O > -NH_2$ [3]
`Variables: (1) -SO3H (2) -NH2 (3) -C=O all sidewall modification`

So, the summarized table described as below:

| No | Chirality | Length | Functional Group | Doped Ti |
| --- | --- | --- | --- | --- |
| 1 | 6,6 | 10 | none | none |
| 2 | 6,6 | 13 | none | none |
| 3 | 6,6 | 15 | none | none |
| 4 | 6,6 | 20 | none | none |
| 5 | 6,6 | 10 | SO3H | none |
| 6 | 6,6 | 10 | C=O | none |
| 7 | 6,6 | 10 | NH2 | none |
| 8 | 6,6 | 10 | none | 1Ti_surface |
| 9 | 6,6 | 10 | none | 1Ti_substitution |
| 10 | 6,6 | 10 | none | 2Ti_surface |
| 11 | 6,6 | 10 | none | 2Ti_substitution |
| 12 | 7,5 | 10 | none | none |
| 13 | 7,5 | 13 | none | none |
| 14 | 7,5 | 15 | none | none |
| 15 | 7,5 | 20 | none | none |
| 16 | 7,5 | 10 | SO3H | none |
| 17 | 7,5 | 10 | C=O | none |
| 18 | 7,5 | 10 | NH2 | none |
| 19 | 7,5 | 10 | none | 1Ti_surface |
| 20 | 7,5 | 10 | none | 1Ti_substitution |
| 21 | 7,5 | 10 | none | 2Ti_surface |
| 22 | 7,5 | 10 | none | 2Ti_substitution |
| 23 | 13,1 | 10 | none | none |
| 24 | 13,1 | 13 | none | none |
| 25 | 13,1 | 15 | none | none |
| 26 | 13,1 | 20 | none | none |
| 27 | 13,1 | 10 | SO3H | none |
| 28 | 13,1 | 10 | C=O | none |
| 29 | 13,1 | 10 | NH2 | none |
| 30 | 13,1 | 10 | none | 1Ti_surface |
| 31 | 13,1 | 10 | none | 1Ti_substitution |
| 32 | 13,1 | 10 | none | 2Ti_surface |
| 33 | 13,1 | 10 | none | 2Ti_substitution |
| 34 | 13,2 | 10 | none | none |
| 35 | 13,2 | 13 | none | none |
| 36 | 13,2 | 15 | none | none |
| 37 | 13,2 | 20 | none | none |
| 38 | 13,2 | 10 | SO3H | none |
| 39 | 13,2 | 10 | C=O | none |
| 40 | 13,2 | 10 | NH2 | none |
| 41 | 13,2 | 10 | none | 1Ti_surface |
| 42 | 13,2 | 10 | none | 1Ti_substitution |
| 43 | 13,2 | 10 | none | 2Ti_surface |
| 44 | 13,2 | 10 | none | 2Ti_substitution |
## Gaussian calculation
**Process:** The workflow can be described as:
```
PM6 (get MM charge) -> UFF -> add H2 -> ONIOM -> freq -> Langmuir equation
```
**PM6 setting:**
```
%chk=1.chk
%mem=4GB
%nprocshared=8
# opt pm6 pop=regular scf=xqc
```
**UFF setting:**
```
%chk=1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc
```
**ONIOM setting:**
```
%chk=1.chk
%mem=4GB
%nprocshared=8
# opt oniom(b3lyp/6-31+g(d):uff)=embedcharge scf=xqc
```
**freq (for SWCNT) setting:**
```
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=77.0

Title: Frequency calculation at 77K

0 1 0 1 0 1

77.0 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=100.0

Title: Temperature at 100K

0 1 0 1 0 1

100.0 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=273.0

Title: Temperature at 273K

0 1 0 1 0 1

273 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=298.15

Title: Temperature at 298.15K

0 1 0 1 0 1

298.15 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=400.0

Title: Temperature at 400K

0 1 0 1 0 1

400.0 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=500.0

Title: Temperature at 500K

0 1 0 1 0 1

500.0 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=600.0

Title: Temperature at 600K

0 1 0 1 0 1

600.0 1.0

--Link1--
%chk=/home/ucaqzti/data/uff/1.chk
%mem=4GB
%nprocshared=8
# opt freq uff scf=xqc geom=check Temperature=700.0

Title: Temperature at 700K

0 1 0 1 0 1

700.0 1.0


```
**freq (for complex) setting:**
```
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=77.0

Title: Frequency calculation at 77K

0 1 0 1 0 1

77.0 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=100.0

Title: Temperature at 100K

0 1 0 1 0 1

100.0 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=273.0

Title: Temperature at 273K

0 1 0 1 0 1

273 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=298.15

Title: Temperature at 298.15K

0 1 0 1 0 1

298.15 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=400.0

Title: Temperature at 400K

0 1 0 1 0 1

400.0 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=500.0

Title: Temperature at 500K

0 1 0 1 0 1

500.0 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=600.0

Title: Temperature at 600K

0 1 0 1 0 1

600.0 1.0

--Link1--
%chk=/home/ucaqzti/data/oniom/1.chk
%mem=4GB
%nprocshared=8
# freq(readiso,readfc) oniom(b3lyp/6-31+g(d):uff)=embedcharge geom=check Temperature=700.0

Title: Temperature at 700K

0 1 0 1 0 1

700.0 1.0

```
**Langmuir equation**
After the Gaussian calculation, the $\Delta G$ of different $T$ had been obtained.
The $\theta$ means the coverage ratio of adsorption, and there are 5 selected pressure (from 1 to 5 bar) to do the calculation with Langmuir equation:

$$K = \exp\left( -\frac{\Delta G^\circ}{RT} \right)$$

$$\theta = \frac{K \cdot (P/P^\circ)}{1 + K \cdot (P/P^\circ)}$$

Hence, all the data has been obtained.
## Dataset construction
| File ID | Temperature (K) | G | Pressure (bar) | theta |
| --- | --- | --- | --- | --- |
| 1 | 77 | -0.000353 | 1 | 0.513297|
| ... | ... | ... | ... | ... |

*Note:* the unit of $\Delta G$ is eV (transfer from Hartree by Gaussian)

## Machine learning models comparison
### Model selection
```
rf = RandomForestRegressor(random_state=42)
svr = SVR()
lr = LinearRegression()
xgb = XGBRegressor(random_state=42, objective='reg:squarederror')
```
### Framework
**The dataset loading**
```
csv_dir = r"D:\UCL Courses\NSCI0016 Literature Report\dataset and models\deepchem\0314analysis\dataset_full_feat.csv"
colnames = ['FileID', 'Temperature', 'E', 'G', 'Pressure' , 'length', 'n', 'm', 'diameter', 'Ti_count', 'FG_C=O', 'FG_NH2', 'FG_SO3H', 'FG_none', 'TiType_1Ti_substitution', 'TiType_1Ti_surface', 'TiType_2Ti_substitution', 'TiType_2Ti_surface', 'TiType_none', 'TDA_H0_max', 'TDA_H0_min', 'TDA_H0_mean', 'TDA_H0_std', 'TDA_H0_sum', 'TDA_H1_max', 'TDA_H1_min', 'TDA_H1_mean', 'TDA_H1_std', 'TDA_H1_sum', 'TDA_H2_max', 'TDA_H2_min', 'TDA_H2_mean', 'TDA_H2_std', 'TDA_H2_sum', 'theta']
df = pd.read_csv(csv_dir)
X = df.drop(['G','E', 'theta','FileID'], axis=1)
y = df['theta']
```
**Pearson correlation analysis and drop features with high correlation**
```
# Pearson analysis
analysis_df = X.copy()
analysis_df['theta'] = y 
plot_correlation_matrix(analysis_df, model_name="Feature_Analysis")
X, dropped_cols = remove_high_correlation_features(X, threshold=0.9)
feature_names = X.columns.tolist()
```
**Data split**
```
# divide the label into bins
y_bins = pd.cut(y, bins=5, labels=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y_bins, shuffle=True)
```
**Normalization**
```
scaler_X = StandardScaler()
X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled = scaler_X.transform(X_test)
```
**Grid search**
```
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
```
**Boostrap uncertainty**
```
models_to_analyze = [
    (best_rf, "Random_Forest"),
    (best_svr, "SVR"),
    (lr, "Linear_Regression"),
    (best_xgb, "XGBoost")
]

uncertainty_results = {}

for model_obj, name in models_to_analyze:
    std_uncertainty = analyze_model_uncertainty(
        model=model_obj, 
        X_train=X_train_scaled, 
        y_train=y_train, 
        X_test=X_test_scaled, 
        n_iterations=15, # You can increase this for better precision
        model_name=name
    )
    uncertainty_results[name] = std_uncertainty
```
### Feature engineering
Pearson correlation heatmap:
![fig](/MLs_without_G/Feature_Analysis_correlation_matrix.png)
### Metrics comparison (Scatter, SHAP, Uncertainty)
#### Simple feature (without TDA)
**Feature:**
```
'Temperature', 'Pressure' , 'length', 'n', 'm', 'diameter', 'Ti_count', 'FG_C=O', 'FG_NH2', 'FG_SO3H', 'FG_none', 'TiType_1Ti_substitution', 'TiType_1Ti_surface', 'TiType_2Ti_substitution', 'TiType_2Ti_surface', 'TiType_none'
```
**Model comparison**
![fig](/ML_without_G_and_TDA/model_comparison.png)

| Model | SHAP bar | SHAP beeswarm | Uncertainty |
| --- | --- | --- | --- |
| LR | ![fig](/ML_without_G_and_TDA/Linear_Regression_shap_bar.png) | ![fig](/ML_without_G_and_TDA/Linear_Regression_shap_beeswarm.png) | ![fig](/ML_without_G_and_TDA/Linear_Regression_uncertainty_analysis.png) |
| RF | ![fig](/ML_without_G_and_TDA/Random_Forest_shap_bar.png) | ![fig](/ML_without_G_and_TDA/Random_Forest_shap_beeswarm.png) | ![fig](/ML_without_G_and_TDA/Random_Forest_uncertainty_analysis.png) |
| SVR | ![fig](/ML_without_G_and_TDA/SVR_shap_bar.png) | ![fig](/ML_without_G_and_TDA/SVR_shap_beeswarm.png) | ![fig](/ML_without_G_and_TDA/SVR_uncertainty_analysis.png) |
| XGBoost | ![fig](/ML_without_G_and_TDA/XGBoost_shap_bar.png) | ![fig](/ML_without_G_and_TDA/XGBoost_shap_beeswarm.png) | ![fig](/ML_without_G_and_TDA/XGBoost_uncertainty_analysis.png) |

#### Complex feature (with TDA)
**Feature:**
```
'Temperature', 'Pressure' , 'length', 'n', 'm', 'diameter', 'Ti_count', 'FG_C=O', 'FG_NH2', 'FG_SO3H', 'FG_none', 'TiType_1Ti_substitution', 'TiType_1Ti_surface', 'TiType_2Ti_substitution', 'TiType_2Ti_surface', 'TiType_none', 'TDA_H0_max', 'TDA_H0_min', 'TDA_H0_mean', 'TDA_H0_std', 'TDA_H0_sum', 'TDA_H1_max', 'TDA_H1_min', 'TDA_H1_mean', 'TDA_H1_std', 'TDA_H1_sum', 'TDA_H2_max', 'TDA_H2_min', 'TDA_H2_mean', 'TDA_H2_std', 'TDA_H2_sum'
```
**Model comparison**
![fig](/MLs_without_G/model_comparison.png)
| Model | SHAP bar | SHAP beeswarm | Uncertainty |
| --- | --- | --- | --- |
| LR | ![fig](/MLs_without_G/Linear_Regression_shap_bar.png) | ![fig](/MLs_without_G/Linear_Regression_shap_beeswarm.png) | ![fig](/MLs_without_G/Linear_Regression_uncertainty_analysis.png) |
| RF | ![fig](/MLs_without_G/Random_Forest_shap_bar.png) | ![fig](/MLs_without_G/Random_Forest_shap_beeswarm.png) | ![fig](/MLs_without_G/Random_Forest_uncertainty_analysis.png) |
| SVR | ![fig](/MLs_without_G/SVR_shap_bar.png) | ![fig](/MLs_without_G/SVR_shap_beeswarm.png) | ![fig](/MLs_without_G/SVR_uncertainty_analysis.png) |
| XGBoost | ![fig](/MLs_without_G/XGBoost_shap_bar.png) | ![fig](/MLs_without_G/XGBoost_shap_beeswarm.png) | ![fig](/MLs_without_G/XGBoost_uncertainty_analysis.png) |

## Graph neural network from Deepchem
### Model selection
**GNN model selection**
- Deepchem [DMPNN](https://deepchem.readthedocs.io/en/latest/api_reference/models.html) model and [ref](https://arxiv.org/pdf/1904.01561).
- Invoke the model `model = dc.models.torch_models.DMPNNModel` and `featurizer = dc.feat.DMPNNFeaturizer()`

**Interpretation strategy selection**
- Integrated Gradient(IG), [ref](https://arxiv.org/abs/1703.01365).

### Framework
**The total process can be display as below:**

```
data_prepare.py -> csv (atom type, x, y, z) -> model.load -> model.split -> model.train -> model.test -> model.analysis
```

**data prepare**
Extract the `atom type` and `xyz` coordinates from gjf files and create new csv files matched the name.

```
for filename in os.listdir(input_folder):
        if filename.endswith(".gjf"):
            file_path = os.path.join(input_folder, filename)
            try:
                file_id_match = re.search(r'(\d+)', filename)
                if file_id_match:
                    original_id = int(file_id_match.group(1))
                    new_id = original_id + 44
                    csv_filename = f"{new_id}.csv"
                else:
                    print(f"skip {filename}: not found the number")
                    continue
            except Exception as e:
                print(f"dealing with {filename} get error: {e}")
                continue
            # ---------------------------
            with open(file_path, 'r') as f:
                lines = f.readlines()

            # find the start of coordinate
            coords = []
            start_reading = False
            
            for line in lines:
                line = line.strip()
                # match the charge line
                if re.match(r'^-?\d+\s+\d+$', line):
                    start_reading = True
                    continue
                
                if start_reading:
                    # if space line
                    if not line:
                        break
                    
                    # divide atom type and coordinate
                    parts = line.split()
                    if len(parts) >= 4:
                        coords.append(parts[:4])

            # transfer to DataFrame
            df = pd.DataFrame(coords, columns=['Element', 'X', 'Y', 'Z'])
```
**load data**
```
if os.path.exists(target_csv):
            mol = csv_to_rdkit_mol_safe(target_csv)
            if mol:
                feat = featurizer.featurize([mol])
                if len(feat) > 0:
                    T = float(row['Temperature (K)'])
                    P = float(row['Pressure (bar)'])
                    phys_feats = [float(row['Temperature (K)']), float(row['Pressure (bar)'])]
                    combined_global = np.concatenate([phys_feats])
                    
                    temp_graphs.append(feat[0])
                    temp_globals.append(combined_global)
                    y_list.append([row['theta']])
                    w_list.append([1.0])
                    f_ids.append(fid)
```

**scaling and dataframe**

```
scaler = StandardScaler()
scaled_globals = scaler.fit_transform(temp_globals)

X = np.array(X_list, dtype=object)
y = np.array(y_list)
w = np.array(w_list)
dataset = dc.data.DiskDataset.from_numpy(X=X, y=y, w=w, ids=f_ids, data_dir=dataset_cache_dir)
```

**data splitting**

```
splitter = dc.splits.RandomSplitter()
train_dataset, test_dataset = splitter.train_test_split(dataset, frac_train=0.8, seed=42)
```

**model construction**

```
model = dc.models.torch_models.DMPNNModel(
    mode='regression',
    n_tasks=1,
    batch_size=64,
    global_features_size=2,  #T,P
    enc_hidden=32,  # Size of hidden layer in the encoder layer
    ffn_hidden=32,  # Size of hidden layer in the feed-forward network layer
    ffn_layers=3,    # Number of layers in the feed-forward network layer
    # learning_rate=1e-4,
    ffn_dropout_p = 0.3,
    learning_rate=dc.models.optimizers.ExponentialDecay(5e-4, 0.9, 1000)
)
```
**model training**

```
num_epochs = 500
train_losses = []
for epoch in range(num_epochs):
    loss = model.fit(train_dataset, nb_epoch=1)
    train_losses.append(loss)
```

### Feature engineering
```
node_feat=[N,133]
edge_feat=[E,14]
cat_feat=[E,147]
encoder_output=[1,32] # enc_hidden=32
global_feat=[2] # T&P
combine_input=[1,34] # combine global_feat
output = [1,1] # theta
```

### Metrics comparison
**GNN result analysis**
Due to that there are only 2 global features (T&P), so the SHAP feature importance analysis has only 2 bars and clusters in the figures below.

| **Scatter plot** | **Learning curve** |
| :--- | :--- |
| ![fig](/GNN_without_TDA/result.png) | ![fig](/GNN_without_TDA/learning_curve.png) |
| **SHAP bar** | **SHAP beeswarm** |
| ![fig](/GNN_without_TDA/shap_importance_bar.png) | ![fig](/GNN_without_TDA/shap_summary.png) |

**Uncertainty analysis**

```
# random sampling
train_indices = np.random.choice(len(train_dataset), len(train_dataset), replace=True)
        resampled_train = train_dataset.select(train_indices)

# New model instance with identical hyperparams
boot_model = dc.models.torch_models.DMPNNModel(
            mode='regression',
            n_tasks=1,
            batch_size=64,
            global_features_size=2, 
            enc_hidden=32,
            ffn_hidden=32,
            ffn_layers=3,
            ffn_dropout_p=0.3,
            learning_rate=5e-4
        )
# Model training
boot_model.fit(resampled_train, nb_epoch=100)

# Prediction
preds_raw = boot_model.predict(test_dataset)
preds = transformers[0].untransform(preds_raw).flatten()
all_boot_preds.append(preds)

# Get results
all_boot_preds = np.array(all_boot_preds)
mean_preds = np.mean(all_boot_preds, axis=0)
std_devs = np.std(all_boot_preds, axis=0)
```

![fig](/GNN_without_TDA/uncertainty_analysis.png)

Based on the `Uncertainty analysis`, we can see the high certainty prediction on the data with high $\theta$ resulting from the distribution of input dataset. For the data with lower value of the label, the uncertainty increases.

**Interpretation**

Because of the highly integrated structure of DPMNN from DeepChem, the `Integrated Gradient (IG)` has been selected in explanation section. The IG process involves uniformly decomposing the molecular characteristics from a "completely blank" state to a "real state" into multiple steps. The cumulative model then calculates the sensitivity (gradient) of the characteristics' changes at each step, thereby accurately determining the contribution of each atom to the prediction result.

The core function of `Integrated Gradient (IG)` is:

$$\text{IntegratedGrads}_i(x) \colon\colon= (x_i - x'_i) \times \int_{\alpha=0}^{1} \frac{\partial F(x' + \alpha(x - x'))}{\partial x_i} d\alpha$$

$\alpha(x - x')$ :
```
f_step = f_ini_baseline + alpha * (f_ini_orig - f_ini_baseline)
```
$\frac{\partial F}{\partial x_i}$:
```
output = py_model(pyg_batch)
loss = output.sum()
loss.backward()
```
$\int_{\alpha=0}^{1} ... d\alpha$:
```
if f_step.grad is not None:
    total_grads += f_step.grad
```
$(x_i - x'_i)$:
```
edge_importance = ((f_ini_orig - f_ini_baseline) * (total_grads / n_steps)).sum(dim=-1)
```

After the integral cumulation, the structural importance graphs can be obtained:

| No | Structural importance |
| :--- | :--- |
| 1 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_1.png) |
| 2 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_2.png) |
| 3 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_3.png) |
| 4 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_4.png) |
| 5 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_5.png) |
| 6 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_6.png) |
| 7 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_7.png) |
| 8 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_8.png) |
| 9 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_9.png) |
| 10 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_10.png) |
| 11 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_11.png) |
| 12 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_12.png) |
| 13 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_13.png) |
| 14 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_14.png) |
| 15 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_15.png) |
| 16 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_16.png) |
| 17 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_17.png) |
| 18 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_18.png) |
| 19 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_19.png) |
| 20 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_20.png) |
| 21 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_21.png) |
| 22 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_22.png) |
| 23 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_23.png) |
| 24 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_24.png) |
| 25 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_25.png) |
| 26 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_26.png) |
| 27 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_27.png) |
| 28 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_28.png) |
| 29 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_29.png) |
| 30 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_30.png) |
| 31 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_31.png) |
| 32 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_32.png) |
| 33 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_33.png) |
| 34 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_34.png) |
| 35 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_35.png) |
| 36 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_36.png) |
| 37 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_37.png) |
| 38 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_38.png) |
| 39 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_39.png) |
| 40 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_40.png) |
| 41 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_41.png) |
| 42 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_42.png) |
| 43 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_43.png) |
| 44 | ![fig](/GNN_without_TDA/test_set_ig_maps/atom_ig_44.png) |

