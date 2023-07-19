from tests import create_folder_if_not_exists,dl_video,get_chat,analyze_kusa_comments,YouTubeVideoTime

id = "Trz-Ur8eRaI"

create_folder_if_not_exists(id)
get_chat(id)
dl_video(id)
top_5_minutes_list = analyze_kusa_comments(id)
youtube_video_time = YouTubeVideoTime()
for item in top_5_minutes_list:
    start_time = youtube_video_time.calculate_time_elapsed(id, item)