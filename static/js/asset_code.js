document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('click', function(event) {
        if (event.target.matches('.copy-button')) {
            const button = event.target;
            const codeBlock = button.parentNode;
            const codeText = getCodeTextWithoutButton(codeBlock);
            copyToClipboard(codeText);
            button.textContent = 'Copied!';
            setTimeout(() => {
                button.textContent = '🗐';
            }, 1500);
        }
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

var emojis = ["🌕", "🌔", "🌓", "🌒", "🌑", "🌘", "🌗", "🌖", "🌕"];
var i = 0;
setInterval(function() {
  document.getElementById("emoji").innerHTML = emojis[i];
  i = (i + 1) % emojis.length;
}, 1000);


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
            responseTextDiv.innerHTML= latestBotResponse;
            
            botResponseDiv.appendChild(responseTextDiv);
            chatContainer.appendChild(botResponseDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;

            // $('body,html').css('background-color', '#343541');
        }
    });
    }
});

