from aiogram import Router, types, F, filters
rt = Router()
students = [
   "AgACAgIAAxkBAAI3UWrgjb0GbY1sUC6pzh7ppGAk_I1mAAIiIGsbM9sJSx9C0h39_EL7AQADAgADdwADPQQ",
   "AgACAgIAAxkBAAI3UmrgjchrUsBfvN1tzxlMecN5bw_CAAIjIGsbM9sJS8XLTvlb1s2gAQADAgADdwADPQQ",
   "AgACAgIAAxkBAAI3U2rgjc7Bli2MFHu3-ezuvuomDqhzAAIkIGsbM9sJS9UPhBoLCWt1AQADAgADdwADPQQ",
]
qoshiqlar = [
   "CQACAgIAAxkBAAI3jWrgkAbNuIO_sSKe5cntmNPTcYEIAAKLBgACdhPgSe0EntNJMpJbPQQ"
]
@rt.message()
async def test(msg: types.Message):
   if msg.contact:
      if msg.contact.user_id == msg.from_user.id:
         await msg.answer("bu sizniki")
      else:
         await msg.answer("iltimos o'zingizni nomeringizni bering")
   if msg.sticker:
      await msg.answer(str(msg.sticker.emoji))
   elif msg.text == "music":
      await msg.answer_audio(qoshiqlar[0])
   # print(msg.photo[-1].file_id)
   if msg.text == "muhammadiso":
      await msg.answer_photo(students[0])
   elif msg.text == "iskandar" or msg.text == "ibrohim":
      await msg.answer_photo(students[1])
   elif msg.text == "miryoqub":
      await msg.answer_photo(students[2])
   else:
      await msg.answer("tur yoqol")
