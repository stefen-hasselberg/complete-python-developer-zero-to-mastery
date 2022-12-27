# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        user = args[0]
        print('decorater wrapper', user)
        if user['valid']:
            return fn(*args, **kwargs)
        else:
            print("Not Authincated.")

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
