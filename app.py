from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/chat.html')
def chat():
    return render_template('chat.html')

@app.route('/chat.html', methods=['POST'])
def ask_question():
    user_question = request.json['question']

    # Use GPT-3.5 Turbo to get an answer
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question},
        ]
    )

    answer = response['choices'][0]['message']['content'].strip()

    response = {'user_question': user_question, 'answer': answer}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
