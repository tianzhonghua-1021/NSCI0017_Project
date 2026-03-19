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

*Note: the unit of $\Delta G$ is eV (transfer from Hartree by Gaussian)*
## Machine learning models comparison
### Model selection
### Framework
### Feature engineering
### Metrics comparison
### Uncertainty and applicability
### Interpretation

## Graph neural network from Deepchem
### Model selection
### Framework
### Feature engineering
### Metrics comparison
### Uncertainty and applicability
### Interpretation
