# def highest_even(li):
#     highest = 0
#     for item in li:
#         if item > highest:
#             highest = item

#     return highest

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)

    return max(evens)


print(highest_even([1, 2, 3, 4, 5, 8]))
