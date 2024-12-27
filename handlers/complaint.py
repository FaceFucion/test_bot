from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.context import FSMContext
from config import database

opros_router = Router()

class Opros(StatesGroup):
    name = State()
    contacts = State()
    report = State()

@opros_router.message(Command("/opros"), default_state)
async def start_opros(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(Opros.name)

@opros_router.message(Opros.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Напишите свои контакты, пожалуйста (номер телефона или аккаунт в соцсетях).")
    await state.set_state(Opros.contacts)

@opros_router.message(Opros.contacts)
async def process_contacts(message: types.Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    await message.answer("Оставьте свою жалобу!")
    await state.set_state(Opros.report)

@opros_router.message(Opros.report)
async def process_report(message: types.Message, state: FSMContext):
    await state.update_data(report=message.text)
    await message.answer("Спасибо за пройденный опрос!")
    data = await state.get_data()
    await state.clear()
    database.save_survey(data)
