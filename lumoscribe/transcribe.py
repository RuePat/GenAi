import openai

def transcribe_audio(audio_path):
    audio_file = open(audio_path, "rb")

    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return (dict(transcript)['text'])