# Word Composition Problem

About Program :-
This program identifies the longest and second longest compounded words from a given list of alphabetically sorted words.

# Design Decisions & Approach:
> I utilized a Set for word storage, because checking the existence of a word in a set is significantly faster than lists.
> My logic uses a recursive approch along with memoization, where the recursive function is used to break down a word into potential prefix and sufix, where as memorization is there to optimize the recursive process by preventing the program from re-calculating the same word segments multiple times, reducing the execution time. 
>I have used time.perf_counter() to measure execution time because it is best suited for performance measurement.

# Steps to Execute:
1. Python version - 3.14.0
2. File Setup: Update the path to the input file in the main.py by changing the variable "File_Path".
3. Result: Run the code, the result will be shown in the terminal showing longest and second longest compounded words and execution time.