import gradio as gr

class IssueClassifier:
    def __init__(self, models):
        self.models = models
        self.model_dropdown = gr.components.Dropdown(choices=list(self.models.keys()), label="Model")
        self.input_choice = gr.components.Radio(choices=["Title and Body", "Link"], value='Title and Body', label="Input Type")

        # Define the textboxes
        self.title_textbox = gr.components.Textbox(label="Title", lines=2, visible=True)
        self.body_textbox = gr.components.Textbox(label="Body", lines=5, visible=True)
        self.link_textbox = gr.components.Textbox(label="Link", visible=False)
        # Combine the inputs and textboxes
        self.inputs = [self.model_dropdown, self.input_choice, self.title_textbox, self.body_textbox, self.link_textbox]

        # Set the outputs
        self.outputs = gr.components.Label(num_top_classes=1)
        
        # Set the title of the interface
        self.title = "Issue Report Classification Demo"
        
        # Set the theme
        self.theme = None

    # Define the function to change the visibility of textboxes
    def change_textboxes(self, choice):
        if choice == "Title and Body":
            return gr.Textbox.update(visible=True), gr.Textbox.update(visible=True), gr.Textbox.update(visible=False)
        elif choice == "Link":
            return gr.Textbox.update(visible=False), gr.Textbox.update(visible=False), gr.Textbox.update(visible=True)
        else:
            return gr.Textbox.update(visible=False), gr.Textbox.update(visible=False), gr.Textbox.update(visible=False)
    
    
    def text_classification(self, model_name: str, input_choice: str, title: str, body: str, link_textbox: str) -> str:
        """
        This function takes inputs and returns the predicted class using a pre-trained model.

        Args:
        model_name (str): Name of the pre-trained model.
        input_choice (str): Choice of input type. Can be "Title and Body" or "Link" to the GitHub issue.
        title (str): Title of the issue.
        body (str): Body of the issue.
        link_textbox (str): Link to the GitHub issue.

        Returns:
        str: Predicted class of the issue.
        """

        if input_choice == "Title and Body":
            text = preprocess(title, body)
        else:
            extracted = extract_github_issue(link_textbox)
            text = preprocess(extracted['title'], extracted['body'])

        model = self.models[model_name]
        predicted_class = model.predict(text)

        return predicted_class
    
    def run(self):
        
        with gr.Interface(fn=self.text_classification, inputs=self.inputs, outputs=self.outputs, title=self.title, theme=self.theme) as iface:
    
            # Set up the radio button to control the visibility of the textboxes
            self.input_choice.change(self.change_textboxes, self.input_choice, [self.title_textbox, self.body_textbox, self.link_textbox])

            # Launch the interface
            iface.launch(share=True)
        
    
