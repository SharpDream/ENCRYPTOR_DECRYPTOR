def decrypt(cmd_list):
    for letter in cmd_list:
        if letter == '0':
            count = cmd_list.index('0')
            cmd_list.remove('0')
            cmd_list.insert(count, ' ')

        elif letter == '1':
            count = cmd_list.index('1')
            cmd_list.remove('1')
            cmd_list.insert(count, 'a')

        elif letter == '5':
            count = cmd_list.index('5')
            cmd_list.remove('5')
            cmd_list.insert(count, 'b')

        elif letter == '3':
            count = cmd_list.index('3')
            cmd_list.remove('3')
            cmd_list.insert(count, 'c')

        elif letter == '2':
            count = cmd_list.index('2')
            cmd_list.remove('2')
            cmd_list.insert(count, 'd')

        elif letter == '6':
            count = cmd_list.index('6')
            cmd_list.remove('6')
            cmd_list.insert(count, 'e')

        elif letter == '~':
            count = cmd_list.index('~')
            cmd_list.remove('~')
            cmd_list.insert(count, 'f')

        elif letter == '4':
            count = cmd_list.index('4')
            cmd_list.remove('4')
            cmd_list.insert(count, 'g')

        elif letter == '8':
            count = cmd_list.index('8')
            cmd_list.remove('8')
            cmd_list.insert(count, 'h')

        elif letter == '7':
            count = cmd_list.index('7')
            cmd_list.remove('7')
            cmd_list.insert(count, 'i')

        elif letter == '9':
            count = cmd_list.index('9')
            cmd_list.remove('9')
            cmd_list.insert(count, 'j')

        elif letter == '(':
            count = cmd_list.index('(')
            cmd_list.remove('(')
            cmd_list.insert(count, 'k')

        elif letter == '{':
            count = cmd_list.index('{')
            cmd_list.remove('{')
            cmd_list.insert(count, 'l')

        elif letter == '[':
            count = cmd_list.index('[')
            cmd_list.remove('[')
            cmd_list.insert(count, 'm')

        elif letter == ')':
            count = cmd_list.index(')')
            cmd_list.remove(')')
            cmd_list.insert(count, 'n')

        elif letter == '}':
            count = cmd_list.index('}')
            cmd_list.remove('}')
            cmd_list.insert(count, 'o')

        elif letter == ']':
            count = cmd_list.index(']')
            cmd_list.remove(']')
            cmd_list.insert(count, 'p')

        elif letter == '+':
            count = cmd_list.index('+')
            cmd_list.remove('+')
            cmd_list.insert(count, 'q')

        elif letter == '*':
            count = cmd_list.index('*')
            cmd_list.remove('*')
            cmd_list.insert(count, 'r')

        elif letter == '/':
            count = cmd_list.index('/')
            cmd_list.remove('/')
            cmd_list.insert(count, 's')

        elif letter == '-':
            count = cmd_list.index('-')
            cmd_list.remove('-')
            cmd_list.insert(count, 't')

        elif letter == '^':
            count = cmd_list.index('^')
            cmd_list.remove('^')
            cmd_list.insert(count, 'u')

        elif letter == '@':
            count = cmd_list.index('@')
            cmd_list.remove('@')
            cmd_list.insert(count, 'v')

        elif letter == '#':
            count = cmd_list.index('#')
            cmd_list.remove('#')
            cmd_list.insert(count, 'w')

        elif letter == '!':
            count = cmd_list.index('!')
            cmd_list.remove('!')
            cmd_list.insert(count, 'x')

        elif letter == '$':
            count = cmd_list.index('$')
            cmd_list.remove('$')
            cmd_list.insert(count, 'y')

        elif letter == '%':
            count = cmd_list.index('%')
            cmd_list.remove('%')
            cmd_list.insert(count, 'z')
        else:
            print(f'"{letter}" is not supported')
