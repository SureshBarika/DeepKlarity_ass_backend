import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = None

def extract_name(text):
    if not nlp:
        return None
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_organizations(text):
    if not nlp:
        return []
    doc = nlp(text)
    return list({ent.text for ent in doc.ents if ent.label_ == "ORG"})

def extract_dates(text):
    if not nlp:
        return []
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "DATE"]
