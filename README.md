# Auto Synced & Translated Dubs
 Automatically translates the text of a video into chosen languages based on a subtitle file, and also uses AI voice to dub the video, while keeping it properly synced to the original video using the subtitle's timings.
 
### How It Works
If you already have a human-made SRT subtitles file for a video, this will:
1. Use Google Cloud/DeepL to automatically translate the text, and create new translated SRT files
2. Create text-to-speech audio clips of the translated text (using more realistic neural voices)
3. Use the timings of the subtitle lines to calculate the correct duration of each spoken audio clip
4. Stretch or shrink the translated audio clip to be exactly the same length as the original speech, and inserted at the same point in the audio. Therefore the translated speech will remain perfectly in sync with the original video.
    - Optional (On by Default): Instead of stretching the audio clips, you can instead do a second pass at synthesizing each clip through the API using the proper speaking speed calculated during the first pass. This drastically improves audio quality.
    
### Additional Key Features
- Creates translated versions of the SRT subtitle file
- Batch processing of multiple languages in sequence
- Config files to save translation, synthesis, and language settings for re-use
- Included script for adding all language audio tracks to a video file
   - With ability to merge a sound effects track into each language track
- Included script for translating a YouTube video Title and Description to multiple languages

