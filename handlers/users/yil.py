from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("yil"))
async def yil(msg: types.Message):
   sana = msg.date + datetime.timedelta(hours=5)

   await msg.answer(
       f"Yil : {sana.year}\n"
   )
