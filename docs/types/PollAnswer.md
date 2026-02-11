#🔮 PollAnswer

**This object represents an answer of a user in a non-anonymous poll.**

##⚙️ Properties

- **`poll_id`** (**`str`** ): **Unique poll identifier**
- **`option_ids`** (**List of `int`** ): **0-based identifiers of answer options, chosen by the user. May be empty if the user retracted
their vote.**
- **`voter_chat`** (**[Chat](Chat.md)** ): **Optional. The chat that changed the answer to the poll, if the voter is anonymous**
- **`user`** (**[User](User.md)** ): **Optional. The user, who changed the answer to the poll**
