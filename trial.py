from flask import Flask, render_template, request, redirect, url_for, jsonify
from miscellaneous import structured_response

app = Flask(__name__)

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    bot_response = r'''Sure, here is a simple Python code snippet that checks if a number is odd or even: <h2>python</h2><pre class='code-block'> def check_odd_even(num): if num % 2 == 0: return "Even" else: return "Odd" # Test the function num = 7 print(f"The number {num} is {check_odd_even(num)}.") <button class='copy-button'>Copy</button></pre> In this code, the function <pre class='small'>check_odd_even</pre> takes an integer <pre class='small'>num</pre> as input. It uses the modulus operator <pre class='small'>%</pre> to find the remainder of <pre class='small'>num</pre> divided by 2. If the remainder is 0, it means <pre class='small'>num</pre> is even, otherwise <pre class='small'>num</pre> is odd. The function then returns the result. The last two lines are used to test the function with an example number, here <pre class='small'>7</pre>. You can replace <pre class='small'>7</pre> with any number you want to check.'''
    if request.method == 'POST':
        chat_history.append([bot_response])
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(chat_history)
        else:
            return redirect(url_for('chat'))

        
    return render_template('trial.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)