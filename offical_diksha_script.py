# All modules
import requests
import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

# Diksha API
# Input_URL -> Contain_ID -> Hit API(for Video link)[content] -> Hit API -> Save it to local
load_dotenv()
DIKSHA_ID = os.getenv("DIKSHA_ID")
FOLDER_PATH_ROW = os.getenv("FOLDER_PATH_ROW")


def extract_content_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    content_id = query_params.get("contentId", None)
    if content_id:
        return content_id[0]
    raise Exception("contentId Not Found in URL!!! Check the URL")


def download_video_diksha(content_id, file_path):
    content_url = f"https://www.diksha.gov.in/api/content/v2/read/{content_id}"
    headers = {
        "accept": "application/json",
        f"Authorization": "Bearer {DIKSHA_ID}",
        "Content-Type": "application/json",
    }
    content_response = requests.get(content_url, headers=headers)
    content_data = content_response.json()
    print(
        "URL LINK =================>",
        content_data.get("result").get("content").get("previewUrl"),
    )
    video_url = content_data.get("result").get("content").get("previewUrl")
    response_data = requests.get(video_url)
    if response_data.status_code == 200:
        print("Sucess")
    else:
        print("Request failed with status code:", response.status_code)

    # Check if path is exists or not
    if not os.path.exists(file_path):
        print(f"The path '{file_path}' does not exist.")
        raise Exception("Please check your path")
    else:
        print(f"The path '{file_path}' exists.")

    # Write a file
    try:
        with open(file_path, "wb") as file:
            file.write(response_data.content)
    except Exception as e:
        raise Exception(e)


def dikhsa(url, file_name):
    try:
        content_id = extract_content_id(url)
        file_path = os.path.join(FOLDER_PATH_ROW, file_name)
        download_video_diksha(content_id, file_path)
    except Exception as e:
        print(e)
