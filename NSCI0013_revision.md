# NSCI0013 Revision
## OM (optical microscopy)
**visible light range:** `380-780 nm`
**resolution:** $R=\frac{0.61\lambda}{N_A},N_A=\mu sin\alpha$ ($\text{R}\downarrow \text{means resolution} \uparrow$)($N_A\uparrow,R\downarrow,\text{but result in}~D_{work}\downarrow$)

**Depth of field and depth of focus:** $D_f=\frac{1.22\lambda}{N_Atan\alpha}$ ($N_A\uparrow,D_f\downarrow,\text{but depth of focus}\uparrow$)

**Aberrations:**
- chromatic: `white light passes through a convex lens, the component wavelengths are refracted according to their frequency`
- spherical : `light rays from a point on the object on the optical axis enter a lens at different angles and cannot be focused at a singlepoint.`
- astigmatism: `rays passing through vertical diameters of the lens are not focused on the same image plane as rays passing through horizontal diameters`

**Filters:**
- neutral density (ND): `regulate light intensity without changing wavelength`
- colored: `isolate specific colors or bands of wavelength`
- heat: `absorb much of the infrared radiation which causes heating`

**Objective lens:**
- Achromat (`correction for two wavelengths, red and blue`)
- Flourite/smi-achromat (FL, `better correction`)
- apochromat (APO, `the highest degree of correction`)

**Speciman preparation:**
```
sectioning->mouting->grinding->polishing->etching
```
**Types of OM:**
- bright & dark field microscopy
- phase contrast microscopy: `condenser annulus & phase plate`
- polarized light microscopy: `only polarized light by sample can be detected`
- flourescence microscopy: `filter out excited light (without blocking emitted flourescence)`

****

## UV-Vis
**Radiation range:** `UV 220-380 nm` + `Visible 380-780 nm`
**Beer-Lambert's Law:** $A=-log(T)=log(\frac{1}{T})=\epsilon c l$
**Planck's equation:** $E=\frac{hc}{\lambda}$
**Transition:** $\pi \to \pi^*$, $n \to \pi^*$, $n \to \sigma^*$
**Integrating sphere:** measure overall or `diffuse reflectance` (transparent, translucent, and opaque solid or liquid samples)
**Process:** 
```
radiation source->(polychromatic light->entrance slit->dispersing device [prism/grating]->monochromatic light)->sample holder->detector
```
**Detectors:**
- phototubes: `light->cathode->e- out->anode->current`
- photomultiplier: `cathode emits photoelectrons->dynode->anode->current`
- silicon dioxides: `P/N junction`

**Cuvette:** 
- `longer ligth path need larger volume` and `lower concentration need longer light path`
- **Absorption < 200 nm**: `quartz or UV disposable
cuvettes`

**Data analysis:**
- high concentration->curve will not be linear
- select highest $\lambda$ with absortion (lower $\lambda$ will be absorbed by many compounds)

## FTIR & Raman

**Wavenumber and wavelength:** $\lambda (nm) = \frac{10,000,000}{\tilde{\nu} (cm^{-1})}$
**Vibration wavenumber range:** `200-4000 cm-1`
**Spring model (harmonic motion):** 
- frequency: $\nu=\frac{1}{2\pi}\sqrt{\frac{k(m_1+m_2)}{m_1m_2}}$
- wavenumber: $\bar\nu=\frac{1}{2\pi c}\sqrt{\frac{k(m_1+m_2)}{m_1m_2}}$

**Normal modes:**
- `3N-6 (non-linear)`
- `3N-5 (linear)`

**FTIR:**
- dipole moment $\uparrow$ -> adsorption $\uparrow$ `O-H > N-H > C-H`
- number of bonds $\uparrow$ -> adsorption $\uparrow$
- `Attenuated Total Reflectance (ATR)` 
  - IR beam bounces through crystal interacting with the sample multiple times
  - *uesd in the lab session*
- `Diffuse Reflectance (DRIFT)`
- Fingerprint area: `< 1500 cm-1`
- Characteristic area: `1500-4000 cm-1`


**Raman**
- Raman scattering: `inelastic scattering`
- Raman shift = $\bar\nu_{ph}-\bar\nu_{out}$
- $N_A$ $\uparrow$ -> sensitivity $\uparrow$
- De-excitation return to:
  - `Ground state` (Rayleigh scattering)
  - `Excited state` (Stokes Raman scattering)

