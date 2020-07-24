'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if length is less than two, it is not a match
    if len(word) < 2:
        return 0

    else:
        # if first two characters are a match
        if word[0:2] == 'th':
            # return 1 + recursive call with substring removing first two letters
            return 1 + count_th(word[2:])
        # if first two characters are not a match
        else:
            # return recursive call with substring removing the first letter
            return count_th(word[1:])