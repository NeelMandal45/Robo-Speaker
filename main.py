import os

def speak(text):
    command=f'powershell "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
    os.system(command)

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 Created by Neel")
    while True:
        x = input("Enter what you want me to speak (or type 'exit' to quit): ")
        if x.lower() == "exit":
           speak("bye bye friend")
           break
        speak(x)

   