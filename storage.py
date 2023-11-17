'''
git commands:

git pull GPT_Web_Personal main --allow-unrelated-histories
git push GPT_Web_Personal main
'''


from bing_Image_generator import ImageGen

auth_cookie = "1glHV2CTJBuTvq2UOoJIWLB6F-ciBOvMFhRX2FNuDybkqaFPfqZofkh9FanSF1z2vBujStWGLXbWRMagfukBkoRMOUdoNEgtkVqOoTYSp_cE3RrooY754f-aYqJOy16W7C3f8yIYuaNMSdsajPmOxUkGFsGkXkXF8tIEE8yfjOjk-y-HGUbcgn-arQHONGdkZtWrkgtHr0xyVLEH6ymkSveFF9x3lM7i1jgoJk1QdJIE"
auth_cookie_SRCHHPGUSR = "HV=1692014599&CW=1646&CH=793&SCW=1628&SCH=1991&BRW=XW&BRH=M&SRCHLANG=en&DM=1&THEME=1&PRVCW=1646&PRVCH=793&DPR=1.1&UTC=330&PV=15.0.0&EXLTT=31&cdxtone=Precise&cdxtoneopts=h3precise,clgalileo,gencontentv3&IG=4B70037EE7AC4BBCB29F7851CEA39E82&CMUID=23622FAE0541681D20E73C8804DA6996&VCW=1628&VCH=793&WEBTHEME=1"
image_generator = ImageGen(auth_cookie, auth_cookie_SRCHHPGUSR)

prompt = "cat"
image_links = image_generator.get_images(prompt)

for link in image_links:
    print(link)


import requests
from bs4 import BeautifulSoup

def google_link_stripper(soup):
    l=[]
    for i in soup:
        i=str(i)
        if "https" in i:
            i=i[i.find("https"):]
            i=i[:i.find('"')]
            l.append(i)
    return l

url = r'''https://www.google.com/search?q=abc&sca_esv=557881931&sxsrf=AB5stBgqrAP78qeurhNRqxkw4Z2eyhZ9IQ%3A1692308294002&source=hp&ei=RZPeZO6DO8KfseMP56y6sAY&iflsig=AD69kcEAAAAAZN6hVsTPOKFeaCq0wUm7c8Jj5EVo3uLu&ved=0ahUKEwiuutnV0-SAAxXCT2wGHWeWDmYQ4dUDCAk&uact=5&oq=abc&gs_lp=Egdnd3Mtd2l6IgNhYmMyBxAjGIoFGCcyDhAAGIoFGLEDGIMBGJECMgsQABiABBixAxiDATIIEAAYgAQYsQMyERAuGIAEGLEDGIMBGMcBGNEDMgsQABiABBixAxiDATILEC4YgAQYsQMYgwEyCxAuGIMBGLEDGIAEMgsQABiABBixAxiDATILEAAYgAQYsQMYgwFIlgpQ4AVYtQhwAXgAkAEAmAG5AaABlwSqAQMwLjO4AQPIAQD4AQGoAgrCAgcQIxjqAhgnwgIUEC4YigUYsQMYgwEYxwEY0QMYkQLCAggQABiKBRiRAsICCxAuGIoFGLEDGIMBwgIFEC4YgATCAgsQABiKBRixAxiDAQ&sclient=gws-wiz'''
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
soup = soup.find_all('a')
links = google_link_stripper(soup)

one_string = ''' '''

for i in links:
    if len(one_string)<10000:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser').text
        one_string+=soup
print(one_string)
print(len(one_string))


from EdgeGPT.EdgeUtils import Query

q = Query(
  "count 1-5",
  style="creative",  # or: 'balanced', 'precise'
  cookie_files="GPT_Updated_Personal\cookies.json"
)
print(q)


website:
'''
from flask import Flask, render_template, request, redirect, url_for, jsonify
from miscellaneous import structured_response

app = Flask(__name__)

# Initialize an empty list to store the chat history
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['user_message']
        if user_message:
            bot_response=structured_response(user_message)
        if not bot_response:
            bot_response = 'no response'
        
        chat_history.append((user_message, bot_response))
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(chat_history)
        else:
            return redirect(url_for('chat'))

        
    return render_template('app_frontend.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)


'''

