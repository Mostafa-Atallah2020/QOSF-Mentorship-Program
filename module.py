# -*- coding: utf-8 -*-
"""utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cAmuduk5800tJOm9zdHu1O58dr9WXi2t
"""

def find_max(numbers):
  max = numbers[0]
  for number in numbers:
    if number > max:
      max = number
  return max
