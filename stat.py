#!/usr/bin/env python
"""Author: Krzysztof Hrybacz <krzysztof@zygtech.pl>"""
"""License: GNU General Public License -- version 3"""

import populartimes, datetime, sys

def saveid(placeid):
    api = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
    content = populartimes.get_id(api,placeid)
    if (sys.argv[1]=="init"):
        f = open("names/" + placeid + ".txt", "w")
        f.write(content["name"] + ' ' + content["address"])
    else:
        f = open("places/" + placeid + ".txt", "a")
        d = datetime.datetime.now()
        try:
            f.write(d.strftime("%Y-%m-%d %H") + ": " + str(content["current_pop$
        except:
            f.write(d.strftime("%Y-%m-%d %H") + ": N\n")
    f.close()

def main():
    saveid("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    saveid("BBBBBBBBBBBBBBBBBBBBBBBBBBB")
    saveid("CCCCCCCCCCCCCCCCCCCCCCCCCCC")
    saveid("DDDDDDDDDDDDDDDDDDDDDDDDDDD")
    saveid("EEEEEEEEEEEEEEEEEEEEEEEEEEE")

if __name__ == '__main__':
    main()
