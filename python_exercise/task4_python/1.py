# candidate=[[(id,name,adhar,pan),[designation,experience,email,address,mobile]]]
candidate = [
    [ (2001, 'Rahul', "1234322341", "HQ255234WQ"),
        ["Software Engineer", 3, "rahul@gmail.com", "302022", "9877656723"]],
        [ (2002, 'Tina', "9873452345", "HQ235534WQ"),
        ["Manager", 4, "Tina@gmail.com", "302020", "9878776723"]],
        [ (2003, 'Tanya', "9876752345", "HQ233334WQ"),
        ["Team Lead", 2, "Tanya@gmail.com", "302010", "9898646723"]],
        [ (2004, 'Ram', "9873452309", "HQ238834WQ"),
        ["Manager", 3, "Ram@gmail.com", "302012", "9879895723"]],
        [ (2005, 'Rishav', "945672345", "HQ230034WQ"),
        ["Software Engineer", 5, "Rishav@gmail.com", "302012", "9879879876"]],
        [ (2006, 'Lakshita', "9873458976", "HQ211234WQ"),
        ["Software Engineer", 6, "Lakshita@gmail.com", "302022", "9879874274"]],
        [ (2007, 'Navpreet', "9873452123", "HQ554234WQ"),
        ["Manager", 7, "Navpreet@gmail.com", "302010", "9879872829"]],
        [ (2008, 'Vipul', "9873872345", "HQ774234WQ"),
        ["Associate Developer", 3, "Vipul@gmail.com", "302023", "987957423"]],
        [ (2009, 'Vaibhav', "9873452312", "HQ256234WQ"),
        ["Software Engineer", 4, "Vaibhav@gmail.com", "302014", "9879876723"]],
        [ (2010, 'Janvi', "9873452529", "HQ223754WQ"),
        ["Associate Developer", 8, "Janvi@gmail.com", "302016", "9879876723"]]
]

#1.find list of all manager , software engineers, intern and associate developer
#2.find list of all candidate having experience more than 5.
#3.find list of all cadidate with pin =302012.
#4.update all the emails of employee with company domain name emails.
#5.add a base salary as 10k for managers,20k for software engineers, 5k for associate managers and 4k for interns.


#que1-----------------------
mang_list = list(filter(lambda x : x[1][0] == 'Manager',candidate))
se_list = list(filter(lambda x : x[1][0] == 'Software Engineer',candidate))
teamlead_list = list(filter(lambda x : x[1][0] == 'Team Lead',candidate))
associate_list = list(filter(lambda x : x[1][0] == 'Associate Developer',candidate))
print(mang_list)
print(se_list)
print(teamlead_list)
print(associate_list)

#que2-----------------------
experience_more_than_5=list(filter(lambda x : x[1][1] > 5,candidate))
print(experience_more_than_5)
 
#que3-----------------------
candidate_pin =list(filter(lambda x: x[1][3] =='302012',candidate))
print(candidate_pin)

#que4-------------------------

update_email = lambda emp: (emp[0], [emp[1][0], emp[1][1], emp[1][2].replace("@", "@company"), emp[1][3], emp[1][4]])
candidate_with_company_emails = list(map(update_email, candidate))
print(candidate_with_company_emails )


#que 5-----------------------
Mang_list = list(filter((lambda x:x[1][0]=="Manager"),candidate))

Se_list = list(filter((lambda x:x[1][0]=="Software Engineer"),candidate)) 

Associate_list = list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))

Team_list = list(filter((lambda x:x[1][0]=="Team Lead"),candidate))


l1=[x[1].append("10000") or  x[1] for x in mang_list]
print(l1)
l2=[x[1].append("20000") or  x[1] for x in se_list]
print(l2)
l3=[x[1].append("5000") or  x[1] for x in associate_list]
print(l3)

#Question 6: Find the Highest Salary in all Designations
#------------------------------------
Mang_list = list(filter((lambda x:x[1][0]=="Manager"),candidate))

Se_list = list(filter((lambda x:x[1][0]=="Software Engineer"),candidate)) 

Associate_list = list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))

Team_list = list(filter((lambda x:x[1][0]=="Team Lead"),candidate))

list1=[x[1].append(10000) or  x[1] for x in Mang_list] 

list2=[x[1].append(20000) or  x[1] for x in Se_list] 

list3=[x[1].append(5000) or  x[1] for x in Associate_list]

list4=[x[1].append(12000) or  x[1] for x in Team_list]  

from functools import reduce

max_sal = reduce(lambda x, y : x if x[1][5] > y[1][5] else y  , candidate)
print(max_sal[1][5])
print(max_sal[1][0])

#Question 7: Find the Aggregate of salaries of Managers, Software Engineers, Team Lead and Associate Developer.
Mang_list = list(filter((lambda x:x[1][0]=="Manager"),candidate))

Se_list = list(filter((lambda x:x[1][0]=="Software Engineer"),candidate)) 

Associate_list = list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))

Team_list = list(filter((lambda x:x[1][0]=="Team Lead"),candidate))

list1=[x[1].append(10000) or  x[1] for x in Mang_list] 

list2=[x[1].append(20000) or  x[1] for x in Se_list] 

list3=[x[1].append(5000) or  x[1] for x in Associate_list]

list4=[x[1].append(12000) or  x[1] for x in Team_list]  

print("Aggregate salary of Manager =",(len(Mang_list)*10000))
print("Aggregate salary of Software Engg =",(len(Se_list)*20000))
print("Aggregate salary of Team Lead =",(len(Team_list)*12000))
print("Aggregate salary of Associate Developer =",(len(Associate_list)*5000))

# Question 8: Find all the employees with pincode near by in range +-10. means -> if the input is 302015 then range upto 302005 to 302025 will be filtered.}}


pin = 302012
pin_range = list(filter(lambda x:((int(x[1][3]) > pin - 10) and (int(x[1][3]) < pin + 10)),candidate))
print(pin_range)


# Question 9: Create a Dictionary with Tuple as Key and List[1] as value. }}

dict = { x[0] : x[1] for x in candidate }
print(dict)

#Question 10: Create a Contact Directory where people can search phone numbers through name or ID.

'''x[0][1] picks name
x[0][0] picks id
x[1][4] picks number'''

contact = [([i[0][0],i[0][1],i[1][4]]) for i in candidate]
print(contact)
