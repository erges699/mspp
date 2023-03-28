from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
    WebAppInfo,
)
from telegram.ext import ContextTypes

from apps.bot import handlers


async def webapp(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    url: str = "https://flaskrenderer.alexpro2022.repl.co/",
    message_text: str = "Нажмите на кнопку ниже, чтобы заполнить анкету",
    button_text: str = "Заполнить анкету",
) -> None:
    await update.callback_query.answer()
    await update.callback_query.delete_message()
    handlers.USER_DATA = context.user_data
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message_text,
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                button_text,
                web_app=WebAppInfo(url=url),
            )))
