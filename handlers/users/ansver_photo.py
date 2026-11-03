from aiogram import Router, filters, types
from filters.admin import AdminFilter
rt = Router()
@rt.message(filters.Command("answer_photo"), AdminFilter())
async def answer_photo(msg: types.Message):
    await msg.answer_photo("https://en.wikipedia.org/wiki/The_Amazing_Spider-Man_%28film%29", caption="bu o'rgimchak odam rasmi")
    await msg.answer("bu answer_photo")
