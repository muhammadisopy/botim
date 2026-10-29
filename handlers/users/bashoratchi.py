from aiogram import Router, F, types
import random

rt = Router()

@rt.message(F.dice)
async def bashoratchi(msg: types.Message):
    emoji = msg.dice.emoji
    son = [1, 2, 3, 4, 5, 6]
    random.shuffle(son)

    if emoji == "🎲":
        await msg.answer(f"🎲 100% {son} tushadi")

    elif emoji == "🎳":
        await msg.answer(f"🎳 100%: {son} ta yiqiladi")
