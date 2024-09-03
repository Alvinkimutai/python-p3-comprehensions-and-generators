#!/usr/bin/env python3

def return_evens(num_list):
    even_list =[n for n in num_list if n%2 ==0]
    return even_list
    pass

print(return_evens([4,7,9,2,0]))

def make_exclamation(sentence_list):
    string_exclamation = [n+'!' for n in sentence_list]
    return string_exclamation
    pass

print(make_exclamation(["hello", "Hi", "Hello World"]))
