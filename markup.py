from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")]
    ]
)

link_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Телеграм", url="https://t.me/dovuziu")],
        [InlineKeyboardButton(text="Сайт", url="https://dovuz.innopolis.university/")],
        [InlineKeyboardButton(text="информация о курсах", url="https://dovuz.innopolis.university/offline-programms")]
    ]
)

menu_points = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="пункт 1")],
        [KeyboardButton(text="пункт 2")],
        [KeyboardButton(text="пункт 3")]
    ]
)

vk_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="перейти", url="vk.com")]
    ]
)

form_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Перейти к анкете")]
    ]
)
