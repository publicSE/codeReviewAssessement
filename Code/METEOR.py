import nltk
from nltk.translate.meteor_score import meteor_score


def calculate_meteor_score(reference, hypothesis):
    reference_tokens = nltk.word_tokenize(reference.lower())
    hypothesis_tokens = nltk.word_tokenize(hypothesis.lower())

    score = meteor_score([reference_tokens], hypothesis_tokens)
    return score

def read_file_as_string(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            content = file.read()
        return content.split("	")[1]
    except FileNotFoundError:
        return ""

if __name__ == "__main__":

    for index in range(0,1291): # 1291
        groundTruth = read_file_as_string("path2GroundTruth"+str(index)+".txt")
        compareTool = read_file_as_string("path2Candiate"+str(index)+".txt")
        score = calculate_meteor_score(groundTruth,compareTool)

        print(str(score))

        with open('./menter-auger.txt', 'a') as f:
            f.write(str(score) + "\n")
