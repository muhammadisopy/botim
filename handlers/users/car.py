from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("cars"))
async def cars(msg: types.Message):
    await msg.answer("bizdan qanday mashina olmoqchisiz")
