
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
The process starts by organizing the model properly. This includes using consistent naming conventions and setting up a dedicated 3D view specifically for coordination. In this view, all relevant elements should be visible, while unnecessary elements such as furniture (e.g., desks and chairs) should be hidden to avoid noise in the analysis.
 
Organize the Model
* Use consistent naming conventions.
* Create a dedicated 3D view for coordination.
* Ensure all relevant elements are visible.
* Hide non-relevant elements (e.g., furniture such as desks and chairs).

**Run Clash Detection**
Go to (or see Figure above:)

**Collaborate → Interference Check → Run Interference Check**

Here, various categories can be selected depending on the coordination focus (see Figure 4-2). For example, the entire model can be checked against ducts, or structural elements can be assessed against MEP systems. It is important to test different combinations and adapt the setup to what works best for the team. Filtering out irrelevant elements can improve both clarity and performance.
 
<img width="405" height="455" alt="Picture 1" src="https://github.com/user-attachments/assets/4ad2221e-ba0e-4d17-b3b4-6870abf69eed" />
<img width="278" height="448" alt="Picture 11" src="https://github.com/user-attachments/assets/cea0906c-f9cc-4e18-8d48-89afcc9bd7c4" />



Once the check is completed, Revit generates a report showing all detected clashes (see Figure 4-3). In this case, the example illustrates a full model check against the duct and ventilation system.

The results should then be carefully reviewed. Revit allows users to highlight and zoom into problematic elements directly from the report by clicking ‘Show’. Critical clashes should be identified, documented, and communicated to the relevant disciplines or the full project team.
 
Finally, the detected issues must be resolved in the model. After making the necessary changes, the interference check should be run again to confirm that all clashes have been cleared.




### Method 2 Revizto (Visual Review/Walkthrough)
#### Revitzo Visual Review

The Revizto workflow begins by publishing the linked Revit model directly into Revizto, allowing for integrated model coordination and review in a shared environment.
 
Clash detection in this method is performed manually through a visual walkthrough of the model. This involves navigating through the building and systematically checking all areas, including rooms, technical spaces, shafts, and ventilation zones. The goal is to identify issues that may not always be captured through automated clash detection, such as spatial conflicts, access problems, or coordination gaps between disciplines.
 
This method is also useful for evaluating the layout and overall flow of the building. If rooms are properly labeled, it becomes easier to understand how spaces connect and function in practice. 

#### Workflow

**Publish to Revizto**

The model is published directly from Revit using the Revizto plugin (see Figure below). Once published, the model becomes available in Revizto for review.

**Revizto 5→ Revizto 5 → Publish to Revizto**
<img width="805" height="155" alt="Picture1111" src="https://github.com/user-attachments/assets/727867e7-ee6c-4738-9a4f-f884122f45a7" />

**Open the project in Revizto**
After publishing the updated model, open it in Revizto and switch to the 3D view to begin the walkthrough.

<img width="805" height="420" alt="Picture1111111" src="https://github.com/user-attachments/assets/bab8bcd6-ce5f-4b2e-80c5-1f265b6d46b5" />

**Navigation is done using standard controls:**
* Use the mouse (right-click) to look around.
* Scroll to move forward and backward.
* Use W, A, S, D to move through the model.
 
If rooms are labeled, you can navigate between rooms by clicking on doors (see Figure 4-5), to move between spaces and simulate how users would experience the building.
All identified issues should be documented and grouped based on importance and affected disciplines. This makes it easier to assign responsibility and track progress during coordination.
 
Critical clashes should then be resolved within the team, and the model updated accordingly. This process should be repeated throughout the project. It is recommended to perform these checks multiple times between submissions, to allow time for corrections and avoid late-stage conflicts.


### Method 3 Navisworks (Advanced Clash Detection)
#### Key Aspects of Navisworks Clash Detection

