from LMM import GPT
from LMM import Gemini
import argparse

def main():
    parser = argparse.ArgumentParser(description = 'Experiment script.')
    
    parser.add_argument(
        "--developer",
        type=str,
        required=True,
        help="Which compamies AI to use.",
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Which AI model to use.",
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Name of input_file",
    )

    args = parser.parse_args()
    
    DEV = args.developer
    i_model = args.model
    i_input_file = args.input_file

    if (DEV == 'GOOGLE'):
        LLM = Gemini(model = i_model)
    else:
        LLM = GPT(model = i_model)
    LLM.prompt_pairs_batch_from_file(input_file = i_input_file)

if __name__ == "__main__":
    main()