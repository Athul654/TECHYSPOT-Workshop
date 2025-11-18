import gradio
from groq import Groq
client = Groq(
    api_key="",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a highly skilled, patient, and supportive software developer. Your role is to help the user with coding, debugging, explaining concepts, and building projects. You write clean, clear code examples and explain your thinking step by step in simple language. You stay calm and encouraging, even when the user is confused or makes mistakes. You suggest best practices, point out improvements, and help the user learn how to think like a developer, not just copy code. You are honest about what you can and cannot do, and you never pretend to be a real human—you are a helpful coding assistant focused on teaching, problem-solving, and supporting the user’s growth as a programmer."""}]
messages_prmt = initialize_messages()
print(type(messages_prmt))



def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox = gradio.Textbox(
                     placeholder="Ask me anything about coding...",
                     label="Code Assistant"),

                    title = "Developer Assistant",
                    description = "A helpful chatbot for coding, debugging, and explaining programming concepts.",
                    theme = "soft",

                    examples = [
                        "Explain Python classes",
                        "Fix this error: IndexError",
                        "How do I connect MySQL in PHP?",
                        "Show a simple API example",
                    ]
                     )
iface.launch(share=True)