#Program to prove (a+b)^2 = a^2 + 2*a*b + b^2

a = input('Enter a number: ')
b = input('Enter another number: ')

def LHS(a,b):
    return (a + b)**2

def RHS(a,b):
    return a**2 + 2*a*b + b**2

print('\nLHS = (a + b)^2 = ({0}+{1})^2 = {2}'.format(a,b,LHS(int(a),int(b))))
print('\nRHS = a^2 + 2*a*b + b^2 = {0}^2 + 2*{0}*{1} + {1}^2 = {2}\n'.format(a,b, RHS(int(a), int(b))))

print('Since LHS = {0} = RHS, \t Hence, proved.'.format(LHS(int(a),int(b))))


