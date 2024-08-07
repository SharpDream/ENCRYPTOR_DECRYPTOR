def encrypt(cmd_list):
    for letter in cmd_list:
        if letter == ' ':
            count = cmd_list.index(' ')
            cmd_list.remove(' ')
            cmd_list.insert(count, '0')

        elif letter == 'a':
            count = cmd_list.index('a')
            cmd_list.remove('a')
            cmd_list.insert(count, '1')

        elif letter == 'b':
            count = cmd_list.index('b')
            cmd_list.remove('b')
            cmd_list.insert(count, '5')

        elif letter == 'c':
            count = cmd_list.index('c')
            cmd_list.remove('c')
            cmd_list.insert(count, '3')

        elif letter == 'd':
            count = cmd_list.index('d')
            cmd_list.remove('d')
            cmd_list.insert(count, '2')

        elif letter == 'e':
            count = cmd_list.index('e')
            cmd_list.remove('e')
            cmd_list.insert(count, '6')

        elif letter == 'f':
            count = cmd_list.index('f')
            cmd_list.remove('f')
            cmd_list.insert(count, '~')

        elif letter == 'g':
            count = cmd_list.index('g')
            cmd_list.remove('g')
            cmd_list.insert(count, '4')

        elif letter == 'h':
            count = cmd_list.index('h')
            cmd_list.remove('h')
            cmd_list.insert(count, '8')

        elif letter == 'i':
            count = cmd_list.index('i')
            cmd_list.remove('i')
            cmd_list.insert(count, '7')

        elif letter == 'j':
            count = cmd_list.index('j')
            cmd_list.remove('j')
            cmd_list.insert(count, '9')

        elif letter == 'k':
            count = cmd_list.index('k')
            cmd_list.remove('k')
            cmd_list.insert(count, '(')

        elif letter == 'l':
            count = cmd_list.index('l')
            cmd_list.remove('l')
            cmd_list.insert(count, '{')

        elif letter == 'm':
            count = cmd_list.index('m')
            cmd_list.remove('m')
            cmd_list.insert(count, '[')

        elif letter == 'n':
            count = cmd_list.index('n')
            cmd_list.remove('n')
            cmd_list.insert(count, ')')

        elif letter == 'o':
            count = cmd_list.index('o')
            cmd_list.remove('o')
            cmd_list.insert(count, '}')

        elif letter == 'p':
            count = cmd_list.index('p')
            cmd_list.remove('p')
            cmd_list.insert(count, ']')

        elif letter == 'q':
            count = cmd_list.index('q')
            cmd_list.remove('q')
            cmd_list.insert(count, '+')

        elif letter == 'r':
            count = cmd_list.index('r')
            cmd_list.remove('r')
            cmd_list.insert(count, '*')

        elif letter == 's':
            count = cmd_list.index('s')
            cmd_list.remove('s')
            cmd_list.insert(count, '/')

        elif letter == 't':
            count = cmd_list.index('t')
            cmd_list.remove('t')
            cmd_list.insert(count, '-')

        elif letter == 'u':
            count = cmd_list.index('u')
            cmd_list.remove('u')
            cmd_list.insert(count, '^')

        elif letter == 'v':
            count = cmd_list.index('v')
            cmd_list.remove('v')
            cmd_list.insert(count, '@')

        elif letter == 'w':
            count = cmd_list.index('w')
            cmd_list.remove('w')
            cmd_list.insert(count, '#')

        elif letter == 'x':
            count = cmd_list.index('x')
            cmd_list.remove('x')
            cmd_list.insert(count, '!')

        elif letter == 'y':
            count = cmd_list.index('y')
            cmd_list.remove('y')
            cmd_list.insert(count, '$')

        elif letter == 'z':
            count = cmd_list.index('z')
            cmd_list.remove('z')
            cmd_list.insert(count, '%')

        elif letter == 'c':
            count = cmd_list.index('c')
            cmd_list.remove('c')
            cmd_list.insert(count, '&')
        else:
            print(f'"{letter}" is not supported')
