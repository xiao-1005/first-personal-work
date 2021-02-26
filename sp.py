import jieba
import json

txt = open(r"C:\Users\曾秋玉\PycharmProjects\comment\video.txt", 'r', encoding='utf-8').read()
dicts = r"C:\Users\曾秋玉\PycharmProjects\comment\10.txt"
jieba.load_userdict(dicts)
words = jieba.cut(txt)

counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
list_ = []
for i in range(200):
    dict_ = {}
    word ,count = items[i]
    dict_['name'] = word
    dict_['value'] = count
    list_.append(dict_)
print(list_)

with open("all.json" , 'w', encoding='utf-8') as f:
    f.write(json.dumps(list_, indent=2, ensure_ascii=False))