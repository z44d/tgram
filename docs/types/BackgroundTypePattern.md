#🔮 BackgroundTypePattern

**The background is a wallpaper in the JPEG format.**

##⚙️ Properties

- **`type`** (**`str`** ): **Type of the background, always “pattern”**
- **`document`** (**[Document](Document.md)** ): **Document with the pattern**
- **`fill`** (**[BackgroundFill](BackgroundFill.md)** ): **The background fill that is combined with the pattern**
- **`intensity`** (**`int`** ): **Intensity of the pattern when it is shown above the filled background; 0-100**
- **`is_inverted`** (**`bool`** ): **Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only**
- **`is_moving`** (**`bool`** ): **Optional. True, if the background moves slightly when the device is tilted**
