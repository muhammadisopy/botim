from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("kun"))
async def kun(msg: types.Message):
   sana = msg.date + datetime.timedelta(hours=5)

   await msg.answer(
       f"kun : {sana.day}\n"
   )
