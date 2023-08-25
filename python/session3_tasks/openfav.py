#!/usr/bin/python3

import favUrl


url = int(input("which website you want to open \n1.google \n2.facebook\n3.whatsapp\n4.yts\n5.github\n6.linkedin\n"))

favUrl.openUrl((url-1))