# 2 Current Danish Legislation

## 2.1 Background
In March, 2021 the Danish government came to an agreement on a national strategy for [sustainable construction](https://www.sbst.dk/byggeri/baeredygtigt-byggeri/national-strategi-for-baeredygtigt-byggeri). One part of this strategy relates to decreasing the global warming impact of the Danish construction sector. The first major step towards reaching this goal came in the form of an amendment to chapter 11 of the Danish building regulation (BR18), which introduced a requirement to document the carbon footprint of new buildings as well as limit values for larger buildings. [This amendment](https://www.sbst.dk/byggeri/baeredygtigt-byggeri/national-strategi-for-baeredygtigt-byggeri/klimakrav-lca-i-bygningsreglementet) entered into force on January 1st, 2023 , and was updated again one year later on January 1st, 2024.

## 2.2 BR18
The 2023 amendment to BR18 introduced two new paragraphs to chapter 11. The first is § 297, which states that for any new building bound by the rules for energy frameworks covered in § 259 or § 260, a calculation of the building’s life cycle carbon footprint must be performed. This, essentially, applies to all heated buildings except for temporary, movable pavilions and vacation homes.
Any building bound by § 297 with a heated floor area larger than 1,000 m² must document a life cycle climate impact equal to or less than the limit value of 12.0 kg CO₂e/m²/yr.

## 2.2.1 Requirements for the calculation
The life cycle carbon footprint calculation must be performed with a consideration period of 50 years and has to include life cycle modules colored blue in the Table 2.1. Note that module D is reported separately and does not count towards the limit value, hence why it is colored a lighter shade of blue. Module D is excluded from the carbon footprint calculation due to being considered a hypothetical benefit. There is currently no definitive way to predict whether materials will be reused or recycled at the conclusion of a project's lifecycle. Therefore, Module D accounts for potential future benefits from materials being utilized in subsequent projects after the building's demolition, which categorically places it outside the scope of the building assessment.

*Table 2.1: Overview of life cycle modules according to EN15804. Modules colored blue are included in BR18 § 297 life cycle carbon footprint calculation.*

![image](https://github.com/user-attachments/assets/455dcc85-ecc2-40e9-8698-aa944804e708)

## 2.2.2 The building model
The carbon footprint of materials is calculated per m² of floor area with the following special modifications:
1.	All basement areas, refuse storage rooms at terrain level and air raid shelters are included.
2.	External ramps, stairs, balconies, and similar elements are included with 25% of their area.
3.	Integrated garages are included with 50% of their area.
4.	Integrated carports, sheds, coverings and similar are included with 25% of their area.
5.	Walk-on ceilings and similar are included with 25% of their area.
6.	Non-integrated garages and carports as well as sheds, greenhouses, covered terraces, utilized roof areas, and similar are not included.

Materials and building elements included in the life cycle carbon footprint calculation are described in BR18 Appendix 2, Table 6 – Building components for calculating climate impact, which can be downloaded [here](https://www.bygningsreglementet.dk/Bilag/B2/Bilag_2/Tabel_6#e53ebfa8-1dea-4737-aa53-69c8a848b30c) (only available in Danish). Some notable exclusions are permanent inventory (toilets, showers, ovens etc.) and all electrical and mechanical installations except solar panels and transportation devices (elevators, lifts, escalators).

Material carbon footprint is calculated either using the generic data basis described in BR18 Appendix 2, table 7 – Generic data basis, which can be downloaded [here](https://www.bygningsreglementet.dk/Bilag/B2/Bilag_2/Tabel_7#787e83a6-b7d9-4a83-a4be-37574156daef) (only available in Danish), or through Environmental Product Declarations (EPD). To use an EPD within the calculation, it must be representative of the material used in the building and must be valid at the date of being implemented into the building.

The BR18 generic data basis also describes a set of default values for technical installations within the building, which can be used as an alternative to save time, instead of calculating the carbon footprint of the specific materials and products used in the installation. The default values can be found in BR18 Appendix 2, table 7. The default values state a climate impact per m² of heated floor area plus heated basement area.

The service life of products and materials are stated in BUILD REPORT 2021:32, which can be found [here](https://vbn.aau.dk/da/publications/build-levetidstabel-version-2021) (only available in Danish). If the service life of a product or materials is shorter than the consideration period of 50 years, it is assumed to be replaced within the consideration period and, therefore, the climate impact of the replacement must also be included in the BR18 LCA as part of module B4. Module B4 is effectively the sum of climate impact of modules A1-3, C3, and C4 from the replacement product. Figure 2.1 shows an example of how module B4 is calculated for a product with a service life of 20 years.

![image](https://github.com/user-attachments/assets/6b3f89c9-ee55-4f13-ba3e-0095c2f6b3fe)  
*Figure 2.1: Illustration showing how climate impact from module B4 is calculated for a product with a service life of 20 years*

As of January 1st, 2024, the climate impact of directly reused building materials is considered to be 0 throughout the entire consideration period in a BR18 LCA. This also means that replacement is also considered to have a climate impact of 0 in the BR18 LCA when using reused materials. Directly reused materials must be included in the BR18 LCA, so it is visible that the materials have been used, but the climate impact is calculated as 0.

## 2.2.3 Operational energy use
The energy framework calculation’s result is needed to calculate the climate impact of the building’s operational energy use (module B6).  To calculate the climate impact of module B6 in a BR18 LCA, the energy requirements from the energy framework calculation without primary energy factors must be used. Emission factors for operational energy use are described in BR18 Appendix 2, table 8 – Emission factors for electricity, district heating and gas, which can be found [here](https://www.bygningsreglementet.dk/bilag/b2/bilag_2/tabel_8/#c93d7bfe-6c32-4182-b858-cf113ba2a371) (only available in Danish). 

## 2.2.4 Special building conditions
For some buildings, special conditions regarding the function of the building can lead to a significantly higher climate impact. For example, if the soil conditions are unfavorable, the foundations might need to be much bigger, leading to a higher climate impact than other buildings. In such cases the climate impact of the building is allowed to exceed the limit value by a certain amount. Please note that this only applies to the individual constructions affected by the special conditions. Keep in mind that only conditions important to the function of the building are granted this bonus, where conditions caused by aesthetic choices are not. It is recommended that any special conditions are clarified with the local municipality to ensure that the building is granted the expected allowable exceedance.

### 2.2.4.1 Constructions
To calculate the allowable exceedance for most constructions, the following formula is used:

![image](https://github.com/user-attachments/assets/bf040906-375d-4c2a-a454-8dfb108fe51d)

where

***x*** is the climate impact of the affected construction over the 50 year consideration period (kg CO₂e)

***r*** is the reference value for the given construction type (kg CO₂e/m²/yr)

***m*** is the area of the affected construction (m²)

***a*** is the reference area of the LCA calculation (m²)

The reference values used to calculate the allowable exceedance can be found in BR18 Appendix 2, table 9 – Reference values for the calculation of climate impact, which are not included in the calculation according to § 298, paragraph 1, which can be found here (only available in Danish). 

### 2.2.4.2 Foundations
To calculate the allowable exceedance for foundations (except for slab foundations), the following formula is used:

![image](https://github.com/user-attachments/assets/824c330e-3f69-4c44-8a9c-fa11445e1da5)

where

***x*** is the climate impact of the affected construction over the 50 year consideration period (kg CO₂e)

***r*** is the reference value for foundations (1.06 kg CO₂e/m²/yr)

***a*** is the reference area of the LCA calculation (m²)

### 2.2.4.3 Columns and beams
To calculate the allowable exceedance for columns and beams, the following formula is used:

![image](https://github.com/user-attachments/assets/cf130e4d-7698-442b-ace2-947689d6c787)

where

***r*** is the reference value for columns and beams (0.47 kg CO₂e/m/yr)

***m*** is the length of the affected columns/beams (m²)

***a*** is the reference area of the LCA calculation (m²)

### 2.2.4.4 Technical installations
To calculate the allowable exceedance for technical installations, the following formula is used:

![image](https://github.com/user-attachments/assets/700d5eb4-fc26-426c-9ca7-554896c3dd26)

where

***i*** is the climate impact of the actual installations over the 50 year consideration period (kg CO₂e)

***s*** is the reference default value for installations in “Other buildings” defined in BR18 Appendix 2, table 7 (kg CO₂e/m²/yr)

***eopv*** is the sum of the total heated floor area and the heated basement area (m²)

***a*** is the reference area of the LCA calculation (m²)

Sources:

- National strategi for bæredygtigt byggeri. (n.d.). https://www.sbst.dk/byggeri/baeredygtigt-byggeri/national-strategi-for-baeredygtigt-byggeri

- Klimakrav (LCA) i bygningsreglement. (n.d.). https://www.sbst.dk/byggeri/baeredygtigt-byggeri/national-strategi-for-baeredygtigt-byggeri/klimakrav-lca-i-bygningsreglementet

- BR18. (n.d.). https://www.bygningsreglementet.dk/Bilag/B2/Bilag_2/Tabel_6#e53ebfa8-1dea-4737-aa53-69c8a848b30c

- BR18. (n.d.-b). https://www.bygningsreglementet.dk/Bilag/B2/Bilag_2/Tabel_7#787e83a6-b7d9-4a83-a4be-37574156daef

- Haugbølle, K., Mahdi, V., Morelli, M., & Wahedi, H. (2021, December 2). BUILD levetidstabel: Version 2021. Aalborg Universitets Forskningsportal. https://vbn.aau.dk/da/publications/build-levetidstabel-version-2021

- BR18. (n.d.-c). https://www.bygningsreglementet.dk/bilag/b2/bilag_2/tabel_8/#c93d7bfe-6c32-4182-b858-cf113ba2a371











