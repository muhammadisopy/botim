from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from states.anceta_state import AnketaState

rt = Router()


@rt.message(filters.Command("mashina"))
async def mashina(msg: types.Message, state: FSMContext):
    await msg.answer("Mashinangiz nomini kiriting:")
    await state.set_state(AnketaState.mashina_nomi)


@rt.message(AnketaState.mashina_nomi)
async def mashina_nomi(msg: types.Message, state: FSMContext):
    await state.update_data(mashina_nomi=msg.text)

    await msg.answer("Mashinangiz rangini kiriting:")
    await state.set_state(AnketaState.mashina_rangi)


@rt.message(AnketaState.mashina_rangi)
async def mashina_rangi(msg: types.Message, state: FSMContext):
    await state.update_data(mashina_rangi=msg.text)

    await msg.answer("Mashinangiz yilini kiriting:")
    await state.set_state(AnketaState.mashina_yili)


@rt.message(AnketaState.mashina_yili)
async def mashina_yili(msg: types.Message, state: FSMContext):

    if msg.text.isdigit():
        await state.update_data(mashina_yili=msg.text)

        data = await state.get_data()

        n = "Sizning mashinangiz haqida ma'lumotlar:\n"
        n += f"Mashina nomi: {data['mashina_nomi']}\n"
        n += f"Mashina rangi: {data['mashina_rangi']}\n"
        n += f"Mashina yili: {data['mashina_yili']}\n"

        await msg.answer(n)

        await state.clear()

    else:
        await msg.answer("Mashinangiz yilini qayta kiriting!!!")