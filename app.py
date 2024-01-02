import gradio as gr

class ChatApp:
    def __init__(self):
        self.init_ui()

    def add_text(self, history, text):
        response = f"You said: '{text}'. Interesting!"
        history.append((text, response))
        return history

    def add_audio(self, history, audio):
        history.append(("User", "[Audio message]"))
        response = "Audio received, but I can't interpret it yet."
        history.append(("Bot", response))
        return history

    def add_file(self, history, file):
        history.append(("User", "[File uploaded]"))
        response = "File received. I'll learn to analyze this soon."
        history.append(("Bot", response))
        return history

    def init_ui(self):
        with gr.Blocks() as self.demo:
            gr.Markdown("# Welcome to Chat App")

            self.chatbot = gr.Chatbot(
                [], height=600, label="Chat App",
                avatar_images=(None, "assets/images/avatar_bot.png")
            )

            with gr.Column():
                with gr.Group():
                    txt = gr.Textbox(label="Type your message", placeholder="Enter text here")
                    txt.submit(self.add_text, inputs=[self.chatbot, txt], outputs=self.chatbot)

                    aud = gr.Audio(label="Record your voice", type='filepath')
                    aud.change(self.add_audio, inputs=[self.chatbot, aud], outputs=self.chatbot)

                    btn_upload = gr.UploadButton("Upload a file", file_types=["file"])
                    btn_upload.upload(self.add_file, inputs=[self.chatbot, btn_upload], outputs=self.chatbot)

                    btn_clear = gr.ClearButton()
                    btn_clear.click(inputs=[], outputs=[txt, self.chatbot, aud])

                with gr.Group():
                    gr.Markdown("### Additional Features:")
                    btn_instruct = gr.Button("Instructions")
                    btn_t2t = gr.Button("Random description")

                dropdown_method = gr.Dropdown(["slow", "fast"], label="Visualization Method", value="fast")
                dropdown_language = gr.Dropdown(["English", "日本語"], label="Speech Language", value="English")

    def launch(self):
        self.demo.launch()

if __name__ == "__main__":
    app = ChatApp()
    app.launch()
