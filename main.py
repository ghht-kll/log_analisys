
from ast import parse
import csv
from lib2to3.pytree import Node
from math import dist
import re
import numpy as np
from heapq import nlargest

tbl = dict()

def add_tbl(item):
    if item in tbl:
        tbl[item] = tbl[item] + 1
    else:
        tbl[item] = 1

def row_parsing(row):
    for item in row:
        match = re.findall(r"tbl_\d{0,}[0-9]", item)
        
        if match != None:
            for i in match:
                result = re.search(r"\d{0,}[0-9]", str(i))
                add_tbl(result.group(0))

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def get_max(count):
    res = nlargest(count, tbl.values())

    for i in res:
        a = get_key(tbl, i)
        print("Таблица: ", a,",  Количество обращений: ", i)

with open('log_week_end.csv', 'r') as log_week_end:
    reader = csv.reader(log_week_end)

    for row in reader:
        row_parsing(row)

get_max(20)