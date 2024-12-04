from openai import OpenAI

with open("graphql.txt") as file:
    file_content = file.read()

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
history = [
    {"role": "system", "content": f"""
     You are an helpful assistant. Answer the user's query strictly based on the following content:

     {file_content}

     If the answer cannot be found in the content, respond with "I don't know based on the provided information."
     """},
]


while True:
    history.append({"role": "user", "content": input("> ")})

    completion = client.chat.completions.create(
        model="lmstudio-ai/gemma-2b-it-GGUF",
        messages=history,
        temperature=0.7,
        stream=True,
    )
    
    new_message = {"role": "assistant", "content": ""}
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")
    print()

    