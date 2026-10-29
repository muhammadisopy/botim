from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("malumot"))
async def malumot(msg: types.Message):
   holat = ""
   if msg.from_user.type == "private":
      holat += "siz lichkamga yozyapsiz!\n"
   else:
      holat += "siz guruhdasiz!\n"
   n = "sizning barcha ma'lumotlaringiz\n"
   n += holat
   n += f"ism: {msg.from_user.first_name}\n"
   n += f"id: {msg.from_user.id}\n"
   f = ""
   if msg.from_user.last_name:
      f += f"{msg.from_user.last_name}"
   else:
      f += "mavjud emas"
   n += f"familya: {f}\n"
   n += f"bu guruh nomi: {msg.from_user.title}\n"
   await msg.answer(n)
