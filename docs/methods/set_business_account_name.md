#🔧 set_business_account_name

**Changes the first and last name of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`first_name`** (**`str`** ): **The new value of the first name for the business account; 1-64 characters**
- **`last_name`** (**`str`** ) (`optional`): **The new value of the last name for the business account; 0-64 characters**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_business_account_name(
    business_connection_id=your_business_connection_id_here,
    first_name=your_first_name_here
)
```

-🔋 **All Parameters**

```python
await bot.set_business_account_name(
    business_connection_id=your_business_connection_id_here,
    first_name=your_first_name_here,
    last_name=your_last_name_here
)
```