**IR active and Ramn active**
- `dipole moment` change is `IR active`
- `polarization` change is `Raman active`
- both active example: $H_2O$
- ionic/polar bond -> `IR stronger`
- covalent bond -> `Raman stronger`
- IR active and Raman active is `mutually exclusive` in molecules which have a symmetric center (eg. $CO_2$)

**Case study-graphene:**
| peak/mode | wavenumber ($cm^{-1}$) | meaning |
| --- | --- | --- |
| G | 1580 | `intensity`: layers; `position`: doping |
| D | 1350 | defect |
| D' | 1600 | defect ($\frac{I_D}{I_{D'}}$=type of defect) |
| 2D | 2680 | `width` and `symmetry`: layers |

****

## SEM
**Resolution range:** `1 nm`
**De Broglie equation:** $\lambda=\frac{h}{mev},v(velocity)$
**Interaction volume:**
- compositional contrast-`BSE-high energy`
- topographic contrast-`SE-low energy`
- atomic number $\uparrow$ -> `BSE` large angle change $\uparrow$ -> lighter zone $\uparrow$
- $\eta=\frac{\eta_{BSE}}{\eta_{i}}$ -> sensitive to the `Z`

**Electron guns:**
- Tungsten
- Thermionic
- field emmision gun (FEG, high current & small beam spot)
  - tiny source size -> small probe size -> high resolution
  - `Temporal Coherency`: lower energy spread -> eletrons with same wavelength -> lower chromatic aberration
  - `Spatial Coherency`: tiny source size -> high spatial coherency
  - advantages compared with traditional electron gun: `FEG: small source size (nm); high brightness; high conherency; low energy spread`

**Structures:**
- `condensor lens`
  - control how many electrons
- `Aperture`
- `objective lens` (can with scanning coil)
  - focus the beam on a spot
  - **The shortest WD generates beam with the smallest diameter and gives the poorest depth of field thus getting an image with the best resolution**
- `speciman stage` (sample)
- `detector`
  - `photon multiplier`
  - `light guide`
  - `faraday cage`
- `vaccum system`


**Resolution:**
total resolution: $d_f=\sqrt{d_p^2+d_s^2+d_c^2+d_d^2}$
- $d_p=(\frac{4i_p}{\beta\pi^2\alpha^2}),~ (i_p=\text{current})$ means the probe size, which is the most important->`controlled by (1) electron gun (2) probe current (3) accelerated voltage`
- $d_s\sim C_s\alpha^3, ~(\alpha=\text{aperture angle})$ means the spherical aberration
- $d_c\sim C_c\alpha(\frac{\Delta E}{E_0})$ means chromatic aberration
- Astigmatism

**Operation variables:**
- `working distance (WD) & depth of field`: decrease aperture size and magnification, and increase WD -> increase the depth of field
- `accelerated voltage & current`: low $i_p$ -> small probe size (high resolution); high accelerated voltage -> small probe size (high resolution)

**Conductive coating:**
- vaccum evaporation
- sputtering

****

## TEM
**Resolution range:** `0.1 nm`
**Electron source:**
- `thermionic gun`: heat -> $e^-$
- `field emission gun (FEG)`: E field -> $e^-$

**Structures:**
- `electron gun (with accelerator)`
- `condense lens`
- `sample`
  - speciman trimmer & diamond knife -> Cu grid -> sample holder
  - $\text{thickness} \sim Z^2$
- `objective lens`
  - first magnified image
- `intermediate lens`
  - mode shift & magnify
- `projective lens`
  - final magnify
- `detector`
  - flourescent screen: phosphor screen
  - CCD: $e^-$ -> screen -> $h\nu$ -> CCD
  - CMOS (FET arrays): $e^-$ -> CMOS
- `vaccum system`
  - rotary puump
  - diffusion pump
  - turbo pump
  - ion getter pump
  - *illumination (highest vaccum), sample holder (medium vaccum), data recording (lowest vaccum)*
  - *$\text{Vaccum}_{TEM}>\text{Vaccum}_{SEM}$*

**Types of TEM:**
- `bright field (BF)`
- `dark field (DF)`
- `selected area electron diffraction (SAED)`: to get electron diffraction pattern
  - SAED aperture
  - back focal plane
