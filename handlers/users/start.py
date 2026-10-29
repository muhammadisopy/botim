from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message):
    await msg.answer("xush kelibsiz, xurmatli foydalanuvchi")
    if "salom" in msg.dice:
        "salom"
    else:
        await msg.answer("ma'lumot topilmadi")
