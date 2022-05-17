Twice a week, a challenge is posted on the discord server. This Github repo is to keep track of them.

In each challenge folder, please upload the file with your discord username as the file name. There will be a new folder made for each challenge.

Discord: https://discord.gg/RaV8zjXfJG

## Task 1. The MARIO problem.


The app needs to ask for a imput for high and you have to give generate a mario triangle

for example i give the height as 4 it would print 

```

   #  
  ## 
 ###  
####
 ```
if you want a harder one it would print 
```
   #  #
  ##  ##
 ###  ###
####  ####
```

## Task 2 The Luhn algorithm
**Instructions**

Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

The task is to check if a given string is valid.
Validating a Number

Strings of length 1 or less are not valid. Spaces are allowed in the input, but they should be stripped before checking. All other non-digit characters are disallowed.
Example 1: valid credit card number

`4539 3195 0343 6467`

The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling

`4_3_ 3_9_ 0_4_ 6_6_`

If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:

`8569 6195 0383 3437`

Then sum all of the digits:

`8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80`

If the sum is evenly divisible by 10, then the number is valid. This number is valid!
Example 2: invalid credit card number

`8273 1232 7352 0569`

Double the second digits, starting from the right

`7253 2262 5312 0539`

Sum the digits

`7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57`

57 is not evenly divisible by 10, so this number is not valid.

## Task 3. Word sort
**Instructions**

Given a phrase, count the occurrences of each word in that phrase.

For the purposes of this exercise you can expect that a word will always be one of:

    A number composed of one or more ASCII digits (ie "0" or "1234") OR
    A simple word composed of one or more ASCII letters (ie "a" or "they") OR
    A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")

When counting words you can assume the following rules:

    The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
    The count is unordered; the tests will ignore how words and counts are ordered
    Other than the apostrophe in a contraction all forms of punctuation are ignored
    The words can be separated by any form of whitespace (ie "\t", "\n", " ")

`For example, for the phrase "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled. the count would be:`

```
that's: 1
the: 2
password: 2
123: 1
cried: 1
special: 1
agent: 1
so: 1
i: 1
fled: 1
```

## Task 4. Caesar Cipher

Caesar Cipher
The Caesar cypher shifts the letters that the user imputers but the amount input.
If the original ```
 a b c d e f g h i j k l m n o p q r s t u v w x y z
``` 
Then a shift by 3 should be
``` ```
 d e f g h i j k l m n o p q r s t u v w x y z a b c
```
The user should be able to choose the amount they shift by.

Challenge:
keep the punctuation in place @Pings 


## Task 5 The Reverser! (second super easy second challenge)
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"

Note: punctuation is not checked 



## Task 6 FIZZBUZZ
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

    If the number is a multiple of 3 the output should be "Fizz".
    If the number given is a multiple of 5, the output should be "Buzz".
    If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
    The output should always be a string even if it is not a multiple of 3 or 5.

**Examples**
```
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"

```

## Task 7 Morse 
Create a function that takes a string as an argument and returns the Morse code equivalent.

Examples
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
Help if needed
This dictionary can be used for coding:

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

## Task 8  Convert to Hex
Convert to Hex
Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.

Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
Notes
Each byte must be seperated by a space.
All alpha hex characters must be lowercase.