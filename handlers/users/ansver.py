from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("answer"))
async def answer(msg: types.Message):
    await msg.answer("oddiy javob")
    await msg.answer("sizni chatingiz answer bo'ldi")
