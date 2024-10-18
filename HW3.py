def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result
print(computePower(2, 3))



def temperatureRange(readings):
    return (min(readings), max(readings))
print(temperatureRange([15, 14, 17, 20, 23, 28, 20]))



def isWeekend(day):
    return day == 6 or day == 7
print(isWeekend(6))


def fuel_efficiency(distance, fuel):
    return distance / fuel
print(fuel_efficiency(70, 21.5))



def decodeNumbers(n):
    last_digit = n % 10
    remaining_digits = n // 10
    return int(str(last_digit) + str(remaining_digits))
print(decodeNumbers(12345))



def find_min_with_for_loop(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val
def find_max_with_for_loops(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val
print(find_min_with_for_loop([2024, 98, 131, 2, 3, 72]))
print(find_max_with_for_loops([2024, 98, 131, 2, 3, 72]))
def find_min_with_while_loop(nums):
    min_val = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    return min_val
def find_max_with_while_loops(nums):
    max_val = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val
print(find_min_with_while_loop([2024, 98, 131, 2, 3, 72]))
print(find_max_with_while_loops([2024, 98, 131, 2, 3, 72]))



def vowel_and_consonant_count(text):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)
text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))
# The homework assignment file says this should output (4, 11) by there are actually eight  v o w e l s  in the sentence... I'm not crazy right?



def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
num = 2468
print(digital_root(num))


