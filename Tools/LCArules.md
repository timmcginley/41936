# Non-negotiable LCA Rules
*May 11, 2026*

## Purpose

Students must prepare two LCA result structures:

| Version | Purpose | Main use |
|---|---|---|
| Version 1: Cross-group comparison LCA / LCA lite | Simple, strict, and comparable between all student groups | Cross-group comparison and initial carbon screening |
| Version 2: DGNB / BR18-aligned LCA | More complete environmental assessment | DGNB Lite ENV1.1 discussion, BR18-aligned interpretation, hotspot analysis, design justification, and points calculation |

- Both versions must use the same quantities where relevant. Version 2 is not a separate project. It is the more complete version of Version 1.
- The reason for having two versions is simple: cross-group comparison only works when all groups use the same simplified assumptions. Full environmental interpretation, however, needs the more complete boundary. Otherwise the numbers will look precise while quietly lying in a table. Classic.

---

## Carbon Responsibility by Subtask

Each group must report the carbon footprint connected to each subject area:

| Subject | Main components included | kg CO₂-eq total | kg CO₂-eq/m² | kg CO₂-eq/desk |
|---|---|---|---|---|
| ARCH | | | | |
| STR | | | | |
| MEP | | | | |
| GEO | | | | |
| MAT | | | | |
| PM/ICT | | | | |

This table should be provided for both Verion 1 and Version 2 as the main carbon responsibility overview. 

---

## Version 1: Cross-group Comparison LCA / LCA Lite

*Simplified renovation LCA for comparability*

### Objective

To compare the climate impact of each group's renovation strategy using the same simple system boundary.

Both versions should focus on the material consequences of the renovation intervention:

1. Materials added to the building
2. Materials removed from the existing building
3. Replacements required during the 50-year reference study period

No creative extra assumptions.

**Version 1 is used for:**

- Cross-group comparison
- Initial carbon screening
- Simple identification of major contributors
- KPI LCA value

**Version 1 is not used for:**

- Final DGNB point calculation
- Final hotspot interpretation
- Final design recommendation
- BR18-aligned environmental conclusion

Those belong to Version 2.

### Functional Unit and Reference Study Period

**kg CO₂-eq / m² building area over 50 years**

Additional reporting unit: kg CO₂-eq / permanent desk over 50 years

Reference study period: 50 years

### Included Life Cycle Stages

**For added or new materials:**

| Stage | Include? |
|---|---|
| A1–A3 | Yes |
| A4 | No |
| A5 | No |
| B4 | Yes |
| B6 | No |
| C1–C4 | Yes |
| D | No |

**For removed existing materials:**

| Stage | Include? |
|---|---|
| A1–A3 | No |
| A4–A5 | No |
| B4 | No |
| C1–C4 | Yes |
| D | No |

### Required Output for Version 1

Each group must provide:

1. **Total GWP for added materials** — kg CO₂-eq total, kg CO₂-eq/m², kg CO₂-eq/desk
2. **Total GWP for removed materials** — kg CO₂-eq total, kg CO₂-eq/m², kg CO₂-eq/desk
3. **Total intervention impact** — added materials + removed materials
4. **Breakdown by life cycle stage** — A1–A3, B4, C1–C4
5. **Short interpretation** — Identify the top 3 carbon hotspots and explain why they dominate.

> **Note:** Detailed hotspot analysis must be done only in Version 2.

---

## Version 2: DGNB / BR18-aligned LCA

*More complete renovation LCA for assessment and design justification*

### Objective

To provide a more complete climate assessment of the proposed renovation strategy and support DGNB Lite / BR18-related discussion.

> **Important:** BR18 does not currently provide a full dedicated renovation-LCA method in the same way as new-build regulation. Students should be honest: this is a renovation assessment inspired by BR18, EN 15978, and DGNB logic, not a legally certified BR18 renovation calculation.

**Version 2 is used for:**

- DGNB Lite ENV1.1 discussion
- DGNB point assessment
- BR18-aligned interpretation
- Final hotspot analysis
- Carbon responsibility by subject

### Functional Unit and Reference Study Period

