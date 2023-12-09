def locateValue(text: str) -> int:
    nums = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }
    w = ''
    value = []
    
    for x in text:
        if w in nums:
            value.append(str(nums[w]))
            break
        elif x.isdigit() == True:
            value.append(x)
            break
        else:
            w = w + x

    w = ''

    for y in text[::-1]:
        if w.strip() in nums:
            value.append(str(nums[w.strip()]))
            break
        if y.isdigit() == True:
            value.append(y)
            break
        else:
            w = y + w 
    
    print(value)
    
    return int(value[0] + value[1])

if __name__ == '__main__':
    values = list()

    with open("test.txt", "r") as file:
        for line in file:
            values.append(locateValue(line))

        calibrationSum = sum(values)
        print(calibrationSum)