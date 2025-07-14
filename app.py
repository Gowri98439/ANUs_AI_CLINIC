from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="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")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message")

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a friendly AI doctor giving empathetic advice. Always suggest to consult a real doctor."},
            {"role": "user", "content": user_message}
        ]
    )
    bot_reply = completion.choices[0].message.content.strip()
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)