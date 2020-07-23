from iconarchive import Page, Icon, Pack, IconFormat
import os
import time
import requests

# Replace with icon pack URL.
url = "ICONSET URL"
# Type the format that you want to get the icons in.
icon = IconFormat.ICO

# -----------------------------------------------------

print("IconArchive Pack Downloader by @ysfchn\n")
print("Fetching data, this may take a while...")

# Fetch the icon pack.
iconset = Pack(url, icon)
iconset.fetch()

# Print the icon pack information.
print(iconset.name)
[print(f"page #{iconset.pages.index(page) + 1} -- {len(page.icons)} icons") for page in iconset.pages]
print(f"\n{len(iconset.pages)} pages, {len(iconset.icons)} icons")

# Wait for 5 seconds, then clear the console.
time.sleep(5)
os.system('cls' if os.name=='nt' else 'clear')

# Create a new folder with icon pack name.
folder = iconset.name + " - " + iconset.iconformat.name
os.mkdir(str(folder))

# Start downloading the icons.
for i, icon in enumerate(iconset.icons):
    # Clear the console.
    os.system('cls' if os.name=='nt' else 'clear')
    print("Downloading...")
    print("—————————————————————————————————————————")
    # Calculate the percent.
    percent = round(((i + 1) / len(iconset.icons)) * 100, 3)
    # Print the progress.
    print(f"% {percent} completed - {i + 1} / {len(iconset.icons)}")
    # Download the icon from web.
    r = requests.get(icon.url, allow_redirects = True)
    # Save it to a file.
    open(str(folder) + "/" + icon.filename, 'wb').write(r.content)

# Done
print("Done!")