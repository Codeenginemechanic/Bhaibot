# BhaiBot - The Funniest Hinglish ChatGPT-Style AI
# Now using LLaMA 3 model via Groq (fully free!)

from groq import Groq

# 🔑 Paste your Groq API key here (replace the string below)
client = Groq(api_key="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")

def bhai_chat(user_msg):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "Tu BhaiBot hai – ek funny, thoda sarcastic, aur desi AI. "
                    "Reply kar Hinglish mein (thoda Hindi, thoda English mix). "
                    "User se bindass baat karni hai, mast style mein!"
                )
            },
            {"role": "user", "content": user_msg}
        ]
    )
    return response.choices[0].message.content.strip()

# 💬 Start chatting
print("🔥 BhaiBot is ready! Bol kya scene hai (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("BhaiBot: Chal bhai, fir milte hain! 😂")
        break
    try:
        reply = bhai_chat(user_input)
        print("BhaiBot:", reply)
    except Exception as e:
        print("BhaiBot: Arre bhai, kuch error aaya 🤕\n", str(e))
