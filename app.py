from flask import Flask, render_template, request
import os
import openai
import string

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def preprocess(question):
    question = question.lower()
    question = question.translate(str.maketrans('', '', string.punctuation))
    return question

def ask_llm(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question concisely:\n{question}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    processed_question = ""
    if request.method == "POST":
        question = request.form.get("question")
        processed_question = preprocess(question)
        answer = ask_llm(processed_question)
    return render_template("index.html", processed_question=processed_question, answer=answer)

if __name__ == "__main__":
    # Use Render's port if available; default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
