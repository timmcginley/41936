*DEPRECIATED*
# Fire
*The subject of fire safety is divided into a part 1, focusing on the safety of occupants, and a part 2, focusing on the structural fire safety. This structure, reflects the timeline of a fire, which can also be divided into two main phases:*

* A pre-flashover phase, including an ignition phase and a growing phase, as combustible materials in the room are successively ignited and the fire spread in the compartment. In the pre-flashover phase, two zones can be identified in the compartment, a lower cooler zone and an upper zone filled with smoke and characterized by high temperatures. The premises should be promptly evacuated, as people safety can be at risk due to smoke in-halation and lack of visibility.

* A post-flashover phase, including a fully developed fire phase and a decay phase, where temperature decreases as the fuel is consumed and the fire is extinguished. In the post-flashover phase the temperature of the gas, which are assumed to be uniform within the compartment, heat the structural elements, which may be at risk of failure.

## Fire Requirements 

## Core fire safety
An open staircase is not enough, there need to be several staircases with a fire cell around (staircase in a core). This can also be staircases on the façade as seen on building 127 (DTU).

* 30 meters distance from any point (so maximum 30m walk to a staircase. So, the maximum distance between staircases is 60m).
* Min. 1.2 meters wide (+ 10 mm pr. person passing) (sizing of staircase if you want to calculate the size Not so important right now)
* Exits (to the open)
* 25 meters distance from any point (Meaning where need to be maximum 25 meters to a door leading to hallway with a staircase)
* Structure: Staircase as a fire cell

## Part 1: Safety of occupants
The following aspects need to be considered in fire safety in the pre-flashover phase:

* evacuation,
* fire spread,
* access of the rescue service,
* passive and active fire protection and
* operation and

In order to secure fire safety within high-rise buildings, the pre-flashover phase has additional requirements.

During the course you can choose to work on:

## Option 1:Minimumfire safety
If you use minimum requirement your team has to follow traditional building rules (no atria, large compartments etc.).

## Option 2: Fire safety as a focus domain with full requirements
If you plan an untraditional building, including large open spaces, you must take care of the full requirements for fire safety.

* For traditional part of the building you should apply the prescriptive rules given in “Eksempelsamling om brandsikring af byggeri 2012” [1] (Unfortunately this document is only available in Danish).
* Remember, that you are free to build anything you want as long as you can verify that people can evacuate without being affected by critical conditions [2]. This you will have to pick relevant scenarios, proof the fire safety using at least hand calculations and make risk calculations and present an event tree.

Please have a look at the File “11080 EÅ19 – FIRE - Further details on fire requirements” for more details. [TO DO: Ask teachers for more information] 

## Part 2: Structural fire safety
You are expected to design and verify that your structure can resist fire. You are allowed to limit your design to a number of structural elements, but you should at least consider:
* one beam
* one column
* one floor slab

The three elements do not necessarily have to be placed in the same compartment and should instead be chosen among those, which are expected to be most critical for fire design, because they are for example heavily loaded or highly exposed to fire. If untraditional elements are present in the building, such as long cantile vers, steel cables, wood connections, or other elements that for some reasons can be expected to have a critical behaviour during a fire, you should also explicitly perform the fire design of those elements too. Special attention should be also paid to elements, the failure of which could lead to disproportionate damage, such as a transfer beam or other key elements, which play a strategic role in carrying the loads to the ground.

Please have a look at the file “11080 FÅ22 – Subj.5 - How to fulfil fire requirements” formore details. [TO DO: Askteachers for more information]

# Fire Integration

## Fire -> Architecture 
* The design of staircases and rescue staircases
* The distribution of spaces chosen determines the choice and size of compartments
* The intended destination of usage influences the loads
* The type of facades and internal walls affects the calculation of thermal inertia
* The presence of suspended ceiling influences the height of the smoke layer and may reduce the temperature of the structural elements behind the ceiling (if fire tight)
* Fire design choices such as type and amount of insulations may be incompatible with aesthetic or architectonic needs
* The type and material of enclosures should fulfil the fire rating and provide sufficient compartmentalization.

