from sys import argv

nums = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }

# find first digit
def checkFront(text: str) -> str:
    w = '' # string to check substrings of

    for i in text:
        for j in range(len(w)): 
            if w[-j:] in nums: # check every substring for digit
                return str(nums[w[-j:]])

        if i.isdigit() == True: # check if current character is digit
            return i
        else:
            w = w + i # add character to string

# find last digit
def checkBack(text: str) -> str:
    w = '' # string to check substrings of

    for i in text[::-1]:
        for j in range(len(w)):
            if w[:j] in nums: # check every substring for digit
                return str(nums[w[:j]])
            
        if i.isdigit() == True: # check if current character is digit
            return i
        else: 
            w = i + w # add character to string

if __name__ == '__main__':
    cat = list()
    values = list()

    with open(argv[1], "r") as file:
        for line in file:
            value = checkFront(line) + checkBack(line) # concatenate first and last digits to form two digit
            values.append(int(value)) # add value to list to be summed

        calibrationSum = sum(values)
        print(calibrationSum)