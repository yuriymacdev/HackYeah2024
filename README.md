# Tax Bot

Currently using a statemachine with possible data validation instead of an llvm.

## installation 
```
#installing ollama (if switched to LLM instead)
curl -fsSL https://ollama.com/install.sh | sh
ollama serve 
ollama pull SpeakLeash/bielik-11b-v2.3-instruct:Q5_K_M
```


## Running
```sh
FLASK_DEBUG=1 flask run
# redirect to external ip
ngrok http 5000
```
