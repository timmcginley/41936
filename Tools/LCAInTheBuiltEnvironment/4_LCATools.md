# 4 LCA Tools
To conduct an LCA of a building, dedicated LCA tools are essential. This section provides a brief introduction to various LCA tools used in the building industry, with a particular focus on LCAbyg – one of the most applied tools in Denmark.

## 4.1 Introduction to LCAbyg
LCAbyg is a free and widely used Danish LCA software designed by BUILD at Aalborg University to assess the environmental impact of buildings throughout the life cycle.  However, not all modules are included in the impact assessment.
In LCAbyg, as shown in Table 4.1, only A1-A3 (product phase), B4 and B6 (use phase), and C3 and C4 (end-of-life phase) are included when documenting a building’s climate impact. Additionally, A4 and A5 (construction process phase) will become mandatory under the new regulations, for details about the addition of the two modules, see [3 New Climate Legislation](https://github.com/timmcginley/41936/blob/151ce26091e0ac09e660d38e0d5b9daede1c892e/Tools/LCAInTheBuiltEnvironment/3_NewClimateLegislation.md) for more information. 

*Table 4.1: Phases that are included in the BR18 LCA using LCAbyg for a building*  
![image](https://github.com/user-attachments/assets/fa90fd96-93ab-4717-96a3-6a6765605257)

The software follows the European standard EN 15978 and is aligned with BR18 goals for climate impact limits. LCAbyg works by allowing users to model a building’s life cycle and calculate its environmental impact based on material choices, energy consumption and end-of-life scenarios.
Users input building components, including material quantities and energy usage, either manually from drawings and energy calculations or by importing building data from Json- and csv-files. 
The software then calculates the environmental impact using predefined datasets, including the generic data described in [BR18 Appendix 2, table 7 – Generic data basis](https://www.bygningsreglementet.dk/Bilag/B2/Bilag_2/Tabel_7#787e83a6-b7d9-4a83-a4be-37574156daef), or data from specific EPDs. Multiple examples are already available in LCAbyg for inspiration, including a “Single-family house, example”. See Figure 4.1 on how to find the example.

![image](https://github.com/user-attachments/assets/40d704d5-08aa-4765-b615-0af4954a5ed3)  
*Figure 4.1: Examples of different types in the LCAbyg software*

Each project includes specific building data, such as gross floor area, heated floor area, operational energy use and supply, and other key information about the building. These are filled out in the “Building and operation” section shown at Figure 4.2.

![image](https://github.com/user-attachments/assets/fa3808ed-1b24-42de-824c-71c140b4a4c1)  
*Figur 4.2: The building and operation section in LCAbyg with information from the single-family house example*

Each building element (e.g. Roof) consists of one or more constructions, which are made up of specific products (e.g. Roof tiles). These products include data from all relevant life cycle stages required for the BR18 LCA either by the Generic Data Basis, or data from specific EPDs. The construction quantities are based on values extracted directly from the building model and are used as input for the constructions. See Figure 4.3 and Figure 4.4 for an example.

![image](https://github.com/user-attachments/assets/5c15f0da-ebd1-4a82-b546-52c309295715)  
*Figure 4.3: The building model section in LCAbyg marking the quantity input of roof tiles*

![image](https://github.com/user-attachments/assets/0278f063-9f63-467c-b920-148865ac17f0)  
*Figur 4.4: An example of data input for the roof tiles (A1-A3)*

With the element inputs, the results are presented in detailed reports, showing impact such as carbon footprint and resource use over the building’s lifetime. See Figure 4.5 for a cut-out of the example results.

![image](https://github.com/user-attachments/assets/dd365217-22e8-4612-8be4-51b1b5020a79)
*Figur 4.5: The results section in LCAbyg displaying the GWP for each input, the total climate impact and compliance with BR18*

To get a clear overview of which elements contribute most to the climate impacts, the “Analysis and Report” section can be used for a hotspot analysis, providing both a table and a graph that show the impact of each element. See Figure 4.6 for a hotspot analysis example.

![image](https://github.com/user-attachments/assets/2efcbf6e-594b-48fc-8298-524d56e85a6e)
*Figur 4.6: The analyse and report section in LCAbyg displaying the hotspot groups in both graph and a table, helping to identify which elements have the biggest impact*

This section has provided a brief overview of LCAbyg. For a detailed example of how LCAbyg is applied to a specific building step by step, see [LCAbyg Workflow](https://github.com/timmcginley/41936/blob/e8beaec052bd4bf33c9dd6b141ce6cbb9c323711/Workflows/LCAbyg.md).

### 4.2 Other LCA Tools Available
For a broader understanding of the different LCA software options available, here’s a quick overview with brief descriptions of some of the most well-known LCA tools, highlighting their unique features, strengths, and areas of application to help guide the choice of software depending on project needs.

### 4.2.1 One Click LCA
[One Click LCA](https://oneclicklca.com/software/design-construction/lca-for-construction) is the highest-rated LCA cloud-based tool for BREEAM but also complies with DGNB, LEED and many other certifications. It is primarily used to optimize early-stage design, enabling significant reduction in a building’s carbon footprint. The software supports both building and infrastructure projects giving automation and ease of use. While not literally one click, it integrates with BIM models, energy models, and quantity takeoffs to automate data extraction, making LCA faster and reducing manual input. Its automation simplifies LCA but may lead users to overlook key assumptions or data inputs to improve the LCA. One Click LCA is applicable for B18 LCA.

### 4.2.2 Real-Time LCA
[Real-Time LCA](https://realtimelca.dk/da-dk/) is a paid online tool that automates complex LCA calculations using material quantities from BIM models, Excel, or manual input. It integrates multiple EPDs, making it easier to assess and improve project emissions. What sets it apart is its AI-driven recommendations for alternative materials to optimize LCA results. By automating calculations, Real-Time LCA claims to reduce human errors and streamline the sustainability assessment process. Real-Time LCA is applicable for BR18 LCA. 

### 4.2.3 DesignLCA
[DesignLCA](https://www.designlca.com/about) is a free plugin for ArchiCAD, a paid software that enables early-stage LCA directly within the BIM model in ArchiCAD. By integrating with ArchiCAD, it allows users to calculate the overall carbon footprint of a building project from the initial design phase. What sets DesignLCA apart is the ability to calculate U-values and simulate energy consumption based on the building’s operational performance, all within the 3D model together with the LCA assessment. This provides a comprehensive, integrated approach to assessing sustainability in the early stages of building design. DesignLCA is applicable for BR18 LCA.

### 4.2.4 EG Sigma
[EG Sigma](https://eg.dk/it/kalkulation-og-opmaaling/eg-sigma/?utm_source=google&utm_medium=cpc&utm_term=&utm_campaign=&utm_adgroup=&gad_source=1&gclid=CjwKCAjwp8--BhBREiwAj7og1yTXrJ2t66DdRyWQtSdvmgUs57CMz450ebgSlcOMFkzBf4Rx57zBiRoCyZIQAvD_BwE) is primarily used for cost estimation and project management in construction, but it also offers an LCA module for building LCA and assessment of environmental impact of materials. EG Sigma requires a paid license and the LCA module requires an additional subscription. The software allows users to analyze both the economic and environmental aspects of a building project, including compliance with Danish building regulations and environmental requirements. EG Sigma is also compatible with LCAbyg as you can import data from Sigma into LCAbyg. This makes EG Sigma a useful tool for both financial and environmental assessment in construction projects. EG can be applicable for BR18 LCA with the LCA module add-on. 

### 4.2.5 OpenLCA
[OpenLCA](https://www.openlca.org/why-openlca/) is a free, open-source LCA tool designed mainly for product-based assessments. It supports various impact methods and databases, offering flexibility for customized analyzing. Its open-source nature makes it cost-effective and adaptable, providing transparency and the ability to tailor the tool to specific needs. OpenLCA is not applicable for BR18 LCA. 

### 4.2.6 SimaPro
[SimaPro](https://simapro.com/craft/) is a widely used LCA product-based software that allows users to conduct detailed environmental impact assessments. It supports a wide range of impact categories and offers extensive databases. SimaPro is known for its comprehensive modeling capabilities, enabling users to analyze complex systems and make data-driven decisions for sustainability. While it is a paid tool, its robust features and flexibility make it a preferred choice for many professionals in environmental research, product development, and sustainability assessments. SimaPro is not applicable for BR18 LCA. 

### 4.2.6 LCAlive
[LCAlive](https://lcalive.dk/) is an online LCA tool designed primarily for the early-design stage of a building. It focuses on climate impact, helping users quickly to assess the environmental impact of different design choices. The tool also incorporates the Reduction Roadmap to guide emissions reductions efforts, offers hotspot analyses of building parts and constructions, and compares the project’s performance to best practice benchmarks. This makes it a useful tool for early-stage decision-making and sustainability optimization. LCAlive is an early-design tool and will not be applicable for the more detailed BR18 LCA.

## 4.3 Summary

Table 4.2: Overview of all mentioned LCA tools, areas of application, strengths, cost and if its applicable for BR18 LCA.  
![image](https://github.com/user-attachments/assets/b9d7b65d-037b-467c-b5cb-7d056d9a1915)


## References
- BR18. (n.d.-f). https://www.bygningsreglementet.dk/Bilag/B2/Bilag_2/Tabel_7#787e83a6-b7d9-4a83-a4be-37574156daef
- #1 Global LCA construction software — reliable, secure & compliant. (n.d.). https://oneclicklca.com/software/design-construction/lca-for-construction
- Real-Time LCA — Forstå, forbedr og dokumentér byggeriets klimaaftryk — spar tid, ressourcer og CO2e | Real-Time LCA. (n.d.). https://realtimelca.dk/da-dk/
- General 4 — DesignLCA. (n.d.). DesignLCA. https://www.designlca.com/about
- Husum, K. (2025, March 6 th). Oplev digitale værktøjer, der gør en forskel - Mød EG på BYGGERI ’25. EG a/S. https://eg.dk/it/kalkulation-og-opmaaling/eg-sigma/?utm_source=google&utm_medium=cpc&utm_term=&utm_campaign=&utm_adgroup=&gad_source=1&gclid=CjwKCAjwp8--BhBREiwAj7og1yTXrJ2t66DdRyWQtSdvmgUs57CMz450ebgSlcOMFkzBf4Rx57zBiRoCyZIQAvD_BwE
- Why OpenLCA? | OpenLCA.org. (n.d.). https://www.openlca.org/why-openlca/
- SimaPro Craft - LCA insights that drive positive change. (2025, February 24 th). SimaPro. https://simapro.com/craft/
- Home. (n.d.). https://lcalive.dk/





