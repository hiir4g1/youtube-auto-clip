from googleapiclient.discovery import build
from typing import List, Dict
import datetime
import json

class YouTubeVideoFetcher:
    def __init__(self):
        """Initializes YouTubeVideoFetcher with a specific developer key.

        Args:
            developer_key: A string representing the developer key.
        """
        with open('./api.json', 'r') as f:
            config = json.load(f)
        api_key = config['api_key']
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def _get_time_threshold(self):
        """Calculates the time threshold for fetching new videos.

        Returns:
            A string representing the time threshold in ISO format.
        """
        time_threshold = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1)
        return time_threshold.isoformat()

    def get_new_youtube_video_list(self, channel_id: str, max_results: int = 10) -> List[Dict[str, str]]:
        """Fetches the list of new YouTube videos from a specific channel.

        Args:
            channel_id: A string representing the YouTube channel ID.
            max_results: An integer representing the maximum number of results to return. Default is 10.

        Returns:
            A list of dictionaries, each containing the ID and title of a new YouTube video.
        """
        time_threshold = self._get_time_threshold()

        response = self.youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=max_results, 
            order="date", 
            publishedAfter=time_threshold,
            type="video"
        ).execute()

        return [{'id': item["id"]["videoId"], 'title': item["snippet"]["title"]} for item in response["items"]]
