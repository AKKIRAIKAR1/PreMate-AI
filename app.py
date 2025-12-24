from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    if request.method == "POST":
        role = request.form["role"]
        level = request.form["level"]

        prompt = f"""
            Generate a {level} React interview question.
            Format strictly like this:

            Question:
            (one line)

            Expected Answer:
            (3–4 short points)

            Key Concepts:
            (2–3 keywords only)
            """

        response = model.generate_content(prompt)
        question = response.text

    return render_template("index.html", question=question)

if __name__ == "__main__":
    app.run(debug=True)
