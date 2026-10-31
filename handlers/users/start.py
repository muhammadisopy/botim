from aiogram import Router, filters, types
from filters.group import GroupFilter

rt = Router()
@rt.message(filters.Command("start"), GroupFilter())
async def start(msg: types.Message):
    await msg.answer("assalomu alaykum xurmatli mijoz\n"
                     "sizga yordam kerak bolsa --> /help <-- shu kamandani ustiga bosing")
