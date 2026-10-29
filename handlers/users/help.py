from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def help(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman")
    n = "mendagi barcha kamandalar:\n"
    n +="/start\n"
    await msg.answer(n)
