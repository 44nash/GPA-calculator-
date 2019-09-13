'''
Marcus Nash
44nash@gmail.com
May 16, 2017
'''
def main():
    print('This program will calculate a projected Semester GPA for a given set of courses\n')

    #Collects current data
    gpanow = float(input('Enter your Current GPA:'))
    gpanow = round(gpanow, 2)
    crednow = float(input('Enter total credits earned so far'))
    crednow = round(crednow, 2)

    numCourses = int(input('How many courses are you taking?'))


    courses = []*numCourses
    credit = []*numCourses
    grade = []*numCourses
    earned = []*numCourses

    order = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth']

    def info(x): #Collects details about courses
        if x <= 8 and x>0:#----------------------------------------
            for i in range(x):
                
                
                    course1 = input("%s course name: " % order[i])
                    cred1 = float(input("%s course credit: " % order[i]))
                    grade1 = input("%s projected course grade: " % order[i])
                    
                    grade1 = grade1.upper()
                    
                    if grade1 == "A":
                        a = 4.0*cred1
                        earned.append(a)
                    
                    elif grade1 == "B":
                        b = 3.0*cred1
                        earned.append(b)
                    
                    elif grade1 == "C":
                        c = 2.0*cred1
                        earned.append(c)
                    
                    elif grade1 == "D":
                        d = 1.0*cred1
                        earned.append(d)
                    else:
                        f = 0.0
                        earned.append(f)
                    
                    courses.append(course1) 
                    credit.append(cred1)
                    grade.append(grade1)
        if x>8 or x<1:#---------------------------------
            print("To Many Courses")#------------------------------
            main()
                
               
              
    def gpacalc():
        gpa = earnedCheck()/creditCheck()
        gpa = round(gpa, 2)
        return gpa


    def creditCheck():
        total = 0.0
        for i in range(numCourses):
            total += credit[i]
        return total
        
    def earnedCheck():
        total = 0.0
        for i in range(numCourses):
            total += earned[i]
        return total
        
    def ovrgpa():
        if numCourses <=8 and numCourses >0:#----------------------------------
            print("\n\n           Total      Letter\n")
            print("Course     Credits     Grade \n")    
            print("------     -------     ----- \n")
            
            for i in range(numCourses):
                print('%s          %s        %s' % (courses[i], round(credit[i], 2), grade[i]))
            print('\nProjected Semester GPA: %s' % gpacalc())
            
            smscred = creditCheck()
            totcred = (crednow + smscred)
            smsgpa = gpacalc()
            totalgpa = (((crednow/totcred)*gpanow) + ((smscred/totcred)*smsgpa))
            totalgpa = round(totalgpa, 2)
            
            print('Projected Overall GPA: %s' % totalgpa)
        else:#------------------------------------------
            print("To Many Courses Try again!!!")#----------------------------




            
    info(numCourses)
    ovrgpa()

    print('\nProgrammed by Marcus Nash on May 16, 2017')

    pause=input('\nPress the Enter key to continue')

main()
