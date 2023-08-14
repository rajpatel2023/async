from pytube import YouTube, Playlist
import os
from dotenv import load_dotenv

load_dotenv()
FOLDER_PATH_ROW = os.getenv("FOLDER_PATH_ROW")


def download_youtube_video(video_url, file_name, preferred_quality="720p"):
    try:
        save_path = FOLDER_PATH_ROW
        yt = YouTube(video_url)
        preferred_streams = yt.streams.filter(
            res=preferred_quality, mime_type="video/mp4"
        ).order_by("resolution")
        max_quality_stream = yt.streams.get_highest_resolution()
        if preferred_streams:
            selected_stream = preferred_streams.first()
        else:
            selected_stream = max_quality_stream
        os.makedirs(save_path, exist_ok=True)
        selected_stream.download(output_path=save_path, filename=file_name)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
