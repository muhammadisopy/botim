from aiogram import Router, types, filters

rt = Router()


@rt.message(filters.Command("salom"))
async def salom(msg: types.Message):



    if msg.from_user.first_name :
        ism = msg.from_user.first_name
    else:
        ism = "yoq"
    if msg.from_user.last_name :
        familya = msg.from_user.last_name
    else:
        familya = "yoq"
    if msg.from_user.username :
        username = f"@{msg.from_user.username}"
    else:
        usernamea = "yoq"

    await msg.answer(f"ism  {ism}")
    await msg.answer(f"familiya  {familya}")
    await msg.answer(f"username  {usernamea}")
    await msg.answer(f" username  {username}")
