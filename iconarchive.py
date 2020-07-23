import requests, re, math
from enum import Enum

class IconFormat(Enum):
    PNG_512 = 512
    PNG_256 = 256
    PNG_128 = 128
    PNG_96 = 96
    PNG_72 = 72
    PNG_64 = 64
    PNG_48 = 48
    PNG_32 = 32
    PNG_24 = 24
    PNG_16 = 16
    ICO = -1
    ICNS = -2
    SVG = -3

class Pack():
    def __init__(self, pack : str, iconformat : IconFormat):
        self.pages = []
        self.icons = []
        if pack.startswith("https://iconarchive.com/show/"):
            self.packid = pack.replace("https://iconarchive.com/show/", "").split(".")[0]
        else:
            self.packid = pack.replace(" ", "-").lower()
        self.name = self.packid.replace("-", " ").title()
        self.iconformat = iconformat
        self.url = "https://iconarchive.com/show/" + self.packid + ".html"

    def fetch(self):
        r = requests.get(self.url)
        if (r.status_code != 200) or ("Uups, Page not found..." in r.text.split("\n")[4]):
            raise Exception("Error, check your connection and URL.")
            exit(1)
        iconcount = int(r.text.split("\n")[4].split(" icons) | ")[0].split("(")[1])
        pagecount = math.ceil(iconcount / 50)
        for i in range(pagecount):
            page = Page(f"https://iconarchive.com/show/{self.packid}.{i + 1}.html", self)
            self.pages.append(page)

class Page():
    def __init__(self, url : str, pack : Pack):
        self.url = url
        self.icons = []
        self.pack = pack
        r = requests.get(url)
        if r.status_code == 200:
            for u in self.parse_links(r.text):
                icon = Icon(u, self, self.pack)
                if icon not in self.icons:
                    self.icons.append(icon)
                    self.pack.icons.append(icon)
        else:
            raise Exception("Error, check your connection and URL.")
            exit(1)

    def parse_links(self, text : str):
        links = []
        if self.pack.iconformat.name.startswith("PNG"):
            l = re.findall('http[s]?://icons\.iconarchive\.com/icons/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.png', text)
            links = list(set(link.replace("/128/", f"/{self.pack.iconformat.value}/") for link in l))
        else:
            l = re.findall('/download/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.' + self.pack.iconformat.name.lower(), text)
            for link in l:
                links.append("https://iconarchive.com" + link)
        return links

class Icon():
    def __init__(self, url : str, page : Page, pack : Pack):
        self.url = url
        ext = self.url.split(".")[len(self.url.split(".")) - 1]
        self.filename = self.url.split("/")[len(url.split("/")) - 1].replace("-"," ").split(".")[0].title() + "." + ext
        if ext.upper() == "PNG":
            self.iconformat = IconFormat[ext.upper() + "_" + self.url.replace("https://icons.iconarchive.com/icons/", "").split("/")[2]]
        else:
            self.iconformat = IconFormat[ext.upper()]
        self.page = page
        self.pack = pack



