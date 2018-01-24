#!/usr/bin/python3
# Copyright (c) 2018 Sascha Strand
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE for the source
# distribution of this software for license terms

# Write a file of somewhat random UUIDs
# Takes two CL params: 
#   the output file name
#   the power of two quantity of UUIDs to generate

import uuid
from sys import argv

t = 2**int(argv[2])

f = open(argv[1], 'w')
d = []
i = 0

while i < t:
    u = str(uuid.uuid4())
    f.write('{}\n'.format(u))
    i +=1
    if i % int(argv[2]) == 0:
        u = list(u)
        temp = u[0]
        u[0] = u[1]
        u[1] = temp
        f.write('{}\n'.format("".join(u)))
        i +=1

print("UUIDs written to file: {}".format(t))

