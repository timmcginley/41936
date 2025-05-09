# LCAbyg
The following guide aims to provide a comprehensive example of how to model an LCA calculation in LCAbyg. For this specific example LCAbyg 2023.2 (5.4.0.5) has been used. The focus of the calculation example is to serve as a guide through the steps to modelling and interpreting a building LCA. LCAbyg has its own guide which provides detailed descriptions of the software’s functions, which can be downloaded from [here](https://www.lcabyg.dk/en/usermanual/user-manual-lcabyg/).

Please note that there is more than one way to model a building LCA, and this guide only serves as a suggested method. What matters most is that the LCA is modelled in a way that is transparent and that the result is correct.

## Creating a project
When opening LCAbyg, you will be met by the window shown on Figure 1. To create a new project, first press the ‘**Files**’ button, then pick ‘**New**’, and finally ‘**Empty project**’ (see Figure 2).

![billede](https://github.com/user-attachments/assets/a3ceaf46-acbe-498d-9aca-4e9b52eadbb2)  
*Figure 1: LCAbyg Front page*

![billede](https://github.com/user-attachments/assets/06df00c1-6b5e-4fb6-b4d8-6c3d464a76a3)  
*Figure 2: Creating empty project in LCAbyg*

## Building and operation
Upon creating a new project, you will be moved to the ‘**Building and operation**’ tab (see Figure 3). In this tab, fill in the various information about the building project.

![billede](https://github.com/user-attachments/assets/fdd292f4-8550-4df5-bcc9-b7bb17e4b156)  
*Figure 3: The 'Building and operation' tab of LCAbyg*

The ‘**Project**’ and ‘**Building**’ fields (see Figure 4) are only for documentation and will not affect the calculation, so if the purpose of the calculation is just analysis, these can be left blank.

![billede](https://github.com/user-attachments/assets/6ba09fb2-18e9-49e0-834c-ff61aa2c2558)  
*Figure 4: The 'Project' and 'Building' fields in LCAbyg*

Under ‘**Operational consumption and supply**’ you will want to fill in the key numbers from the energy framework calculation. Specifically, it requires the three highlighted results in Figure 5.

![billede](https://github.com/user-attachments/assets/d246bb07-732f-4f0c-b34c-0da8c6ba8f7f)  
*Figure 5: Energy framework key numbers*

In the ’**Operational heat use**’ box, fill in the result for **‘Heat’ (1)**.
In the ‘**Operational electricity use**’ box, fill in the result for **‘El. for operation of building’ (2)**.
If the result for **‘Solar cells’ (3)** exceeds 13.2 kWh/m² year, enter only the amount exceeded in the ‘**Exported electricity**’ box. For example, if the result for **‘Solar cells’ (3)** is 15.0 kWh/m² year, you will want to enter 1.8 in LCAbyg.
Choose the relevant energy supply from the two drop-down menus.

![billede](https://github.com/user-attachments/assets/f99950f4-5c2c-4e8f-bb02-76714bf97348)  
*Figure 6: The 'Operational consumption and supply' field in LCAbyg*


