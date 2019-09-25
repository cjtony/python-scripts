import sys as sistem
import time

flag_pro = True

print("\n********** PROGRAM LOADED **********")

while flag_pro == True:
    print("\n ***** SELECT AN OPTION ***** \n")
    print("A). Number greater than two numbers.\nB). Number greater than three numbers.\nC). Length of a list.\nD). Character is vowel?\nE). Sum and multiplication of numbers in a list.\nF). Reverse chain.\nG). Palindromas words.\nH). Superposition of two lists.\nI). Generate characters.\nJ). Procedure histogram.\nXC). Exit the program.\n")

    option = str(input("Write the option: "))


    def max_two_numbers(nO, nT):
        if nO > nT:
            print(" \n** The number: " + str(nO) + " is greater than: " + str(nT) + " **")
        elif nT > nO:
            print(" \n** The number: " + str(nT) + " is greater than: " + str(nO) + " **")
        else:
            print(" \n** The numbers are equal" + " **")

    def max_three_numbers(nO, nT, nE):
        if nO > nT and nO > nE:
            print(" \n** The number: " + str(nO) + " is greater than the number: " + str(nT) + " y " + str(nE) + " **")
        elif nT > nO and nT > nE:
            print(" \n** The number: " + str(nT) + " is greater than the number: " + str(nO) + " y " + str(nE) + " **")
        elif nE > nO and nE > nT:
            print(" \n** The number: " + str(nE) + " is greater than the number: " + str(nO) + " y " + str(nT) + " **")
        else:
            print(" \n** The numbers are equal")

    list_fruits = ['Apple', 'Cherry', 'Strawberry', 'Orange', 'Mango', 'Pear', 'Lemon']

    def lenght_list():
        cont = 0
        for i in list_fruits:
            cont += 1
        return cont

    def character_vowel(character):
        list_character = ['a','e','i','o','u','A','E','I','O','U']
        flag = False
        for ch in list_character:
            if character == ch:
                flag = True
        return flag

    def sum_numbers_in_a_list(list_numbers):
        value_sum = 0
        for sn in list_numbers:
            value_sum += sn
        return value_sum

    def mul_numbers_in_a_list(list_numbers):
        value_mul = 1
        for sm in list_numbers:
            value_mul *= sm
        return value_mul

    def reverse_chain(chain):
        inverse = ''
        count = len(chain)
        index = -1
        while count >= 1:
            inverse += chain[index]
            index = index + (-1)
            count -= 1
        return inverse

    def palindromas_word(word):
        flag = False
        word_inverse = reverse_chain(word)
        index = 0
        count = 0
        for i in range(len(word)):
            if word_inverse[index] == word[index]:
                index += 1
                count += 1
            else:
                break
        if count == len(word):
            flag = True
        return flag
    
    def superposition_list(listOne, listTwo):
        flag = False
        for i in listOne:
            for x in listTwo:
                if i == x:
                    flag = True
        return flag
    
    def generate_characteres(character, length):
        char = length * character
        return char

    def procedure_histogram(listSend):
        for i in listSend:
            print(i * "x")

    if option == 'A' or option == 'a':
        numberOne = int(input("Write the first number: "))
        numberTwo = int(input("Write the second number: "))
        max_two_numbers(numberOne, numberTwo)
    elif option == 'B' or option == 'b':
        numberOne = int(input("Write the first number: "))
        numberTwo = int(input("Write the second number: "))
        numberThr = int(input("Write the third number: "))
        max_three_numbers(numberOne, numberTwo, numberThr)
        #Second option
        #print("The number max is: " + str(max(numberOne, numberTwo, numberThr)))
    elif option == 'C' or option == 'c':
        print("The length of our list is: "+ str(lenght_list()) +". Fruits on the list: ")
        for fruit in list_fruits:
            print(str(fruit)+".")
    elif option == 'D' or option == 'd':
        character = str(input("Write a character: "))
        flag = character_vowel(character)
        if flag:
            print("The character: " + character + " it's a vowel.")
        else:
            print("The character: " + character + " it's not a vowel.")
    elif option == 'E' or option == 'e':
        list_numbers = [1,2,3,4]
        value_sum = sum_numbers_in_a_list(list_numbers)
        value_mul = mul_numbers_in_a_list(list_numbers)
        print(" \n** The result of the sum of the numbers on the list is: " + str(value_sum) + ".")
        print(" \n** The result of the multiplication of the numbers in the list: " + str(value_mul) + ".")
    elif option == 'F' or option == 'f':
        chain = str(input("Write a string: "))
        chain_reverse = reverse_chain(chain)
        print("The inverse to the chain " + chain + " is: " + str(chain_reverse) + ".")
    elif option == 'G' or option == 'g':
        word = str(input("Write a word: "))
        word_res = palindromas_word(word)
        if word_res:
            print("The word " + word + " it's palindroma")
        else:
            print("The word " + word + " it's not palindroma")
    elif option == 'H' or option == 'h':
        listOne = [0,93,7,8,101,23]
        listTwo = [2,9,22,4,10,24]
        result_super = superposition_list(listOne, listTwo)
        print("\n**Numbers of the list one: ")
        for i in listOne:
            print(i, end=" ")
        print("\n**Numbers of the list two: ")
        for x in listTwo:
            print(x, end=" ")
        if result_super:
            print("\n\nIn both lists there is at least an equal number")
        else:
            print("\n\nThere are no equal numbers in the lists")
    elif option == 'I' or option == 'i':
        character = str(input("Write a character: "))
        length = int(input("Write the length: "))
        res_gen = generate_characteres(character, length)
        print("Characters generated: "+str(res_gen) + " the " + character + " and length " + str(length))
    elif option == 'J' or option == 'j':
        listSend = [2,3]
        print("\nOur list:")
        for i in listSend:
            print(i, end=" ")
        print("\nThe result:")
        print(str(procedure_histogram(listSend)))
    elif option == 'XC' or option == 'xc':
        print("\n********** PROGRAM FINISHED **********")
        sistem.exit()
    else:
        print("\nThe option you selected is not available...\n")
        print("********** PROGRAM FINISHED **********")
        sistem.exit()