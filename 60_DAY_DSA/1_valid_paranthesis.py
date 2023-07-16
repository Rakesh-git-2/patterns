arr = ['{','(',')','}','[','{']

hash_keys = {
    '}':'{',
    ']':'[',
    ')':'('
}
stack = []

for i in arr :
    if i in hash_keys.values():
        stack.append(i)
    elif len(stack)>0 and  hash_keys[i] == stack[-1]:
        stack.pop()
if len(stack) > 0 :
    print('invalid paranthesis')
else :
    print('valid paranthesis')

