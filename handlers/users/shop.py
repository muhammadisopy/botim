from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("shops",))
async def shops(msg: types.Message):
    await msg.answer("bizdan qanday narsa olmoqchisiz")
