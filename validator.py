def validate_response(client, output):
    validation_prompt = f"""
    You are a response validator. Evaluate the following chatbot reponse and check if it is a number or not:
    Chatbot Response: {output}
    Provide feedback in this format:
    - Number: Yes/No
    """
    completion = client.chat.completions.create(
        model="lmstudio-ai/gemma-2b-it-GGUF",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for validating response."},
            {"role": "user", "content": validation_prompt}
        ],
        temperature=0.7,
        stream=True,
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            response += chunk.choices[0].delta.content

    return response