# NSCI0013 Revision
## OM (optical microscopy)
**visible light range:** `380-780 nm`
**resolution:** $R=\frac{0.61\lambda}{N_A},N_A=\mu sin\alpha$ ($\text{R}\downarrow \text{means resolution} \uparrow$)($N_A\uparrow,R\downarrow,D_{work}\downarrow$)

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
- Fingerprint area: `1500-5000 cm-1`


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

****


## TEM

****


## XRF

****


## SIMS

****


## PL

****


## XPS

****


## XRD

****

