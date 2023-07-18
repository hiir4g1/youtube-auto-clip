from tests import create_folder_if_not_exists,dl_video,get_chat,analyze_kusa_comments

id = "Trz-Ur8eRaI"

create_folder_if_not_exists(id)
get_chat(id)
dl_video(id)
top_5_minutes_list = analyze_kusa_comments(id)