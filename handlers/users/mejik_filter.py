from aiogram import Router, types, F
rt = Router()
@rt.message(F.photo)
async def mejik_filter(msg: types.Message):
   await msg.answer("siz rasm yubordingiz")

@rt.message(F.animation)
async def mejik_filter(msg: types.Message):
   await msg.answer("siz gif yubordingiz")

@rt.message(F.video)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz video yubordingiz")

@rt.message(F.text)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz text yubordingiz")

@rt.message(F.sticker)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz text yubordingiz")

@rt.message(F.contact)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz contact yubordingiz")

@rt.message(F.dice)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz dice yubordingiz")

@rt.message(F.document)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz document yubordingiz")

@rt.message(F.location)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz locatsiya yubordingiz")

@rt.message(F.venue)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz venue yubordingiz")

@rt.message(F.voice)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz voice yubordingiz")

@rt.message(F.audio)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz audio yubordingiz")

