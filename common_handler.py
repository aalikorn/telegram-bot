from aiogram.types import Message
from markup import menu_points, vk_link
from aiogram import Router


router = Router()
data = []


# @router.message()
# async def reply(message: Message):
#     if message.text.lower() in ["меню", "/menu"]:
#         text = "<b>Меню:</b>\n\n1 пункт: описание пункта.\n\n2 пункт: описание пункта.\n\n3 пункт: описание пункта."
#         await message.answer(text=text, reply_markup=menu_points, parse_mode="html")
#     if message.text.lower() == "пункт 1":
#         await message.answer(text="пункт 1 из меню")
#     if message.text.lower() == "пункт 2":
#         await message.answer(text="пункт 2 из меню. нажмите ниже чтобы перейти на сайт", reply_markup=vk_link)
#     if message.text.lower() == "пункт 3":
#         await message.answer(text="пункт 3 из меню")
#     if message.text.lower() == "перейти к анкете":
#         await message.answer(text="Введите имя и фамилию")
#     else:
#         data.append(message.text)


