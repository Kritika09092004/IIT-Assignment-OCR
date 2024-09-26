# OCR Web Application

This is an OCR (Optical Character Recognition) web application built using EasyOCR and Gradio. It allows users to upload images containing Hindi and English text, extracts the text, and highlights any searched keywords.

## Features

- Upload images with Hindi and English text.
- Extract text from images using EasyOCR.
- Search for keywords in the extracted text and highlight them.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or later
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Install Required Packages**:

It is recommended to create a virtual environment for your project. You can do this using venv:

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Then install the required packages:

pip install -r requirements.txt

3. **Running the Web Application Locally**
To run the application locally, use the following command:

python app.py
After running the command, you can access the web application in your browser at http://127.0.0.1:7860.

4. **Deployment Process**
You can deploy this application on platforms like Hugging Face Spaces or Streamlit Sharing. Below are the general steps for deploying on Hugging Face Spaces:

Create a New Space:Go to Hugging Face Spaces and create a new Space.
Upload Your Files:Upload all necessary files including:
                  app.py (the main application file)
                  requirements.txt (dependencies)
Configure the Space:Ensure your Space is set to use a Gradio or Streamlit template based on your application framework.
Deploy:Once everything is uploaded and configured, your application should deploy automatically. You will be provided with a public URL to access your application.

5. **Acknowledgements**
EasyOCR for the OCR functionality.
Gradio for creating the web interface.