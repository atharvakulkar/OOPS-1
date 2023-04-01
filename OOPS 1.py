#!/usr/bin/env python
# coding: utf-8

# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

# In[1]:


A class is a blueprint for creating objects providing initail value for state
and impolementation of behaviour
An object is an instance of a class,created at runtime.
Each object has its own unique set of attributes and operate on that data


# In[ ]:



     
    


# In[11]:


class Car:
  def __init__(self, name, model, year):
    self.name = name
    self.model = model
    self.year = year
    self.odometer_reading = 0
    
  def description(self):
    return f"{self.name} {self.model}, manufactured in {self.year}"

my_car = Car("Toyota", "Camry", 2022)
print(my_car.name) 
print(my_car.model) 
print(my_car.year)
print(my_car.odometer_reading)
print(my_car.description()) 


# In[ ]:


Q2. Name the four pillars of OOPs.

*Encapsulation
*Inheritance
*Polymorphism
*Abstraction


# In[ ]:


Q3. Explain why the init() function is used. Give a suitable example.

The init method is a special method in Python classes that acts as a 
constructor. It is automatically called when an object of the class is 
created.
The init method is used 
to initialize the attributes of the class and set the default values.


# In[12]:


# Example

class Car:
  def __init__(self, name, model, year):
    self.name = name
    self.model = model
    self.year = year
    self.odometer_reading = 0
   

my_car = Car("Toyota", "Camry", 2022)
print(my_car.name) 
print(my_car.model) 
print(my_car.year)


# In[13]:


get_ipython().set_next_input('Q)4Why self is used in OOPs');get_ipython().run_line_magic('pinfo', 'OOPs')

self is a reference to the current instance of the class.
It is used to access the attributes and methods of the class within the class definition

Q5. What is inheritance? Give an example for each type of inheritance.

inheritance is a mechanism in object-oriented programming that allows a new class to be derived from an existing class,
inheriting its attributes and behavior. This is useful for creating new classes that are related to existing classes and

share some of their functionality.

Types of Inheritance

Single Inheritance
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code 
reusability and the addition of new features 


# In[14]:


#example
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()


# In[15]:


Multiple Inheritance:
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
In multiple inheritances, all the features of the base classes are inherited into the derived class.

 


# In[16]:


class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


# In[ ]:




