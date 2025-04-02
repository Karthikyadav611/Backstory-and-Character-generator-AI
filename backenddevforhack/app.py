from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from groq import Groq
import requests
import os
import time

# API Keys (Replace with your own keys)
GROQ_API_KEY = "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"
STABILITY_API_KEY = "sk-f41LQr5nYz0dXnjL9BdHKZtCJ7tQhY5jlDmQ5h4J3WgKS2TE"

# Initialize API Client for Groq
client = Groq(api_key=GROQ_API_KEY)

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Stability AI Image Generation API URL
STABILITY_API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

# Function to Generate Character Backstory
def generate_backstory(name, skills, ability, rank):
    """Generate a concise 100-word backstory for a game character."""
    prompt = f"""
    Create a concise 100-word backstory for a game character.
    - Name: {name}
    - Skills: {skills}
    - Ability: {ability}
    - Rank: {rank}
    The backstory should be engaging and game-oriented.
    """
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating backstory: {str(e)}"

@app.route("/generate-story", methods=["POST"])
def generate_story():
    """API endpoint to generate a game character backstory."""
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    name = data.get("name", "Unknown Hero")
    skills = data.get("skills", "Sword Fighting, Stealth")
    ability = data.get("ability", "Time Manipulation")
    rank = data.get("rank", "Elite Warrior")

    backstory = generate_backstory(name, skills, ability, rank)
    return jsonify({"story": backstory})

@app.route("/generate-image", methods=["POST"])
def generate_image():
    """API endpoint to generate images based on the story."""
    data = request.json
    story = data.get("description", "")

    if not story:
        return jsonify({"error": "No story provided"}), 400

    sentences = story.split(".")  # Split into sentences
    os.makedirs("static/generated_images", exist_ok=True)
    images = []

    for i, sentence in enumerate(sentences):
        if not sentence.strip():
            continue

        print(f"🎨 Generating image for: {sentence}")
        response = requests.post(
            STABILITY_API_URL,
            headers={
                "Authorization": f"Bearer {STABILITY_API_KEY}",
                "Accept": "image/*",
            },
            files={"none": ''},
            data={"prompt": sentence},
        )

        if response.status_code == 200:
            file_name = f"static/generated_images/image_{i + 1}.jpg"
            with open(file_name, "wb") as file:
                file.write(response.content)
            images.append(file_name)
        
        time.sleep(1)  # Prevent hitting API limits

    return jsonify({"images": images})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
