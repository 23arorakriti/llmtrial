
import json
from mistralai import Mistral

def perform_validation(sec_key, model, json_file_path, validation_text_file_path, txt_file_path):
    def load_json_file(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def load_validation_text(file_path):
        with open(file_path, 'r', encoding='Windows-1252') as file:
            return file.read()

    def validation_summary(sec_key, model, json_content, validation_text):
        client = Mistral(api_key=sec_key)
        jsonfile = json.dumps(json_content)

        messages = [
            {
                "role": "user",
                "content": f"This is the misconception summary: {jsonfile}. Please provide an accurate validation summary in less than 30 words for each misconception in the given json using the following text: {validation_text}. make the validation that it starts by saying its a true or partially true or false and then make sure to give the validation.print misconception as it is first.generate only one validation for each misconception."
            }
        ]
        chat_response = client.chat.complete(
            model=model,
            messages=messages,
        )
        
        return chat_response.choices[0].message.content

    def save_summary_to_txt(summary, file_path):
        with open(file_path, mode='w', encoding='utf-8') as file:
            file.write(summary)

    def read_summary_from_txt(file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            return file.read()

    json_content = load_json_file(json_file_path)
    validation_text = load_validation_text(validation_text_file_path)
    summary = validation_summary(sec_key, model, json_content, validation_text)
    save_summary_to_txt(summary, txt_file_path)

    return read_summary_from_txt(txt_file_path)
