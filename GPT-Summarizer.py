import os
import json
import argparse
import requests

# Fancy banner
banner = """
╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╔╦╗╔╦╗╔═╗╦═╗╦╔═╗╔═╗
║ ╦╠═╝ ║───╚═╗║ ║║║║║║║╠═╣╠╦╝║╔═╝║╣ 
╚═╝╩   ╩   ╚═╝╚═╝╩ ╩╩ ╩╩ ╩╩╚═╩╚═╝╚═╝
     Made with <3 by @mkdirlove
"""

# Print banner
os.system("clear")
print(banner)

# Define and parse command-line arguments
parser = argparse.ArgumentParser(description='GPT-Summarizer - An AI-based summarizing tool written in pure Python.')
parser.add_argument('-t', '--text', type=str, help='The text to summarize')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='The path to a file containing the text to summarize')
parser.add_argument('-n', '--num_sentences', type=int, default=5, help='The number of sentences to include in the summary')
args = parser.parse_args()

# Check if text or file argument is empty
if not args.text and not args.file:
    parser.print_help()
    exit()

# Extract text from file or command-line argument
if args.text:
    text = args.text
else:
    with args.file as file:
        text = file.read()

# Set up API request
url = "https://gpt-summarization.p.rapidapi.com/summarize"
payload = {
    "text": text,
    "num_sentences": args.num_sentences
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "18140c0733msh4177590f10ca716p1ba0c8jsnd344b761be19",
    "X-RapidAPI-Host": "gpt-summarization.p.rapidapi.com"
}

# Send API request and print summary
response = requests.request("POST", url, json=payload, headers=headers)
summary = json.loads(response.text)['summary']
print(summary)
