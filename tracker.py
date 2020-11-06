#!/usr/bin/env python3
"""Author: Krzysztof Hrybacz <krzysztof@zygtech.pl>"""
"""License: GNU General Public License -- version 3"""

import populartimes, datetime, sys, os
from pathlib import Path

def saveid(placeid):
    api = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
    path = os.path.dirname(os.path.abspath(__file__))
    content = populartimes.get_id(api,placeid)
    if (len(sys.argv) == 1):
        f = open(path + "/places/" + placeid + ".txt", "a")
        d = datetime.datetime.now()
        try:
            f.write(d.strftime("%Y-%m-%d %H") + ": " + str(content["current_popularity"]) + "\n")
        except:
            f.write(d.strftime("%Y-%m-%d %H") + ": N\n")
        f.close()
    else:
        if (sys.argv[1]=="init"):
            if not(Path(path + "/names").is_dir()):
                os.mkdir(path + "/names") 
            if not(Path(path + "/places").is_dir()):
                os.mkdir(path + "/places")
            f = open(path + "/names/" + placeid + ".txt", "w")
            f.write(content["name"] + ' ' + content["address"])
            f.close()

def main():
    saveid("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    saveid("BBBBBBBBBBBBBBBBBBBBBBBBBBB")
    saveid("CCCCCCCCCCCCCCCCCCCCCCCCCCC")
    saveid("DDDDDDDDDDDDDDDDDDDDDDDDDDD")
    saveid("EEEEEEEEEEEEEEEEEEEEEEEEEEE")

if __name__ == '__main__':
    main()
