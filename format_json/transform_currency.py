

def flatten_json(row_from_json_file):
    
    indicator_dict = {str('indicator_')+str(k):v for k,v in row_from_json_file.get('indicator').items()}
    
    country_dict = {str('country_')+str(k):v for k,v in row_from_json_file.get('country').items()}

    other_data = {str('currency_')+str(k):v for k,v in row_from_json_file.items() if isinstance(v,dict) == False}
    
    return{**indicator_dict,**country_dict,**other_data}
