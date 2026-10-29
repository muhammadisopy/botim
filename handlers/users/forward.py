from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("forward"))
async def forward(msg: types.Message):
    await msg.answer("forward qilindi")
