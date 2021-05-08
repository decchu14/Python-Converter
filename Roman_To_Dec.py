tallies = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def RomanNumeralToDecimal(RomanNumeral):
    sum = 0
    for i in range(len(RomanNumeral)-1):
        left = RomanNumeral[i]
        right = RomanNumeral[i+1]

        if(tallies[left] > tallies[right]):
            sum = sum + tallies[left]
        else:
            sum = sum - tallies[left]

    sum = sum+tallies[RomanNumeral[-1]]
    return sum


print(RomanNumeralToDecimal('MDCLXVI'))
