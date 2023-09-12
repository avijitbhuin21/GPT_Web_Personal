import openai
import os
import shutil

openai.api_key="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"

def make_convo_location():
    path="GPT_Updated_Personal/New_Conversations"
    if not os.path.exists(path):
        os.makedirs(path)
    path='GPT_Updated_Personal/New_Conversations/Conversation_1.txt'
    i=2
    while True:
        if os.path.exists(path):
            path= f"GPT_Updated_Personal/New_Conversations/Conversation_{i}.txt"
            i+=1
        else:
            break
    return path

def write_file(path,x):
    with open(path,"a") as file:
        file.write(x+"\n")

def stream_store_response(user_prompt):
    Final_messages = []
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k',messages=[{"role": "system", "content": "you're a helpful assistant."},{'role': 'user', 'content': user_prompt}],max_tokens=14000,temperature=0,stream=True)
    print("")
    print("GPT-3.5:")
    for chunk in response:
        if 'choices' in chunk and chunk['choices'][0].get('delta') and 'content' in chunk['choices'][0]['delta']:
            chunk_message = chunk['choices'][0]['delta']['content']
            Final_messages.append(chunk_message)
            print(chunk_message,end="")
    return ''.join(Final_messages)

def remove_cache():
    shutil.rmtree('GPT_Updated_Personal/__pycache__')