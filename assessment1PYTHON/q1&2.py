#! /usr/bin/python3
import re


##CMT115 COURSEWORK 2018/19 ###
###############################
##You need to implet the following methods:
##
##Question 1
##anagram_validator()  [15 marks]
##
##Question 2
##credit_card_validator()  [15 marks]

################################

###################################################
# Question 1: Check for anagrams:#
###################################################
def read_anagram(file_name):
    '''
    Input: a file name
    Return: a nested list of two words list
    Example : [[word1,word2],[word3,word4]...etc]
    '''
    anagram=[]
    anagram_list = open('anagram.txt', 'r')
    for line in anagram_list.readlines():
        for i in line.split():
            anagram.append(i.split(','))

    return anagram
    anagram_validator(anagram)


def anagram_validator(anagram):
    '''
    Input is the output from "read_anagram()".
    Return: list of "anagrams" or "Not anagrams" values for each two words
    example input (dog,gdo),(try,elm) then output would be ["anagrams","Not anagrams"] with sequence of the input
    '''
    Anagrams = []

    for i in anagram:
        if(sorted(i[0]) == sorted(i[1])):
            Anagrams.append("Anagrams")
        else:
            Anagrams.append("Not anagrams")
    return  Anagrams




############################################
# Question 2: Validate credit cards         #
############################################
def read_credit_cards(file_name):
    '''
    Input: a file name
    Return tuple of numbers
    '''


    tup=[]
    tup_list = open('credit_cards.txt', 'r')
    for line in tup_list.readlines():
        for i in line.split():
            tup.append(i.split(','))

    for i in tup:
        x = i.replace('[','').replace(']', '')
        tup.append(x)

    numbers = tuple(tup)
    return numbers

    credit_card_validator(tup)

def credit_card_validator(tup):
    '''
    Input: tuple of numbers
    Return:
        dictionary of credit card numbers where key is the number and value if valid or invalid
    '''
   # credit_number = str(credit_number)
    #if
     #   print(len(credit_number))
    vcc=0
    nvcc = 0
    pattern1 = re.compile(r'(\d)\1{3}')
    matches = pattern1.findall(tup)
    for i in matches:
        print(tup)
    pass


def print_credit_card_summary(dict_o):
    '''
    Input: dict
    Return:
        printing summary of validation result - space between credit card and status is 40 width
        example:
        378282246310005		Invalid
        30569309025904		Invalid
    '''
    pass


####### THE CODE BELOW IS FOR TESTING###################
############### DO NOT  CHANGE #########################


import sys

if __name__ == '__main__':
    # Take care of the console inputs
    if len(sys.argv) <= 1:
        sys.argv = ['', "anagram.txt", "credit_cards.txt"]
    stars = '*' * 40
    print(stars)
    print("Testing Question 1 --- Anagrams?")
    print(stars)

    # testing reading_anagrams
    try:
        anagram = read_anagram(sys.argv[1])
        if not anagram:
            print("read_anagram() returns None.")
        else:
            print("anagram: ", anagram)
            print()
    except Exception as e:
        print("Error (readnumbers()): ", e)

    # testing anagram_validator
    Anagrams = 0
    NAnagrams = 0
    try:
        if not anagram:  # Question 1 has not been implemented
            print("anagram_validator() skipped....")
        else:
            result = anagram_validator(anagram)
            if result == None:
                print("anagram_validator() returns None.")
            else:
                for i in result:
                    if i == "Anagrams":
                        Anagrams += 1
                    elif i == "Not anagrams":
                        NAnagrams += 1
                print("Number of valid Anagrams is {} and Not anagrams is {}.".format(Anagrams, NAnagrams))

    except Exception as e:
        print("Error (anagram_validator()):", e)

    # testing  Question 2
    print("\n\n" + stars)
    print("Testing Question 2 --- Credit Card Validator")
    print(stars)

    # Testing reading_credit_cards
    try:
        tup = read_credit_cards(sys.argv[2])
        if not tup:
            print("read_credit_cards() returns None.")
        else:
            print("The tuple of credit_cards: {}".format(tup))
    except Exception as e:
        print("Error (read_credit_cards()):", e)

    # Testing credit_card_validator
    vcc = 0
    ivcc = 0
    try:
        if not tup:  # Readin_Question 2 has not been implemented
            print("credit_card_validator() skipped...")
        else:
            cc_dict = credit_card_validator(tup)
            tmp_cc_dict = cc_dict
            if not cc_dict:
                print("credit_card_validator()  returns None.")
            else:
                for items in cc_dict.keys():
                    if cc_dict[items] == "Valid":
                        vcc += 1
                    elif cc_dict[items] == "Invalid":
                        ivcc += 1
                print("Number of valid credit cards is {} and invalid {}.".format(vcc, ivcc))
    except Exception as e:
        print("Error (credit_card_validator()):", e)

    # testing  Question 2
    print("\n\n" + stars)
    print("Testing Question 2b --- Print Credit Card Summary")
    print(stars)
    # Testing print_credit_card_summary
    try:
        if not tmp_cc_dict:  # Dict credit card output has not been implemented
            print("print_credit_card_summary() skipped...")
        else:
            import io  # do not delete this line
            from contextlib import redirect_stdout  # do not delete this line

            f = io.StringIO()
            with redirect_stdout(f):
                print_credit_card_summary(tmp_cc_dict)
                out = f.getvalue()
            if not out:
                print("print_credit_card_summary()  returns None.")
            else:
                count44 = 0
                count46 = 0
                for line in out.splitlines():
                    if len(line) - len(line.split()) == 44:
                        count44 += 1
                    elif len(line) - len(line.split()) == 46:
                        count46 += 1
                if count44 == vcc and count46 == ivcc:
                    print("Your format looks good")
                else:
                    print("You might have some issues in your summary format")

    except Exception as e:
        print("Error (print_credit_card_summary()):", e)


