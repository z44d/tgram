import tgram
import asyncio
from tgram.errors import MutedError, FloodWait


async def check_mute(m: "tgram.types.Message") -> bool:
    storage = m._me.storage

    packet = (m.chat.id, (m.from_user or m.sender_chat).id)
    mute_list = await storage.get_mute_list()

    if packet in mute_list:
        not_deleted = True
        while not_deleted:
            try:
                await m.delete()
                not_deleted = False
            except FloodWait as f:
                if f.value > 25:
                    break
                else:
                    await asyncio.sleep(f.value)
            except Exception:
                break

        return True
    else:
        return False


async def store_user_and_chat_info(update: "tgram.types.Update") -> None:
    chat, user = None, None
    storage = update._me.storage

    for update_object in update.__dict__.values():
        if update_object is None:
            continue

        if not hasattr(update_object, "__dict__"):
            continue

        if all((chat, user)):
            break

        for obj in update_object.__dict__.values():
            if isinstance(obj, tgram.types.User):
                user = obj
                break
            elif isinstance(obj, tgram.types.Chat):
                chat = obj
                break

    if chat:
        await storage.add_chat(chat)

    if user:
        await storage.add_user(user)

    return


async def check_update(update: "tgram.types.Update"):
    storage = update._me and update._me.storage
    is_muted = False
    if not storage:
        return

    if m := update.message:
        is_muted = await check_mute(m)

    await store_user_and_chat_info(update)

    if is_muted:
        raise MutedError()

    return
