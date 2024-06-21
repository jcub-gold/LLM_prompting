from LMM import GPT
from LMM import Gemini

def main():
    LLM = input('Would you like to use ChatGPT(1) or Gemini(2)?\n')
    i_model = input('What model would you like to use?\n')
    if (LLM == '1'):
        LLM = GPT(model = i_model)
    else:
        LLM = Gemini(model = i_model)
    i_input_file = input('Please enter the name of your input file (including the .txt):\n')
    LLM.prompt_pairs_batch_from_file(input_file = i_input_file)

if __name__ == "__main__":
    main()