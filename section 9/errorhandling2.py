def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'oops {err}')

    finally:
        print('ok, I am done now')


print(sum(1, 0))
