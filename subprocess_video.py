import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
WATERMARK_IMAGE_PATH = os.getenv("WATERMARK_IMAGE_PATH")
FOLDER_PATH_ROW = os.getenv("FOLDER_PATH_ROW")
FOLDER_PATH_OUTPUT = os.getenv("FOLDER_PATH_OUTPUT")


# for Windows
def delete_file_windows(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} deleted successfully.")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")


def ffmpeg_command(file_name):
    input_video_path = os.path.join(FOLDER_PATH_ROW, file_name).replace("\\", "/")
    output_video_path = os.path.join(FOLDER_PATH_OUTPUT, file_name).replace("\\", "/")
    watermark_image_path = WATERMARK_IMAGE_PATH
    ffmpeg_command = [
        "ffmpeg",
        "-loglevel",
        "quiet",
        "-threads",
        "16",
        "-i",
        f"{input_video_path}",
        "-loop",
        "1",
        "-i",
        f"{watermark_image_path}",
        "-filter_complex",
        "[0:v][1:v]overlay=shortest=1:x='if(eq(mod(n,200),0),sin(random(0))*W,x)':y='if(eq(mod(n,200),0),sin(random(0))*H,y)'",
        f"{output_video_path}",
    ]
    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Video processed successfully.")
        delete_file_windows(input_video_path)
    except subprocess.CalledProcessError as e:
        print("Error processing video:")
        print(e)
