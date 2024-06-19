from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form
from re import fullmatch
from aiogram.filters import Command
from database import create_profile, edit_profile



router = Router()


@router.message(Form.wait)
async def waiting(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    if message.text.lower() == "перейти к анкете":
        await state.set_state(Form.name)
        text = "Введите имя"
        await message.answer(text=text)
    else:
        text = "Я тебя не понимаю( Нажми на кнопку ниже, чтобы начать заполнять анкету"
        await message.answer(text=text)



@router.message(Form.name)
async def name(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        text = "Отлично! Введите возраст"
        await message.answer(text=text)
    else:
        text = "некорректное имя"
        await message.answer(text=text)
        await state.set_state(Form.stop)


@router.message(Form.age)
async def age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.set_state(Form.email)
        await state.update_data(age=message.text)
        text = "Введи электронную почту"
        await message.answer(text=text)
    else:
        text = "Введи корректный возраст"
        await message.answer(text=text)


@router.message(Form.email)
async def email(message: Message, state: FSMContext):
    if fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)", message.text):
        await state.update_data(email=message.text)
        data_dict = await state.get_data()
        await create_profile(data_dict['id'])
        await edit_profile(data_dict['id'], data_dict['name'], data_dict['age'], data_dict['email'])
        await message.answer(
            "Спасибо, анкета заполнена! Нажмите /menu, чтобы перейти в меню",
        )
    else:
        await message.answer("Введите корректный адрес электронной почты")








