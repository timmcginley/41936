# Quantity take-off and pricing

This page is dedicated to cost estimation.
It will consist of couple of things. Sigma installion guide, manual links and videos also some FAQs (it will be updated as questions grows).
Then there will be some information about quantity take-off flow, pricing, and FAQs as well.

## Sigma

### Sigma introduction

Sigma Enterprise is a cost estimating software. It provides utilities to estimate entire life-cycle of the project. The core of which are price books. In Advanced Building Design case, the pricing should be based on Molio Price Books. The software also provides a way to establish templates, updates quantities also from BIM models. More details will come in sections below. Let's get to it.

### Sigma registration and installation

This is Sigma registration link: https://sigmaservice.net/education/register/

1. Use your name and school e-mail. It is super short form.
2. When you will have filled the form, you will get an e-mail from Sigma with following content.
- **Sigma Enterprise link** - click or copy to get installation file. Choose Danish region. Sigma can be still be installed in English language so you do not have to worry. 
- **Personal license number** - this is the key you need to fill when you want to activate the software. Bear in mind, license is personal and cannot be shared.
- **Sigma Autodesk Integration (Revit)** - this link provides add-on if you want to integrate quantities with Revit file. It is up to you if you want to use it.
- **Molio Price book** - use the link called "Molio Prisdata". When you open Sigma you should have new database as a tab on your ribbon called **Molio Prisdata**. The database is also visible under **Libraries** tab.
- **EG Sigma LCA Tool** - it is up to you. It is not requirement for cost estimation.

### Sigma usage

1. Quantity and cost breakdwon structure.

  When you open a new project start from the template called **Design Kalkulation - SfB**.
  
   ![Sigma_new_project](https://github.com/user-attachments/assets/a1206d6f-cd6e-477a-a175-b498cb5ce23a)

  You will be presented pricing structure as below. Not all categories are applicable.
  
  ![Cost_structure](https://github.com/user-attachments/assets/95040916-1fac-4dbb-8746-e25e348de3ae)

2. Here are list of links that could help you with starting with take-offs and pricing:
- Here are guidelines from official Sigma website: https://community.sigmaestimates.com/. I would suggest check each category, link and video, and follow and watch the ones you find necessary. There is also PDF guide at this website.
- Sigma session 2: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922441
- Sigma integration presentation: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922443
- BIM 5D and Estimating Presentation: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922446
- Sigma short presentation: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922447
- Sigma and Instances cost schedule: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922453
- Sigma and Insight tools: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922457
- Sigma Revit and other stuff: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922457
- Sigma presentation and Q&A: https://learn.inside.dtu.dk/d2l/le/lessons/245955/topics/922471

### Sigma FAQ:

**Q1:** _The license number is invalid for this Sigma version_:
   
**A1:** This occured in this week. Currently there is not explation how to fix it. It is likely on the software site. Reinstalling currently does not help but it is advisable to try reinstallation from time to time. 
- Currently: **Unresolved**

## Quantity take-off

### Quantity take-off division

The most straight forward approach is to divide quantities based on:
- Materials/Elements - the most important part. They are built elements that are the substance of buildings. For the units, take a look at Molio Pricebook. The most common are volume (m<sup>3</sup>), areas (m<sup>2</sup>), length/running meters (m). If the base quantities from your BIM model are in different unit than in pricebook, e.g., you have m<sup>3</sup> but the same element in pricebook is in m<sup>2</sup>, it usually means that they are accounted for different thickness or width. In this situation pick the closest thickness and recalculate your volume into the area.  
- Machinery/Equipment - The most essential are cranes, excavators, concrete pumps. Some of them you want to calculate by the time you rent it, and some are included in pricing of the materials.
- Safety - There are a lot of safety precautions that needs to be considered during construction. In the scenarios of renovation, please account for temporary equipment (such as shuttering support or similar).
- Site rig/unrig and running site - It will be mostly renting time of equipement such as fences, renting of containers (for worker, material, and waste). Usage of energy, water should be also there.
- Time - Sometimes the time is the lead unit. Renting a crane is this example. You need to have certain lift capacity and then just only the time of usage the crane.

![Quantity take-off](https://github.com/user-attachments/assets/43a63430-5cc3-4a1a-86ef-3292c66e76f4)

### Quantity workflow

To make the process of estimating easier, follow the approach: **REDI**
- Remove (element). Quantify elements with appropiate units.
- Evaluate (evaluate feasibility). Estimate how much of removed elements could be reused (it might not be necessary but mainly refer to other subject if elements can be reused).
- Dispose/Repair (element). It is based on evaluation. If the element can be repaired, this should be reflected in either increase of quantity or unit price. Increase of unit price is suggested.
- Install (install exisiting element or a new one). It would account for combine quantity of reused or new elements.

### Cost workflow

In cost you should cover:
1. Excavation - foundation.
2. Materials related to the building.
3. Services related to constructing the building, storeys, etc.
4. Process of rigging/unrigging the site, as well as running it.
5. Rent or lease of equipment used during construction.
6. Overhead related to managing the construction of the building.

1. Use the SfB structure to fill the elements. If you cannot find appropiate category for your element, you are welcome to create a new one (but please to try to fit it somewhere existing). Helpful thing would be to start creating custom library where you can adjust your own unit prices.
2. If an element needs to be removed then:
    1. Find an entry related to the element removal and fill the quantities.
        1. If an element is not feasible for reuse then add the cost of removing waste (Blue book). In this case you bear the case for a new element (Red or Blue book).
        2. If an element is feasible for reuse then add the cost of removing the element and storing (Blue book). In this case you need to adjust prices for recycled elements (e.g., material-wise it could be cheaper, but the labor would have higher rate). You can also account for some cosmetics or whatever you find it fit in Orange book (renovation).  <!-- It needs to be further clarified if some positions in Sigma refer to removal and recycle for material or entire reuse -->
    2. Depending how you handled the the previous step (e.g., you tripled labour price for installation the reused component) and the type of component, it might be necessary to include machinery or some temporary structure.
3. If it is a new element then you proceed with putting quantities to specific price entry. The only caveat is if new elements are in exisiting stories. Then you might add some markup for labour cost.

### Quantity take-off and pricing FAQ:

**Q1:** _How to calculate services such as HVAC?_:

**A1:** It is going to be by square meters. Whether or not take current total area or only new area (e.g., extra storey), it will be determined soon. <!-- Determine how it should be done. -->

**Q2:** _Should HVAC you need be calculated separately?_:

**A2:** It most likely should be calculated seperately.

## Summary
So here it is an overview of take-offs, cost and Sigma. This is foundation. Some adjustment can be expected.
