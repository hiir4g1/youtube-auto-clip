import pytchat
import time
import csv
# PytchatCoreオブジェクトの取得
#video_id = "Z6-yIwtqerQ"
def get_chat(id):
    video_id = id
    livechat = pytchat.create(video_id = video_id)
    data = []
    while livechat.is_alive():
        # チャットデータの取得
        chatdata = livechat.get()
        
        for c in chatdata.items:
            chat = []
            print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
            chat.append(c.datetime)
            chat.append(c.author.name)
            chat.append(c.message)
            chat.append(c.amountString)
            data.append(chat)
            '''
            JSON文字列で取得:
            print(c.json())
            '''
        #time.sleep(5)

    with open("./output/"+video_id+'/'+video_id + ".csv",mode="w",encoding = "utf-8",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
        
    print("download csv of youtube chat in ./output/" + video_id)