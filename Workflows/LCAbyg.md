# LCAbyg
The following guide aims to provide a comprehensive example of how to model an LCA calculation in LCAbyg. For this specific example LCAbyg 2023.3 (5.4.0.5) has been used. The focus of the calculation example is to serve as a guide through the steps to modelling and interpreting a building LCA. LCAbyg has its own guide which provides detailed descriptions of the software’s functions, which can be downloaded from [here](https://www.lcabyg.dk/en/usermanual/user-manual-lcabyg/).

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

### Default values for installations
To model the technical installations using default values, first right-click the relevant element group and then press ‘**Create and add element…**’ as shown in Figure 25. Do this for the element groups ‘**Drainage**’, ‘**Ventilation and cooling**’, and ‘**Water systems**’.

![billede](https://github.com/user-attachments/assets/9314f0da-fa21-4021-bfd1-cbd4ec98c64d)  
*Figure 25: Create a new element*

For each group of technical installations, choose the subgroup highlighted in Figure 26.

![billede](https://github.com/user-attachments/assets/0a256605-f6d7-438d-9a9c-42bb66bf5df4)  
*Figure 26: Subgroups for each default value*

For each of the three elements, you will want to add a construction (see Figure 27).

![billede](https://github.com/user-attachments/assets/2fc89de3-44a6-4050-9ea4-a2bdb22891b4)  
*Figure 27: Add construction in LCAbyg*

From the list, choose the default value that matches your building type and then add it to the element by pressing the checkmark (see Figure 28).

![billede](https://github.com/user-attachments/assets/5bc280a7-f089-4333-9cca-7b400ea2f980)  
*Figure 28: Default values in the LCAbyg construction library*

When entering the quantities for each default value, the amount should be equal to sum of the heated floor area and the heated basement area. For reference, these are the same floor areas used in the energy framework calculation, but counting the full heated basement area as opposed to 50% like in the energy framework.

![billede](https://github.com/user-attachments/assets/53864ee6-c028-40d1-9cef-4316be471e4c)  
*Figure 29: Enter area for default value*

### EPDs
To use an EPD in your project, first identify the construction where you want to use the EPD. For this example, we will be applying an EPD for concrete in the ground slab. The specific EPD used in the example is for [UNI-GREEN C25/30 concrete](https://www.epd-norge.no/epder/byggevarer/ferdig-betong/uni-green-beton-c25-30-lava-concrete-in-passive-environmental-exposure-class).

Right-click the construction and choose ‘**Create and add product…**’ (see Figure 30). If it is a generic LCAbyg construction, you will have to create a copy of it first. Make sure to also remove the product that is being replaced.

![billede](https://github.com/user-attachments/assets/a884321e-d0a7-4a61-8bda-d4f66403c248)  
*Figure 30: Create and add a new product*

Right-click on the newly created product and press ‘**Create and add stage…**’ (see Figure 31).

![billede](https://github.com/user-attachments/assets/eb3db0d0-4038-4bc5-9a83-b5863a3ea970)  
*Figure 31: Add new stage to a product*

Give the stage a name and choose the appropriate primary, secondary, and tertiary category. The EPD used in this example is a product specific EPD, and we will begin by modelling the A1-A3 stage (see Figure 32).

![billede](https://github.com/user-attachments/assets/dbfc0e21-ccf5-45ea-81ce-be4931e78b6f)  
*Figure 32: Fill in category of the product*

‘**Stage unit**’ is the unit you will use to quantify the amount of product. This will usually be the same as the ‘**Indicator unit**’, which should be equivalent to the declared unit in the EPD. The declared unit is usually found on one of the first pages of an EPD. 

‘**Standard**’ refers to the standard used to develop the EPD, which will either be *EN15804+A1* or *EN15804+A2*. This information is usually found on one of the first pages of an EPD. 

‘**Indicator factor**’ should almost always be 1, except if the declared unit is different from the indicator unit. For example, if the indicator unit is kg and the declared unit is 1 metric ton, then ‘**Indicator factor**’ should be 1000 as there are 1000 kg per metric ton.

Some EPDs cover multiple products of the same category and provide scaling factors to apply to the impacts to represent the various products’ impact. In this case, the EPD only covers one product, thus ‘**Scaling factor**’ should be 1.

‘**Mass factor**’ refers to the weight per indicator unit. This is typically found on one of the earlier pages of an EPD.

If stage unit and indicator unit are the same, then ‘**Unit factor**’ should be 1. Otherwise, it should be the number of indicator unit per stage unit.

‘**Expiration date**’ refers to the final day the EPD is considered valid. This is typically stated on the front page of an EPD. Enter it in the format ‘yyyy-mm-dd’.

![billede](https://github.com/user-attachments/assets/3e7642a8-db2c-45ef-ba0e-77cfbfc6b679)  
*Figure 33: Enter information from EPD*

Next enter the external information (see Figure 34). This is necessary for documentation but does not affect the results. In this example, the EPD is from EPD Norway so that is entered in ‘**External source**’.

‘**External id**’ refers to declaration/registration number used for the EPD by the program operator, which is usually declared on the front page of an EPD.

‘**External version**’ is only relevant in case the EPD has been revised/updated, which will also be stated on the front page if it has.

In ‘**External URL**’ enter the URL to where the EPD can be downloaded from.

![billede](https://github.com/user-attachments/assets/b676635c-5b47-4eee-841b-dfb97e7fbcd7)  
*Figure 34: External EPD information in LCAbyg*

Then enter the GWP of the stage (see Figure 35). This can be found in the results of the EPD. Specifically, look for the indicator named GWP-total. If the EPD adheres to the *EN15804+A1* standard, you will need to also enter a bunch of other indicators.

![billede](https://github.com/user-attachments/assets/df47a5c1-a9d7-440c-8e3a-7eea4099cf78)  
*Figure 35: GWP value from EPD*

Once this is done, press ‘**Create**’. Repeat this process for stages C3, C4, and D. The EPD will then be modelled in the project, and it will be available from the list of products in LCAbyg, should you need it somewhere else. Then, like when adding any other product, enter quantity and service life of the product.

### Reuse
To label a product as reused, such that its impact is calculated as 0, simply change the service life of the product to 0 years (see Figure 36).

![billede](https://github.com/user-attachments/assets/6ba474f1-7858-4df6-98b0-e9b5480e2d6a)  
*Figure 36: Mark product as reuse*

### Special building conditions
To add a special condition to your model, go to the ‘**Building and operation**’ tab, scroll down to the section labeled ‘**Special building conditions**’, and press ‘**Add / edit special conditions**’ (see Figure 37).

![billede](https://github.com/user-attachments/assets/db45716a-558d-4337-a15a-adbe9d6b85f0)  
*Figure 37: The 'Special conditions' field in LCAbyg*

Then choose the relevant group and subgroup from the drop-down menu and fill in the quantity affected by the special condition (see Figure 38). In the ‘**Documentation**’ box, fill in the reason for the special condition. In this example, the soil conditions are bad, which means that a stronger ground slab is required to compensate. Once everything is filled in, press ‘**Add condition**’. If you wish to edit or update an existing special condition, the process is the same.

![billede](https://github.com/user-attachments/assets/1f9c62e8-9100-4c56-a73b-5e8ced85eaa2)  
*Figure 38: Fill out special condition*

Next, go to the ‘**Building model**’ tab and find the construction(s) affected by the special building condition. Select the relevant construction(s) and tick the box labeled ‘**Special condition**’ (see Figure 39).

![billede](https://github.com/user-attachments/assets/d4258adf-34e7-46ab-b81d-6dd76c3e4623)  
*Figure 39: Enable the special condition*

If a special condition applies to the foundation system, except for slab foundations, the quantity is automatically filled out as the reference area of the LCA. You also will not have to tick a ‘*Special condition*’ box.

## Results
The ‘**Results**’ tab provides a list of all the materials in the model (see Figure 40). By choosing a different option from the drop-down menu at the top, it can also list the impact of every material in project or provide key numbers for the building regulation (pictured in Figure 41).

![billede](https://github.com/user-attachments/assets/61a17e42-d94d-48a6-88e8-62f5fa17194d)  
*Figure 40: The 'Results' tab in LCAbyg*

![billede](https://github.com/user-attachments/assets/1c3716c3-8c20-40db-b4ce-a3553d87b645)  
*Figure 41: Key numbers for BR18*

## Analyse and report
The ‘**Analyse and report**' tab provides different graph options to analyze the impact distribution in the project (see Figure 42). This section will only show the ‘**Hotspot analysis**' option, but experimentation with the different graphs is encouraged.

![billede](https://github.com/user-attachments/assets/2f9b64a8-9fab-49ea-b86e-26303accfb26)
*Figure 42: The 'Analyse and report' tab in LCAbyg*

A ‘**Hotspot analysis**' provides an overview of the impact distribution in the project (see Figure 43). This is especially useful when trying to identify possibilities for reducing impact, as the highest impact groups are typically also those with the largest reduction potential. You can also change the hotspot graph to show the impact distribution per element, construction etc. by choosing a different option from the ‘**Level**’ drop-down menu.

![billede](https://github.com/user-attachments/assets/a4320d3c-c4bf-4427-85cc-884c7cb0e22a)  
*Figure 43: A hotspot graph from LCAbyg*

The four buttons at the top of the window will provide documentation for the model inputs and results, each in a different format. ‘**Export report**’ and ‘**Export BR**’ are recommended for documentation, whereas '**Export Excel**’ is suitable for further analysis. ‘**Export json**’ provides the model in a json-file, which may be useful for advanced analysis.

## Simple variation study
Variation studies provide helpful information when choosing the composition of various building elements. There are multiple different ways to do variation studies with LCAbyg depending on what is being analyzed. This section provides one example of how to model a simple variation study in LCAbyg.

For this example, we will be comparing the climate impact of three different partition walls:
  •	Aerated concrete with 125 mm thickness
  •	2x gypsum on a 100 mm wooden frame
  •	2x gypsum on a 100 mm steel frame

First, create an empty project and set both the heated floor area and gross floor area to 1 m². Then go to the ‘**Building model**’ tab and create an element for each variant (see Figure 44).

![billede](https://github.com/user-attachments/assets/40c10702-2ae3-407a-b433-246e03fe03ac)  
*Figure 44: An element for each variant*

In each element, model the required materials for 1 m² of partition wall. In this example, that means 1 m² of middle construction and 2 m² of wall surface (1 m² on each side of the wall) (see Figure 45). 

![billede](https://github.com/user-attachments/assets/d82877cb-8458-4764-a486-2b541f718394)  
*Figure 45: The three variants modelled in LCAbyg*

Once all variants have been modelled, you can then go to the ‘**Results**’ tab and pull the numbers directly. Alternatively, go to the ‘**Analyse and report**’ tab, choose ‘**Hotspot analysis**’, and then pick ‘**Elements**’ from the ‘**Level**’ drop-down menu. You will then be presented with a bar chart showing the climate impact of each variant (see Figure 46).

![billede](https://github.com/user-attachments/assets/e3f33a9f-7c9f-4e62-acdf-f821babdcfc3)  
*Figure 46: The climate impact of the variants shown in a hotspot graph*

In this example, we see that the gypsum partition wall with a wooden frame has the lowest climate impact of the three variants. It is, however, important to not only make decisions based on climate impact as there are plenty of other factors of significance to consider, e.g. acoustic performance or cost.

## LCAbyg tips

