from pytube import YouTube


def bytes_to_mb(bytes_size):
    mb_size = bytes_size / (1024 * 1024)
    return mb_size


def seconds_to_minutes(seconds):
    minutes = seconds // 60
    return minutes


video_url = "https://www.youtube.com/watch?v=mgisw1UotZQ&ab_channel=AlarmTimer"

yt = YouTube(video_url)

print("Video Title:", yt.title)
video_length_minutes = seconds_to_minutes(yt.length)
print("Video Length (minutes):", video_length_minutes)

# Get available video streams
video_streams = yt.streams

for stream in video_streams:
    print("Quality:", stream.resolution)
    file_size_mb = bytes_to_mb(stream.filesize)
    rounded_file_size_mb = round(file_size_mb, 2)  # Round to 2 decimal places
    print("File Size (MB):", stream.filesize_mb)
    print("Type:", stream.mime_type)
    print("fsp", stream.fps)
    if stream.video_codec:
        print("Video Codec:", stream.video_codec)
    else:
        print("Audio Codec:", "None")
    print("---------")
