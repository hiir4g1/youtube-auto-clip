from YoutubeAutoClip import create_folder_if_not_exists, dl_video, get_chat, analyze_kusa_comments, YouTubeVideoTime, CreateClipVideo

class VideoProcessor:
    def __init__(self, video_id: str):
        """Initialize VideoProcessor with a specific YouTube video ID.

        Args:
            video_id: A string representing the YouTube video ID.
        """
        self.id = video_id
        self.youtube_video_time = YouTubeVideoTime()
        self.create_clip = CreateClipVideo(video_id)

    def _execute_video_preparation(self):
        """Executes a series of actions to prepare for video analysis and cutting."""
        try:
            create_folder_if_not_exists(self.id)
            get_chat(self.id)
            dl_video(self.id) 
        except Exception as e:
            raise Exception(f"Failed to prepare video {self.id}. Reason: {str(e)}")

    def process_top_comments(self):
        """Analyzes the top comments of the video and cuts the related video segments."""
        try:
            top_5_minutes_list = analyze_kusa_comments(self.id)

            for i, item in enumerate(top_5_minutes_list):
                print(f"{i}  {item}")
                start_time = self.youtube_video_time.calculate_time_elapsed(self.id, item)
                self.create_clip.cut_video(start_time)
        except Exception as e:
            raise Exception(f"Failed to process top comments for video {self.id}. Reason: {str(e)}")

def main(video_id: str):
    """Main function to execute the video processing.

    Args:
        video_id: A string representing the YouTube video ID.
    """
    processor = VideoProcessor(video_id)
    processor._execute_video_preparation()
    processor.process_top_comments()

if __name__ == "__main__":
    video_id = "8dwtgKiSYf4"
    main(video_id)
