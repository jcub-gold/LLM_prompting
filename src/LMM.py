import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

class LLM:
    def __init__(self, **kwargs):
        allowed_attributes = {'model': None}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])
    
    def set_prompt(self, **kwargs):
        allowed_attributes = {'prompt': None}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])

    def set_input_file(self, **kwargs):
        allowed_attributes = {'input_file': None}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])

    def generate_response(self, **kwargs):
        pass

    def prompt_pairs_batch_from_file(self, **kwargs):
        line_num = 0
        self.set_input_file(**kwargs)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, 'Dataset', self.input_file)
        with open(file_path, 'r') as input:
            print('reading file...')
            for line in input:
                line_num = line_num + 1
                i_prompt = line.strip()
                response = self.generate_response(prompt = i_prompt)
                flag = 'a'
                if (line_num == 1):
                    flag = 'w'
                output_file = self.input_file + '_' + self.get_model() + '_output.txt'
                file_path = os.path.join(current_dir, 'Output', output_file)
                with open(file_path, flag) as output:
                    if (line_num % 2 == 1):
                        output.write("Prompt #" + str((line_num + 1) // 2) + ": ")
                    else:
                        output.write("Folow-up prompt #" + str(line_num // 2) + ": ")
                    output.write(i_prompt + "\n\nResponse: " + response + "\n\n")
                    if (line_num % 2 == 0):
                        output.write("\n")
            print('done')
    

class Gemini(LLM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_key = os.getenv("GOOGLE_API_KEY")

    def generate_response(self, **kwargs):
        super().set_prompt(**kwargs)
        model = genai.GenerativeModel(self.model)
        genai.configure(api_key=self.api_key)
        response = model.generate_content(self.prompt)
        return response.text

    def get_model(self):
        return self.model
    
    def set_input_file(self, **kwargs):
        return super().set_input_file(**kwargs)
    
    def prompt_pairs_batch_from_file(self, **kwargs):
        return super().prompt_pairs_batch_from_file(**kwargs)

class GPT(LLM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key = self.api_key)

    def generate_response(self, **kwargs):
        super().set_prompt(**kwargs)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": self.prompt}])
        return response.choices[0].message.content
    
    def get_model(self):
        return self.model
    
    def set_input_file(self, **kwargs):
        return super().set_input_file(**kwargs)

    def prompt_pairs_batch_from_file(self, **kwargs):
        return super().prompt_pairs_batch_from_file(**kwargs)

