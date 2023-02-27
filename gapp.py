import gradio as gr

def gapp_fun(text):
    return len(text.split())


ui = gr.Interface(
    fn = gapp_fun,
    inputs = [
        gr.inputs.Textbox(placeholder='Symboling'),
    ],
    outputs = "text",
)

if __name__ == "__main__":
    ui.launch()