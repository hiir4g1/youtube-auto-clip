import json
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz


class YouTubeVideoTime:
    def __init__(self):
        with open('./api.json', 'r') as f:
            config = json.load(f)
        api_key = config['api_key']
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_info(self, video_id):
        request = self.youtube.videos().list(
            part="liveStreamingDetails",
            id=video_id
        )
        response = request.execute()

        for item in response['items']:
            #title = item['snippet']['title']
            #published_at = item['snippet']['publishedAt']
            published_at = item['liveStreamingDetails']['actualStartTime']

            # Convert the published time from UTC to JST
            dt_utc = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
            dt_jst = pytz.timezone('UTC').localize(dt_utc).astimezone(pytz.timezone('Asia/Tokyo'))

            #print(f'Title: {title}')
            print(f'Published at (JST): {dt_jst}')

            return dt_jst

    def calculate_time_elapsed(self, video_id, specific_datetime_str):
        # Convert specific_datetime_str into datetime object
        specific_datetime = datetime.strptime(specific_datetime_str, '%Y-%m-%d %H:%M:%S')
        specific_datetime = pytz.timezone('Asia/Tokyo').localize(specific_datetime)

        dt_jst = self.get_video_info(video_id)

        # Calculate time elapsed in seconds
        time_elapsed = specific_datetime - dt_jst
        time_elapsed_in_seconds = time_elapsed.total_seconds()

        print(f'Time elapsed from the video published time (in seconds): {time_elapsed_in_seconds}')

        return time_elapsed_in_seconds