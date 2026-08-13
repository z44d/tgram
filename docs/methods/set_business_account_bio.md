#🔧 set_business_account_bio

**Changes the bio of a managed business account.**

##⚙️ Parameters

- **`business_connection_id`** (**`str`** ): **Unique identifier of the business connection**
- **`bio`** (**`str`** ) (`optional`): **The new value of the bio for the business account; 0-140 characters**

##📲 Returns

#### `bool`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.set_business_account_bio(
    business_connection_id=your_business_connection_id_here
)
```

-🔋 **All Parameters**

```python
await bot.set_business_account_bio(
    business_connection_id=your_business_connection_id_here,
    bio=your_bio_here
)
```
