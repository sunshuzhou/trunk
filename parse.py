import xml.etree.ElementTree as ET
import json
import subprocess
import sys
import urllib.request
import string
import contextlib
import datetime
import queue
import threading
import time

mesh_terms = {}
mesh_from_title = {}
q = queue.Queue()

name_file = "ab_ti_id_toYH.xml"
input_file = "data/" + name_file
output_file = "output/" + name_file

def main():
    tree = ET.ElementTree(file=input_file)
    n = 0
    e = 0

    with open(output_file, "w") as output:
        for item in tree.iterfind('RECORD'):
            _id = item.findtext('id')
            abstract = item.findtext('abstract')
            output.write(abstract + '\n')


if __name__ == '__main__':
    main()
