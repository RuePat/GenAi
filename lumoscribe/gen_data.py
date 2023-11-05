import re
import mutagen
import datetime
import json
import time


from transcribe import transcribe_audio
from summarize import split_chunks
from quest_gen import *

def gen_data(audio_path):

    # os.environ['OPENAI_API_KEY'] = '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'
    # openai.api_key  = os.getenv('OPENAI_API_KEY')
    
    audio = mutagen.File(audio_path)

    duration = audio.info.length

    text = transcribe_audio(audio_path)

    time.sleep(15)

    chunks = split_chunks(text)

    summaries = []

    for chunk in chunks:
        summary = generate_summary(chunk).strip()

        summaries.append(summary)
    
    summary = " ".join(summaries)

    time.sleep(15)

    flashcards = generate_flashcards(text)

    try:
        flashcards = json.loads(re.sub(r'^[a-zA-Z\s]*\[', '[', flashcards))    
    except:
        flashcards = flashcards

    time.sleep(15)
    
    fibs = generate_fib(text)

    try:
        fibs = json.loads(re.sub(r'^[a-zA-Z\s]*\[', '[', fibs))    
    except:
        fibs = fibs

    time.sleep(15)
    
    tfs = generate_tf(text)

    try:
        tfs = json.loads(re.sub(r'^[a-zA-Z\s]*\[', '[', tfs))    
    except:
        tfs = tfs

    time.sleep(15)

    mcqs = generate_mcq(text)

    try:
        mcqs = json.loads(re.sub(r'^[a-zA-Z\s]*\[', '[', mcqs))    
    except Exception as e:
        mcqs = mcqs

    today = datetime.date.today()

    record = {
        "title": "Neural Networks Notes #1",
        "transcript": text,
        "summary": summary,
        "duration": duration,
        "questions": {
            "flashcards": flashcards,
            "mcqs": mcqs,
            "fibs": fibs,
            "tfs": tfs
        },
        "created": today.strftime('%m/%d/%Y'),
        "subject": "AIPI520"
    }

    with open('record.json', 'w') as f:
        json.dump(record, f)
    return record