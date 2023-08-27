# FoodieGPT🍙
---

## Motivation
A personal assistant that can help you remember your favorite food and restaurants for personalized recommendation.


## Installation & Usage (local)

With `Python 3.8.10`, please run
```bash
pip install -r requirements.txt
```

To run the module, please use
```bash
streamlit run src/main.py 
```
## Installation & Usage (Docker)

To build the image, 
```bash
docker image build . --tag brave_hackathon:latest   
```

To run it on port 8501, please do
```bash
docker container run -p 8501:8501 brave_hackathon 
```

# Reference

- [longChain Agents Doc](https://python.langchain.com/docs/modules/agents/)
  - agent is a wrapper around model
- [CSV Agent langchain tutorial](https://python.langchain.com/docs/integrations/toolkits/csv)


