css = '''
<style>
/* Chat Message Styles */
.chat-message {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 15px;
    display: flex;
    align-items: flex-start;
}

.chat-message.user {
    background-color: #2979FF;
    justify-content: flex-end;
}

.chat-message.bot {
    background-color: #FF4081;
    justify-content: flex-start;
}

/* Avatar Styles */
.chat-message .avatar {
    width: 15%;
    padding: 5px;
}

.chat-message .avatar img {
    max-width: 50px;
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}

/* Message Styles */
.chat-message .message {
    width: 85%;
    padding: 10px;
    border-radius: 10px;
    color: #fff;
}

/* Additional Styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}

/* Apply scrollbar for overflow messages */
.chat-container {
    height: 300px;
    overflow-y: auto;
    padding: 10px;
    border-radius: 10px;
    background-color: #fff;
    box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.1);
}
</style>

'''




bot_template = '''
    <div class="chat-message bot">
        <div class="avatar">
            <img src = "https://w7.pngwing.com/pngs/567/444/png-transparent-robotics-chatbot-technology-robot-education-electronics-computer-program-humanoid-robot-thumbnail.png">
        </div>
        <div class="message">{{MSG}}</div>
    </div>
'''

user_template = '''
    <div class="chat-message user">
        <div class="avatar">
            <img src = "https://media.licdn.com/dms/image/D5603AQEpgK1m5PKzvQ/profile-displayphoto-shrink_400_400/0/1695147321740?e=1707955200&v=beta&t=TMxwMqsgj2RT-ryv_lGg_KSDlIeOwemC0FjEcr9i0jU">
        </div>
        <div class="message">{{MSG}}</div>
    </div>
'''

