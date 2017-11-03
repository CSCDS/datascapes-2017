
Travel time on road segments (historical)
=========================

# Description #  
In order to collect data on the state of the traffic, the City of Montreal deploys a network of sensors using Bluetooth 
technology on certain strategic road segments and to calculate the travel time on these segments. This dataset presents
the travel times. The Road Segments collection of travel time segments describes segments of the collection network.

### Year ###
2016-01 / 2017-02

## Data Dictionary ##

| Column name | Description |
|-------------|-------------|
| __LinkId__ | Unique ID |
| __NATURE__ | Unique identifier of the travel time segment. Format LXX_AA-BB, XX identifier of the route, AA identifier of the source, BB identifier of the destination. This idenfiant makes it possible to make the link with the data set road segments collection of travel times.|
|__SrcDetectorId__ |Unique identifier of the original sensor of the segment |
| __DestDetectorId__ |Unique identifier for the segment destination sensor|
| __PathDistance_m__ |Length of the segment, in meters.|
| __TripStart_dt__ | Date and time of the capture at the point of origin of the segment in the format YYYY-MM-DD HH: MM: SS|
| __TripEnd_dt__ | Date and time of the capture at the destination point of the segment in the format YYYY-MM-DD HH: MM: SS|
| __Speed_kmh__ | Average speed calculated on the segment, in kilometers per hour.|
| __TravelTime_s__ | Travel time calculated on the segment, in seconds. |
