# LLM_QA_CLI.py
import os
import openai
import string

# Make sure you set your OpenAI API key in environment variables
# Windows: setx OPENAI_API_KEY "your_key_here"
openai.api_key = os.getenv("OPENAI_API_KEY")

def preprocess(question):
    # Lowercase
    question = question.lower()
    # Remove punctuation
    question = question.translate(str.maketrans('', '', string.punctuation))
    return question

def ask_llm(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question concisely:\n{question}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to LLM Q&A CLI. Type 'exit' to quit.")
    while True:
        question = input("Enter your question: ")
        if question.lower() == "exit":
            print("Goodbye!")
            break
        processed_question = preprocess(question)
        answer = ask_llm(processed_question)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()
