from aiogram import Router, types, filters
import datetime
rt = Router()
@rt.message()
async def test(msg: types.Message):
   if msg.text == "salom":
      await msg.answer("qalesan")
   elif msg.text == "qalesan":
      await msg.answer("salom")
   elif msg.text == "yahshi":
       await msg.answer("yomon")
   elif msg.text == "yomon":
       await msg.answer("yahshi")
   elif msg.text == "tepa":
       await msg.answer("past")
   elif msg.text == "past":
       await msg.answer("tepa")
   elif msg.text == "aka":
       await msg.answer("uka")
   elif msg.text == "uka":
       await msg.answer("aka")
   elif msg.text == "Backend":
       await msg.answer("Frontend №2 😢")
   elif msg.text == "Frontend":
       await msg.answer("Backend Legendary №1 ☠️")
   else:
      await msg.answer("tushinmadim")
