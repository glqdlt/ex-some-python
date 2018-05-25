def my_function():
    print('wow')


if __name__ == '__main__':
    my_function()
    the_file = open('../ex-some-python.iml')

    for line in the_file:
        print(line)

    print('the_file closing..')
    the_file.close()
