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

Under ‘**Calculation prerequisites**’, choose calculation type and building type from the two drop-down menus. ‘**Commissioning year**’ refers to the year that the building is finished. Then, enter your building’s heated floor area, gross floor area, and any integrated garages and additional areas in their respective boxes (see Figure 5).

![billede](https://github.com/user-attachments/assets/5ec7175d-b097-42e4-b9f4-eebd6b46e180)  
*Figure 5: The 'Calculation prerequisites' field in LCAbyg*

Under ‘**Operational consumption and supply**’ you will want to fill in the key numbers from the energy framework calculation. Specifically, it requires the three highlighted results in Figure 6.

![billede](https://github.com/user-attachments/assets/d246bb07-732f-4f0c-b34c-0da8c6ba8f7f)  
*Figure 6: Energy framework key numbers*

In the ’**Operational heat use**’ box, fill in the result for **‘Heat’ (1)**.
In the ‘**Operational electricity use**’ box, fill in the result for **‘El. for operation of building’ (2)**.
If the result for **‘Solar cells’ (3)** exceeds 13.2 kWh/m² year, enter only the amount exceeded in the ‘**Exported electricity**’ box. For example, if the result for **‘Solar cells’ (3)** is 15.0 kWh/m² year, you will want to enter 1.8 in LCAbyg.
Choose the relevant energy supply from the two drop-down menus.

![billede](https://github.com/user-attachments/assets/f99950f4-5c2c-4e8f-bb02-76714bf97348)  
*Figure 7: The 'Operational consumption and supply' field in LCAbyg*

## Building model
The ‘**Building model**’ tab (see Figure 8) is where all the materials in the LCA will be modelled.

![billede](https://github.com/user-attachments/assets/994614b9-f300-4c3f-97a4-0e935ec0ba37)  
*Figure 8: The 'Building model' tab in LCAbyg*

To start modelling the building elements, first right-click the element group that you wish to model, and then press ‘**Create and add element…**’ as shown in Figure 9.

![billede](https://github.com/user-attachments/assets/162ec70d-101d-4374-854b-f86a4fccb2df)  
*Figure 9: Create and add and element in LCAbyg*

You will then be prompted to give your element a name and pick a subgroup (see Figure 10).

![billede](https://github.com/user-attachments/assets/183a0711-02a3-4a0d-ac96-0d37e0899557)  
*Figure 10: Naming an element*

Repeat this process for each element of the building you are modelling. Your ‘**Elements**’ column may look something like Figure 11. Note that technical installations are missing. These will be modelled using default values, which are described in their own subsection.

![billede](https://github.com/user-attachments/assets/659f21ce-b684-425e-add7-82732a3c9439)  
*Figure 11: Filled out 'Elements' column*

The next step is to model the individual constructions. LCAbyg contains a library of generic constructions to use. To insert a generic construction, right click on the relevant building element and then choose ‘**Add construction…**’ (see Figure 12).

![billede](https://github.com/user-attachments/assets/caa2057b-76e3-4bd8-b55c-07819c241660)  
*Figure 12: Adding construction in LCAbyg*

Then find the relevant construction in the list on the left (see Figure 13). You can also narrow the list by using the search function at the top of the window. Once you have chosen a construction press it and then click the checkmark on the bottom right to add it to your project.

![billede](https://github.com/user-attachments/assets/17086ec1-ebe2-4ad5-a914-8ab1a5f5692e)  
*Figure 13: LCAbyg's construction library*

Next enter the quantity of the construction by clicking on it and filling out the ‘**Amount**’ box on the right (see Figure 14). Make sure to check that you are using the correct unit.

![billede](https://github.com/user-attachments/assets/8a346aa6-be8b-436c-9c67-c431fd0bb0af)  
*Figure 14: Enter amount in LCAbyg*

Often the generic constructions will not fit what is used in the project. The way to get around this is to either use a similar generic construction as a base and then modify it to fit, or you can model a construction from scratch. To modify a generic construction, first repeat the previous step to insert it into the model. You will not be able to edit it directly, so instead right-click the construction and choose ‘**Duplicate and replace**’ (see Figure 15). This will replace the construction with an editable copy.

![billede](https://github.com/user-attachments/assets/62fb8d03-f230-486e-96c6-500df13fa53f)  
*Figure 15: Duplicate and replace a construction*

For transparent documentation, right click on the copy and press ‘**Rename…**’ to make sure the name fits the actual construction (see Figure 16).

![billede](https://github.com/user-attachments/assets/72a319fc-9451-4184-a4da-184728f97693)  
*Figure 16: Renaming a construction in LCAbyg*

In this example we want a 250 mm layer of mineral wool sheets instead of the 300 mm of blowable mineral wool modeled in the generic construction. To do this delete the product that you want to replace by right clicking it and pressing ‘**Remove product**’ (see Figure 17). Then right-click on the construction and choose ‘**Add product…**’ (see Figure 18).

![billede](https://github.com/user-attachments/assets/3453adc1-e297-40e1-948e-ac8b5496eede)  
*Figure 17: Remove a product from a construction*

![billede](https://github.com/user-attachments/assets/f63cae9c-8124-44a2-9ed3-32489ad70352)  
*Figure 18: Add a product to a construction*

You will then be presented with the entire contents *BR18 appendix 2, table 7*. Use the search function at the top of the window to narrow the search. Then select the desired product and press the checkmark on the bottom right to add it to the construction (see Figure 19).

![billede](https://github.com/user-attachments/assets/5f73048c-5d44-4098-8803-ec4a9cedc810)  
*Figure 19: LCAbyg product library*

Next, select the product and add the amount of the product per unit of construction in the ‘**Amount**’ box (see Figure 20). In this case it is 0.25 m³ of mineral wool per m² of wall. Then enter the service life of the product according to *BUILD REPORT 2021:32* in the ‘**Service life**’ box. Alternatively, press the ‘**Service life table**’ button and select the relevant service life there (see Figure 21).

![billede](https://github.com/user-attachments/assets/69eb0ee7-4abd-4762-8c93-b99cc82f955b)  
*Figure 20: Product information in LCAbyg*

![billede](https://github.com/user-attachments/assets/9926cdd7-3f3b-4cbf-9408-3461b1f4eca0)  
*Figure 21: Service life table in LCAbyg*

To model a construction from scratch, we will be using an external basement wall as an example. It will consist of a 150 mm concrete element and a 250 mm layer of XPS insulation towards the ground. First, right-click the relevant building element and press ‘**Create and add construction…**’ (see Figure 22). Then give the construction a name in the ‘**Name**’ box and choose a unit for your construction with the ‘**Unit**’ drop-down menu pictured in Figure 23. In this case, the unit will be m². Next, press the ‘**Create and add**’ button.

![billede](https://github.com/user-attachments/assets/54f7ebe9-460f-4ebc-93b3-095e2bc56130)  
*Figure 22: Create a new construction*

![billede](https://github.com/user-attachments/assets/20662d14-c364-457e-803b-74e45efefc43)  
*Figure 23: Name a new construction*

Then, like Figure 18 , right-click on the newly created construction and choose ‘**Add product…**’. Like Figure 19 use the search function at the top of the window to find the relevant products and press the checkmark on the bottom right to add them to the construction.
For each product, select the product and add the amount of the product per unit of construction in the ‘**Amount**’ box like in Figure 20. 

In this case it is 0.25 m³ of XPS per m² of wall and 1 m² concrete wall element per m² of wall. Then enter the service life of the product according to *BUILD REPORT 2021:32* in the ‘**Service life**’ box. Alternatively, press the ‘**Service life table**’ button and select the relevant service life like in Figure 21, which in this case will be 120 years for a concrete wall element and 80 years for XPS insulation (see Figure 24).

![billede](https://github.com/user-attachments/assets/0aa34d47-0fcc-43cf-8720-538ce3670942)  
*Figure 24: Product information in LCAbyg*

## Default values for installations
To model the technical installations using default values, first right-click the relevant element group and then press ‘**Create and add element…**’ as shown in Figure 25. Do this for the element groups ‘**Drainage**’, ‘**Ventilation and cooling**’, and ‘**Water systems**’.

![billede](https://github.com/user-attachments/assets/9314f0da-fa21-4021-bfd1-cbd4ec98c64d)  
*Figure 25: Create a new element*

For each group of technical installations, choose the subgroup highlighted in Figure 26.

![billede](https://github.com/user-attachments/assets/0a256605-f6d7-438d-9a9c-42bb66bf5df4)  
*Figure 26: Subgroups for each default value*
