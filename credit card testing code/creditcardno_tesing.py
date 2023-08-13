card_no = input("Enter a credit card number : ")
if len(card_no) == 13 or len(card_no) == 15 or len(card_no) == 16:
    list1 = []
    q = -1
    for i in list(str(card_no)):
        if q % 2 == 0 :
            list1.append(list(str(card_no))[q])
        q = q-1

    list1_1 = [int(i) * 2 for i in list1]

    list1_2 = []
    for num in range(len(list1_1)):
        for x in str(list1_1[num]):
            list1_2.append(int(x))

    list2 = []
    q2 = -1
    for i2 in list(str(card_no)):
        if q2 % 2 != 0 :
            list2.append(int(list(str(card_no))[q2]))
        q2 = q2-1

    final = list1_2+list2

    print(list1_2)

    # final = list(map(int, new))

    if sum(final) % 10 == 0:
        print("credit card number is correct")

    else:
        print("credit card number is incorrect")
else:
    print("Please enter 13 or 15 or 16 digit credit card number")