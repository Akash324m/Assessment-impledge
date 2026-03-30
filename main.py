import time

File_Path = "data/Input_02.txt"   # Change here the file path

def Read_Words(File_Name):                                                      # Read words from file
    with open(File_Name, 'r') as f:
        words = [line.strip() for line in f]
    return words

def Can_Form(word, word_set, memo,org = True):                                  # Main function 
    if word in memo:
        return memo[word]

    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]

        if left in word_set:
            if right in word_set or Can_Form(right, word_set, memo, False):
                memo[word] = True
                return True

    memo[word] = False
    return False

def Find_Compound_Words(words):
    Word_Set = set(words)
    Compound_Words = []
    for word in words:
        Word_Set.remove(word)                                                   # temporarily remove the word to avoid using itself
        mem = {}
        if Can_Form(word,Word_Set,mem):
            Compound_Words.append(word)
        Word_Set.add(word)
    return Compound_Words


start_time = time.perf_counter()                                                # Start Time tracking

words = Read_Words(File_Path)
Compound_Words = Find_Compound_Words(words)

Compound_Words.sort(key=len, reverse=True)                                      # sort by length (descending)
longest = Compound_Words[0] if len(Compound_Words) > 0 else ""
second_longest = Compound_Words[1] if len(Compound_Words) > 1 else ""


end_time = time.perf_counter()
total_time = (end_time - start_time) * 1000

print("-"*(35+len(longest)))                                                    # Results log
print(f"Longest Compound Word:        {longest}")
print(f"Second Longest Compound Word: {second_longest}")
print(f"Time taken:                   {total_time:.2f} ms")
print("-"*(35+len(longest)))