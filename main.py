import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def start():
    speak('yes sir')
    print('Yes Sir..')

    while True:

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio2 = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print('Listening...')
            world = recognizer.recognize_google(audio2)
            print(world)

            if world.lower() == 'open google':
                print('opening')
                speak('opening')
                webbrowser.open('www.google.com')
            elif world.lower() == 'open youtube':
                print('opening')
                speak('opening')
                webbrowser.open('https://www.youtube.com/')
            elif world.lower() == 'open github':
                print('opening')
                speak('opening')
                webbrowser.open('https://github.com/')
            elif world.lower() == 'open instagram':
                print('opening')
                speak('opening')
                webbrowser.open('https://www.instagram.com/')
            elif world.lower() == 'open linkedin':
                print('opening')
                speak('opening')
                webbrowser.open('https://linkedin.com/')
            elif world.lower() == 'open facebook':
                print('opening')
                speak('opening')
                webbrowser.open('facebook.com')
            elif world.lower() == 'open twitter':
                print('opening')
                speak('opening')
                webbrowser.open('https://twitter.com')
            elif world.lower() == 'open whatsapp':
                print('opening')
                speak('opening')
                webbrowser.open('https://web.whatsapp.com')
            elif world.lower() == 'open gmail':
                print('opening')
                speak('opening')
                webbrowser.open('https://mail.google.com')
            elif world.lower() == 'open amazon':
                print('opening')
                speak('opening')
                webbrowser.open('https://www.amazon.in')
            elif world.lower() == 'open flipkart':
                print('opening')
                speak('opening')
                webbrowser.open('https://www.flipkart.com')
            elif world.lower() == 'open spotify':
                print('opening')
                speak('opening')
                webbrowser.open('https://open.spotify.com')
            elif world.lower() == 'open netflix':
                print('opening')
                speak('opening')
                webbrowser.open('https://www.netflix.com')


            elif world.lower() == 'close':
                print('Thanks')
                speak('Thanks')
                break

        except:
            print('Error 2')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listening_audio():
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)

                speak('listening')
                print('listening')

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            command = recognizer.recognize_google(audio)
            speak(command)
            print(f'You said - \n{command}')

            if command.lower() == 'jarvis':
                    start()
                    break
            elif command.lower() == 'close':
                    speak('Goodbye Sir')
                    break

        except sr.RequestError:
            print('Netwotk Error')
        except :
            print('Error')

if __name__ == "__main__":
    speak('Initializing...')
    listening_audio()
