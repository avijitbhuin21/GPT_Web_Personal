from flask import Flask, render_template, request, redirect, url_for, jsonify
from miscellaneous import structured_response

app = Flask(__name__)

# Initialize an empty list to store the chat history
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    bot_response = 'no response'
    if request.method == 'POST':
        user_message = request.form['user_message']
        if user_message != "":
            bot_response=structured_response(user_message)
            chat_history.append([user_message, bot_response])

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(chat_history)
        else:
            return redirect(url_for('chat'))

        
    return render_template('app_frontend.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)


