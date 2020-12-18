import logging
import time
import os
import json

import azure.functions as func
import pandas as pd

from format_json import transform_currency


def main(inblob: func.InputStream, outblob: func.Out[bytes], context: func.Context):

    logging.info(
        f"Python blob trigger function processed blob \n" f"Name: {inblob.name}\n"
    )
    #reading in our JSON file thats just been loaded in. 
    json_data = json.loads(inblob.read())
        
    #format data to it is a list of dicts
    json_data_formatted = [transform_currency.flatten_json(i) for i in json_data[1]]
    
    #As its a list of dicts we can through that into a pandas dataframe
    data_to_load_into_storage = pd.DataFrame(json_data_formatted)
    
    #converting our pandas dataframe to a CSV file. 
    output = data_to_load_into_storage.to_csv(encoding='utf-8')
    
    #saving that CSV files to the "processed" folder outlined in the function.json file.
    outblob.set(output)
