# -*- coding: utf-8 -*-
"""歡迎使用 Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

score = input().split()

countF = 0
for s in score:
  if int(s) < 60:
    countF += 1
print(countF)