#!/usr/bin/python3

import algo

while(True):
    text = input('algo > ')
    result, error = algo.run('<stdin>', text)

    if error: 
        print(error.as_string())
    else:
        print(result)