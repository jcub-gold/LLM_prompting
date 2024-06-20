from LMM import GPT
from LMM import Gemini

"""
FUCNTION: prompt_pairs_batch_from_file
---------
PARAMETERS: 
    input_file - the name of a txt file formated with one prompt per line
    output_file - the name of txt file; content of this file will be overwritten
                    with the prompts and AI responses
    model_instance - an initialized instance of one of the models from the LMM  file
-----------
DESCRIPTION:
This function read prompts from a file and uses the specified model instance
to generate a response from the AI model. The prompts are expected to be in pairs,
meaning every two prompts relate to each other. This function has no return value
but will update the contents of the output file with the contents of the prompts
responses.    
"""
def prompt_pairs_batch_from_file(input_file, output_file, model_instance):
    line_num = 0

    with open(input_file, 'r') as input:
        print('reading file...')
        for line in input:
            line_num = line_num + 1
            prompt = line.strip()
            response = model_instance.generate_response(prompt)
            flag = 'a'
            if (line_num == 1):
                flag = 'w'
            with open(output_file, flag) as output:
                if (line_num % 2 == 1):
                    output.write("Prompt #" + str((line_num + 1) // 2) + ": ")
                else:
                    output.write("Folow-up prompt #" + str(line_num // 2) + ": ")
                output.write(prompt + "\n\nResponse: " + response + "\n\n")
                if (line_num % 2 == 0):
                    output.write("\n")
        print('done')

def main():
    LLM = input('Would you like to use ChatGPT(1) or Gemini(2)?\n')
    model = input('What model would you like to use?\n')
    if (LLM == '1'):
        LLM = GPT(model)
    else:
        LLM = Gemini(model)
    input_file = input('Please enter the name of your input file (including the .txt):\n')
    output_file = input('Please eneter the name of your ouput file (including the .txt):\n')
    prompt_pairs_batch_from_file(input_file, output_file, LLM)

if __name__ == "__main__":
    main()