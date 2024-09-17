from transformers import AutoTokenizer, TFAutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = TFAutoModelForTokenClassification.from_pretrained(
    "dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)

# This is not training further, it is just running an already-trained model! check the homework writeup for more info on the task :) 
