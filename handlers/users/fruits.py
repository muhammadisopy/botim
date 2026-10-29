from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("fruits"))
async def fruits(msg: types.Message):
    await msg.answer("olma\n"
                     "banana\n"
                     "uzum")