app_front_html:
'''
<!DOCTYPE html>
<html>
<head>
    <title>Chat App</title>
    <link rel="stylesheet" type="text/css" href="static/css/asset_code.css"/>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>GPT-Web-Personal</h1>
    
    <div id="chat-container">
        {% for user_message, bot_response in chat_history %}
            <div class="message user-message">{{ user_message }}</div>
            <div class="message bot-response">
                <div class="response-text">{{ bot_response.text }}</div>
                {% for code_block in bot_response.code_blocks %}
                    <pre class="code-block">{{ code_block }}</pre>
                {% endfor %}
            </div>
        {% endfor %}
    </div>
    <div id="generating-message" style="display: none;">Generating...</div>
    
    <form method="post" class="wrap">
        <div class="search">
            <input type="text" name="user_message" class="searchTerm" placeholder="Enter your message">
            <button type="submit" class="searchButton"><img src="{{ url_for('static', filename='Image/arrow.png') }}" class="icon" alt="Send"></button>
            <i class="fa fa-search"></i>
            </button>
        </div>
    </form>

    <script type="text/javascript">
        $('form').on('submit', function(event) {
        event.preventDefault();
        var user_message = $('input[name="user_message"]').val();
        $('#chat-container').append('<div class="message user-message">' + user_message + '</div>');
        $('#generating-message').show();
        $.post('/', {user_message: user_message}, function(data) {
            $('#generating-message').hide();
            var chat_container = $('#chat-container');
            chat_container.html('');
            
            for (var i = 0; i < data.length; i++) {
                var user_message = data[i][0];
                var bot_response = data[i][1];
                
                // Replace placeholders with actual code blocks
                for (var j = 0; j < bot_response.code_blocks.length; j++) {
                    var code_block = bot_response.code_blocks[j];
                    bot_response.text = bot_response.text.replace(`__CODE_BLOCK_${j}__`, '<pre class="code-block">' + code_block + '</pre>');
                }
                
                chat_container.append('<div class="message user-message">' + user_message + '</div>');
                chat_container.append('<div class="message bot-response">' + bot_response.text + '</div>');
            }
        });

    });
    </script>
</body>
</html>
'''

asset_code_css:

'''
body,html {
    background-color: #444654;
    margin: 0;
    padding: 0;
}
h1 {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    color: #fbfcfe;
    display: flex;
    align-items: center; 
    justify-content: center;
    z-index: 2;
    border-radius: 5px;
    background-color: #343541;
    width: 99%;
    height: 40px;
    margin-top: 0;
    box-shadow: 0 0 5px #000000;
}
#chat-container {
    width: 100%;
    margin: 0 auto;
    padding: 30px 20px 80px; 
    box-sizing: border-box;
    position: relative;
    border-radius: 10%;
}
#messages {
    max-height: 300px;
    overflow-y: auto;
}
.message {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px #c5c3c34d;
    color: #fff;
}
.user-message {
    background-color: #343541;
}
.bot-response {
    background-color: #444654;
    padding-right: 10px;
}
form {
    position: fixed;
    bottom: -5px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    z-index: 2;
}
.search {
    width: 100%;
    position: relative;
    display: flex;
}
.searchTerm {
    width: 100%;
    border: 3px solid #58585d;
    border-right: none;
    padding: 5px;
    height: 13px;
    border-radius: 8px 8px 8px 8px;
    outline: none;
    color: #DCDCDC;
    background-color: #58585d;
}
.searchTerm:focus {
    color: #ffffff;
}
.searchButton {
    width: 40px;
    height: 27.5px;
    border: none;
    border-radius: 5px 5px 5px 5px;
    cursor: pointer;
    background-color: transparent;
}
.wrap {
    position: fixed;
    width: 80%;
    top: 96%;
    left: 50%;
    transform: translate(-50%, -50%);
}
img.icon{
    top: -10%;
    left: 95.3%;
    position: fixed;
    width: 40px;
    height: 28px;
}
.code-block {
    max-width: 100%;
    overflow: auto;
    white-space: pre-wrap;
}
.message.bot-response .response-text {
    background-color: #444654;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px #c5c3c34d;
    margin: 10px 0;
    color: #fff;
}
.message.bot-response .code-block {
    background-color: #343541;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px #c5c3c34d;
    margin: 10px 0;
    color: #fff;
    white-space: pre-wrap;
    overflow: auto;
    max-width: 100%;
}
'''
miscellanious:

'''
from EdgeGPT.EdgeUtils import Query
import re
def structured_response(user_input):
    q = str(Query(user_input, style="precise", cookie_files="GPT_Web_Personal\\templates\\cookies.json"))
    pattern = r'```(.*?)```'
    code_blocks = re.findall(pattern, q, re.DOTALL)
    
    # Replace code blocks with placeholders
    for i, block in enumerate(code_blocks):
        placeholder = f'__CODE_BLOCK_{i}__'
        q = q.replace('```' + block + '```', placeholder)
    
    return {'text': q, 'code_blocks': code_blocks}

'''




update:

