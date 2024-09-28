from mistralai import Mistral

# Define your Mistral API key and model
sec_key = 'Fnf32jVSo1ljuCPlnl7wsEOtxu48lioc'
model = 'mistral-large-latest'

# Define file paths using raw string literals
input_txt_file_path = r'C:\Kriti\college\codefile\llm\trial\cancer_extracted.txt'
output_txt_file_path = r'C:\Kriti\college\codefile\llm\trial\cancer_sum.txt'

# Checkpoint 1: Reading text from input file
try:
    with open(input_txt_file_path, 'r', encoding='Windows-1252') as file:
        text = file.read()
    print("Checkpoint 1: Successfully read input file.")
except Exception as e:
    print(f"Error at Checkpoint 1: {e}")

# Initialize Mistral client
try:
    client = Mistral(api_key=sec_key)
    print("Checkpoint 2: Mistral client initialized.")
except Exception as e:
    print(f"Error at Checkpoint 2: {e}")

# Generate summary
try:
    messages = [
        {
            "role": "user",
            "content": f"Summarize the following text in detail and depth in 2000 or more words:\n\n{text}"
        }
    ]
    
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
    )
    print("Checkpoint 3: Successfully generated summary.")
except Exception as e:
    print(f"Error at Checkpoint 3: {e}")

# Print the summary
try:
    summary = chat_response.choices[0].message.content
    print("Checkpoint 4: Summary generated successfully.")
    print(summary)
except Exception as e:
    print(f"Error at Checkpoint 4: {e}")

# Optionally, save the summary to the output file
try:
    with open(output_txt_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(summary)
    print("Checkpoint 5: Summary written to output file successfully.")
except Exception as e:
    print(f"Error at Checkpoint 5: {e}")
