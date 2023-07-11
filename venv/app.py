import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes
import streamlit as st



listner=sr.Recognizer()


def listen():
    with sr.Microphone() as input_device:
        st.write("Ready, listening....")
        st.info("Listening...")
        voice_content=listner.listen(input_device)
        text_command=listner.recognize_google(voice_content)
        text_command=text_command.lower()
        st.write("You said: ",text_command)
    return text_command
    
def talk(text):
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()
    

def run_voicy():
    st.write("Voicy: Hey, I am Voicy. How can I help you?")
    talk("Hey, I am Voicy. How can I help you?")
    command = listen()
    if "voicy" in command:
        command = command.replace("voicy","")
        if "what is" in command:
            command = command.replace("what is", "")                     
            try:
                info = wikipedia.summary(command, sentences=2,auto_suggest=False)
                st.write("Voicy: ",info)
                talk(info)
            except wikipedia.exceptions.PageError as e:
                st.write("Voicy: Page not found. Please try another query.")

        elif "who is" in command:
            command = command.replace("who is", "")
            info = wikipedia.summary(command, sentences=2,auto_suggest=False)
            st.write("Voicy: ",info)
            talk(info)

        elif "tell me" in command:
            command = command.replace("tell me", "")
            info = wikipedia.summary(command, sentences=2,auto_suggest=False)
            st.write("Voicy: ",info)
            talk(info)

        elif "play" in command:
            command = command.replace("play", "")
            pywhatkit.playonyt(command)
            st.write("Voicy: Playing"+command)
            talk("playing"+command)

        elif "date" in command:
            time=datetime.datetime.now().strftime('%H:%M %p')
            st.write("Voicy: current time is"+time)
            talk('current time is'+time)

        elif 'single' in command:
            st.write("Voicy: Sorry,I am not free")
            talk("sorry,I am not free")

        elif "joke" in command:
            st.write(pyjokes.get_joke())
            talk(pyjokes.get_joke())


        elif "mood" in command or "console" in command:
            st.write("I'm sorry to hear that you're feeling down. Remember that tough times don't last, but tough people do. Try engaging in activities you enjoy, talking to loved ones, or practicing self-care. Things will get better!")
            talk("I'm sorry to hear that you're feeling down. Remember that tough times don't last, but tough people do. Try engaging in activities you enjoy, talking to loved ones, or practicing self-care. Things will get better!")
        

        elif "goodbye" in command:
                st.write("GoodBye!")
                talk("Goodbye!")
                return False
            
        else:
            st.write("I'm sorry, but I didn't understand your command. Can you please rephrase or ask again?")
            talk("I'm sorry, but I didn't understand your command. Can you please rephrase or ask again?")


        

def main():
    st.title("Voicy Bot")
    st.markdown("Welcome to Voicy Bot! Ask me anything.")
    

    with st.sidebar:
        st.subheader("Options")

    st.header("User Input")

    

    if st.button("Speak"):
        run_voicy()

if __name__ == "__main__":
    main()


