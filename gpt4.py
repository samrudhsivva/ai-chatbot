import openai
import yaml

# Load OpenAI API key from config.yaml
with open("config.yaml") as f:
    config_yaml = yaml.load(f, Loader=yaml.FullLoader)
openai.api_key = config_yaml['token']

# Define a function to get user input at runtime
def get_user_input():
    return input("Please enter your message: ")

# Generate conversation messages including user input
def generate_messages(user_input):
    return [
        {"role": "system", "content": "You are a 4th grade teacher."},
        {"role": "user", "content": user_input},
    ]

# Get user input
user_input = get_user_input()

# Generate messages for the conversation
messages = generate_messages(user_input)

# Generate a chat completion using the OpenAI API
ans = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # You can replace this with any available model
    max_tokens=2048,
    messages=messages,
)

# Print the completion response
print('--------------------------------------------------')
print(ans["choices"][0]["message"]["content"])
