# Speckle based workflow
This guide will help you understand how to integrate Speckle into your workflow, making your design and engineering processes more connected, flexible, and efficient. 

## Getting Started with Speckle
For DTU Students – 2025 Edition

### 1. Create a Speckle Account
* visit [https://app.speckle.systems](https://app.speckle.systems)
* Sign up using your @dtu.dk or @student.dtu.dk email address. 
* You’ve been automatically invited to join the DTU Workspace. Check your email and accept the invitation to collaborate with classmates and access shared content. 

### 2. Install a Connector
* After signing in, go to the Connectors tab in the Speckle Web App. 
* Download and install the connector for your software (e.g., Revit, Rhino, Grasshopper, etc.)

```{info} Best Model Award
The model that passes all the tests and get the most sticker votes.
```
### 3. Create a Project and Model 
* From your Speckle Web App dashboard, click "New Project" 
* Name your project ABD-[year]-[team]-[stage](e.g., "ABD-25-10-C-ARCH") ● Within your project, create one or more Models. For example: 
      * "ARCH" 
      * "Structural Core" 
      * "Services Layout"
  
### 4. How Multi-Disciplinary Teams Work on One Project in Speckle: 
● Invite team members by email and assign them roles: 
 
○ Owner – Full control over the project 
○ Editor – Can publish data and manage models. 
○ Viewer – Can view models and leave comments. 
💡 In the DTU Workspace, all students can view each other’s projects by default; this is useful for peer review and collaborative learning. 

### 3. Set Up a Speckle Stream
A "Stream" in Speckle is like a shared project where you send and receive data.
* Open your Speckle Web App and create a new stream.
* Name it (e.g., “My Revit to Rhino Project”) and save it.
* Copy the Stream URL—you’ll use it to send data from your software.
* Send Data from Revit (or Other Software)

Let’s say you want to send a Revit model to Rhino :
* Open Revit and go to the Speckle Connector (found in the Add-ins tab).
* Select the stream you created earlier.
* Choose the elements or the entire model to send.
* Click "Send"—Speckle will upload your data to the cloud.

Receive Data in Rhino (or another tool)
* Open Rhino and launch the Speckle Connector (from the toolbar or command line).
* Select the same stream from your Speckle account.
* Click "Receive"—your Revit model will now appear in Rhino!

Now you’ve successfully transferred data between Revit and Rhino using Speckle
## How multi-disciplinary Teams Work on One Project in Speckle:
### 1) Set Up a Shared Speckle Stream for the Project
A **Speckle Stream** acts as a central repository where each discipline contributes their model data. Follow these steps to collaborate efficiently with your team.
* Open the **Speckle Web App**.
* Click **"Create a New Stream"** (e.g., "Mixed-Use Tower Project").
* Share the stream with all team members (architects, structural engineers, MEP designers).
* Assign roles
Now, every discipline can send and receive data without overwriting each other’s work.

### 2) Sending and Receiving Data per Discipline
Each team works in their own software and **sends updates to the shared Speckle stream.**
Now, all models are stored separately but visible together in the Speckle web viewer.

### 3) Viewing the Combined Model in Speckle Web
      1) Go to the **Speckle Web App** and open the shared project stream.
       2) Turn on/off different layers (Architectural, Structural, MEP).
       3) Use the **"Compare Versions"** tool to track updates from each discipline.
       4) Add **comments** for feedback directly in the 3D viewer.
This allows all teams to see the entire project without needing Revit, Rhino, or Tekla.
