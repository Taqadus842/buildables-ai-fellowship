from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found! Check your PyCharm environment variables.")
else:
    print("✅ OPENAI_API_KEY loaded successfully.")

client= OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
def chat_cli():
    print("Welcome to CLI Chatbot")

    messages=[{"role":"system","content":"you are helpful assistant"}]

    while True:
        try:
            user_input=input("You: ")
            if user_input.lower()=="exit":
                print("Chat ended")
                break
            messages.append({"role":"user","content":user_input})

            response=client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            reply=response.choices[0].message.content
            print("Bot: ",reply, "\n")

            messages.append({"role":"assistant","content":reply})
        except Exception as e:
            print("Error: ",e)

if __name__=="__main__":
    chat_cli()