## Fire -> Structure 
* structural choices have a great impact on the fire design and should be discussed and agreed with all the group members since the very early stage of the project
* The structural and static scheme chosen in Subj. 2 should be consistent with those used for fire calculations
* Constructive details (e.g. the way a floor slab is supported by the beams) affect the section factor and therefore the temperature of the elements
* Modifications on the element size or material for being compliant with fire verifications reflects on the weight and stiffness of the structure assumed in Subj. 2 and vice-versa. This means that it may be necessary to recalculate the whole structure after the fire verifications. Please take into account this time, so that the modifications to the structure can be documented in the 3-week report at latest.

## Fire -> MEP 
* ventilation systems might influence the smoke spread in the building and the opening factor of the compartment
* Energy saving materials and wall insulation affect the calculation of the thermal inertia of the compartment
* when designing the pipe system, attention should be paid to the definition of fire compartments and possible escape of smoke and fire from holes and venting in the walls
* Consider fire safety installations for fire extinguishing, overpressure in staircases, etc.
* The type of beam-slab system used may affect the space you have for the installation; holes made to let pipes through structural elements strongly increase the exposure and heating temperature of the elements, as well as the complexity and of the insulating solutions.

## Fire -> Geotech 
* Limitations of fire spread in the underground parking lot
* Evacuation from the underground parking lot

## Fire -> PM/ICT 
The fire subject needs support from ICT/PM to model the costs of different fire engineering options.

* Fire strategy and insulation choices have a great impact on the overall costs and should be discussed and agreed among the group members. Attention should be paid on the effect of the fire design choices on the overall economy, sustainability and resilience of the building and in particular
* Evacuation strategy: cost related to training of staff and occupants, maintenance of the alarm systems etc
* Active measures: cost related to installing and maintenance of the sprinkler system or other fire suppression provisions.
* Passive measures: amount and type of insulations influences the costs of the building (for example, fire resistant glasses are beautiful, but often uneconomical; intumescent paint is also a good aesthetic choice, but is more expensive and less reliable of other type of insulations; furthermore, some type of painting can be toxic and have repercussion on the people and environment).
* Structural elements: composite sections such as delta-beams and concrete filled steel hollow section may have better fire performance than steel sections, due to the heat capacity of the concrete that absorb part of the heat; it is however not possible to take this aspect into account by means of simple calculations. This means that, unless you are not willing to spend significant time by implementing a thermal model of the section e.g. in Abaqus, you will conservatively verify the sole external steel section against fire. The result is that the benefit of using a composite section (which costs and weight more than a steel section) are completely lost after the fire verification, where you also add additional costs for the insulation. The use of composite sections should therefore be considered car efully and all related costs of materials and insulation should be documented in Subj.6. Similar considerations also apply to hollow-core slabs that need bottom insulation in order to prevent cracking of the flange below the holes and a consequent faster heating of the element [10].
* Cost management: All system used for fire safety and structural fire safety should be added in the total cost of the building.

## Fire -> Materials
* Concrete is often considered to have good fire behaviour, but it is permanently damaged by the fire, while structural steel regain full strength after cooling. On the other side, steel elements typically need to be insulated and the cost of fire protection must be added to the structural costs. In short, there is no ultimate better material for fire, as long as all costs are included and a design optimization is considered, where both the costs of the structural material and of the insulation are considered.
* A special mention goes to timber, as it pose special challenges to fire safety for three main reasons:
* * from the structural point of view, a full timber structure constitutes a significant addition to the fuel load of the compartments (even if it is not directly exposed);
* * from the evacuation point of view, exposed timber causes smoke and hinders evacuation;
* * consequently, from the compartmentalization point of view, the risk of fire spread is also higher. This includes horizontal and vertical fire spread in the building, but also external fire spread to adjacent buildings (even in case there is no exposed timber on the facade).
