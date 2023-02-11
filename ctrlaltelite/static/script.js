let userMessage = document.querySelector('.user-message-input');
let sendButton = document.querySelector('.send-button');
let closeButton = document.querySelector('.close-button');
let messageContainer = document.querySelector('.message-container');
let logoContainer = document.querySelector('.logo-container');

//scroll to bottom of message
var someElement = document.querySelector('.message-container');
var observer = new MutationObserver(scrollToBottom);
var config = {childList: true};
observer.observe(someElement, config);
function scrollToBottom() {
    messageContainer.scrollTop = messageContainer.scrollHeight;
}

//initally set ... to none
let typingIndicator = document.querySelector('.typing-indicator');
typingIndicator.style.display = 'none';

function onInput() {
    if (userMessage.value.length > 0) {
        typingIndicator.style.display = 'flex';
    } else {
        typingIndicator.style.display = 'none';
    }
}

// function to add user message to the screen
function addUserMessage() {
    let userMessageContainer = document.createElement('div');
    userMessageContainer.classList.add('user-message');

    let userMessageText = document.createElement('p');
    userMessageText.innerText = userMessage.value;


    let messageDate = document.createElement('p');
    messageDate.classList.add('message-date');
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    messageDate.innerText = hours + ':' + minutes + ' ' + ampm;

    userMessageContainer.appendChild(userMessageText);
    userMessageContainer.appendChild(messageDate);
    messageContainer.appendChild(userMessageContainer);

}

// function to add chatbot message to the screen
function addBotMessage(message) {
    let botMessageContainer = document.createElement('div');
    botMessageContainer.classList.add('bot-message');

    let botMessageText = document.createElement('p');
    botMessageText.innerText = message;

    let messageDate = document.createElement('p');
    messageDate.classList.add('message-date');
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    messageDate.innerText = hours + ':' + minutes + ' ' + ampm;


    botMessageContainer.appendChild(botMessageText);
    botMessageContainer.appendChild(messageDate);
    messageContainer.appendChild(botMessageContainer);
}

// event listener for the send button
sendButton.addEventListener('click', function () {
    typingIndicator.style.display = 'none';
    addUserMessage();
    
    // simulate a chatbot reply
    if (userMessage.value.length > 0) {
        setTimeout(function() {
            fetch("/chat/", {
                method: "POST",
                headers: {'Content-Type': 'application/json'}, 
                body: JSON.stringify({message:"hello"})
              }).then((res)  => res.json()).then((data) => addBotMessage(data["message"]))
        }, 800);
    }
    else {
        setTimeout(function() {
            addBotMessage('Please enter a message');
        }, 800);
    }

    // clear the input field after sending the message
    userMessage.value = '';
});

function enter() {
    sendButton.click();
}

closeButton.addEventListener('click', function () {
    let Close = document.querySelector('.chat-container');
    Close.style.display = 'none';
    logoContainer.style = 'opacity: 100 %';
});



