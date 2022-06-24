def kbc(question_list):
    options_list = [["[1]->Jeff Bezos", "[2]->Elon Musk", "[3]->BIll Gates", "[4]->Mukesh Ambani"],["[1]->Facebook","[2]->Instagram","[3]->Twitter","[4]->Whatsapp"],["[1]->Larry Paige,[2]->Yukihiro Matsumoto,[3]->Sundar Pichai,[4]->Guido van Rossum"],["[1]->Tripura","[2]->Goa","[3]->Sikkim","[4]->Nagaland"]]
    solution_list = [2, 1, 4, 3]
    i=0
    count=0
    while i < len(question_list):
        print(question_list[i])
        j = 0
        while j < len(options_list[i]):
            print(options_list[i][j])
            j +=1
        user_option=int(input("enter your number option: "))
        if user_option == solution_list[i]:
            print('congrates')
            count+=1
            if count==1:
                print("1 lakh")
            elif count==2:
                print("4 lakh")
            elif count==3:
                print("7 lakh")
            else:
                print("10 lakh")
        else:
            print("your answer was wrong !!\ncorrest answer is->",solution_list[i])
            break
        i+=1
kbc(question_list = ["Who is the richest man on world? ","Which app is most influential ?","Who designed Python?","Which is the second smallest state in India?"])