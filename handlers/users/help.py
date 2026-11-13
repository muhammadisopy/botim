from aiogram import Router, filters, types
from filters.group import GroupFilter
from filters.admin import AdminFilter
rt = Router()
@rt.message(filters.Command("help"), GroupFilter(), AdminFilter())
async def help(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman")
    n = "mendagi barcha kamandalar:\n"
    n += "/start\n"
    n += "/anketa\n"
    await msg.answer(n)
