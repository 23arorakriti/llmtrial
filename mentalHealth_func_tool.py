import pandas as pd
from pandasql import sqldf

mentalHealth_dataframe = pd.read_excel(r"C:\Kriti\college\codefile\llm\trial\final_mentalHealth_excel.xlsx")


def mentalHealth_results(number_of_results):
    '''
    This function tool gives the summaries and the links based on the query by passing the parameter based on 
    the mental health dataframe

    number_of_tokens : This is the paramters which tells how many results have to be retrieved 

    '''
    #mentalHealth_dataframe = pd.read_excel(r"C:\Users\anshumaan.garg\Documents\MV\final_excels\final_autoimmune_excel.xlsx")
    query = f"Select summary,links from mentalHealth_dataframe LIMIT {number_of_results}"
    result = sqldf(query,globals())
    result = result.to_string()
    return result


