The primary goal is to create a frictionless experience where the path from idea to generated story is as short and intuitive as possible. The design emphasizes clear input fields and a clean, readable output display.
A flexible text area that allows the user to define specific plot points, character names, or thematic elements. This is the primary driver of the story's content.
Offers options (e.g., short paragraph, 500 words, 1000 words) to specify the desired story length, ensuring the output meets the user's requirement for detail and scope.
A simple, one-click button to copy the final generated story text to the clipboard for easy sharing or integration into external writing tools.
Leverages the Gemini API (gemini-2.5-flash-preview-09-2025 model) for sophisticated text generation and creative reasoning.

 Running the Application
 
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python storygenerator.py
   ```
3. .env file to store api
4.  GEMINI_API_KEY="your-gemini-api-key"
