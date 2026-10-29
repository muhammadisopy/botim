from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("copy_to"))
async def copy_to(msg: types.Message):
    await msg.copy_to(8744975719)
    await msg.answer("kopy qilindi")

