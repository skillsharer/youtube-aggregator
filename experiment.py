import requests
import json
import time
import os
import logging
from youtube_transcript_api import YouTubeTranscriptApi

OPENAI_BEARER_TOKEN = os.environ['OPENAI_BEARER_TOKEN']

def chunk_words(string, chunk_size):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    words = string.split()
    chunks = []
    chunk = []
    for word in words:
        new_length = len(' '.join(chunk + [word]))
        if new_length > chunk_size:
            chunks.append(' '.join(chunk))
            chunk = [word]
        else:
            chunk.append(word)
    if chunk:
        chunks.append(' '.join(chunk))
    return chunks

def summarize(text, model_input_size = 4000):
    temp_prompt = "Please summarize the video transcript chunk focusing on the key points: "
    answer = text
    logging.info(f'The answer length: {len(answer)}')
    while len(answer) > model_input_size:
        chunk_answers = []
        chunks = chunk_words(answer, model_input_size - len(temp_prompt))
        for chunk in chunks:
            chunk = temp_prompt + chunk
            chunk_response = get_text(chunk)
            chunk_answers.append(chunk_response)
            time.sleep(3.01)
        answer = ' '.join(chunk_answers)

    final_prompt = f'Please summarize the video transcript focusing on the key points: {answer}'
    answer = get_text(final_prompt)

    return answer

def get_text(prompt, model="gpt-3.5-turbo"):
    try:
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + OPENAI_BEARER_TOKEN
        }
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        response = response.json()["choices"][0]["message"]["content"].replace('\n', '')
        logging.info(f"Response: {response}")
    except Exception as e:
        response = ""
        logging.error(f"An error occurred: {e}")

    return response

video_id = "lchWriufJD8"
srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
all_text = ' '.join([element["text"] for element in srt])

print(summarize(all_text, 4000))