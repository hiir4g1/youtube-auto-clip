from tests import create_folder_if_not_exists,dl_video,get_chat,analyze_kusa_comments,YouTubeVideoTime,CreateClipVideo
id = "LshIhcPr0dk"

def main(id):
    create_folder_if_not_exists(id)
    get_chat(id)
    dl_video(id)
    top_5_minutes_list = analyze_kusa_comments(id)
    youtube_video_time = YouTubeVideoTime()
    creat_clip = CreateClipVideo(id)
    i = 0

    for item in top_5_minutes_list:
        print( str(i)  + '  ' + item)
        i = i + 1
        start_time = youtube_video_time.calculate_time_elapsed(id, item)
        creat_clip.cut_video(start_time)
        
id = "LshIhcPr0dk"
main(id)