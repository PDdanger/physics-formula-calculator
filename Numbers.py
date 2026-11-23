# Numbers.py

# 1. Function to find the sum of a list of numbers
def sum_numbers(numbers):
    return sum(numbers)


# 2. Function to find the average (mean) of a list
def average(numbers):
    if not numbers:
        raise ValueError("The list must not be empty.")
    return sum(numbers) / len(numbers)


# 3. Function to find the median and mode of a list
def median_mode(numbers):
    if not numbers:
        raise ValueError("The list must not be empty.")

    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)

    # Find the median
    if count % 2 == 1:
        median = sorted_numbers[count // 2]
    else:
        middle_right = count // 2
        middle_left = middle_right - 1
        median = (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2

    # Find the mode
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1

    highest_frequency = max(frequencies.values())

    if highest_frequency == 1:
        modes = []
    else:
        modes = [
            number
            for number, frequency in frequencies.items()
            if frequency == highest_frequency
        ]

    return median, modes


# Testing the functions
if __name__ == "__main__":
    numbers = [2, 4, 4, 6, 8]

    print("Sum:", sum_numbers(numbers))
    print("Average:", average(numbers))

    median, modes = median_mode(numbers)
    print("Median:", median)
    print("Mode:", modes)
    