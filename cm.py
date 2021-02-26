import requests
import re
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
}

comment = []
comments = []
cursor = '0'
source = '1614274588872'

for i in range(0, 1000):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor +'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + str(source)
    html = requests.get(url, headers=headers).content.decode()

    comment = re.compile('"content":"(.*?)"', re.S).findall(html)
    comments.append(comment)

    lastId = re.compile('"last":"(.*?)"', re.S).findall(html)[0]
    source = str(int(source) + 1)

with open("video.txt", "w", encoding="utf-8") as f:
    for i in comments:
        for cmt in i:
            f.write(cmt)
            f.write("\n")
print("爬取完成")