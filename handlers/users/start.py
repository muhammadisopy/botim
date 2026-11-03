from aiogram import Router, filters, types
from filters.group import GroupFilter
from filters.admin import AdminFilter
rt = Router()
@rt.message(filters.Command("start"), GroupFilter(), AdminFilter())
async def start(msg: types.Message):
    await msg.answer("assalomu alaykum xurmatli mijoz\n"
                     "sizga yordam kerak bolsa --> /help <-- ustiga bosing")
