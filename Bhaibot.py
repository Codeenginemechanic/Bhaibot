import random
from textblob import TextBlob

# Define tone types
def get_tone(message):
    rude_words = ["stupid", "idiot", "nonsense", "bkl", "madarchod", "bhosdike"]
    emojis = ["😂", "🤣", "😢", "😡", "❤️", "😎"]
    
    if any(word in message.lower() for word in rude_words):
        return "rude"
    elif any(emoji in message for emoji in emojis):
        return "emoji"
    elif message.isupper():
        return "shouting"
    elif "?" in message:
        return "question"
    else:
        return "normal"

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"

# Responses per behavior
responses = {
    "positive": [
        "Oye hoye! Positive energy aa rahi hai yahan se 😄🔥",
        "Kya baat hai bhai, tu to full power mein hai 💪"
    ],
    "negative": [
        "Are bhai, tension na le! Ek meme bheju kya? 😂",
        "Lage raho, par thoda chill bhi kar bhai 🧘"
    ],
    "neutral": [
        "Hmm... kuch khas baat nahi lag rahi, tu theek hai na? 😐",
        "Aise kaise? Bata to sahi kya scene hai 😶"
    ],
    "rude": [
        "Abe thoda tameez se bhai, tu road pe nahi hai 😤",
        "Arre bhai gussa kyu ho raha hai? Ye bot hai, biwi nahi 😆"
    ],
    "emoji": [
        "Emoji game strong bhai! 😂🔥",
        "Bas yahi vibes chahiye life mein 😎"
    ],
    "shouting": [
        "CHILL KAR BRO! CAPS MEIN KYU CHILLA RAHA 😵‍💫",
        "Aree re re, itna zor se kyu bol raha bhai 😂"
    ],
    "question": [
        "Sawal acha hai, lekin jawab shayad Google ko puchhna pade 😜",
        "Bhai tu detective hai kya? Puchta hi jaa raha 😂"
    ],
    "normal": [
        "Bas aise hi casual baat cheet chal rahi hai 😌",
        "Theek hai bhai, main sun raha hoon 🤖"
    ]
}

# Full smart response function
def bhai_response(msg):
    tone = get_tone(msg)
    mood = get_sentiment(msg)

    if tone == "rude":
        return random.choice(responses["rude"])
    elif tone == "emoji":
        return random.choice(responses["emoji"])
    elif tone == "shouting":
        return random.choice(responses["shouting"])
    elif tone == "question":
        return random.choice(responses["question"])
    elif mood == "positive":
        return random.choice(responses["positive"])
    elif mood == "negative":
        return random.choice(responses["negative"])
    else:
        return random.choice(responses["neutral"])

# Start chat
print("👋 BhaiBot: Yo bro! Tera BhaiBot tayyar hai. Bol kya haal hai?")
while True:
    user = input("🧍 You: ")
    if user.lower() in ['exit', 'bye']:
        print("👋 BhaiBot: Chal fir bhai, khush rehna! 😎")
        break
    reply = bhai_response(user)
    print("🤖 BhaiBot:", reply)
