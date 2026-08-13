#🔧 delete_business_messages

**Deletes messages on behalf of a business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection on behalf of which to delete the messages**
- **`message_ids`** (**List of `int`** ): **A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat.**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.delete_business_messages(
    business_connection_id=your_business_connection_id_here,
    message_ids=your_message_ids_here
)
```
