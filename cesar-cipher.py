#!/usr/bin/python
# -*- coding: utf-8 -*-
strs = "abcdefghijklmnopqrstuvwxyzåäö"      #String with swedish character
def shifttext(shift, inp):
    data = []
    for i in inp:
        if i.strip() and i in strs:                 # if the char is not a space ""
            data.append(strs[(strs.index(i) + shift) % 29])
        else:
            data.append(i)           #if space the simply append it to data
    output = ''.join(data)
    print (output);
    return output;
def decipher(inp):
    for i in range(29):
        output = shifttext(int(i), inp);

inp = input('Input encrypted message here: ');
decipher(inp.lower());