- `high angle annular dark field (HAADF)`: $Z-contrast:~ Z\uparrow ~ brighter$
- `electron energy loss spectroscopy (EELS)`:
  - zero loss peak (ZLP) -> `thickness`
  - plasmon region -> `band gap`,`hybridization`
  - inner shell ionization -> `chemical composition`, `valance analysis` -> sensitive to low `Z`

****

## XRF
**Light range:** 
- X-ray `0.01-10 nm`
- hard X-ray `> 10 keV`; soft X-ray `< 10 keV`

**Degree of flourescence:**
- thickness
- density
- material sample

**Principle:**
```
[high energy e- -> target material] -> X-ray -> sample -> detector (semiconductor Ge/Si)
```
**X-ray analysis**
- Characteristic X-ray
- Continous X-ray (background/noise)
- setting intensity of X-ray (K-edge):
  - below K-edge: only scatter peak
  - above K-edge: $K_\alpha/K_\beta$ + scatter peak

**Auger electrons**
```
x-ray -> e(K) -> h+ -> e(L) jump to K -> emit new x-ray -> another e'(L) ejected [Auger electron]
```
**Types of XRF:**
- energy dispersive XRF (ED-XRF)
  - fast & cheap
  - poor resolution & low sensitivity to low Z
- wavelength dispersive XRF (WD-XRF)
  - high resolution & high sensitivity to low Z
  - change angle of collimator -> find out characteristic wavelength

****

## SIMS
**Method:** `destructive`, but all elements detectable
**Process:**
```
select primary ion -> change settings -> complete mass spectra
```
**Primary ion source:**
- $O_2^{2+}$ (high electronegativity) -> `positive secondary ion` -> detect $Na,Mg,B...$ (low electronegativity)
- $Cs^{+}$ (low electronegativity) -> `negative secondary ion` - detect $H,C,O,P...$ (high electronegativity)

**Mass analyzer:**
- magnetic sector
  - electrostatic -> select `v (velocity)` (E field)
  - magnetic -> `charge to mass` (B field) -> $R=\frac{mv}{qB}$
- time of flight (TOF): `lower mass` -> `higher velocity` -> `shorter time`

**Modes:**
- static SIMS: complete spectrum (low sputtering rate, low incident) -> surface -> `TOF`
- dynamic SIMS: depth profile for certain ion (high sputtering rate, high incident) -> profile of depth -> `magnetic`
- image SIMS: scan (like static)

**Total sputter yield:**
- sputter yield
- ion sputter yield
- influence by:
  - Matrix effect
  - Surface coverage of reactive elements
  - Background pressure
  - Orientation of crystallographic axes
  - Angle of emission of detected secondary ions

**SIMS vs EDX**
|TYPE | SIMS | EDX |
| :-: | :-: | :-: |
| in | ions | x-ray |
| out | secondary ions | characteristic x-ray |
| sampling depth | surface (0.5-1 nm) | deep (0.5-5 $\mu m$) |
| information | element/isotope | element composition |
| detection | 1ppm or lower (ppb) | ~hundreds ppm |
| spot size | hundreds of $\mu m$ or 1mm | 10 nm |
| depth profiling | high | low |
| insulating sample | okay | need conductive surface |
| surface damage | destructive | non-destructive |

****

## PL
**Information from $\lambda$:**
- FWHM $\downarrow$ - crystal quality $\uparrow$
- from $\lambda$ -> band gap ($E_g=\frac{hc}{\lambda}$)
- other peaks -> crystal defects/impurity

**Flourescence & phosphorescence:**
- flourescence: `S1->S0`
- phosphorescence: `T1->S0`

**Application:**
- band gap
- defect identification (semiconductor)
- impurity detection

**Case study (p13 UV-Vis vs PL):**
- UV-Vis vs PL: red shift -> Stokes shift ($\Delta \lambda \rightarrow\Delta E$)
- TRPL (time resolved PL): SLG -> carriers -> transfer charges -> lower counts of photon emission

**Quantum dot:**
- two methods of fabrication:
  - top-down
  - bottom-up
- core-shell structure:
  - post treatment (thermal annealing)
  - composition gradient
  - `QD (0-dim) - discrete DOS -> narrow band gap -> pure light`
  - `shell` can protect, deal with dangling bond
  - `ligand` can enhance stability, surface modification, ligand exchange
- `QD size` larger -> `narrow band gap` -> `red` light

****


