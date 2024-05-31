
import sys
import requests
import pandas as pd

##############################################
# Function for get data from any provided URL#
#                                            #
##############################################

def GetDataFromUrl(url):
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            UrlData = response.json()
            # Convert Json Data into DataFrame
            JsonDF = pd.json_normalize(UrlData)
            return JsonDF
        else:
            print(f"Failed to fetch data. \nHTTP response code: {response.status_code}.")
    except requests.RequestException as Err:
        print(f"Error occurred while executing URL.\n Error :{Err}")

def GetTaskCompleteDetails(CalcDF):
        #print(CalcDF)
        if CalcDF is not None:
            CalculatedDataFrame = CalcDF.groupby('userId').agg(TotalTasksCount = ('id', 'count'),CompleteTaksCount = ('completed','sum') 
            ).reset_index()
            #print(CalculatedDataFrame)
            
            CalculatedDataFrame['CompleteTaksPerc'] = (CalculatedDataFrame['CompleteTaksCount'] / CalculatedDataFrame['TotalTasksCount']) * 100
            return CalculatedDataFrame
        else:
            print("Check DataFrame may be empty or None")


if __name__ == '__main__':
    
    url = 'https://jsonplaceholder.typicode.com/users'

    UserDatilsDF = GetDataFromUrl(url)
    #print(UserDatilsDF)
    
    url = 'https://jsonplaceholder.typicode.com/todos'
    ToDoDF = GetDataFromUrl(url)
    #print(ToDoDF)
    
    #ToDoDF.info()
    #UserDatilsDF.info()
    for column in UserDatilsDF.columns:
        UserDatilsDF[column] = pd.to_numeric(UserDatilsDF[column],errors='ignore')
    #UserDatilsDF.info()
    
    ## filter as per lat and lng data
    CityDataframe = UserDatilsDF[UserDatilsDF["address.geo.lat"].between(-40,5) & UserDatilsDF["address.geo.lng"].between(5,100)]
    #print(CityDataframe)
    
    ## Calculate task complete as per todo list
    CalculatedToDo = GetTaskCompleteDetails(ToDoDF)
    #print(CalculatedToDo)
    
    MappedDataFrame = pd.merge(CityDataframe, CalculatedToDo, how='inner', left_on='id', right_on='userId')
    #print(FinalData)
    
    FinalDataFrame = MappedDataFrame[MappedDataFrame['CompleteTaksPerc']> 50]
    print(FinalDataFrame.drop(CalculatedToDo.columns,axis = 1))
    
    
    

