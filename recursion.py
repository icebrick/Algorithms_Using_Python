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


def rev_str(str):
    '''Return the reverse of given string
    Exercise for Self Check 1 of Chapter 4.2.3'''
    if len(str) == 1:
        return str[0]
    return rev_str(str[1:]) + str[0]

print('-'*20)
print('Test func rev_str:')
print('jayden --> ' + rev_str('jayden'))


def is_palindrome(str):
    '''Check if the input string is a palindrome.
    Exercise for Self Check 2 of Chapter 4.2.3'''
    if len(str) in [0,1]:
        return True
    return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print('-'*20)
print('Test func is_palindrome:')
print('kayak --> ' + str(is_palindrome('livenotonevil')))


###################Visualising Recursion###########################
import turtle
# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len-5)
# draw_spiral(my_turtle, 100)
# my_win.exitonclick()

def tree(branck_len, t):
    if branck_len > 5:
        t.forward(branck_len)
        t.right(20)
        tree(branck_len-15, t)
        t.left(40)
        tree(branck_len-15, t)
        t.right(20)
        t.backward(branck_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    my_win.exitonclick()
main()
