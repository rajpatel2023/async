from pytube import YouTube, Playlist
import os

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


# def download_video(url, preferred_quality="720p"):
#     # Create a YouTube object
#     yt = YouTube(url)

#     # Filter streams by preferred quality and sort by resolution
#     preferred_streams = yt.streams.filter(res=preferred_quality).order_by("resolution")
#     max_quality_stream = yt.streams.get_highest_resolution()

#     if preferred_streams:
#         # If the preferred quality is available, get the first stream
#         selected_stream = preferred_streams.first()
#     else:
#         # If preferred quality is not available, use the max quality stream
#         selected_stream = max_quality_stream

#     # Download the video
#     print(f"Downloading '{yt.title}' in {selected_stream.resolution}...")
#     selected_stream.download()
#     print("Download completed.")


# def download_playlist(video_url, save_path):
#     try:
#         playlist_url = video_url
#         pl = Playlist(playlist_url)
#         for video_url in pl.video_urls:
#             yt = YouTube(video_url)
#             video_stream = yt.streams.get_highest_resolution()
#             video_stream.download(output_path=save_path)
#             print(f"Downloaded: {yt.title}")
#         print("Playlist downloaded successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    video_url = "https://youtu.be/_RdYrjn_FDs"
    save_path = "C:/Users/ITIDOL-7/OneDrive/Desktop/RAJ_TEACHMENT/row_videos"
    try:
        download_youtube_video(video_url=video_url, save_path=save_path)
    except Exception as e:
        print(e)
