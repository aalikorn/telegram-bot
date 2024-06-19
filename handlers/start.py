from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, PollAnswer, InputMediaPhoto
from markup import menu_button, form_button
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form
from erg import get_photo


router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Form.wait)
    text = "Привет! Перед началом необходимо заполнить небольшую анкету. Нажми на кнопку ниже, чтобы перейти к заполению!"
    await message.answer(text=text, reply_markup=form_button)
    # await bot.send_photo(chat_id=message.chat.id, photo="images/2024-06-15 09.21.52.jpg", caption="Фото")
    # images = ['images/2024-06-15 09.21.52.jpg', 'images/2024-06-15 10.17.37.jpg']
    photo = await get_photo("имя фотографии")
    await message.answer_photo(photo=photo)
    # await message.answer(text="Привет! Нажми на кнопку ниже, чтобы открыть меню", reply_markup=menu_button)
    # question = 'Какой-то вопрос'
    # options = ['вариант 1', 'вариант 2']
    # await message.answer_poll(question=question, options=options, is_anonymous=False)
    # await message.delete()
    images = [InputMediaPhoto(media=await get_photo("")), ]
    await message.answer_media_group(media=images)
    # # await message.answer_location(latitude=55.75350826419063, longitude=48.74339838777191)
    # text = "другой текст `этот текст копируется при нажатии`"
    # await message.answer(text=text, parse_mode='MarkdownV2')

@router.poll_answer()
async def poll_answer(poll_answer: PollAnswer):
    answer_ids = poll_answer.user
    print(answer_ids)





