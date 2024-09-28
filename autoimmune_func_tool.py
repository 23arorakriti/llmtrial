import pandas as pd
from pandasql import sqldf

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


autoimmune_dataframe = pd.read_excel(r"C:\Kriti\college\codefile\llm\trial\final_autoimmune_excel.xlsx",engine='openpyxl')

def autoimmune_results(number_of_results: int) -> pd.DataFrame:
    '''
    This function tool gives the summaries and the links based on the query by passing the parameter
    based on the cancer dataframe
    
    number_of_tokens : This is the paramters which tells how many results have to be retrieved 

    '''
    #cancer_dataframe = pd.read_excel(r"C:\Users\anshumaan.garg\Documents\MV\final_excels\final_cancer_excel.xlsx")
    query = f"Select summary,links from autoimmune_dataframe LIMIT {number_of_results}"
    result = sqldf(query,globals())
    # result = result.to_string()
    return result