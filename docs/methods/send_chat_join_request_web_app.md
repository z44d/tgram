#🔧 send_chat_join_request_web_app

**Use this method to send a message from a chat join request web app.**

##⚙️ Parameters

- **`chat_id`** (**`int` or `str`** ): **Unique identifier for the target chat or username of the target supergroup
(in the format @supergroupusername)**
- **`user_id`** (**`int`** ): **Unique identifier of the target user**
- **`query_id`** (**`str`** ): **Unique identifier of the query to be answered**
- **`web_app_info`** (**[WebAppInfo](../types/WebAppInfo.md)** ): **Web App information**

##📲 Returns

#### [SentWebAppMessage](../types/SentWebAppMessage.md)

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.send_chat_join_request_web_app(
    chat_id=your_chat_id_here,
    user_id=your_user_id_here,
    query_id=your_query_id_here,
    web_app_info=your_web_app_info_here
)
```
