#! /usr/bin/python3
'''
Ég ákvað að gera skriftuna í python þar sem ég hef meiri reynslu af csv vinnslu þar og það er einfaldara. Ég nota
os module sem gerir mig kleift að keyra skipanir beint í cli.
'''

import os  # Þetta module gerir mig kleift að keyra linux skipanir
import csv # Sérstakt library til að vinna með csv skrám

# Hér opna ég user skránna í read mode og með utf-8 encoding svo hægt sé að vinna með íslenska stafi.
with open("linux_users.csv", 'r', encoding="utf-8") as file:
    # Hér eru allar línurnar settar í lista inn í lista þar sem , skilir á milli færsla.
    reader = list(csv.reader(file, delimiter=","))
    # Hér er farið í gegnum alla notendurnar.
    for info in reader[1:]:
        # Notandinn er búinn til með home directory, fullt nafn, grúppu og id.
        os.system(f"useradd -m -c \"{info[0]}\" -g {info[5]} {info[6]} {info[3]}")
        # Output to terminal: useradd -m -c "test testsson" -g testgroup -u 291 test

        # Hérna kom upp skrýtið vandamál. Ég ætlaði að nota flókna mkdir skipun sem væri t/{t1 t2} eða eitthvað en sama
        # hvað ég reyndi þá virkaði það ekki. Svo ég endaði á því að skipta einfaldlega um möppu og gera þessa einföldu
        # skipun
        os.chdir("/home/"+info[3])
        os.system("sudo mkdir Documents Downloads Desktop Music Pictures Public Templates Videos")