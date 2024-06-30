import re

def extract_pirads(text):
    
    match = re.search(r"PI[-\s]?RADS\D{0,10}(\d)", text)
    if match:
        return int(match.group(1))
    else:
        return None  

import spacy
from spacy.training import Example

nlp = spacy.blank("en")

if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

ner.add_label("PI-RADS")

train_data = [
    ("The patient has a PI-RADS 4 lesion.", {"entities": [(21, 29, "PI-RADS")]}),
    ("PI-RADS: 5 indicates high likelihood of malignancy.", {"entities": [(0, 8, "PI-RADS")]}),
]

optimizer = nlp.resume_training()
for itn in range(10):
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.5, sgd=optimizer)

nlp.to_disk("/path/to/model")

