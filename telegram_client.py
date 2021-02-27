import os
from telethon.sync import TelegramClient, events
from tqdm import tqdm

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = "<api_id>"
api_hash = "<api_hash>"
limit = 100  # total de mensajes. No todos tienen media

with TelegramClient('name', api_id, api_hash) as client:
    group_id = -177532564  # pinacoteca
    messages = client.get_messages(group_id, limit=limit)  # limit defaults to 1

    for msg in tqdm(messages):
        # import ipdb, pprint, json; ipdb.set_trace(context=10); pass
        msg.download_media(file=os.path.join('media', str(msg.id)))

        print("\t".join([str(msg.id), str(msg.sender_id), msg.date.isoformat()]))

        # se puede usar para obtener otros conjuntos de docs. ej: todos los links a youtube
        # msg.message
