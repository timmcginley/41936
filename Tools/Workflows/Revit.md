# Revit based collaboration

The following is a step by step guide on how you can create a central file in Revit and use work sharing through OneDrive. 

Collaboration in the AEC is normally supported in the AEC with a CDE. However these are frequently cloud based propritary platforms that lock your data into them. Whilst we understand the need to use propritory authoring tools in the course, we are keen to find alternatives to these cloud lock in platforms therefore the course will not promote platforms such as BIM360.

An alternative Revit based approach is provided below, please also check out the [Speckle](Speckle.md) alternative.

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

```{note}
It is critical for all disciplines to follow the same zero coordinate before linking the files, so all models are aligned when they are linked. 
```
**First do the following before linking**
To ensure proper coordination among all disciplines, follow these steps:
1.	Go to the Site View in Revit.
2.	Select all the grids, but make sure to exclude the zero coordinate from your selection.
3.	Choose an intersection of two grids as a reference point.
4.	Move all the selected grids so that the chosen intersection aligns with the zero coordinate.
5.	Ensure that all disciplines use the same zero coordinate for consistency.
Look at the picture below :
![image](https://github.com/user-attachments/assets/34301344-5f0c-4166-a40f-ed97fcc804fe)

**Now follow these steps to link the files.**
1.	Open your Revit file.
2.	Go to Insert → Link Revit.
3.	Select the latest version of the other discipline’s Revit files.
4.	Choose Origin to Origin or Shared Coordinates for proper alignment.
5.	Click Open → The file will be linked into the model.

## Updating Links Regularly
Whenever team members update their files:
1.	Replace the old linked file with the updated one.
2.	Ensure that all elements are coordinated correctly.
3.	Communicate with the team to avoid inconsistencies.



