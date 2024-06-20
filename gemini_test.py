import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

line_num = 0
file_output = "gemini_response.txt"

with open('prompt_pairs.txt', 'r') as file1:
    for line in file1:
        line_num = line_num + 1
        prompt = line.strip()
        response = model.generate_content(prompt)
        print(response.text)
        flag = 'a'
        if (line_num == 1):
            flag = 'w'
        with open(file_output, flag) as file2:
            if (line_num % 2 == 1):
                file2.write("Prompt #" + str((line_num + 1) // 2) + ": ")
            else:
                file2.write("Folow-up prompt #" + str(line_num // 2) + ": ")
            file2.write(prompt + "\n\nResponse: " + response.text + "\n\n")
            if (line_num % 2 == 0):
                file2.write("\n")