// Get chatbot elements
const chatbot = document.getElementById('chatbot');
const conversation = document.getElementById('conversation');
const inputForm = document.getElementById('input-form');
const inputField = document.getElementById('input-field');
const sendButton = document.getElementById('submit-button');

async function sendJsonRequest(url, data) {
  try {
    // Send the request
    const response = await fetch(url, {
      method: 'POST', // Or 'GET', depending on the request type
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data), // Converts JavaScript object to a JSON string
    });

    inputField.disabled = true;
    sendButton.disabled = true;
    inputField.value = "Proszę czekać, generowanie odpowiedzi..."


    // Wait for the JSON response
    const result = await response.json();

    // Handle the result
    console.log('Response:', result);
    return result;
  } catch (error) {
    // Handle any errors
    console.error('Error:', error);
  }
}

// sendJsonRequest('https://example.com/api', { key1: 'value1', key2: 'value2' });



// Add event listener to input form
inputForm.addEventListener('submit', async function(event) {
  // Prevent form submission
  event.preventDefault();

  // Get user input
  const input = inputField.value;

  // Clear input field
  inputField.value = '';
  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: "2-digit" });

  // Add user input to conversation
  let message = document.createElement('div');
  message.classList.add('chatbot-message', 'user-message');
  message.innerHTML = `<p class="chatbot-text" style="background: #eeeeff;" sentTime="${currentTime}">${input}</p>`;
  conversation.appendChild(message);

  // Generate chatbot response
  // const response = generateResponse(input);

  response = await sendJsonRequest('/api', { userMessage: input });

  //await (new Promise(resolve => setTimeout(resolve, 1000)));


  inputField.disabled = false;
  sendButton.disabled = false;
  inputField.value = ""
  inputField.focus();

  // Add chatbot response to conversation
  message = document.createElement('div');
  message.classList.add('chatbot-message','chatbot');
  message.innerHTML = `<p class="chatbot-text" style="background: #eeffee;" sentTime="${currentTime}">${(response["serverMessage"])}</p>`;
  conversation.appendChild(message);
  message.scrollIntoView({behavior: "smooth"});
});

// Generate chatbot response function
/*function generateResponse(input) {
    // Add chatbot logic here
    const responses = [
      "Hello, how can I help you today? 😊",
      "I'm sorry, I didn't understand your question. Could you please rephrase it? 😕",
      "I'm here to assist you with any questions or concerns you may have. 📩",
      "I'm sorry, I'm not able to browse the internet or access external information. Is there anything else I can help with? 💻",
      "What would you like to know? 🤔",
      "I'm sorry, I'm not programmed to handle offensive or inappropriate language. Please refrain from using such language in our conversation. 🚫",
      "I'm here to assist you with any questions or problems you may have. How can I help you today? 🚀",
      "Is there anything specific you'd like to talk about? 💬",
      "I'm happy to help with any questions or concerns you may have. Just let me know how I can assist you. 😊",
      "I'm here to assist you with any questions or problems you may have. What can I help you with today? 🤗",
      "Is there anything specific you'd like to ask or talk about? I'm here to help with any questions or concerns you may have. 💬",
      "I'm here to assist you with any questions or problems you may have. How can I help you today? 💡",
    ];
    
    // Return a random response
    return responses[Math.floor(Math.random() * responses.length)];
  }*/
  //tab switch

  window.onblur = function (tabs) { 
// alert('trying to switch tabs eh !'); 
  };
  
  