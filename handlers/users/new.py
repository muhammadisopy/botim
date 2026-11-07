from aiogram import Router, types
from filters.group import GroupFilter
rt = Router()
@rt.message(GroupFilter())
async def new(msg: types.Message):
    if msg.new_chat_members:
        user = msg.new_chat_members[0]
        user2 = msg.from_user
        if user.first_name == user2.first_name:
            await msg.reply(f"{user.first_name} o'zi qo'shildi!")
        else:
            n = f"{user.first_name} xush kelibsiz!\n"
            n += f"Sizni {user2.first_name} qo'shdi"
            await msg.reply(n)