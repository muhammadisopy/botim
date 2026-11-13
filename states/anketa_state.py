from aiogram.fsm.state import State, StatesGroup

class AnketaState(StatesGroup):
    ism = State()
    familiya = State()
    yoshi = State()