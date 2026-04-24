
# Clash Detection Guide
## Introduction
This guide provides a practical walkthrough of clash detection, combining basic theory with step-by-step workflows using BIM tools. The purpose of clash detection is to identify and resolve conflicts between different building systems early in the design phase, reducing errors, rework, and delays later in the project.


## Theory
Clash detection identifies conflicts among building elements, such as structure, architecture, and installations, within a digital model.
These conflicts can be divided into three main types:

1. **Hard clashes:** 
  Physical overlap between elements (e.g., a ventilation duct running through a structural beam).
  These typically need to be addressed directly. 
2. **Soft clashes** (clearance clashes):
  Situations where there is not enough space for elements to function properly or be maintained (e.g., insufficient space around ventilation systems).
3. **Workflow clashes** (only relevant for construction planning):
  Conflicts related to construction scheduling.
  These are more relevant in later project stages and are typically not the main focus in early design phases. 

Clash detection allows teams to identify and resolve these issues early, improving coordination and reducing costly changes during construction.

## Workflow
### 1. Prepare Models
Before running clash detection, the models must be properly prepared to ensure reliable results.
* Ensure models from all disciplines are updated 
* Set deadlines for regular updates throughout the project 
* Check coordinates and alignment between models 
* Ensure consistent file naming (e.g., CAD naming standard) 
Early alignment is critical. Errors in coordinates or positioning can lead to incorrect clash results.

### 2. Methods for Clash Detection ( among many)
| **Method**                 | **Description**                  | **Advantages**                                                                                         | **Limitations**                                                        |
| -------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Revit (Linked Models)**  | Integrated clash detection using linked models     | Fast and integrated in the design process.Good for continuous checking during modelling.     | More manual process. Risk of missing clashes. Less structured overview |
| **Revizto (Visual Review / Walkthrough)** | Visual walkthrough and manual clash identification | Easy to use. Provides a strong visual overview. Useful for reviewing spaces (technical rooms, shafts, etc.)             | Manual process.Clashes can be overlooked.              |
| **Navisworks (Advanced Clash Detection)** | Automated and rule-based clash detection           | Detects all clashes systematically. Allows direct comparison between models. Provides structured and detailed analysis. | Time-consuming to set up. Requires additional software and learning.  |

### Practical Tips
* Not all clashes need to be fixed.
* Start with major clashes first!
* Expect many clashes in the early stages.
* Do it regularly and document the process
* Coordination between disciplines is key.
* It can be time-consuming, but it prevents bigger issues later.

## Detailed Method
### Method 1 Revit (Linked Model)
#### Key Aspects of Revit Clash Detection
The Interference Check tool in Revit is located under the Collaborate tab (see Figure below) and is used to detect clashes between elements in different linked models. To keep the overview clear, it is recommended to only select relevant categories and work through them systematically instead of checking everything at once.

<img width="595" height="348" alt="Picture 1" src="https://github.com/user-attachments/assets/cd03935a-6abf-4d20-9e42-482471a89f2a" />

#### Workflow




### Method 2 Revizto (Visual Review/Walkthrough)
### Method 3 Navisworks (Advanced Clash Detection)
### Conclusion
