import numpy as np

input = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def shuffle(input):

    np.random.shuffle(input)

    return input

def bubblesort(input):

    input = shuffle(input)
    checked = 0

    while (len(input) - checked) != 0:
        for i in range(len(input) - checked):
            print(input)
            try:
                if input[i] > input[i+1]:
                    input[i], input[i+1] = input[i + 1], input[i] #simultaneous
            except:
                break
        checked += 1

    return input

# A checking algorithm just means you have to
# make more passes through the list!!!

# def bubbleCheck(input, sortedFlag):
#
#     for i in range(len(input) - 1):
#         if (input[i + 1] < input[i]):
#             sortedFlag = False
#             return sortedFlag
#
#     sortedFlag = True
#     return sortedFlag

out = bubblesort(input)
print(out)
