from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("hammasi"))
async def hammasi(msg: types.Message):
   sana = msg.date + datetime.timedelta(hours=5)

   await msg.answer(
       f"{sana.year}, {sana.month}, {sana.day}, {sana.hour}, {sana.minute}, {sana.second}\n"
   )
