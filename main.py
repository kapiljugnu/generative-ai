from openai import OpenAI
from generator import response_generator
from validator import validate_response

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
history = [
    {"role": "system", "content": """
     You are an intellegent assistant.
     If user say y generate a number between 1 to 100
     """},
    {"role": "user", "content": "Give me a number"},
]

while True:
    response = response_generator(client, history)
    response = validate_response(client, response)

    new_message = {"role": "assistant", "content": response}
    
    history.append(new_message)
    # Uncomment to see chat history
    import json
    gray_color = "\033[90m"
    reset_color = "\033[0m"
    print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    print(json.dumps(history, indent=2))
    print(f"\n{'-'*55}\n{reset_color}")
    print()
    history.append({"role": "user", "content": input("> ")})



    # build 2 chat bot one to respond json other to validate
    # read file and respond