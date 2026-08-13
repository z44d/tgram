#🔮 ChatBoost

**This object contains information about a chat boost.**

##⚙️ Properties

- **`boost_id`** (**`str`** ): **Unique identifier of the boost**
- **`add_date`** (**`int`** ): **Point in time (Unix timestamp) when the chat was boosted**
- **`expiration_date`** (**`int`** ): **Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged**
- **`source`** (**[ChatBoostSource](ChatBoostSource.md)** ): **Optional. Source of the added boost (made Optional for now due to API error)**
