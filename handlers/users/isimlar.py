from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("ismlar"))
async def ismlar(msg: types.Message):
    await msg.answer("Muhammadiso\n"
                     "Miryoqub\n"
                     "Ibrohim\n"
                     "Iskandar")