website:
'''from flask import Flask, render_template, request, redirect, url_for, jsonify
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
'''
HTML:
'''<!DOCTYPE html>
<html>
<head>
    <title>Chat App</title>
    <link rel="stylesheet" type="text/css" href="static/css/asset_code.css"/>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>GPT-Web-Personal</h1>
    
    <div id="chat-container">
        {% for user_message, bot_response in chat_history %}
            <div class="message user-message">{{ user_message }}</div>
            <div class="message bot-response">
                <div class="response-text">{{ bot_response | safe }}</div>
            </div>
        {% endfor %} 
    </div>
    
    <div id="generating-message" style="display: none;">Generating...</div>
    
    <form method="post" class="wrap" id="chat-form">
        <div class="search">
            <input type="text" id="user-message-input" name="user_message" class="searchTerm" placeholder="Enter your message">
            <button type="submit" class="searchButton"><img src="{{ url_for('static', filename='Image/arrow.png') }}" class="icon" alt="Send"></button>
        </div>
    </form>
    <script src="static/js/asset_code.js"></script>
    
</body>
</html>
'''

css:
'''body,html {
    background-color: #444654;
    margin: 0;
    padding: 0;
}
h1 {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    color: #fbfcfe;
    display: flex;
    align-items: center; 
    justify-content: center;
    z-index: 2;
    border-radius: 5px;
    background-color: #343541;
    width: 99%;
    height: 40px;
    margin-top: 0;
    box-shadow: 0 0 5px #000000;
}
#chat-container {
    width: 100%;
    margin: 0 auto;
    padding: 30px 20px 80px; 
    box-sizing: border-box;
    position: relative;
    border-radius: 10%;
}
#messages {
    max-height: 300px;
    overflow-y: auto;
}
.message {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px #c5c3c34d;
    color: #fff;
}
.user-message {
    background-color: #343541;
}
.bot-response {
    background-color: #444654;
    padding-right: 10px;
}
form {
    position: fixed;
    bottom: -5px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    z-index: 2;
}
.search {
    width: 100%;
    position: relative;
    display: flex;
}
.searchTerm {
    width: 100%;
    border: 3px solid #58585d;
    border-right: none;
    padding: 5px;
    height: 13px;
    border-radius: 8px 8px 8px 8px;
    outline: none;
    color: #DCDCDC;
    background-color: #58585d;
}
.searchTerm:focus {
    color: #ffffff;
}
.searchButton {
    width: 40px;
    height: 27.5px;
    border: none;
    border-radius: 5px 5px 5px 5px;
    cursor: pointer;
    background-color: transparent;
}
.wrap {
    position: fixed;
    width: 80%;
    top: 96%;
    left: 50%;
    transform: translate(-50%, -50%);
}
img.icon{
    top: -10%;
    left: 95.3%;
    position: fixed;
    width: 40px;
    height: 28px;
}
pre.code-block {
    background-color: #343541;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px #c5c3c34d;
    margin: 10px 0;
    color: #fff;
    white-space: pre-wrap;
    overflow: auto;
    max-width: 100%;
}
pre.small{
    display: inline-block;
    background-color: #5f6063;
    padding: 3px;
    border-radius: 5px;
    margin: 0;
    color: #fff;
    white-space: pre-wrap;
}
h2 {
    color: #fbfcfe;
    display: flex;
    align-items: left; 
    font-size: 130%;
}

.copy-button {
    background-color: #3498db;
    color: #fff;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 5px;
}
.copy-button:hover {
    background-color: #2980b9;
}
'''

js:
'''document.addEventListener('DOMContentLoaded', function() {
    const copyButtons = document.querySelectorAll('.copy-button');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const codeBlock = this.parentNode;
            const codeText = getCodeTextWithoutButton(codeBlock);
            copyToClipboard(codeText);
            this.textContent = 'Copied!';
            setTimeout(() => {
                this.textContent = 'Copy';
            }, 1500);
        });
    });

    function getCodeTextWithoutButton(codeBlock) {
        const clonedCodeBlock = codeBlock.cloneNode(true);
        const buttonsInClonedBlock = clonedCodeBlock.querySelectorAll('.copy-button');
        buttonsInClonedBlock.forEach(button => {
            button.remove(); // Remove the buttons from the cloned block
        });
        return clonedCodeBlock.textContent;
    }

    function copyToClipboard(text) {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
    }
});
'''

miscellanious:

