#This is A Voting Machine

import shutil
EVM = "[+] ELECTRONIC VOTING MACHINE [+]"

columns, rows = shutil.get_terminal_size()

resized_EVM = EVM.center(columns)

print(resized_EVM)

import time
print("\n Welcome! \n")
time.sleep (1)

name = input("What is Your Name : ")

try:
    age = int(input("Please Mention Your Age : "))
except ValueError:
    print("Invalid input for age! Please enter a valid age as a number.")
    exit()

if age >= 18:
    time.sleep(1)
    print("\nCongratulations You Are Eligible!!")
    
else:
    time.sleep(1)
    print("Sorry , You Are Not Eligible")
    time.sleep(0.5)
    exit()


time.sleep(0.5)
print("\nGreetings!" , name)
time.sleep(0.5)

print("\nBefore You Can Vote \n We want you To Have Some Knowledge On Voting and Rules Of Voting :-")
time.sleep(2)

print("\n*Voting is a method by which a group, such as a meeting or an electorate, can convene together for the purpose of making a collective decision or expressing an opinion usually following discussions,\ndebates or election campaigns. Democracies elect holders of high office by voting.")
time.sleep(1)


print("\n*The Indian Constitution clearly lays down the eligibility criterion for voting in India. The people who meet the following eligibility criteria can vote in the elections.")
time.sleep(1)

print("\nRULES FOR VOTING :-")
time.sleep(1.5)
print("\n1.You should be an Indian citizen")
time.sleep(0.5)
print("\n2.You must be above 18 years of age")
time.sleep(0.5)
print("\n3.Report The Political Party That Might Be Harrasing or Forcing You To Vote For Them") 
time.sleep(0.5)
print("\n4.A Citizen is not allowed to vote if he/she do not meet the Age Eligibility Criteria For Voting") 
time.sleep(0.5)
print("\n5.You can cast only one vote")
time.sleep(0.5)
print("\n6.You must have Voter ID or EPIC card or photo identity election card")
time.sleep(0.5)
print("\n7.You can vote only at your registered constituency.")
time.sleep(0.5)

try:
    agree_disagree = int(input("\nDo You Agree To The Rules Mentioned Above? \n1.Yes\n2.No\nPress 1 for Yes and 2 For No: "))
except ValueError:
    time.sleep(1)
    print("Invalid input for agreement! Please enter a valid choice as a number.")
    time.sleep(0.5)
    exit()

if agree_disagree == 1:
    time.sleep(1)
    print("\nGreat!!")
elif agree_disagree == 2:
    time.sleep(1)
    print("\nYou Have To Agree to the Rules In Order to Vote!!")
    time.sleep(1)
    agree_disagree_confirmation = print("\nPls Confirm Again If You Agree To the Rules Mentioned Above!!!")
    time.sleep(0.5)
    agree_disagree_confirmation_input = input("\nDo You Agree To The Rules Mentioned Above? \n1.Yes\n2.No\nPress 1 for Yes and 2 For No: ")
    if agree_disagree_confirmation_input == "1":
        print("\nGreat!")
    elif agree_disagree_confirmation_input == "2":
        time.sleep(1)
        print("\nAs You Do Not Agree With the Rules Above, You Are Not Allowed to Vote")
        time.sleep(0.5)
        print("Thank You")
        time.sleep(1)
        exit()
        

time.sleep(1)   
print("\nPolitical Party Voting List :-")
time.sleep(1) 
print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
time.sleep(1)

print("                                                                                          Please Give Vote Acoording to ")
print("                                                                                            SL.no's of the following Political Parties")

try:
    Voting = int(input("\nPlease Vote For Your Preferred Political Party: "))
except ValueError:
    time.sleep(1)
    print("\nInvalid input for voting! Please enter a valid choice as a number.")
    time.sleep(3)
    exit()

