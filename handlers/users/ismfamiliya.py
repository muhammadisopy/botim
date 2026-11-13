from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from states.anketa_state import AnketaState
rt = Router()
@rt.message(filters.Command("anketa"))
async def anketa(msg: types.Message, state: FSMContext):
    await msg.answer("ismingizni kiriting: ")
    await state.set_state(AnketaState.ism)

@rt.message(AnketaState.ism)
async def ism(msg: types.Message, state: FSMContext):
    global ism
    ism = msg.text
    await msg.answer(f"{ism} familyangizni kiriting: ")
    await state.set_state(AnketaState.familiya)
    await state.update_data(ism=msg.text)

@rt.message(AnketaState.familiya)
async def familya(msg: types.Message, state: FSMContext):
    await msg.answer(f"{ism} yoshingizni kiriting: ")
    await state.set_state(AnketaState.yoshi)
    await state.update_data(familya=msg.text)

@rt.message(AnketaState.yoshi)
async def yosh(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        await msg.answer("sen haqingda barcha narsani bilaman uhlading nominga kredit olamah hahahaha 🤣🤣🤣🤣")
        await state.update_data(yosh=msg.text)
        data = await state.get_data()
        await state.clear()
        n = "siz haqingizda barcha ma'lumotlar:\n"
        n += f"ism: {data['ism']}\n"
        n += f"familya: {data['familya']}\n"
        n += f"yosh: {data['yosh']}\n"
        await msg.answer(n)
    else:
        await msg.answer("yoshingizni qayta kiriting!")
        await state.set_state(AnketaState.yoshi)
