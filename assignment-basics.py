# 1 Create 2 variables - 1 with your name and 1 with your age

user_name = input('Enter your name: ')
user_age = input('Enter your age: ')

# 2 Create a function which prints your data as one string


def print_user_data():
    print(user_name + ' - ' + user_age)


print_user_data()

# 3 Create a function which prints ANY (2 arguments) data as one string


def print_any_data(any_data1, any_data2):
    print(any_data1 + ' - ' + any_data2)


print_any_data(user_name, user_age)

# decade calculator


def calculate_decades(age):
    decades_lived = age // 10
    return decades_lived


decades = calculate_decades(int(user_age))
print(decades)
