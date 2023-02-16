<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/GPT-Summarizer"><img src="https://github.com/mkdirlove/GPT-Summarizer/blob/main/logo.png" alt="GPT-Summarizer"></a>
  <br>
  An AI-based summarizing tool written in pure Python.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```
git clone https://github.com/mkdirlove/GPT-Summarizer.git
```
```
cd GPT-Summarizer
```
```
python3 GPT-Summarizer.py -h
```

#### Usage
```
╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╔╦╗╔╦╗╔═╗╦═╗╦╔═╗╔═╗
║ ╦╠═╝ ║───╚═╗║ ║║║║║║║╠═╣╠╦╝║╔═╝║╣ 
╚═╝╩   ╩   ╚═╝╚═╝╩ ╩╩ ╩╩ ╩╩╚═╩╚═╝╚═╝
     Made with <3 by @mkdirlove

usage: GPT-Summarizer.py [-h] [-t TEXT] [-f FILE] [-n NUM_SENTENCES]

GPT-Summarizer - An AI-based summarizing tool written in pure Python.

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  The text to summarize
  -f FILE, --file FILE  The path to a file containing the text to summarize
  -n NUM_SENTENCES, --num_sentences NUM_SENTENCES
                        The number of sentences to include in the summary
```

#### Sample Usage #1

Read text from input:
```
python3 GPT-Summarizer.py -t 'Put some text here...' -n 3
```
#### Sample Usage #2

Read text from text file:
```
python3 GPT-Summarizer.py -f text.txt -n 3
```
