import gradio as gr

def add_text(history, text):
    # Logic for processing text input
    response = f"You said: '{text}'. Interesting!"
    history.append(("User", text))
    history.append(("Bot", response))
    return history

def add_audio(history, audio):
    # Logic for processing audio input
    response = "Audio received, but I can't interpret it yet."
    history.append(("Bot", response))
    return history

def add_file(history, file):
    # Logic for processing file upload
    response = "File received. I'll learn to analyze this soon."
    history.append(("Bot", response))
    return history

with gr.Blocks() as demo:
    gr.Markdown("# Welcome to Chat App")

    chatbot = gr.Chatbot(
        [], height=600, label="Chat App",
        avatar_images=(None, "assets/images/avatar_bot.png")
    )

    with gr.Column():
        with gr.Group():
            txt = gr.Textbox(label="Type your message", placeholder="Enter text here")
            txt.submit(add_text, inputs=[chatbot, txt], outputs=chatbot)

            aud = gr.Audio(label="Record your voice", type='filepath')
            aud.change(add_audio, inputs=[chatbot, aud], outputs=chatbot)

            btn_upload = gr.UploadButton("Upload a file", file_types=["file"])
            btn_upload.upload(add_file, inputs=[chatbot, btn_upload], outputs=chatbot)

            btn_clear = gr.ClearButton()
            btn_clear.click(inputs=[], outputs=[txt, chatbot, aud])

        with gr.Group():
            gr.Markdown("### Additional Features:")
            btn_instruct = gr.Button("Instructions")
            btn_t2m = gr.Button("Text-to-Motion")
            btn_m2t = gr.Button("Motion-to-Text")
            btn_t2t = gr.Button("Random description")

        dropdown_method = gr.Dropdown(["slow", "fast"], label="Visualization Method", value="fast")
        dropdown_language = gr.Dropdown(["English", "中文"], label="Speech Language", value="English")

demo.launch()