## XPS
[Youtube video](https://youtu.be/jBd4xy7y4IU?si=Qwgf8S8G_-GcAfT_)
**Principle:**
incident light -> $e^-$ overcome BE (binding energy) -> arrive $E_F$ (Fermi energy level) -> overcome $\phi_{work function}$ -> emitted

**Levels:**
- valence level: `properties`
- core level: `element type` & `concentration`

**Spin-orbital coupling:**
total angular momentum number: `j=|l+s|`
s-orbital: `l=0`, `s=1/2,-1/2` `j=1/2`
p-orbital: `l=1`, `s=1/2.-1/2` `j=1/2 or 3/2` (2 peaks of $p^{\frac{3}{2}} ~and ~p^\frac{1}{2}$)
the number of electrons in these orbitals can be calculated: `2j+1`, for $p^{\frac{3}{2}} = 2 \times \frac{3}{2} + 1 = 4$


**Hard X-ray Photoelectron Spectroscopy (HAXPES)**
- noram XPS: `depth 4-7 nm`
- HAXPES: `depth 20-30 nm`
****

## XRD
**Measure:** the angle $2\theta$
**Bragg's equation:** $n\lambda=2dsin\theta$
**Miller indices:**
- plane (hkl) {family}
- vector [hkl] \<family\>

**Peak chracteristic:**
- `samller` angle -> `larger` distance
- `narrower` peak -> `larger` crystallite size
- **Sherrer equation:** $D=\frac{K\lambda}{\beta cos\theta}$ and $Rad=\frac{degree\times \pi}{180}$
- `intensity`:lower intensity -> less atoms present contributing to specific reflection -> detect (1) direction of growth/preferred orientation (2) point defects

**SAXS and WAXS:**
- smaller angle -> larger distance
- SAXS can be used for `microstructure`
- case: `SAXS->average shape` and `WAXS->crystall/atomic`

**Neutron diffraction:**
Neutron absorption is not tied to mass of elements in sample


****

## Conclusion for each characterization methods with application
- `SEM`: Surface details, fracture morphology or three-dimensional structure
- `TEM`: To see the atomic-level details. Observe the lattice stripes, internal defects, the precise size of nanoparticles, and the electron diffraction of extremely thin samples.
- `XRF`: Quickly and non-destructively determine which chemical elements are present in the material and their respective contents.
- `XRD`: Crystal structure. Used to distinguish whether a material is crystalline or amorphous, and to identify different mineral phases or chemical phases.
- `XPS`: The chemical information at the surface (10 nanometers) level, particularly the valence and oxidation states of the elements
- `FTIR & Raman`: Chemical bonds, molecular structure or functional groups
- `PL`: Electronic structure, especially for semiconductors and luminescent materials. Crystal quality and defects
- `SIMS`: Extremely high sensitivity (at the ppb/ppm level) is required for detecting trace elements or isotopes. It is most suitable for conducting depth profiling analysis to observe the distribution of elements along the depth.
- `UV-Vis`: Measure the concentration of the solution, the band gap of the solid, or the transparency/absorption characteristics of the coating


## Key points of last year paper:
*10 MCQ + 3-4 short answer/explanation + 1 bonus*
1. **OM resolution**
   $R=\frac{0.61\lambda}{N_A},~N_A=\mu sin\theta$
2. **OM filter**
   ND, color filter, heat filter
3. **TEM/SEM voltage & d-spacing**
   - `accelerating voltage`: high voltage -> low abberation -> small probe -> high resolution -> increase interaction volume -> but surface information vague -> low signal-noise-ratio -> sharp but coarse image
   - `voltage range`: SEM 1-30kV; TEM 80-200kV
4. **Beer-Lambert calculation**
   $A=\epsilon b c$
5. **SEM edges of spherical particles**
   `more electron` escape (compared with flat surface) -> edges of spherical particles `brighter`
6. **Vaccum system of SEM/TEM**
   Rotary pump ($10^5-10^{-4} Pa$)
   Diffusion pump ($10^0-10^{-8} Pa$)
   Turbo pump ($10^{-2}-10^{-8} Pa$)
   Ion getter pump (up to $10^{-9} Pa$, `final stage`)
7. **Quantum dots type I & II**
8. **XRD SAXS WAXS**
   XRD use `coherent scattering (elastic)`
9.  **selection of characterization methods for a certain condition**
10. **Raman of graphene**