if Voting == 1:
    time.sleep(0.5)
    print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        BJP_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if BJP_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        BJP_1 = "Bharatiya Janta Party"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_1 + " "*(border_width+1+len(BJP_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    elif BJP_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            BJP_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if BJP_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_1 + " "*(border_width+1+len(BJP_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif BJP_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_2 + " "*(border_width+1+len(BJP_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BJP_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_3 + " "*(border_width+1+len(BJP_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BJP_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_4 + " "*(border_width+1+len(BJP_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BJP_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_5 + " "*(border_width+1+len(BJP_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BJP_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_6 + " "*(border_width+1+len(BJP_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BJP_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_7 + " "*(border_width+1+len(BJP_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BJP_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BJP_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BJP_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BJP_R_8 + " "*(border_width+1+len(BJP_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()


elif Voting == 2:
    time.sleep(0.5)
    print("\n[+] You Voted For Indian National Congress (INC)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        INC_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if INC_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        INC_1 = "Indian National Congress"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_1 + " "*(border_width+1+len(INC_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    elif INC_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            INC_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if INC_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_1 + " "*(border_width+1+len(INC_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif INC_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_2 + " "*(border_width+1+len(INC_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif INC_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_3 + " "*(border_width+1+len(INC_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif INC_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_4 + " "*(border_width+1+len(INC_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif INC_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_5 + " "*(border_width+1+len(INC_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif INC_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_6 + " "*(border_width+1+len(INC_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif INC_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_7 + " "*(border_width+1+len(INC_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif INC_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            INC_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(INC_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + INC_R_8 + " "*(border_width+1+len(INC_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

elif Voting == 3:
    time.sleep(0.5)
    print("\n[+] You Voted For All India Trinamool Congress (AITC)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        AITC_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if AITC_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        AITC_1 = "All India Trinamool Congress"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_1 + " "*(border_width+1+len(AITC_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    elif AITC_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            AITC_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if AITC_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_1 + " "*(border_width+1+len(AITC_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif AITC_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_2 + " "*(border_width+1+len(AITC_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AITC_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_3 + " "*(border_width+1+len(AITC_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AITC_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_4 + " "*(border_width+1+len(AITC_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AITC_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_5 + " "*(border_width+1+len(AITC_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AITC_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_6 + " "*(border_width+1+len(AITC_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AITC_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_7 + " "*(border_width+1+len(AITC_R_7)%2) + "|")
            print(border)

            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AITC_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AITC_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AITC_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AITC_R_8 + " "*(border_width+1+len(AITC_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

elif Voting == 4:
    time.sleep(0.5)
    print("\n[+] You Voted For Bahujan Samaj Party (BSP)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        BSP_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if BSP_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        BSP_1 = "Bahujan Samaj Party"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_1 + " "*(border_width+1+len(BSP_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    elif BSP_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            BSP_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if BSP_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_1 + " "*(border_width+1+len(BSP_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif BSP_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_2 + " "*(border_width+1+len(BSP_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BSP_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)
            
            BSP_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_3 + " "*(border_width+1+len(BSP_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BSP_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_4 + " "*(border_width+1+len(BSP_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BSP_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_5 + " "*(border_width+1+len(BSP_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BSP_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_6 + " "*(border_width+1+len(BSP_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BSP_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_7 + " "*(border_width+1+len(BSP_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif BSP_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            BSP_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(BSP_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + BSP_R_8 + " "*(border_width+1+len(BSP_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

elif Voting == 5:
    time.sleep(0.5)
    print("\n[+] You Voted For Communist Party of India (CPI)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        CPI_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if CPI_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        CPI_1 = "Communist Party of India"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_1 + " "*(border_width+1+len(CPI_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    
    elif CPI_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            CPI_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if CPI_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_1 + " "*(border_width+1+len(CPI_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif CPI_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_2 + " "*(border_width+1+len(CPI_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif CPI_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_3 + " "*(border_width+1+len(CPI_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif CPI_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_4 + " "*(border_width+1+len(CPI_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif CPI_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_5 + " "*(border_width+1+len(CPI_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif CPI_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_6 + " "*(border_width+1+len(CPI_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif CPI_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_7 + " "*(border_width+1+len(CPI_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif CPI_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            CPI_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(CPI_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + CPI_R_8 + " "*(border_width+1+len(CPI_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

elif Voting == 6:
    time.sleep(0.5)
    print("\n[+] You Voted For Nationalist Congress Party (NCP)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        NCP_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if NCP_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        NCP_1 = "Nationalist Congress Party"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_1 + " "*(border_width+1+len(NCP_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    elif NCP_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            NCP_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if NCP_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_1 + " "*(border_width+1+len(NCP_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif NCP_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_2 + " "*(border_width+1+len(NCP_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NCP_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_3 + " "*(border_width+1+len(NCP_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NCP_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_4 + " "*(border_width+1+len(NCP_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NCP_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_5 + " "*(border_width+1+len(NCP_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NCP_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_6 + " "*(border_width+1+len(NCP_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NCP_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_7 + " "*(border_width+1+len(NCP_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NCP_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NCP_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NCP_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NCP_R_8 + " "*(border_width+1+len(NCP_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

elif Voting == 7:
    time.sleep(0.5)
    print("\n[+] You Voted For National People's Party (NPP)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        NPP_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if NPP_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        NPP_1 = "National People's Party"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_1 + " "*(border_width+1+len(NPP_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    elif NPP_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            NPP_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if NPP_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)
            
            NPP_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_1 + " "*(border_width+1+len(NPP_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif NPP_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_2 + " "*(border_width+1+len(NPP_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NPP_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_3 + " "*(border_width+1+len(NPP_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NPP_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_4 + " "*(border_width+1+len(NPP_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NPP_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_5 + " "*(border_width+1+len(NPP_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NPP_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_6 + " "*(border_width+1+len(NPP_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NPP_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_7 + " "*(border_width+1+len(NPP_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif NPP_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            NPP_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(NPP_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + NPP_R_8 + " "*(border_width+1+len(NPP_R_8)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

elif Voting == 8:
    time.sleep(0.5)
    print("\n[+] You Voted For Aam Aadmi Party (AAP)!!")
    time.sleep(0.5)
    try:
        print("\nAre You Sure You Want To Keep Your Decision Or Change It? : ")
        AAP_Confirmation = int(input("\n1.I Want to Keep It\n2.I Want to Change It\nPlease Enter Your Decision:"))
    except ValueError:
        time.sleep(1)
        print("\nInvalid input for voting! Please enter a valid choice as a number.")
        time.sleep(3)
        exit()
        
    if AAP_Confirmation == 1:
        time.sleep(0.5)
        print("\n==> Your Decision Has Been Saved!!")
        time.sleep(1)

        AAP_1 = "Aam Aadmi Party"
        border_width = 1
        border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_1)+border_width*2+2) + "+"

        print(border)
        print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_1 + " "*(border_width+1+len(AAP_1)%2) + "|")
        print(border)
            
        time.sleep(1)
        print("\n[+] Voting Complete! Thank You!!")
        time.sleep(3)
        exit()
    
    elif AAP_Confirmation == 2:
        time.sleep(0.5)
        print("\nPolitical Party Voting List :-")
        time.sleep(1)
        print("\n 1.Bharatiya Janta Party \n 2.Indian National Congress \n 3.All India Trinamool Congress \n 4.Bahujan Samaj Party \n 5.Communist Party of India \n 6.Nationalist Congress Party \n 7.National People's Party \n 8.Aam Aadmi Party")
        time.sleep(1)
        try:
            AAP_Revoting = int(input("\nPlease Vote For Your Preferred Political Party: "))
        except ValueError:
            time.sleep(1)
            print("\nInvalid input for voting! Please enter a valid choice as a number.")
            time.sleep(3)
            exit()
        if AAP_Revoting == 1:
            print("\n[+] You Voted For Bharatiya Janta Party (BJP)!!")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AAP_R_1 = "Bharatiya Janta Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_1)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_1 + " "*(border_width+1+len(AAP_R_1)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()
        
        elif AAP_Revoting == 2:
            print("\n[+] You Voted For Indian National Congress (INC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AAP_R_2 = "Indian National Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_2)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_2 + " "*(border_width+1+len(AAP_R_2)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AAP_Revoting == 3:
            print("\n[+] You Voted For All India Trinamool Congress (AITC)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AAP_R_3 = "All India Trinamool Congress"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_3)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_3 + " "*(border_width+1+len(AAP_R_3)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AAP_Revoting == 4:
            print("\n[+] You Voted For Bahujan Samaj Party (BSP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AAP_R_4 = "Bahujan Samaj Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_4)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_4 + " "*(border_width+1+len(AAP_R_4)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AAP_Revoting == 5:
            print("\n[+] You Voted For Communist Party of India (CPI)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AAP_R_5 = "Communist Party of India"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_5)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_5 + " "*(border_width+1+len(AAP_R_5)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AAP_Revoting == 6:
            print("\n[+] You Voted For Nationalist Congress Party (NCP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)

            AAP_R_6 = "Nationalist Congress Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_6)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_6 + " "*(border_width+1+len(AAP_R_6)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AAP_Revoting == 7:
            print("\n[+] You Voted For National People's Party (NPP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)
            AAP_R_7 = "National People's Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_7)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_7 + " "*(border_width+1+len(AAP_R_7)%2) + "|")
            print(border)
            
            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()

        elif AAP_Revoting == 8:
            print("\n[+] You Voted For Aam Aadmi Party (AAP)!! ")
            time.sleep(1)
            print("\n==> Your Decision Has Been Saved!!")
            time.sleep(1)
            
            AAP_R_8 = "Aam Aadmi Party"
            border_width = 1
            border = "+" + "-"*(len(name)+border_width*2+2) + "+" + "-"*(len(str(age))+border_width*2+2) + "+" + "-"*(len(AAP_R_8)+border_width*2+2) + "+"

            print(border)
            print("|" + " "*(border_width+1) + "Name: " + name + " "*(border_width+1+len(name)%2) + "|" + " "*(border_width+1) + "Age: " + str(age) + " "*(border_width+1+len(str(age))%2) + "|" + " "*(border_width+1) + "Voted For: " + AAP_R_8 + " "*(border_width+1+len(AAP_R_8)%2) + "|")
            print(border)

            time.sleep(1)
            print("\n[+] Voting Done! Thank You!")
            time.sleep(3)
            exit()