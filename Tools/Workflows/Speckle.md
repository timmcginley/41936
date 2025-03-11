# Speckle based workflow
This guide will help you understand how to integrate Speckle into your workflow, making your design and engineering processes more connected, flexible, and efficient. 

## Getting Started with Speckle
### 1. Create a Speckle Account
* Go to [speckle.system](https://www.speckle.systems/) and sign up for a free account.
* Once registered, log in to the Speckle Web App (this is your online hub)

### 2. Install Speckle Connectors
Speckle works by connecting your software (like Revit, Rhino, AutoCAD) to a cloud-based system. You need to install the right "Connector" for your tool
* Download Speckle Manager from Speckle’s website.
* Open Speckle Manager and install the connectors for your software (e.g., Revit, Rhino, Grasshopper)

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