- kg CO₂-eq / m² building area / year
- kg CO₂-eq / m² building area over 50 years
- kg CO₂-eq / permanent desk over 50 years
- kg CO₂-eq / permanent desk / year

Reference study period: 50 years

### Included Life Cycle Stages

**For added or new materials:**

| Stage | Include? |
|---|---|
| A1–A3 | Yes |
| A4 | Yes |
| A5 | Yes |
| B4 | Yes |
| B6 | Yes |
| C1–C4 | Yes |
| D | Report separately |

**For removed existing materials:**

| Stage | Include? |
|---|---|
| A1–A3 | No |
| A4–A5 | No |
| B4 | No |
| C1–C4 | Yes |
| D | Report separately |

### Module B6: Operational Energy

Students must include B6 in Version 2.

**Preferred source:** MEP building energy model

**If no energy model is available**, use the current operational energy use of the building, clearly stating:

- Source of the data
- Annual energy use
- Energy carrier (e.g. district heating, electricity, cooling)
- Emission factors used
- Whether the value is measured, estimated, or assumed

The LCA Version 2 requires operational energy modelling using the same weather file, occupancy assumptions, internal gains, HVAC assumptions, and 50-year grid decarbonisation based on BR18 data.

### Module B2: Maintenance

Students must discuss B2, but should not include it numerically unless a consistent method is used.

**Required discussion:**

- What parts require maintenance?
- How often?
- Does the maintenance require material replacement, coating, cleaning, access equipment, or energy?
- Is the carbon impact likely significant or minor?
- Why was it included or excluded?

B2 is qualitative.

### Module D: Reuse, Recovery, and Recycling Benefits

Module D must be:

- Reported separately
- Not included in the main total
- Not used to reduce the main DGNB/BR18-aligned result

---

## Data Source Rules

Students may use the following data sources, in this priority order:

1. Product-specific EPDs
2. Generic EPDs
3. BR18 generic data
4. LCAbyg / ÖkobauDAT / One Click LCA / recognised LCA databases
5. Peer-reviewed literature
6. Clearly justified proxy data

> **Note:** AI-generated data is not acceptable as final carbon-factor evidence unless it leads to a traceable source. AI can help search, organise, and explain, but it cannot be the source of the emission factor.

For each data point, the following must be documented:

| Item | Required |
|---|---|
| Material/component name | Yes |
| Quantity | Yes |
| Unit | Yes |
| Data source | Yes |
| Life cycle modules covered | Yes |
| Assumed service life | Yes |
| Replacement count | Yes |
| End-of-life assumption | Yes |

---

## Assumption Hierarchy

Students must follow this hierarchy:

1. **First check BR18 and DGNB guidance.** If relevant assumptions are available there, they must use them.
2. **If BR18/DGNB do not provide a required assumption**, students may use assumptions from:
   - EPDs
   - LCAbyg
   - Recognised LCA databases
   - Manufacturer documentation
   - Peer-reviewed literature
3. **If students define their own assumptions**, they must justify:
   - Why the assumption was needed
   - Why the chosen value is reasonable

Examples of assumptions that may need justification:

- A4 transport distance
- A5 installation impacts
- Service life of components

### Assumption Rules

All assumptions must be stated explicitly. At minimum, students must define:

- Reference study period
- Building area used for normalisation
- Number of permanent desks
- Included building components
- Excluded building components
- Service lives
- Replacement logic
- Energy emission factors
- End-of-life scenarios
- Treatment of reused materials
- Treatment of Module D
- Data sources

---

## Note Regarding Part C Submission

We understand that these LCA instructions have been provided relatively late and close to the Part C submission deadline. For Part C, you should therefore do your best to apply this structure as far as possible within the time available.

If some parts are incomplete or not fully aligned with these instructions, this will be reported back to you through feedback. The purpose is to help you identify what needs to be corrected, improved, or completed before the final Part D submission.

Therefore, do not worry if you cannot fully complete every target for Part C. However, you should still clearly show your current method, assumptions, data sources, preliminary results, and the parts that still need further development. The more clearly you document your current work, the more useful and specific the feedback will be.

The aim of Part C is to help you avoid repeating the same methodological mistakes in the final submission and to support you in developing a more complete, consistent, and well-documented LCA for Part D.
