# 文字コード関連

## 日本語コメントを書きたい時時とか

```python
# -*- coding: utf-8 -*-
```


## とある文字コードとしてファイルを開く

```python
import codecs
f = codecs.open(intro_file, 'r', 'utf-8')
```
