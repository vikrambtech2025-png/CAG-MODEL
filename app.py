import requests

API_KEY = "YOUR_API_KEY"  #FROM SARVAM AI


def load_context():
    with open("context.txt", "r", encoding="utf-8") as f:
        return f.read()


def ask_llm(prompt):

    url = "https://api.sarvam.ai/v1/chat/completions"

    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sarvam-m",
        "messages": [
            {"role": "system", "content": "Answer using the given context only."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()["choices"][0]["message"]["content"]


def main():

    context = load_context()

    while True:

        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        prompt = f"""
        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        answer = ask_llm(prompt)

        print("\nAnswer:", answer)


if __name__ == "__main__":
    main()
