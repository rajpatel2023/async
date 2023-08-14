import pandas as pd
from collections import defaultdict
from offical_diksha_script import dikhsa
from subprocess_video import ffmpeg_command
from youtube_script import download_youtube_video
import os
import random
import string
import uuid


def generate_random_name(length=10):
    random_string = "".join(
        random.choices(string.ascii_letters + string.digits, k=length)
    )
    unique_id = uuid.uuid4().hex[:6]  # Generate a unique identifier
    return f"random_{random_string}_{unique_id}.mp4"


def optimize_code(df):
    error_files = []
    unknown_urls = []
    diksha_list = []
    youtube_list = []

    for index, row in df.iterrows():
        file_name = row["Content file name ( Video File Name ) - NEW"]
        url = row["Content file name ( Video File Name )"]

        if pd.isna(file_name):
            file_name = generate_random_name()

        if "youtu" in str(url):
            print("youtube ===========>", url)
            print("File name =========>", file_name)
            try:
                download_youtube_video(video_url=url, file_name=file_name)
                ffmpeg_command(file_name=file_name)
                youtube_list.append({file_name: url})

            except Exception as e:
                error_files.append({url: e})

        elif "diksha" in str(url):
            print("diksha ===========>", url)
            try:
                dikhsa(url, file_name=file_name)
                ffmpeg_command(file_name=file_name)
                diksha_list.append({file_name: url})
            except Exception as e:
                error_files.append({url: e})
        else:
            print(f"Unknown URL type: {url}")
            unknown_urls.append(url)

    error_files_df = pd.DataFrame(error_files)
    error_files_df.to_csv("url_errors.csv", index=False)
    print("Error DataFrame saved as CSV: url_errors.csv")

    unknown_urls_df = pd.DataFrame(unknown_urls)
    unknown_urls_df.to_csv("unknown_urls_df.csv", index=False)
    print("Unknown URLs DataFrame saved as CSV: unknown_urls_df.csv")

    youtube_list_df = pd.DataFrame(youtube_list)
    youtube_list_df.to_csv("youtube_list_df.csv", index=False)
    print("Unknown URLs DataFrame saved as CSV: youtube_list_df.csv")

    diksha_list_df = pd.DataFrame(diksha_list)
    diksha_list_df.to_csv("diksha_list_df.csv", index=False)
    print("Unknown URLs DataFrame saved as CSV: diksha_list_df.csv")


if __name__ == "__main__":
    sheet_name = "Mastersheet (English) - With OE"
    df = pd.read_excel(
        "UP Chapter List - For Ashish External.xlsx", sheet_name=sheet_name
    )
    optimize_code(df)
