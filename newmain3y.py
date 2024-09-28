import functools
from autoimmune_func_tool import autoimmune_results
from mentalHealth_func_tool import mentalHealth_results
from cancer_func_tool import cancer_results
from mistralai import Mistral
from tool import tools
import json
from val_sum2 import perform_validation

names_to_functions = {
    'cancer_results': functools.partial(cancer_results),
    'autoimmune_results': functools.partial(autoimmune_results),
    'mentalHealth_results': functools.partial(mentalHealth_results),  
    }

api_key = "Fnf32jVSo1ljuCPlnl7wsEOtxu48lioc"
model = "mistral-large-latest"

messages = [{"role": "user", "content": "Show me 6 misconceptions regarding cancer diseases"}]

client = Mistral(api_key=api_key)
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="any",
)

results = []

for tool_call in response.choices[0].message.tool_calls:
    function_name = tool_call.function.name
    function_params = json.loads(tool_call.function.arguments)
    function_result = names_to_functions[function_name](**function_params)
    print(f"function_name: {function_name}")
    print(f"function_result: {function_result}")

    
    if hasattr(function_result, 'to_dict'):  
        function_result = function_result.to_dict()  
    
    data = {
        "Function": function_name,
        "Result": function_result
    }

    results.append(data)

   

with open("resp.json", 'w') as f:
    json.dump(results, f, indent=4)

a=input("\nDo you have any misconception to validate (y/n)=")
if(a=='y'or a=='Y'):
 b=input("\nenter your misconception to validate=")
 data = {"misconception": b}
 with open('user.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
 print("\nGenerating validations...\n")
 sec_key = "Fnf32jVSo1ljuCPlnl7wsEOtxu48lioc"
 model = "mistral-large-latest"
 json_file_path = r"C:\Kriti\college\codefile\llm\user.json"
 validation_text_file_path = r"C:\Kriti\college\codefile\llm\trial\cancer_summary.txt"
 txt_file_path = r"C:\Kriti\college\codefile\llm\trial\user_validation.txt"
 summary = perform_validation(sec_key, model, json_file_path, validation_text_file_path, txt_file_path)
 print(f"Validation summary:\n{summary}")

 
# a=input("\nDo you want validation(y/n)=")
# if(a=='y'or a=='Y'):
#  print("\nGenerating validations...\n")
#  sec_key = "Fnf32jVSo1ljuCPlnl7wsEOtxu48lioc"
#  model = "mistral-large-latest"
#  json_file_path = r"C:\Kriti\college\codefile\llm\resp.json"
#  validation_text_file_path = r"C:\Kriti\college\codefile\llm\trial\mentalhealth_summary.txt"
#  txt_file_path = r"C:\Kriti\college\codefile\llm\trial\mentalhealth_validation.txt"
#  summary = perform_validation(sec_key, model, json_file_path, validation_text_file_path, txt_file_path)
#  print(f"Validation summary:\n{summary}")

