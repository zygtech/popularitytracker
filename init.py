#!/usr/bin/env python
"""Author: Krzysztof Hrybacz <krzysztof@zygtech.pl>"""
"""License: GNU General Public License -- version 3"""

import populartimes

def saveid(placeid):
    api = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
    content = populartimes.get_id(api,placeid)
    f = open("names/" + placeid + ".txt", "w")
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
