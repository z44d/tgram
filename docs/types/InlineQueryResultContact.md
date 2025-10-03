#🔮 InlineQueryResultContact

**Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.**

##⚙️ Properties

- **`phone_number`** (**`str`** ): **Contact's phone number**
- **`first_name`** (**`str`** ): **Contact's first name**
- **`last_name`** (**`str`** ): **Optional. Contact's last name**
- **`vcard`** (**`str`** ): **Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the contact**
- **`thumbnail_url`** (**`str`** ): **Optional. Url of the thumbnail for the result**
- **`thumbnail_width`** (**`int`** ): **Optional. Thumbnail width**
- **`thumbnail_height`** (**`int`** ): **Optional. Thumbnail height**
