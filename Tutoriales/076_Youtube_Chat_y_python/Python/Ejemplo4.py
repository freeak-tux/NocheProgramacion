import pytchat
Video_id = "123456"
chat = pytchat.create(video_id=Video_id)
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"Creador: {c.datetime} [{c.author.name}]- url:{c.author.channelUrl} imagen{c.author.imageUrl}")
