
my_age = 20
name = "Bohdan"

if my_age < 18 and not name == "Bohdan":  # if - якщо
    print('You allowed')
elif my_age > 18 and not name == "Bohdan:": # elif - або (or)
    print('You are young')
else:
    print('You are not allowed')

#
# if my_age < 18:
#     print('You are not allowed')
# if my_age == 18:
#     print('You are allowed')



#
# if card_number == 1111222233334444 and cvv == 123:  # => if True and False: => if False:
#     print('Trx is completed')
# elif cvv != 123:
#     print("CVV is incorrect!")
# else:
#     print('Trx is canceled')


# if True:
#     print('True')
# #
# if False:  # не буде працювати
#     print('False')
#
#
# # false буде для
bool([])
bool(dict())
bool(tuple())
bool(set())
bool(False)
bool(0)
bool(0.0)
bool('')
#

my_list = {} # bool(my_list) = True


# if not 25:
#     print('Empty')
# #
# #
# # response = []
# # if not response:  # => if not False: => if True:
# #     print('Empty response ')
# #
# # if not bool(response):  # => if not bool([]): => if not False: => if True:
# #     print('Empty response ')
#
# if response["status"] == "success":
#     print("Payment passed")
# elif response["status"] == "pending":
#     print("Payment is pending")
# else:
#     print("Payment failed")
#
# card_number = 1111222233334444
# cvv = 122
#
need_details = True
has_money = True
card_number = 1111222233334442
cvv = 123
# if card_number == 1111222233334444 and cvv == 123:  # => if True and False: => if False:
if card_number == 1111222233334444 and cvv == 123 and has_money:  # => if True and False: => if False:
    print('Trx is completed')

else:
    print('Trx is canceled')

    if not has_money:
        print('You have no money')

    else:
        if need_details: # False

            if card_number != 1111222233334444:
                print('You put wrong card number')

            if cvv != 123:
                print('You put wrong cvv')

        else:

            if card_number != 1111222233334444 or cvv != 123:
                print('smth goes wrong')



