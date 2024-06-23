# Dual Prompting: Single Modality Prompting Pairs


Prepare a text file containg prompts, configure your API keys, and just run it!

Please note that this code repo is intended for research purpose, and might not be suitable for large-scale production.


# Installation
Install packages using pip:
```bash
$ pip install -r requirements.txt
```

# Setup API keys
## For GPT-series models offered by OpenAI
Get your OpenAI API key from [here](https://platform.openai.com/api-keys);

## For Gemini-series models offered by Google AI Studio
Get you Gemini API key from [here](https://aistudio.google.com/app/apikey);

## Creating .env File
1. Copy the contents of the env.template into a .env file
2. Delete the environment template
3. Replace "your_api_key_here" with personal acquired keys


# Dataset preparation
Prepare one text file, each line should contain a prompt. You can find examples under the `dataset/` folder. Note there should be no seperation between prompt pairs. Here's a quick preview (your can check out prompt_pairs.txt for a more thorough example): 

This is the prompt number 1

This is the follow up prompt number 2


## Expected directory structure
```
src/
├── Dataset
│   └── prompt_pairs.txt
├── Output
│   └── prompt_pairs.txt_gemini-pro_output.txt
├── LMM.py
├── env.template
└── run.py

```

# Run the experiment
Run the experiment script, and it'll save all the formatted responses in `{input_file}_{MODEL}_output.txt`. Note: model options for OpenAI can be found [here](https://platform.openai.com/docs/models); and for Google [here](https://ai.google.dev/gemini-api/docs/models/gemini);
```bash
python run.py --developer=GOOGLE --model=gemini-pro --input_file=prompt_pairs.txt
```
