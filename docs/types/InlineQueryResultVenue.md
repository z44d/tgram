#🔮 InlineQueryResultVenue

**Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.**

##⚙️ Properties

- **`latitude`** (**`float`** ): **Latitude of the venue location in degrees**
- **`longitude`** (**`float`** ): **Longitude of the venue location in degrees**
- **`title`** (**`str`** ): **Title of the venue**
- **`address`** (**`str`** ): **Address of the venue**
- **`foursquare_id`** (**`str`** ): **Optional. Foursquare identifier of the venue if known**
- **`foursquare_type`** (**`str`** ): **Optional. Foursquare type of the venue, if known. (For example,
“arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)**
- **`google_place_id`** (**`str`** ): **Optional. Google Places identifier of the venue**
- **`google_place_type`** (**`str`** ): **Optional. Google Places type of the venue. (See supported types.)**
- **`reply_markup`** (**[InlineKeyboardMarkup](InlineKeyboardMarkup.md)** ): **Optional. Inline keyboard attached to the message**
- **`input_message_content`** (**[InputMessageContent](InputMessageContent.md)** ): **Optional. Content of the message to be sent instead of the venue**
- **`thumbnail_url`** (**`str`** ): **Optional. Url of the thumbnail for the result**
- **`thumbnail_width`** (**`int`** ): **Optional. Thumbnail width**
- **`thumbnail_height`** (**`int`** ): **Optional. Thumbnail height**
