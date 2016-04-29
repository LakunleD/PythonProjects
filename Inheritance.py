class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent Constructor called"
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        
        print ("Parent Last Name - "+self.last_name)
        print ("Parent Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print "Child Constructor called"
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print ("Last Name - "+self.last_name)
        print ("Eye Color - "+self.eye_color)
        print ("Number of toys - "+str(self.number_of_toys))


billy_cyrus = Parent("Dos", "white")

billy_cyrus.show_info()

##print billy_cyrus.last_name
##
milly_cyrus = Child("Kunle", "brown", 5)
##print milly_cyrus.last_name
##print milly_cyrus.number_of_toys

print milly_cyrus.show_info()
