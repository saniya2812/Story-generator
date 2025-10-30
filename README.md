

# 📖 Gemini Story Generator (Tkinter Desktop App)

This is a simple, standalone desktop application built with **Python's Tkinter** library that leverages the **Google Gemini API** to generate creative stories based on a user-provided prompt. It demonstrates how to make HTTP requests to the Gemini API and integrate the response into a basic GUI.
The primary goal is to create a frictionless experience where the path from idea to generated story is as short and intuitive as possible. The design emphasizes clear input fields and a clean, readable output display.

A flexible text area that allows the user to define specific plot points, character names, or thematic elements. This is the primary driver of the story's content.

Offers options (e.g., short paragraph, 500 words, 1000 words) to specify the desired story length, ensuring the output meets the user's requirement for detail and scope.

A simple, one-click button to copy the final generated story text to the clipboard for easy sharing or integration into external writing tools.

Leverages the Gemini API (gemini-2.5-flash-preview-09-2025 model) for sophisticated text generation and creative reasoning.


## 🚀 Features

* **GUI Interface:** Easy-to-use graphical interface built with Python's built-in `tkinter`.
* **Gemini Integration:** Connects to the `gemini-2.5-flash-preview-09-2025` model via a direct HTTP POST request.
* **Prompt-Based Storytelling:** Generates a creative story based on the text entered by the user.
* **Error Handling:** Includes checks for missing API keys and handles common API and connection errors.

## 🛠️ Prerequisites

Before you begin, ensure you have the following:

1.  **Python 3.x:** Installed on your system.
2.  **Gemini API Key:** Obtain a key from Google AI Studio.
3.  **Required Python Libraries:** You will need the `requests` library for making HTTP calls.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/gemini-story-generator.git](https://github.com/YOUR_USERNAME/gemini-story-generator.git)
    cd gemini-story-generator
    ```

2.  **Install dependencies:**
    The application primarily uses built-in Python libraries (`tkinter`, `os`, `json`, `sys`) but requires the `requests` library.
    ```bash
    pip install requests
    ```

## 🔑 Configuration

You need to configure your **Gemini API Key** for the application to work. You have two options:

### Option 1: Using Environment Variable (Recommended)

Set the `GEMINI_API_KEY` environment variable in your system. The script will automatically detect it.

**For Linux/macOS:**
```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```
For Windows (Command Prompt):

```Bash

set GEMINI_API_KEY="YOUR_API_KEY_HERE"
```
## Option 2: Editing the Script
You can directly replace the placeholder in the Python script (story_generator.py) file:

```bash
# --- GEMINI API CONFIGURATION ---
# Replace 'YOUR_GEMINI_API_KEY_HERE' with your actual key.
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE") 
# ...
```
## How to Run
Execute the Python script from your terminal:

```Bash

python storygenerator.py
```
The Gemini Story Generator window will open.

Enter a prompt (e.g., "A lonely robot who finds an ancient, glowing flower on Mars.") into the entry field.

Click the "Generate Story" button.

The application will connect to the Gemini API, and the generated story will appear in the large text area.
   
  GEMINI_API_KEY="your-gemini-api-key"

## Model and Configuration Details

Model Name  - 	gemini-2.5-flash-preview-09-2025  - 	A fast and versatile model for creative and generative tasks.

Max Output Tokens	  -  1000	 -  Limits the length of the generated story.

Temperature	 -  0.7  - 	Controls the randomness of the output. A value of 0.7 encourages creativity.d Configuration Details
