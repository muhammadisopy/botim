from aiogram import Router, types
rt = Router()
@rt.message()
async def tajriba(msg: types.Message):
    if msg.entities:
        if msg.entities[0].type in ["url", "type","mention"]:
            await msg.delete()

