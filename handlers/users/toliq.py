from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("toliq"))
async def toliq(msg: types.Message):
   sana = msg.date + datetime.timedelta(hours=5)

   await msg.answer(
       f"yil : {sana.year}\n"
       f"Oy : {sana.month}\n"
       f"kun : {sana.day}\n"
       f"soat : {sana.hour} : {sana.minute}\n"
       f"minut : {sana.minute}\n"
       f"sekund : {sana.second}\n"
   )
