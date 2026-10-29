from aiogram import Router, types
rt = Router()
@rt.message()
async def test(msg: types.Message):
    await msg.answer(str(msg.text))
