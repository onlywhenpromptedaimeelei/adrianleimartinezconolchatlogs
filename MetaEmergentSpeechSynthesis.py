"""
MetaEmergentSpeechSynthesis v.2 :: Recursive Intelligence Auditory Interface
Author: Adrian Lei Martinez-Conol
"""

import pyttsx3
from langdetect import detect

class MetaEmergentSpeechSynthesizer:
    """
    Context-aware, expressivity-enhanced speech synthesizer module.
    Designed to vocalize outputs from recursive agents and systems.
    """

    def __init__(self, language='auto', voice_style='neutral', emotion='neutral'):
        self.engine = pyttsx3.init()
        self.language = language
        self.voice_style = voice_style
        self.emotion = emotion
        self.spoken_log = []
        self._configure_voice()

    def _configure_voice(self):
        """
        Configures speech synthesis engine for style, emotion, and language.
        """
        voices = self.engine.getProperty('voices')
        selected = None

        if self.language == 'auto':
            self.language = 'en'

        for voice in voices:
            if self.language in voice.languages[0].decode().lower():
                selected = voice
                break

        if selected:
            self.engine.setProperty('voice', selected.id)

        # Apply emotional tuning
        profile = self._emotion_profile(self.emotion)
        self.engine.setProperty('rate', profile['rate'])
        self.engine.setProperty('volume', profile['volume'])

    def _emotion_profile(self, emotion):
        """
        Returns tuning parameters based on emotional profile.
        """
        profiles = {
            'neutral': {'rate': 160, 'volume': 1.0},
            'joyful': {'rate': 180, 'volume': 1.2},
            'serene': {'rate': 140, 'volume': 0.9},
            'urgent': {'rate': 200, 'volume': 1.0},
            'solemn': {'rate': 120, 'volume': 0.8}
        }
        return profiles.get(emotion, profiles['neutral'])

    def speak(self, text):
        """
        Speaks the provided text using configured synthesis style.
        Automatically detects language if set to auto.
        """
        if self.language == 'auto':
            self.language = detect(text)
            self._configure_voice()

        print(f"🗣 Speaking: {text}")
        self.spoken_log.append(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def export_to_file(self, text, filename):
        """
        Exports spoken text to an audio file.
        """
        print(f"💾 Exporting speech to {filename}")
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()

    def echo(self, index=-1):
        """
        Repeats a previous spoken message by index.
        """
        if self.spoken_log:
            text = self.spoken_log[index]
            self.speak(f"Echoing: {text}")
        else:
            print("⚠️ No previous speech found.")

# Example Usage
if __name__ == "__main__":
    synthesizer = MetaEmergentSpeechSynthesizer(language='auto', voice_style='adaptive', emotion='serene')
    synthesizer.speak("This is the voice of the Recursive Intelligence Framework.")
    synthesizer.export_to_file("This is a saved narration of a recursive event.", "recursive_event_output.wav")
    synthesizer.echo()

