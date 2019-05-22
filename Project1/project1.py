# -*- coding: utf-8 -*-

import requests


# FIXME: put actual code here
def example():
    print('Hello')


def addNumbers(a, b):
    return a + b


def wordCount(book):
    resp = requests.get(book)
    text = resp.text
    words = text.split()
    return len(words)


def writeLigand(PDB_code):
    pdb_file = requests.get('http://www.ebi.ac.uk/pdbe/entry-files/pdb{}.ent'.format(PDB_code.lower()))
    print('http://www.ebi.ac.uk/pdbe/entry-files/pdb{}.ent'.format(PDB_code.lower()))
    text = pdb_file(text)
    line1 = text.splitlines()
    char = line1.split()
    atom = line1.startswith('HETATM')
    print(char[2])
