import pandas as pd
from pandasql import sqldf


cancer_dataframe = pd.read_excel(r"C:\Kriti\college\codefile\llm\trial\final_cancer_excel.xlsx",engine='openpyxl')


def cancer_results(number_of_results):
    '''
    This function tool gives the summaries and the links based on the query by passing the parameter
    based on the cancer dataframe
    
    number_of_tokens : This is the paramters which tells how many results have to be retrieved 

    '''
    #cancer_dataframe = pd.read_excel(r"C:\Users\anshumaan.garg\Documents\MV\final_excels\final_cancer_excel.xlsx")
    query = f"Select summary,links from cancer_dataframe LIMIT {number_of_results}"
    result = sqldf(query,globals())
    # for i in range(len(result)):
    #     if result[]
    # result = result.to_string()
    # result.to_json("new.json")
    return result

#print(cancer_results(12))