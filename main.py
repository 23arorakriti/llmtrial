# importing the necessary function from the defined function tools
from autoimmune_func_tool import autoimmune_results
from mentalHealth_func_tool import mentalHealth_results
from cancer_func_tool import cancer_results

# importing the necessary libraries from the llama index 
from llama_index.core.agent import ReActAgent
from llama_index.llms.mistralai import MistralAI
from llama_index.core.tools import  FunctionTool

from llama_index.core import PromptTemplate

# declaring the function tools to be used by the LLM
autoimmune_tool = FunctionTool.from_defaults(fn = autoimmune_results)
mentalHealth_tool = FunctionTool.from_defaults(fn = mentalHealth_results)
cancer_tool = FunctionTool.from_defaults(fn = cancer_results)


# declaration of LLM model to be used and the api key
llm = MistralAI(api_key="o7yegwqm6laeMvsuaoHYDNBAHgJ8smHo")


with open(r"C:\Kriti\college\codefile\llm\trial\react_system_header.md",'r') as f:
    data = f.read()

agent = ReActAgent.from_tools([autoimmune_tool,mentalHealth_tool,cancer_tool], llm=llm, verbose=True,)
#agent.get_prompts()
react_system_prompt = PromptTemplate(data)
agent.update_prompts({"agent_worker:system_prompt":react_system_prompt})

# agent.reset()
res = agent.chat("Provide me 5 misconceptions regarding autoimmune diseases")
print(res)




