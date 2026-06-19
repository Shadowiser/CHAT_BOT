import customtkinter as ctk
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
 #config ia
api_key = os.getenv("MY_API_KEY")


genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")




#fonction de réponse du chatbot

def chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

#fonction envoyer le message
def send_message(event=None):
    user_message = user_input.get()
    if user_message.strip()!= "":
        chat_history.configure(state="normal")
        chat_history.insert("end",f"Vous: {user_message}\n", "user")
        bot_response = chatbot_response(user_message)
        chat_history.insert("end",f"Bot: {bot_response}\n", "bot")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        user_input.delete(0,"end")




#config de l'interface
app = ctk.CTk()
app.geometry("500x600")
app.title("Mon chatbot")

#en tête

header = ctk.CTkLabel(app,text="Bienvenue sur mon chatbot",font=("Nulshock",20,"bold"))
header.pack(pady=10)

#zone affichage du message

chat_history = ctk.CTkTextbox(app, height=400,state="disabled")
chat_history.tag_config("user", foreground="white")
chat_history.tag_config("bot", foreground="green")
chat_history.pack(pady=10,padx=10,fill="both",expand= True)
chat_history.configure(font=("Orbitron",18,"bold"))


# champ de saisie
user_input_frame = ctk.CTkFrame(app)
user_input_frame.pack(pady=10,padx=10,fill="x")

user_input = ctk.CTkEntry(user_input_frame,placeholder_text="Entrez votre message...",width=350)
user_input.pack(side="left",padx=5)

send_btn = ctk.CTkButton(user_input_frame,text="Envoyer",command=send_message)

send_btn.pack(side="left")

#associer une touche pour envoyer le message

app.bind("<Return>",send_message)
app.mainloop()