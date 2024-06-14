from types_ import *

print(
    Message(
        1,
        1,
        Chat(1, "s"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hi nigga", web_app=WebAppInfo("t.me/ssss"))
                ]
            ]
        )
    ).to_json()
)