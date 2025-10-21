import tkinter as tk
from tkinter import scrolledtext
import requests
import json
import os
import sys

# --- GEMINI API CONFIGURATION ---
# The API Key is obtained either from the GEMINI_API_KEY environment variable
# or defaults to a placeholder.
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"
MODEL_NAME = "gemini-2.5-flash-preview-09-2025"
# --------------------------------

# --- Tkinter UI Setup ---
root = tk.Tk()
root.title("Gemini Story Generator")
root.geometry("800x800")

tk.Label(root, text="Enter a prompt for your story (using Gemini):").pack(pady=10)

story_entry = tk.Entry(root, width=50)
story_entry.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=70, height=18)
output_text.pack(pady=10, padx=10)

def generate_story():
    """Fetches a generated story from the Gemini API based on user prompt."""
    
    # Get the prompt from the entry widget
    prompt = story_entry.get()
    if not prompt:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a prompt.\n")
        return
    
    # Check if API key is configured
    if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Please set your Gemini API key.\n")
        output_text.insert(tk.END, "You can either:\n")
        output_text.insert(tk.END, "1. Set GEMINI_API_KEY environment variable\n")
        output_text.insert(tk.END, "2. Replace 'YOUR_GEMINI_API_KEY_HERE' with your actual API key in the script\n")
        return
    
    # Show loading message
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Generating story with Gemini... Please wait.\n")
    root.update()
    
    try:
        # Construct the API request payload for Gemini
        payload = {
            "contents": [
                {
                    "role": "user", 
                    "parts": [
                        {"text": f"Write a creative story based on the following prompt: {prompt}"}
                    ]
                }
            ],
            "generationConfig": {
                "maxOutputTokens": 1000,
                "temperature": 0.7
            }
        }

        # Make the POST request to the Gemini API. 
        # The API key is passed in the URL query string.
        response = requests.post(
            f"{API_URL}?key={API_KEY}",
            headers={
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            try:
                data = response.json()
                # Extract the generated text from the Gemini response structure
                story = data["candidates"][0]["content"]["parts"][0]["text"]
                
                output_text.delete(1.0, tk.END)
                output_text.insert(tk.END, story)
            except (KeyError, IndexError, TypeError) as e:
                output_text.delete(1.0, tk.END)
                output_text.insert(tk.END, f"Error parsing Gemini response: {str(e)}\n")
                output_text.insert(tk.END, f"Raw response: {response.text}")
        else:
            output_text.delete(1.0, tk.END)
            try:
                error_data = response.json()
                error_msg = error_data.get("error", {}).get("message", "Unknown error")
                output_text.insert(tk.END, f"API Error {response.status_code}: {error_msg}\n")
                if response.status_code in [401, 403]:
                    output_text.insert(tk.END, "Please check if your API key is valid and has the necessary permissions.\n")
            except json.JSONDecodeError:
                output_text.insert(tk.END, f"Error: {response.status_code}\n{response.text}")
                
    except requests.exceptions.Timeout:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Request timed out. Please try again.\n")
    except requests.exceptions.ConnectionError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Connection failed. Please check your internet connection.\n")
    except requests.exceptions.RequestException as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Request error: {str(e)}\n")
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Unexpected error: {str(e)}\n")

generator_button = tk.Button(root, text="Generate Story", command=generate_story)
generator_button.pack(pady=10) 

if __name__ == "__main__":
    # If the API key is the placeholder, display a warning on startup
    if API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        output_text.insert(tk.END, "WARNING: API Key placeholder detected.\n")
        output_text.insert(tk.END, "Please replace 'YOUR_GEMINI_API_KEY_HERE' in the script or set the GEMINI_API_KEY environment variable before generating a story.")
        
    root.mainloop()
