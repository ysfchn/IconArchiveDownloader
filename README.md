# IconArchiveDownloader

A simple script that downloads a whole icon pack on [iconarchive.com](https://iconarchive.com). Because some packs have not a "download the whole pack" option (as their download links redirects to another sources), this script allows to download the **all** icon packs on IconArchive by searching for pages and downloading the icons one by one. And it does that by parsing the website source.

It supports all sizes and icon formats as same on the website itself, so you can specify the icon format like PNG, ICO, ICNS and SVG.

## Usage
Open `app.py` file, find this line:
```py
# Replace with icon pack URL.
url = "ICONSET URL"
```

And replace it with the icon pack URL, like this:
```py
# Replace with icon pack URL.
url = "https://iconarchive.com/show/papirus-apps-icons-by-papirus-team.html"
```

Lastly, you can specify the icon format;
```py
# Type the format that you want to get the icons in.
icon = IconFormat.PNG_512
```

All icon formats that exists on IconArchive, so you can use any option you want:
```py
# Type the format that you want to get the icons in.
IconFormat.PNG_512
IconFormat.PNG_256
IconFormat.PNG_128
IconFormat.PNG_96
IconFormat.PNG_72
IconFormat.PNG_64
IconFormat.PNG_48
IconFormat.PNG_32
IconFormat.PNG_24
IconFormat.PNG_16
IconFormat.ICO
IconFormat.ICNS
IconFormat.SVG
```

Then execute the `app.py`!

_This project is not affiliated with iconarchive.com_