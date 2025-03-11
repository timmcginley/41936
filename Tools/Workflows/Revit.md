# Revit

The following is a step by step guide on how you can create a central file in Revit and use work sharing through OneDrive. Ideally, collaboration is carried out using the BIM360 framework but as this option is currently unavailable, the below approach is proposed as an alternative.  

## Option 1: Creating a central file 
### Step 1: Create a shared folder on OneDrive

Create a folder on OneDrive  and share it with other team members with Edit access. The folder can indicate your group/project name. 

### Step 2: Create a Revit central file

1. Open Revit and go to Collaborate → Collaborate in (Worksharing)
![image](https://github.com/user-attachments/assets/5e462535-80d9-433f-9e39-bfe9d19659b6)

2. Turn on worksharing and define Worksets if needed.
![image](https://github.com/user-attachments/assets/58cb9907-94f1-4429-8e06-84c7451e5fc8)
![image](https://github.com/user-attachments/assets/733d8623-5796-41e4-834e-101bd96e10e0)

3. Click File → Save As → Project.

![image](https://github.com/user-attachments/assets/b5fa3bc2-3995-4f6c-92d6-4be4faeaaede)

4. Navigate to the OneDrive folder you created above
5.	Check "Make this a Central Model after saving".
6.	Close the file to finalize the central model.

### Step 3: Create local files for team members

Each collaborator should do the following:

1.	Go to the OneDrive folder and locate the central Revit file.
2.	Copy and place the central file in *C:\Revit_Local_Files* or another local path of your choice.
3.	Open Revit → Open → Select the copied file.
4.	Check "Create New Local"
5.	Click Open.

## Collaboration and Syncing

### Syncing with the central file
1.	Edit the model as needed on your local machine.
2.	Save Local Changes.
3.	Click Collaborate → Synchronize with Central.
4.	The central file stored in OneDrive  should now be updated with your changes.
5.	Close the model when done.

### Tips and best practices
1.	Always use "Create New Local" when opening the model.
2.	Avoid opening the central file directly.
3.	If OneDrive  sync is stuck, pause and resume OneDrive.
4.	Only one user should sync at a time to avoid conflicts.
5.	Set automatic backups in Revit (File → Options → File Locations).
OneDrive  keeps version history, so you can restore an earlier file if needed.
![image](https://github.com/user-attachments/assets/c2039e82-6386-4dcf-a274-d4b84cab17e8)

Overview of the collaboration architecture with One Drive

## Option 2: Alternative Collaboration Without a Central File
If your team cannot work with a Central File due to location constraints, follow these steps instead:
### Share Updated Files
1.	Each user works on their own separate Revit file.
2.	At the end of a work session, the updated file should be shared with the team.(Can be on OneDrive)
3.	Each team member should always start with the latest version of all files.
### Linking Discipline Files 
Whether you use option 1 or 2 all disciplines should always link their files so changes are visible to all disciplines. 

*Note: It is critical for all disciplines to follow the same zero coordinate before linking the files, so all models are aligned when they are linked. 

