import spacy
from sentence_tranformers import SentenceTransformer

nlp = spacy.load("en_core_web_sm") 

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')