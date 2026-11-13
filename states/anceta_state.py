from aiogram.fsm.state import State, StatesGroup

class AnketaState(StatesGroup):
    mashina_nomi = State()
    mashina_rangi = State()
    mashina_yili = State()