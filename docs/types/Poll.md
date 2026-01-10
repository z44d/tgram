#🔮 Poll

**This object contains information about a poll.**

##⚙️ Properties

- **`id`** (**`str`** ): **Unique poll identifier**
- **`question`** (**`String`** ): **Poll question, 1-300 characters**
- **`options`** (**List of [PollOption](PollOption.md)** ): **List of poll options**
- **`total_voter_count`** (**`int`** ): **Total number of users that voted in the poll**
- **`is_closed`** (**`bool`** ): **True, if the poll is closed**
- **`is_anonymous`** (**`bool`** ): **True, if the poll is anonymous**
- **`type`** (**`str`** ): **Poll type, currently can be “regular” or “quiz”**
- **`allows_multiple_answers`** (**`bool`** ): **True, if the poll allows multiple answers**
- **`question_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions**
- **`correct_option_id`** (**`int`** ): **Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.**
- **`explanation`** (**`String`** ): **Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters**
- **`explanation_entities`** (**List of [MessageEntity](MessageEntity.md)** ): **Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation**
- **`open_period`** (**`int`** ): **Optional. Amount of time in seconds the poll will be active after creation**
- **`close_date`** (**`int`** ): **Optional. Point in time (Unix timestamp) when the poll will be automatically closed**
