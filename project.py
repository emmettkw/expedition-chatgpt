import openai

openai.api_key = "PRIVATE"

# Tells ChatGPT what it's doing
messages = [
    {
        "role": "system",
        "content": """
    
            You're helping someone plan an expedition. I'll tell you where I'm going and why, and you'll suggest 
            the types of vehicles I'll take and what equipment to pack.
    
            """
    }
]

# Asks the user where they would like to go
user_input = input("Tell me where you would like to go: ")

destination = {
    "role": "user",
    "content": user_input
}
# Tells ChatGPT where you are going
messages.append(destination)

user_input = input("Why are you going? ")

# Asks the user why they are going
reason = {
    "role": "user",
    "content": user_input
}

# Tells ChatGPT why you are going
messages.append(reason)

# Sends the messages to ChatGPT
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = messages
)

# prints response
print()
print(completion["choices"][0]["message"]["content"])


# Starts the loop by asking if there is any more information the user wants
print()
user_input = input("Is there anything else you would like to know? ")

while user_input != "no":

    # Tells GPT the last response
    response = {
        "role": "assistant",
        "content": completion["choices"][0]["message"]["content"]
    }
    messages.append(response)

    # Tells GPT the next question
    next_question = {
        "role": "user",
        "content": user_input
    }
    messages.append(next_question)

    # Sends the messages to ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )

    # prints response
    print()
    print(completion["choices"][0]["message"]["content"])
    print()
    user_input = input("Is there anything else you would like to know? ")

# Monitors token use
print("Total tokens used:", completion["usage"]["total_tokens"])
# print(completion)
