from aiogram import Router, F, types
from filters.admin import AdminFilter
from filters.group import GroupFilter
rt = Router()

@rt.message(F.dice, AdminFilter(), GroupFilter())
async def zar(msg: types.Message):
    emoji = msg.dice.emoji
    son = msg.dice.value

    if emoji == "🎲":
        await msg.answer(f"🎲 Tushgan son: {son}")

    elif emoji == "🎳":
        await msg.answer(f"🎳 Tushgan ochko: {son}")