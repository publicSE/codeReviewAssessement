import openai
from tqdm import tqdm


api_client = openai.Client(
    base_url = 'https://api.deepseek.com',
    api_key = 'sk-6a3387100db54e6c99209d934a0a5130'
)

common_info = '''
System: You are a smart code reviewer. You will be asked to grade a generated code review. 

You can mimic answering them in the background 15 times and provide me with the most frequently appearing answer. 

Furthermore, please strictly adhere to the output format specified in the question. There is no need to explain your answer.

Scenario Matching: I am going to give you a generated code review as well as its reference review. You should grade 

the generated review by comparing it to the reference review, and output a grade based on the following criteria:

1. If the generated review is identical to the reference review, Grade=5;
2. If the generated review is essential/semantic equivalent to the reference review although their expressions are not identical, Grade=4;
3. If the generated review explicitly and correctly specifies some comments/suggests presented in the reference review,  Grade=3;
4. If the generated review  is only loosely related with the reference review, but there are significant incorrect expressions, Grade=2;
5. If the generated review is completely unrelated to the reference review in semantic, Grade=1.
Please NOTE that you should only output a grade without any explanation.

'''

ex_user1 = common_info + "Reference Code Review: "


def read_file_as_string(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            content = file.read()
        return content.split("	")[1]
    except FileNotFoundError:
        return ""


def invokeGPT(comment1, comment2):
    messages = [
        {"role": "system", "name": "example_user", "content": ex_user1 + "\""+comment1 +"\""+ "Generated Code Review: \"" + comment2+"\"."},
        ]
    
    response = api_client.chat.completions.create(
                        model='deepseek-chat',
                        messages=messages,
                        temperature=0,
                        top_p=0.001,
                    )
    msg = response.choices[0].message.content
    # respond = response['choices'][0]['message']['content']

    if "=" in msg:
        return msg.split("=")[1].strip()
    else:
        return msg



if __name__ == "__main__":

    method_names = ['auger', 'issre', 'icse', 'cfinder']

    for method_name in method_names:
        
        for index in tqdm(range(0,1291), desc=method_name):
            groundTruth = read_file_as_string("./files/gt"+str(index)+".txt")
            compareTool = read_file_as_string(f"./files/{method_name}{index}.txt")
            score = invokeGPT(groundTruth,compareTool)

            # print(str(score))

            with open(f'./deepseek-{method_name}-score-1291-R6.txt', 'a') as f:
                f.write(str(score) + "\n")
