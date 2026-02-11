#🔧 set_business_account_username

**Changes the username of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`username`** (**`str`** ) (`optional`): **The new value of the username for the business account; 0-32 characters**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_business_account_username(
    business_connection_id=your_business_connection_id_here
)
```

-🔋 **All Parameters**

```python
await bot.set_business_account_username(
    business_connection_id=your_business_connection_id_here,
    username=your_username_here
)
```
