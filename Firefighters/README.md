
Firefighter interventions in Montreal
=========================

# Description #  
Data set listing the interventions carried out by the Montreal Fire Safety Service (MIS), including rentals of interventions and units deployed since 2005. These data are taken from the Workstation Assisted Distribution (CAD) system. The central system of the management system interventions that allows real-time management, distribution of vehicles and operational monitoring of interventions. This data is collected to produce reports required by the Ministry of Public Security and necessary for the SIM. It also compiles statistics to disseminate information to citizens and the media.

### Year ###
2005 onwards

## Data Dictionary ##

| Column name | Description |
|-------------|-------------|
| __INCIDENT_NBR__ | identifying the event by year.|
| __CREATION_DATE_TIME__ | date and time of the event.|
| DESCRIPTION_GROUPE |grouping of types of interventions in 6 categories: Building fires, Other fires, Without fire, Fire alarms, First responders, False alerts / cancellations. |
| __INCIDENT_TYPE_DESC__ |type of incident|
| __CASERNE__ |number of the barracks responsible for the territory where the event occurred.|
| __NOM_VILLE__ | Name of the city where the event occurred.|
| __NOM_ARROND__ | Name of the district where the event occurred.|
| __DIVISION__ | number of the MIS division responsible for the territory where the event occurred.|
| __LONGITUDE,LATITUDE__ | geographical position of the event after obfuscation at an intersection according to the WGS84 geodesic datum. |
| __NOMBRE_UNITES__ |number of vehicles deployed to respond to the event. A unit can consist of 3 to 5 firefighters.|
