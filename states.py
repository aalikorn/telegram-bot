from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    wait = State()
    name = State()
    age = State()
    stop = State()
    email = State()