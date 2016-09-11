import yaml
import random
import datetime

with open('Students.yaml','r') as students:
    f1 = yaml.load(students)
    a = f1['Eligible_students']
    b = f1['Ineligible_students']

dict_ineligible = {}
dict_eligible = {}
dict_name_eligible = {}
dict_name_ineligible = {}


def validate(data):
    try:
        datetime.datetime.strptime(data, '%d.%m.%Y')
    except ValueError:
        print ("Incorrect date! It must take this form: DD.MM.YYYY")
        birthday = str(raw_input())

def fit_years(year):
    if year<1986 or year>1998:
        return False
    else:
        return True

def fit_average(average):
    if 1.>average>10.:
        print "The average can be between 1 and 10"
        average = raw_input(float())
    if float(average) > 8.50:
        return True
    else:
        return False


def find():
    while True:
        name = raw_input("Add student name and surname you are looking for:")
        if name == " ":
            print "You have not entered anything"
            find()
        else:
            found_in = None
            for k,v in f1.iteritems():
                if name in v:
                    print name
                    print str(v[name])
                    found_in = k

            if found_in == None:
                print "This student you are looking for does not exist in the database"
                print "Want to add ?"
                answer = raw_input("'Yes' sau 'No'")
                if answer == 'No':
                    answer1 = raw_input("'Enter = exit','A = again'")
                    if answer1 == "":
                        exit()
                    elif answer1 == "A":
                        find()
                else:

                    print "Add birthday for:" + " " + name
                    birthday = str(raw_input())
                    validate(birthday)
                    birthday = datetime.datetime.strptime(birthday,'%d.%m.%Y')
                    year = datetime.datetime.date(birthday).year
                    birthday = datetime.datetime.strftime(birthday,'%d.%m.%Y')
                    fit_years(year)

                    print "Enter the student's admission average"
                    average = raw_input(float())
                    fit_average(average)

                    if fit_years(year) and fit_average(average):
                        dict_eligible['average'] = float(average)
                        dict_eligible['birthday'] = birthday
                        registration_number = random.randint(1000,99999)
                        dict_eligible['registration_number'] = registration_number
                        dict_name_eligible[name] = dict_eligible
                        a.update(dict_name_eligible)
                        print (name + " " + " will be an eligible student.")
                    else:
                        dict_ineligible['average'] = float(average)
                        dict_ineligible['birthday'] = birthday
                        dict_name_ineligible[name] = dict_ineligible
                        b.update(dict_name_ineligible)
                        print (name + " " + " will be an ineligible student.")

                with open('Students.yaml','w') as students:
                    yaml.dump(f1,students,default_flow_style=False)
                    students.close()
            else:
                print "This student was found in: ", found_in

find()















