from rouge_score import rouge_scorer


def calculate_rouge(reference, candidate):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True) #, 'rouge2', 'rougeL'
    scores = scorer.score(reference, candidate)
    result = scores['rougeL'].fmeasure
    return result

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
        compareTool = read_file_as_string("path2Candidate"+str(index)+".txt")
        score = calculate_rouge(groundTruth,compareTool)

        print(str(score))

        with open('./rougeL-issre.txt', 'a') as f:
            f.write(str(score) + "\n")



