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

# Dataset preparation
Prepare one text file, each line should contain a prompt. You can find examples under the `dataset/` folder. Note there should be no seperation between prompt pairs. Here's a quick preview: 

This is prompt 1
This is prompt 2


## Expected directory structure
FILL OUT

# Run the experiment
Run the experiment script, and it'll save all the formatted responses in `{MODEL}_output.txt`.
```bash
python run.py --developer=GOOGLE --model=gemini-pro --input_file=prompt_pairs.txt
```
