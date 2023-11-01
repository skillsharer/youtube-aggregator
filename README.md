# YouTube Aggregator

## About

This repository hosts a Python script designed to fetch and summarize YouTube video transcripts. Utilizing the YouTubeTranscriptApi, the script extracts the transcript of a specified video. It then segments the transcript text into manageable chunks and employs OpenAI's language model to generate concise summaries of each segment, ultimately providing a coherent and condensed version of the video's content.

## Prerequisites

Before running the script, ensure the following prerequisites are met:

Python 3.x installed on your system.
Access to OpenAI's API with a valid bearer token.
Installation of the required Python libraries: requests, json, time, os, and youtube_transcript_api.

## How to Run It

To run the script, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary Python libraries using the command: `pip install requests youtube_transcript_api`.
3. Set the `OPENAI_BEARER_TOKEN` environment variable with your OpenAI API bearer token.
4. Modify the video_id variable in the script with the ID of the YouTube video you wish to summarize.
4. Execute the script using the command: `python experiment.py`.
The script will output a summary of the video transcript in the console.

## Detailed Medium Article

For an in-depth walkthrough and explanation of the code, please refer to our Medium article. It provides a step-by-step guide and delves into the technical aspects of the script, ensuring a comprehensive understanding of its functionality and potential applications. The article will be linked here once it is published: <medium_url>.
