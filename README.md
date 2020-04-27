# Homework for lesson #4, python course spring 2020
## 1 create a project
The idea is to create multiple files project somehow reflecting what's going on in the reality
## 2 Create the hierarchy of classes
With given Student - Lecturer - Worker relationship there were 2 options:
* create superclass Person
## 3. make everything properly working 
Some HW description was not 100% correct, like it is always in Tech Requirements.
Make everything working and usable.
--------------
## 1: תכתבו מחלקות "Employee" "Lecturer" "Student" 
Create classes structure, including **methods**, **getters** and **setters** for the given:

תוסיפו פרמטרים הנדרשים, רצוי שכמה מהם יהיו "פרמטרי פנים" – ללא אפשרות לשינוי ללא פונקציה
תכתבו מטודות – setters  – פונקציות לקביעת ערך הפרמטרים
תכתבו פונקציות לקבלת הפרמטרים

  WORKER | STUDENT | Lecturer 
 --------- | ---------- | ----------- 
First Name | First Name | First Name 
Last name | Last name | Last name
Id | Id | Id   
Address | Address | Address 
Profession | Study year | Study year
Base salary | Courses | Courses they teach
 - | - | Rate per hour

## Rewrite the Person as a base class
You might use this code as a base
`ALSO`
Rewrite the Person class so that a person’s age is calculated for the first time when a new person instance is created, and recalculated (when it is requested) if the day has changed since the last time that it was calculated.

שכתוב מח' Person כך שגילו של האדם תחושב בפעם הראשונה כאשר אובייקט של אדם חדש נוצר, ויחושב מחדש (כשזה מתבקש) ואם היום לא השתנה מאז הפעם האחרונה שהוא היה מחושב.


```python
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age
```
#### main.py MUST contain

```python
person = Person(
    "שירלי",
    "משולם",
    datetime.date(1992, 3, 12), # year, month, day
    "רח' שבי בשקט 13",
    "012 12345678",
    "sh.meshulam@example.com"
)

print(person.name)
print(person.email)
print(person.age())
```

## תמלאו את התוכן של המחלקות, שהתוכנית תכתוב:
Fill up/rewrite the code:

```python
class Person:
    def __init__(self, name: str, surname: str, birth_date: date, address: str, person_id: int, ......
				):
		pass

	@property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    pass

class Student:
    pass

class Lecturer:
    pass

class Worker:
    pass
    	
```
#### main.py better contain
```python   
student1 = Student("Muhammad","Ben-Ami","15","Some street 13 at Some City",('Python','Java'),2020)
student2 = Student("Iris","York","16","Some street 14 at Some City",('Python','C#'),2020)
student1.takes_courses()
student2.takes_courses()

lecturer1 = Lecturer('Whoever','Ben-Zakkai','19','Some addr',('Python','Advanced Algorithms'),2020)

if lecturer1.teaches_something(student1) :
    print(f'{lecturer1.name()} {lecturer1.surname()} teaches {student1.takes_courses_from(lecturer1)}’)

print(f’ {student1.name()} and {student2.name()} study {lecturer1.taught_students(student1, student2)} from {lecturer1.name()}’)
```

#### RESULTING OUTPUT MUST CONTAIN
```
--------
name: Muhammad Ben-Ami; address: Some street 13 at Some City;
 in year 2020 takes courses : Python, Java
--------
name: Iris York; address: Some street 14 at Some City;
 in year 2020 takes courses : Python, C#
--------
Lecturer Whoever Ben-Zakkai
 in year 2020 teaches: 
['Python'] to name: Muhammad Ben-Ami; address: Some street 13 at Some City;
['Python'] to name: Iris York; address: Some street 14 at Some City;
--------
Muhammad Ben-Ami 
Takes:
 - ['Python'] from Whoever Ben-Zakkai
```




 

