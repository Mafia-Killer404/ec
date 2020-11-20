# -*- coding: utf-8 -*-
import cchardet as chardet
with open(r"src/tests/samples/wikipediaJa_One_Thousand_and_One_Nights_SJIS.txt", "rb") as f:
    msg = f.read()
    result = chardet.detect(msg)
    print(result)
