def logestPalindrome(s) : 
    if len(s) == 1 : return s 
    start = 0 
    max_len = 1 # because string at least one character here 
    for i in range(len(s)) : # iterator element 
        for j in range(2) : # this line code find odd-length and even-length 
            low = i 
            high = i + j  # use algorithem twopointer method 
            while low >= 0 and high < len(s) and s[low] == s[high] : #check panlidrome 
                current_val = high - low + 1 # set value at least 1 
                if current_val > max_len :  # check max val 
                    start = low
                    max_len = current_val
                low -= 1
                high += 1
    return s[start:start+max_len]

s = "babad"
print(logestPalindrome(s))
