import pandas as pd
import openai
from openai.embeddings_utils import cosine_similarity
import plotly.express as px

import bertEmbedding
# from sklearn.metrics.pairwise import cosine_similarity

import blue
import numpy as np


openai.api_base = 'HTTP'
openai.api_key = 'KEY'

def get_embeddings(text):
    embedding = openai.Embedding.create(model="text-embedding-3-large",input=[text])['data'][0]['embedding']
    return embedding

def calculate_consine(em1, em2):
    cosine = cosine_similarity(em1, em2)
    return cosine

def load_file(filePath):
    with open(filePath, 'r') as file:
        file_content = file.read().split("\t")[1]
    return file_content


if __name__ == "__main__":

    for index in range(0,1921):
        groundTruth = load_file("path2groundtruth/"+str(index)+".txt")
        compareTool = load_file("path2generatedReview"+str(index)+".txt")
    
        gtEmbedding = get_embeddings(groundTruth)
        ctEmbedding = get_embeddings(compareTool)
    
        similarity = calculate_consine(gtEmbedding,ctEmbedding)
        with open('./gpt-issre-first.txt', 'a') as f:
            f.write(str(similarity) + "\n")


