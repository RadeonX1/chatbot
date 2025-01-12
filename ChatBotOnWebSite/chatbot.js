// JavaScript (chatbot.js)

const botTemplate = "BOT : {0}";

const name = "Bot";
const weather = "cloudy";

// Define a dictionary containing a list of responses for each message
const responses = {
    "what's your name?": [
        `my name is ${name}`,
        `they call me ${name}`,
        `I am ${name}`
    ],

    "what's today's weather?": [
        `the weather is ${weather}`,
        `it's ${weather} today`
    ],

    'statement': [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way?',
        'I find that extremely interesting',
        'can you back that up?', 'oh wow!',
        ':)'
    ],

    'question': [
        "I don't know :(",
        'you tell me!'
    ],

    'xxxn': [
        ":(",
        'you tell me!'
    ],

    "default": ["คือระ ?"]
};

// Use Math.random() to choose a matching response
function respond(message) {
    message = message.toLowerCase();
    if (responses[message]) {
        // Return a random matching response
        const responseArray = responses[message];
        const botMessage = responseArray[Math.floor(Math.random() * responseArray.length)];
        return botMessage;
    } else {
        // Return a random "default" response
        const defaultResponse = responses["default"];
        const botMessage = defaultResponse[Math.floor(Math.random() * defaultResponse.length)];
        return botMessage;
    }
}

function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let botResponse = respond(userInput);

    // Append user message and bot response to the chatbox
    let chatBox = document.getElementById("chatBox");
    chatBox.innerHTML += `<div class="user">You: ${userInput}</div>`;
    chatBox.innerHTML += `<div class="bot">Bot: ${botResponse}</div>`;

    // Clear the input field after sending the message
    document.getElementById("userInput").value = "";
}
