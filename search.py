def binary_search(ord_list, item):
    start_i = 0
    end_i = len(ord_list) - 1
    while start_i < end_i:
        mid_i = (end_i + start_i)//2
        if item == ord_list[mid_i]:
            return True, mid_i
        if item < ord_list[mid_i]:
            end_i = mid_i - 1
        else:
            start_i = mid_i + 1
    return False, -1
# print(binary_search([1,2,3,4,5,6], 3))

