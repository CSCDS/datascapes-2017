
Travel time on road segments (historical)
=========================

# Description #  
In order to collect data on the state of the traffic, the City of Montreal deploys a network of sensors using Bluetooth 
technology on certain strategic road segments and to calculate the travel time on these segments. This dataset presents
the travel times. The Road Segments collection of travel time segments describes segments of the collection network.

### Year ###
2016-01 / 2017-02

### Links to Dataset ###
1. Travel time on road segments (historical) - http://depot.ville.montreal.qc.ca/temps_parcours_bluetooth/trips.csv
2. Road segments for collecting travel time - http://donnees.ville.montreal.qc.ca/dataset/a8f68bfa-5ead-4dda-ab52-b48e45ce9ea0/resource/5c342221-14c1-4593-9e2e-d1044b41dd90/download/bornes.csv

## Data Dictionary ##

### 1. Travel time on road segments (historical) ###

| Column name | Description |
|-------------|-------------|
| __LinkId__ | Unique identifier of the travel time segment.|
|__SrcDetectorId__ |Unique identifier of the original sensor of the segment |
| __DestDetectorId__ |Unique identifier for the segment destination sensor|
| __PathDistance_m__ |Length of the segment, in meters.|
| __TripStart_dt__ | Date and time of the capture at the point of origin of the segment in the format YYYY-MM-DD HH: MM: SS|
| __TripEnd_dt__ | Date and time of the capture at the destination point of the segment in the format YYYY-MM-DD HH: MM: SS|
| __Speed_kmh__ | Average speed calculated on the segment, in kilometers per hour.|
| __TravelTime_s__ | Travel time calculated on the segment, in seconds. |

### 2. Road segments for collecting travel time  ### 

| Column name | Description |
|-------------|-------------|
| __IdLink__ | Unique identifier of the travel time segment.|
|__channel_name__ | Channel name |
| __active__ | Segment activity at the time of data export. 0: inactive, 1:active |
| __LinkID__ | Textual identifier of the travel time segment. Format LXX_AA-BB, XX: identifier of the route, AA: identifier of the source, BB: identifier of the destination.|
| __SrcDetectorId__ | Identifier of the original sensor of the segment (starting point) |
| __SrcLatitude__ | Latitude of the sensor of origin of the segment according to the WGS84 repository. |
| __SrcLongitude__ | Longitude of the original capture of the segment according to the WGS84 repository. |
| __DestDetectorId__ | Segment destination sensor identifier (end point). |
| __DestLatitude__ | Latitude of the destination sensor according to the WGS84 repository. |
| __DestLongitude__ | Longitude of the destination sensor according to the WGS84 repository. |
| __LinkName__ | Full name of the segment. |
| __RouteDirectionName__ |Segment direction of travel time according to the axis of the road segment. N: north, E: east, S: south, O: west. |
| __SrcChannelId__ | Unique identifier of the original channel. |
| __DestChannelId__ | Unique identifier of the destination channel. |
| __LineDistance_m__ | Length of the segment in meters. |
| __last_poll_time__ | The date and time of the last sensor data collection in YYYY-MM-DD HH: MM: SS: mmm format. |