'''from EdgeGPT.EdgeUtils import Query
import re

def structured_response(user_input):
    a = str(Query(user_input, style="precise", cookie_files="templates\\cookies.json"))
    pattern = r'```(.*?)```'
    code_blocks = re.findall(pattern, a, re.DOTALL)
    c_b = code_blocks[:]  # Make a copy

    for i in range(len(code_blocks)):
        h = code_blocks[i].split('\n')[0]
        if len(h.split()) == 1:
            h = "<h2>" + h + "</h2>"
            code_blocks[i] = "\n".join(code_blocks[i].split('\n')[1:])
        else:
            h = ""
        code_blocks[i] = h + "<pre class='code-block'>" + '\n' + '\n'.join(code_blocks[i].split('\n')) + "<button class='copy-button'>Copy</button>" + "</pre>"

    for i in range(len(c_b)):
        a = a.replace('```' + c_b[i] + '```', code_blocks[i])  # Reassign 'a' with replaced content

    pattern = r'`(.*?)`'
    code_blocks = set(re.findall(pattern, a, re.DOTALL))
    for i in code_blocks:
        a=a.replace("`"+i+"`","<pre class='small'>"+i+"</pre>")
    return a'''

new_js:

'''
document.addEventListener('DOMContentLoaded', function() {
    const copyButtons = document.querySelectorAll('.copy-button');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const codeBlock = this.parentNode;
            const codeText = getCodeTextWithoutButton(codeBlock);
            copyToClipboard(codeText);
            this.textContent = 'Copied!';
            setTimeout(() => {
                this.textContent = 'Copy';
            }, 1500);
        });
    });

    function getCodeTextWithoutButton(codeBlock) {
        const clonedCodeBlock = codeBlock.cloneNode(true);
        const buttonsInClonedBlock = clonedCodeBlock.querySelectorAll('.copy-button');
        buttonsInClonedBlock.forEach(button => {
            button.remove(); // Remove the buttons from the cloned block
        });
        return clonedCodeBlock.textContent;
    }

    function copyToClipboard(text) {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
    }
});
document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
        
    var userMessageInput = document.getElementById('user-message-input');
    var userMessage = userMessageInput.value.trim(); // Trim whitespace
    
    // Check if user input is not blank
    if (userMessage !== "") {
        // Update chat history
        var chatContainer = document.getElementById('chat-container');
        var userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user-message';
        userMessageDiv.textContent = userMessage;
        
        // Clear the input field
        userMessageInput.value = '';
            
        // Scroll to the bottom of the chat container to show the new message
        chatContainer.appendChild(userMessageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
        
        // Use AJAX to send the user's message to the server and get the bot's response
        $.ajax({
            type: 'POST',
            url: '/',
            data: { user_message: userMessage },
            success: function(response) {
                // Get the latest bot response
                var latestBotResponse = response[response.length - 1][1];
                
                // Create and style the bot's response element
                var botResponseDiv = document.createElement('div');
                botResponseDiv.className = 'message bot-response';
                
                var responseTextDiv = document.createElement('div');
                responseTextDiv.className = 'response-text';
                responseTextDiv.textContent = latestBotResponse;
                
                botResponseDiv.appendChild(responseTextDiv);
                
                // Append the bot's response to the chat container
                chatContainer.appendChild(botResponseDiv);
                
                // Scroll to the bottom of the chat container to show the new bot response
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        });
    }
});

'''

NEW_IMAGE_GENERATOR: 

from bing_Image_generator import ImageGen
from IPython.display import Image,display
import json

f = open("templates\cookies.json")
data = json.load(f)
for i in data:
    if i["name"]=='SRCHHPGUSR':
        auth_cookie_SRCHHPGUSR=i["value"]
    elif i["name"]=='_U':
        auth_cookie=i["value"]
if auth_cookie and auth_cookie_SRCHHPGUSR:
    image_generator = ImageGen(auth_cookie_SRCHHPGUSR, auth_cookie, all_cookies=data)

    prompt = "Einstein Walking through an empty Howrah Bridge in Kolkata."
    image_links = image_generator.get_images(prompt)

    for link in image_links:    
        print(link)    
        display(Image(url=link))    
    else:
        print("No cookies available")

trial_for_Image_with_bard:

import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
from miscellaneous import image_bytes

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", 'cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.')
session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7vRa89IuM6Jf4PoXJh0ukbAHn23xENACptTwGeDrNaVDdYjmQybgqaBLt_kcEAA")
session.cookies.set("__Secure-1PSIDCC", "ACA-OxOzhCDRJNyclB7URnynkQcso8WMarpKNIitqxz19PI11jhStHIFtSrK-ry6ctVyzSgUCS0")

bard = Bard(token='cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.', session=session)

url='https://th.bing.com/th/id/OIG.vKLFI7Sx6L.WA6uUC.Bd?pid=ImgGn'
image_bytes=image_bytes(url)
res=bard.get_answer(image=image_bytes, input_text='can you explain this image?')
print(res['content'])