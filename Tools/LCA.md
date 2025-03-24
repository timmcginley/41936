# LCA Calculation for Renovated Buildings (DGNB-Compliant)
This page provides a practical summary for a DGNB Compliant LCA Calculation for renovated buildings.

## 1. Define Your LCA Scope
*	Timeframe: 50 years (as per DGNB and EN 15978).
*	Functional unit: 1 m² of gross floor area (GFA) over 50 years.
*	Life cycle stages:
    *	A1–A3: Material production
    *	B4: Replacements (e.g., windows, HVAC)
    *	B6: Operational energy (heating, cooling, lighting, etc.)
    *	C3–C4: End-of-life (demolition, disposal)
    *	D: Reuse/recycling benefits (report separately)

## 2. Collect Input Data
*	Material quantities:
    *	From BIM/Revit models or renovation drawings.
    *	Include insulation, windows, HVAC, façade cladding, etc.
*	Product data:
    *	Use EPDs (Environmental Product Declarations) – prioritize product-specific EPDs.
*	Replacements:
    *	Find expected service lives (e.g., paint every 10 years, windows every 30 years).
    *	Multiply original material impact by number of replacements.
*	Operational energy:
    *	Estimate annual consumption (kWh/m²/year) for:
        * Electricity
        * Heating
        * Possibly cooling and DHW
    * Include updated systems post-renovation.
* Emission factors:
    * Use national values or DGNB defaults (e.g., kg CO₂e/kWh for electricity and heating).

## 3. Model in LCA Software (e.g., SimaPro)
###	1. Start a New Project
Name your project and define the functional unit (e.g., “1 m² renovated area / 50 years”).
### 2. Build the Life Cycle Inventory (LCI)
For each material:
  * Use SimaPro’s library to find the closest EPD or generic dataset (e.g., mineral wool, aluminum window frame).
  * If EPD is not available, input data manually using process creation.
  * Input quantities per m² or for the entire building, then normalize later.
### 3. Model Replacements (B4)
  * Multiply initial material amounts by the number of expected replacements within 50 years.
  * Add as separate processes or increase the quantity accordingly.
### 4. Add Operational Energy (B6)
  * Select “Electricity, low voltage, DK mix” or other relevant sources.
  * Multiply annual use by 50 (or enter total for 50 years).
  * Include both regulated and unregulated energy, if required.
### 5. End-of-Life (C3, C4) and Module D
  * Add disposal processes (e.g., landfill, incineration).
  * Include recycling credits in Module D but report them separately.
### 6. Select Impact Assessment Method
  * Use EN 15804, CML-IA, or ReCiPe Midpoint.
  * Focus on GWP (kg CO₂e) and other DGNB categories: AP, EP, POCP, ADP, etc.
### 7. Run Calculation
  * Analyze total environmental impacts.
  * Break down by life cycle stage and material where possible.
### 8. Normalize Results
Convert total impact to:
  * kg CO₂e/m² over 50 years
  * or kg CO₂e/m²/year for DGNB comparison
________________________________________
## 4. Calculate Environmental Impacts
*	Use EN 15804 or CML impact method.
*	Focus on:
o	GWP (Global Warming Potential) – in kg CO₂e/m²/year.
o	Also include Acidification (AP), Eutrophication (EP), and other DGNB impact categories.
•	Normalize total impacts to:
o	kg CO₂e/m²/50 years
o	or kg CO₂e/m²/year (for DGNB comparison)
________________________________________
## 5. Interpret the Results
•	Identify carbon hotspots (e.g., insulation, HVAC, operational energy).
•	Compare results with DGNB target:
o	Aim for <9.4 kg CO₂e/m²/year for DGNB Gold level.
•	Optional: Do sensitivity analysis (e.g., changing façade material, using greener energy).
________________________________________
## 6. Document for DGNB and Reporting
•	Include:
o	Material list and quantities
o	EPD references
o	Energy use assumptions
o	Life cycle stage breakdown (A, B, C, D)
o	Final GWP result (kg CO₂e/m²/year)
•	Use tables and graphs to present:
o	Impact per life cycle phase
o	Contribution by building element
________________________________________
## Tips
•	Follow DGNB rules for system boundaries and exclusions (ignore screws, nails, <1% rule).
•	Always document your assumptions.
•	Keep LCA modular and simple—start with key materials, refine later.
