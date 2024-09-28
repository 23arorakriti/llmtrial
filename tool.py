tools = [
    {
        "type": "function",
        "function": {
            "name": "cancer_results",
            "description": "Get cancer results",
            "parameters": {
                "type": "object",
                "properties": {
                    "number_of_results": {
                        "type": "integer",
                        "description": "number of results to be fetched",
                    }
                },
                "required": ["number_of_results"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "autoimmune_results",
            "description": "Get autoimmune results",
            "parameters": {
                "type": "object",
                "properties": {
                    "number_of_results": {
                        "type": "integer",
                        "description": "number of results to be fetched",
                    }
                },
                "required": ["number_of_results"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mentalHealth_results",
            "description": "Get mentalHealth results",
            "parameters": {
                "type": "object",
                "properties": {
                    "number_of_results": {
                        "type": "integer",
                        "description": "number of results to be fetched",
                    }
                },
                "required": ["number_of_results"],
            },
        },
    },
 

 

]