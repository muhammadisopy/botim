from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("sekund"))
async def sekund(msg: types.Message):
    sana = msg.date + datetime.timedelta(hours=5)

    await msg.answer(
        f" sekund: {sana.second}"
    )