# SDET

As per my understanding result data having lat between ( -40 to 5) and long between ( 5 to 100) for this users task completion percentage should be greater than 50.

Python requests module is used to fetch the data from URL.
Python Pandas is use to store and manipulation of data as per requirement.

GetDataFromUrl ==> this Function is used to fetch JSON data from parse URL then convert it into DataFrame.
GetTaskCompleteDetails ==> this function is use to calculate total task as per user and compute total percentage of task completion as per completed status.

==  Step to Run ==
Set UserUrl for users data URL.
Set TodosUrl for todos data URL.
set LatLower and LatUpper for LAT values.
set LngLower and LngUpper for LNG Values.
set TaskComplete for percentage of task completion.

After setting values 
run =>
python SDET.py 
