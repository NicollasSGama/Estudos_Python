def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    least_difference(1, 5, -5)
    4"""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(10, 12, 31))

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

help(least_difference)

print(1, 2, 3, sep='<')

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

help(round)
print(round(3.14159, 2))

# def retornoDuasCasas(num):
#     """Retorna o número digitado mais duas casas decimais deste.
#     >>> retornoDuasCasas(3.14159)
#     3.14"""
#     return round(num, 2)
# print(retornoDuasCasas(25.2564896))
#
# help(retornoDuasCasas)

def return_num(num):
    """
    Retorna o número digitado de acordo com o ndigits:
        -> round(num, -1) retornará na base 10;
        -> round(num, -2) retornará na base 100;
        -> round(num, -3) retornará na base 1000;
        -> e assim por diante.
        --------
        Exemplos:
        --------
        -> print(round(338.424, -2))
           338.000
        -> print(round(2.166.000, -3))
           2.166.000
    """
    return round(num, -2)
print(return_num(222.12341234))
help(return_num)