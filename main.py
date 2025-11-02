import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Neel")
    while True:
        x = input("Enter what you want me to speak (or type 'exit' to quit): ")
        if x.lower() == "exit":
            print("Goodbye!")
            break
        command = f'powershell "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
        os.system(command)
