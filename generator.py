

def response_generator(client, history):
    completion = client.chat.completions.create(
        model="lmstudio-ai/gemma-2b-it-GGUF",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            response += chunk.choices[0].delta.content


    return response;