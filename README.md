# mute-songs
mute specified sections of video (when uploading GTA games to youtube)

# usage

1. Upload a video with the sound intact to YouTube
2. Get copyright complaints, and go look at the detailed page (https://www.youtube.com/video_copynotice?v=xxxxxxxxx) 
3. Copy all of the time stamps/durations into a new text file (`see examples.txt`)
4. Run `python mute.py list.txt`
5. Copy the `ffmpeg` command and run it
6. Upload this new version to Youtube
7. Go back to step 2 if you still get copyright issues
