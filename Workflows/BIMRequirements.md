# Generate Graph from BIM Model
The following contains a step by step guide and a list of requirements to gerenrate a graph from a basic BIM model: 
## Basic BIM Requirements
### 1.The following elements must be modeled in the BIM model:

- Floors  
- Walls  
- Ceilings  
- Doors  
---

### 2. Rooms and Room Bounding

- All rooms must be properly located in the model.
- Rooms must be created using the room tool so they can be exported to IFC.
- When creating walls, make sure the “Room Bounding” option is checked in the wall properties panel.

#### Important:
**Walls must be created separately for each space (room)**. Avoid using continuous walls that spans across multiple rooms. This is to make sure that adjacencies are detected correctly.

---

### 3. Required Room Attributes

Each room must include the following attributes:

- Room Name
- Area
- Volume
- Occupancy

#### Pharma Projects (ISO Grade)
- If a room has an ISO grade, write it **after the room name**, separated by a hyphen.

**Example:**

 `Weighing Room - ISO 7`

 `Clean Corridor - ISO 8`

- If a room is **unclassified**, do **not** add anything after the room name.

---

### 4. Export to IFC

- Export the model using [IFC 4x3] (https://timmcginley.github.io/41936/Workflows/IFC4X3Export.html) 

- Make sure you are using the latest version of the Revit/IFC exporter.

- Follow the instructions below to ensure the IFC export and room attributes are set up correctly.


<img width="980" height="613" alt="ifc 1" src="https://github.com/user-attachments/assets/4af93649-6811-4070-8fb6-8eb1a14e45b5" />


<img width="980" height="617" alt="ifc 2" src="https://github.com/user-attachments/assets/46bceb01-e206-4e9e-97a5-41fe4ead3b43" />


---

## Graph Specification

### Purpose of the Graph

The graph is a simplified representation of the building used for early-stage reasoning and interdisciplinary exchange. The graph:

- focuses on spaces and their relationships
- does not represent detailed geometry
- acts as an intermediate layer between basic BIM models and later detailed design
- is generated automatically from the IFC file

---

### Graph Structure Overview

- **Nodes** represent spaces (rooms)
- **Edges** represent relationships between spaces
- **Attributes** store key information needed for analysis

---

### Nodes (Spaces)

Each space(room) in the BIM model becomes one node in the graph.

Nodes represent:
- A functional space (defined by the room name)
- The attributes associated with that space


---

### Edges (Relationships)

Edges represent direct adjacency between spaces. An edge is created when two rooms share a wall or boundary in the BIM model

Edges represent:
- Which spaces belong to which level (containment)
- Which spaces are directly connected
- Edges are undirected (adjacency works both ways)

---

### Graph Visulaization
To see the graph in the graph viewer, clone the GitHub repository [ABDGraph GitHub repository](https://github.com/rominabarouti/ABDGraph)
 to your computer and follow the instructions in the README to run it locally.



