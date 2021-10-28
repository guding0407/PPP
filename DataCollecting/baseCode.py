import requests
from bs4 import BeautifulSoup


def main():
    raw = requests.get("https://tv.naver.com/r")
    html = BeautifulSoup(raw.text, "html.parser")

    clips = html.select("div.inner")

    for i in clips:
        title = i.select_one("dt.title")
        chn = i.select_one("dd.chn")
        hit = i.select_one("span.hit")
        like = i.select_one("span.like")

        print("제목", title.text.strip())
        print("채널명", chn.text.strip())
        print(hit.text.strip())
        print(like.text.strip())
        print("="*50)

    clips = html.select("div.cds")

    for i in clips:
        title = i.select_one("dt.title")
        chn = i.select_one("dd.chn")
        hit = i.select_one("span.hit")
        like = i.select_one("span.like")

        print("제목", title.text.strip())
        print("채널명", chn.text.strip())
        print(hit.text.strip())
        print(like.text.strip())
        print("=" * 50)