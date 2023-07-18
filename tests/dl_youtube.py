from yt_dlp import YoutubeDL
def dl_video(id):
    video_id = id
    option = {
        'outtmpl' : './output/'+video_id+'/'+video_id+'.%(ext)s',
    }
    with YoutubeDL(option) as ydl:
        result = ydl.download(['https://www.youtube.com/watch?v='+video_id])
    print('download youtube video for ./output/' + video_id)
