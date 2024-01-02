import gradio as gr

def echo(message, history):
    return message

demo = gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo Bot", chatbot=gr.Chatbot(
                [], height=800, label="Chat App",
                avatar_images=(None, "assets/images/avatar_bot.png")
            ))
demo.launch()
