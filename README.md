# Backstory-and-Character-generator-AI
# Character Backstory Generator with AI-Powered Image Generation

## Overview
This project is a Flask-based web application that generates engaging game character backstories using AI and visualizes them with AI-generated images. It leverages Groq API for text generation and Stability AI for image generation.

## Features
- Generate a 100-word character backstory based on user-provided attributes (name, skills, ability, rank).
- AI-powered image generation for the story using Stability AI.
- Interactive web interface to view generated stories and images.
- Flask backend with REST API endpoints for generating text and images.
- Simple and responsive UI.

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** Groq API (Text Generation), Stability AI API (Image Generation)
- **Storage:** Local storage for images

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Flask and required dependencies installed
- API keys for Groq and Stability AI

### Steps to Run the Project
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Install required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up API keys in the `app.py` file:
   ```python
   GROQ_API_KEY = "your_groq_api_key"
   STABILITY_API_KEY = "your_stability_api_key"
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
5. Open the web app in your browser:
   ```
   http://127.0.0.1:5001
   ```

## API Endpoints
### Generate Backstory
- **Endpoint:** `/generate-story`
- **Method:** POST
- **Request Body (JSON):**
  ```json
  {
    "name": "Character Name",
    "skills": "Skill1, Skill2",
    "ability": "Special Ability",
    "rank": "Character Rank"
  }
  ```
- **Response:**
  ```json
  {
    "story": "Generated backstory here..."
  }
  ```

### Generate Images
- **Endpoint:** `/generate-image`
- **Method:** POST
- **Request Body (JSON):**
  ```json
  {
    "description": "Generated backstory here..."
  }
  ```
- **Response:**
  ```json
  {
    "images": ["generated_images/image_1.jpg", "generated_images/image_2.jpg"]
  }
  ```

## Folder Structure
```
project-folder/
│── static/               # Static files (CSS, JS, Images)
│── templates/            # HTML templates
│── generated_images/     # AI-generated images (auto-created)
│── app.py                # Flask backend
│── requirements.txt      # Python dependencies
│── README.txt            # Project documentation
```

## Troubleshooting
- If images are not displaying, check that `generated_images/` is accessible.
- Ensure API keys are correctly set and valid.
- Run the Flask app with `debug=True` for error logs.

## Future Enhancements
- Add a database to store generated stories.
- Implement user authentication.
- Allow users to download generated images and stories.

## License
This project is open-source and available under the MIT License.

## Author
Karthik Yadav

For any queries, feel free to connect!

