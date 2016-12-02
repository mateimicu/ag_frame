#!/usr/bin/env python

fi = open("stuff", "r")

vals = {}


for _ in range(1000/2):
    start = fi.readline().strip()
    finish = fi.readline().strip()
    if finish in vals:
        if start not in vals[finish]:
            vals[finish].append(start)
    else:
        vals[finish] = [start]

# make csv format
for key in vals.keys():
    if not len(vals[key]):
        continue
    l = []
    l.append(key)
    l.extend(vals[key])
    print ", ".join(l)
