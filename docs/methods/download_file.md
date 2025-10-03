#🔧 download_file

****

##⚙️ Parameters

- **`file_id`** (**`str`** )
- **`file_path`** (**`str`** ) (`optional`)
- **`in_memory`** (**`bool`** ) (`optional`)

##📲 Returns

#### `Path` or `BytesIO`

##📀 Examples

-🪫 **Required Parameters**

```python
await bot.download_file(
    file_id=your_file_id_here
)
```

-🔋 **All Parameters**

```python
await bot.download_file(
    file_id=your_file_id_here,
    file_path=your_file_path_here,
    in_memory=your_in_memory_here
)
```
