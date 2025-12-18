from aiogram.fsm.state import State, StatesGroup


class FigureState(StatesGroup):
    waiting_filter = State()
    waiting_figure_type = State()


class UploadState(StatesGroup):
    waiting_file = State()
