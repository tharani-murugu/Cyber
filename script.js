const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

function sendMessage() {
    const message = userInput.value.trim();

    if (message !== '') {
        // Add user message to chat box
        appendMessage('you', message,);
     

        // Check for cyberbullying
        if (detectCyberbullying(message)) {
            // Alert user about cyberbullying
            appendMessage('System', 'Warning:Hello user! You send wrong word Please Change it!.');
        }

        // Clear input field
        userInput.value = '';
    }
}

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);

    // Scroll chat box to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

function detectCyberbullying(message) {
    // You can implement your cyberbullying detection algorithm here
    // This is just a placeholder example
    const bannedWords = ['hate', 'kill', 'ugly', 'stupid','fuck','loser'];
    for (let word of bannedWords) {
        if (message.toLowerCase().includes(word)) {
            return true;
        }
    }
    return false;
}