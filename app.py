import easyocr
import gradio as gr
import re

# Initialize the EasyOCR reader for Hindi and English languages
reader = easyocr.Reader(['en', 'hi'])

# EasyOCR function
def ocr_and_search(image, search_queries=""):
    result = reader.readtext(image)
    extracted_text = "\n".join([text for (_, text, _) in result])
    
    # If search queries are provided, search within the extracted text
    highlighted_text = extracted_text
    if search_queries:
        keywords = [kw.strip() for kw in search_queries.split(",")]
        for keyword in keywords:
            highlighted_text = re.sub(
                re.escape(keyword),
                f"<span style='background-color: #f1c40f; color: #000; font-weight: bold;'>{keyword}</span>",
                highlighted_text,
                flags=re.IGNORECASE
            )
    return extracted_text, highlighted_text

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center; color: #1abc9c; font-family: Verdana, Geneva, sans-serif;'>OCR Application with EasyOCR</h1>")
    gr.Markdown("<p style='text-align: center; font-size: 18px; color: #34495e; font-family: Georgia, serif;'>Upload an image with Hindi and English text, and search for specific keywords.</p>")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="filepath", label="Upload Image", elem_id="image-input")  # Image upload box
            search_input = gr.Textbox(label="Search Keywords", placeholder="Enter keywords (comma-separated)...", lines=1, elem_id="search-input")
            submit_button = gr.Button("Process Image", elem_id="submit-button", variant="#3D3737FF")
        
        with gr.Column():
            extracted_output = gr.Textbox(label="Extracted Text", interactive=False, lines=10, elem_id="extracted-text")
            highlighted_output = gr.HTML(label="Highlighted Search Results", elem_id="highlighted-results")

    submit_button.click(
        ocr_and_search,
        inputs=[image_input, search_input],
        outputs=[extracted_output, highlighted_output]
    )

# CSS styling
demo.css = """
body {
    background-color: #e0e0e0;
}

#image-input {
    background-color: #f0f0f0;
    border: 2px dashed #1abc9c;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

#search-input {
    background-color: #f0f0f0;
    border: 2px solid #1abc9c;
    border-radius: 12px;
    padding: 12px;
    font-family: 'Verdana', sans-serif;
}

#submit-button {
    background-color: #000;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px;
    font-weight: bold;
    font-family: 'Arial', sans-serif;
    width: 100%;
    transition: background-color 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

#submit-button:hover {
    background-color: #333;
}

#extracted-text {
    background-color: #f7f9f9;
    border: 1px solid #d1d1d1;
    border-radius: 8px;
    padding: 15px;
    font-family: 'Verdana', sans-serif;
    color: #2c3e50;
    max-height: 300px;  /* Height limit for scrolling */
    overflow-y: auto;   /* Enable vertical scrolling */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#highlighted-results {
    background-color: #f7f9f9;
    border: 1px solid #d1d1d1;
    border-radius: 8px;
    padding: 15px;
    font-family: 'Verdana', sans-serif;
    color: #2c3e50;
    max-height: 300px;  /* Height limit for scrolling */
    overflow-y: auto;   /* Enable vertical scrolling */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    font-family: 'Verdana', sans-serif;
    font-size: 32px;
}

p {
    font-family: 'Georgia', serif;
    font-size: 18px;
    color: #2c3e50;
}

h3 {
    font-family: 'Verdana', sans-serif;
    color: #1abc9c;
}
"""
demo.launch()