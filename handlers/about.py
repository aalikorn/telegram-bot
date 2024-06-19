from aiogram.filters import Command
from aiogram.types import Message
from markup import link_keyboard
from aiogram import Router


router = Router()


@router.message(Command("about"))
async def about(message: Message):
    text = "Информация о боте"
    await message.answer(text=text, reply_markup=link_keyboard)
    await message.delete()