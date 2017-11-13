def list_sum(num_list):
    '''Sum all the number in num_list
    Refer to Chapter 4.2.1'''
    if len(num_list) == 1:
        return num_list[0]
    return num_list.pop() + list_sum(num_list)


def to_str(n, base):
    '''convert any integer to the given base format
    Refer tp Chapter 4.2.3'''
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    return to_str(n//base, base) + convert_string[n%base]

print(to_str(487, 8))
print(to_str(98784, 16))

