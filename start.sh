#! /bin/bash

source venv/bin/activate
pip install -r requirements.txt
#ollama create jarvis -f ./Modelfile
#ollama run jarvis
python main.py