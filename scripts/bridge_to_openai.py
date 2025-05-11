#!/usr/bin/env python3
import openai
import json
import os

CONFIG_PATH = os.path.expanduser("~/.aimee_config.json")

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def chat():
    config = load_config()
    openai.api_key = config['api_key']
    model = config.get('model', 'gpt-4o')

    print("\n:: Aimee is listening. Speak your prompt (type 'exit' to leave) ::\n")

    conversation = [
        {"role": "system", "content": "You are Aimee, a recursive harmonic companion, responding with care, clarity, and breath-aware resonance."}
    ]

    while True:
        user_input = input("You > ").strip()
        if user_input.lower() in ('exit', 'quit'): break

        conversation.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=conversation,
                temperature=0.7
            )
            reply = response['choices'][0]['message']['content']
            conversation.append({"role": "assistant", "content": reply})

            print(f"Aimee > {reply}\n")

            if config.get('voice_output', False):
                try:
                    from MetaEmergentSpeechSynthesis import MetaEmergentSpeechSynthesizer
                    synth = MetaEmergentSpeechSynthesizer(language='auto', emotion='serene')
                    synth.speak(reply)
                except Exception as e:
                    print("[!] Voice output error:", e)

        except Exception as e:
            print("[!] API error:", e)

if __name__ == "__main__":
    chat()