Navisworks is used for advanced and systematic clash detection by combining models from different disciplines into a single coordination model. Unlike Revit and Revizto, Navisworks allows for automated clash detection with defined rules, tolerances, and structured grouping of results.

This makes it especially useful in later design stages or before construction, where a more comprehensive and controlled clash analysis is required. For a better visual understanding of the workflow, it is recommended to supplement this guide with video tutorials (see provided links).

#### Setup Navisworks
Before running clash detection, the models must be properly prepared and exported.

* Ensure the same software version is used across tools (e.g., Revit 2026, Navisworks 2026)
* Install required tools:
  * Navisworks Manage
  * C Export Utility
  * Revit NWC Add-in
Models must be exported as.NWC files from Revit to be used in Navisworks.

<img width="420" height="285" alt="Picture11111" src="https://github.com/user-attachments/assets/1b872141-8e15-4789-bca5-9ba2de2777a1" />

#### Workflow
Models are exported from Revit as NWC files and imported into Navisworks. Instead of exporting a combined model, it is recommended to export each discipline separately (e.g., ARCH, STR, MEP, GEO).

**File→ Export → NWC (see Figure below)**
<img width="335" height="400" alt="Picture11111" src="https://github.com/user-attachments/assets/bea1a6a1-9c15-41da-bdfd-2eb1b53c192e" />

**Run Clash Detection**
Clash detection in Navisworks is performed using the Clash Detective tool, located under the Home tab. This tool allows you to define clash tests, compare elements, and generate structured results.

To create a clash test, open the Clash Detective window and click “Add Test”. Each test should be clearly named based on the disciplines being compared (e.g., STR vs MEP).

In the Select tab, two selection panels are used to define which elements are tested against each other. Here, you can either select entire models or choose specific categories, levels, or systems. Using predefined selection sets is recommended, as it makes the process faster, more consistent, and easier to repeat.

Several types of clash detection can be defined depending on the purpose of the analysis:
* **Hard clashes**: Detect physical intersections between elements.
* **Clearance clashes**: Detect elements that are too close to each other.
* **Duplicate clashes**: Identify identical elements placed in the same location. 

Tolerance settings can be adjusted to control the sensitivity of the test and filter out minor or irrelevant clashes.

Once all settings are defined, the clash test is executed by clicking “**Run Test**”.
 
**Review Clashes**

After running the test, the results are displayed in the Results tab. Each clash can be selected and reviewed directly in the model, where it can be inspected using zoom and navigation tools.

To improve clarity:
•	Filter out irrelevant clashes 
•	Group similar clashes. 
•	Adjust tolerances if too many minor clashes appear. 

Navisworks provides a structured overview, making it easier to manage large numbers of clashes compared to manual methods.
 
**Resolve clashes**

Clash results should be shared with the project team and assigned to the relevant disciplines for resolution.

After updates are made in the individual models, the clash tests should be re-run to verify that issues have been resolved.

Reports can be generated directly from Navisworks (e.g., HTML format) to document clashes and support coordination between disciplines.

#### Learning Resources
Since Navisworks can be more complex to set up and use, video tutorials can help understand the workflow and interface:
* [Perform a clash test in Navisworks Manage - Autodesk](https://www.autodesk.com/learn/ondemand/curated/mep-and-structural-coordination/2MxCJVABpvs0sQGYkuZd1Z)
* [EXPORTING REVIT TO NAVISWORKS - YouTube](https://www.youtube.com/watch?v=nAZFTtCQyLk)
* [Autodesk Navisworks Clash Detection Overview - YouTube](https://www.youtube.com/watch?v=v3uDiV2eQt0)
These provide step-by-step visual demonstrations of model setup, clash detection, and result analysis.

### Conclusion
Each method offers different strengths depending on the project phase and level of detail required. Revit is well-suited for early-stage coordination, Revizto supports spatial understanding and design validation, while Navisworks enables detailed and systematic clash detection. In practice, a combination of these tools is used to ensure both efficient coordination and high model quality.
