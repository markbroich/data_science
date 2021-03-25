"""
Write a simple regex verifier. The regex patterns to match are a-z (any lowercase character) . * 
Where <dot> stands for any (lowercase) character, and <star> means the previous character 
(lowercase or dot) 0 or more times. 
The regex must match the entire stringing, not a substringing

"""

# ask about: 
# - length of input, length of output, compute time and 
# ram constrains
# ask if return is boolian

# pattern steps can be:
# char
# char*
# char.
# char.*
# char*.
# .
# .*
# and the above in repeated fashion e.g.
# charchar*char.char*


# examples:
# string = a
# pat = a
# ret = 1

# string = a
# pat = b
# ret = 0

# string = a
# pat = .
# ret = 1

# string = a
# pat = a*
# ret = 1

# string = b
# pat = a*
# ret = 0

# string = a
# pat = a.
# ret = 0

# string = aa
# pat = a*
# ret = 1

# string = b ###
# pat = a*b
# ret = 1

# string = aa
# pat = a.
# ret = 1

# string = a
# pat = a.
# ret = 0

# string = aab
# pat = a*bc
# ret = 0


## Observations:
# w/o the *, i can do one pass over arrays 
# at the same time and match either against char or .

# challenge is the *, which means that i 
# - either skip the char* in the pat 
# - or move to the next char in the string

## w/o star brute forth
def regex_matcher_bf(string, pat): # output -- boolean 
    if not pat:  # ran out of pattern? 
        return not string # ran out of string? 
    if string and pat[0] in {string[0], "."}: # still have string and char in pat in string or '.'
        return regex_matcher(string[1:], pat[1:])
    return False

## w star brute forth
def regex_matcher_w_star(string, pat): 
    if not pat:  # ran out of pattern? 
        return not string # ran out of string? 
    #
    firstMatch = string and pat[0] in {string[0], "."} # still have string and char in pat in string or '.'
    if len(pat) >= 2 and pat[1] == '*': 
        # the * can be either ignored by moving the pat by 2 chars or used (if firstmatch) by moving to the next string char
        return regex_matcher(string, pat[2:]) or firstMatch and regex_matcher(string[1:], pat)
    elif firstMatch:
        return regex_matcher(string[1:], pat[1:])
    return False


## w star memo 
def regex_matcher_memo(string, pat, demo=False): 
    memo = {}
    def topDown(i,j):
        if j >= len(pat):  # ran out of pattern? 
            return i >= len(string) # ran out of string? 
        #
        # demo of memo being triggered
        if demo and (i,j) in memo:
            print(i, j, memo[(i,j)])
        # not already known subtree
        if not (i,j) in memo:
            firstMatch = i < len(string) and pat[j] in {string[i], "."} # still have string and char in pat in string or '.'
            if j+1 < len(pat) and pat[j+1] == '*': 
                # the * can be either ignored by moving the pat by 2 chars or used (if firstmatch) by moving to the next string char
                ret = topDown(i,j+2) or firstMatch and topDown(i+1,j) 
            elif firstMatch:
                ret = topDown(i+1,j+1)
            else:
                ret = False
            memo[(i,j)] = ret
        return memo[(i,j)]
    return topDown(0,0)

## demo of memo beeing triggered
print('Memo triggers on the following index combos that reccure:')
print('in string:  mississippi    and')
print('in pattern: mis*s*s*is*b* ')
print('e.g. 3,4:      ||         ')
print('see figure "regex_example_triggering_top_down_dp_speedup.png"')
print('showing that 2,2 split into 2,4 and 3,2')
print('both 2,4 and 3,2 split into 3,4: the overlapping subproblem!')
print('fig kindly provided by Prudhvi Raju. tnx ')
print()
 
string =    'mississippi'
pat =       'mis*s*s*is*b*'
regex_matcher_memo(string, pat, True)
print()



def testing(regex_matcher):
    testcount = 0
    passcount = 0

    string = 'a' 
    pat = 'a'
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    string = 'a' 
    pat = 'ab'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    string = 'ab' 
    pat = 'a'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    string = 'ab' 
    pat = 'a.'
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    string = 'ab.cd' 
    pat = 'ab..d'
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    string = '.b.cd' 
    pat = 'a.cd'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    # expected True
    string = 'mississippi'
    pat = 'mississippi'
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    # expected True (using .)
    string = 'mississippi'
    pat = 'mississ.ppi'
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    # expected False (length unequal)
    string = 'mississippi'
    pat =    'mississipp'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    # expected False () (pat differs)
    string = 'mississippi'
    pat =    'mississipii'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    #expected False () (pat differs)
    string = 'mississippi'
    pat =    'mississippii'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    string =    'mississippi'
    pat =       'mis*s*s*is*b*'
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    string = 'mississippi'
    pat =    'mis*i.*ip*i'
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    string = "mississippi"
    pat =    "mis*is*p*."
    # print(regex_matcher(string, pat) == False)
    passcount += regex_matcher(string, pat) == False
    testcount += 1

    string = "aab"
    pat =    "c*a*b"
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    string = "aa"
    pat =  "a*"
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    string = "ab"
    pat =  ".*"
    # print(regex_matcher(string, pat) == True)
    passcount += regex_matcher(string, pat) == True
    testcount += 1

    print(passcount, 'of', testcount, 'tests passed')

# testing
regex_matcher = regex_matcher_bf
testing(regex_matcher)

regex_matcher = regex_matcher_w_star
testing(regex_matcher_w_star)

regex_matcher = regex_matcher_memo
testing(regex_matcher)









