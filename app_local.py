import random
from flask import Flask, render_template

# 撰寫 qoute list
qoute_list = [
  '早起的鳥兒有蟲吃',
  '學海無涯, 回頭是岸',
  '休息是為了走更長遠的路',
  '走更遠的路, 是為了休息的更久'
]

# print(random.choice(qoute_list))