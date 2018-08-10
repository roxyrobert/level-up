import re
my_list = []

class User:

    def __init__(self, firstname, surname, phoneNumber, email, password):
        self._id = 0
        self.firstname = firstname
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.email = email
        self.password = password
    
    def full_name(self):
        full_name =f"{self.firstname} {self.surname}"
        return full_name
    
    def validate_email(self):
        email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if email_regex.match(self.email):
            return "Valid email"
        return "Invalid email entered"
    
    
    
    def add_user(self):

        _id = len(my_list)
        self._id = _id + 1
        new_user = {
            '_id' : self._id,
            'firstname':self.firstname,
            'surname' : self.surname,
            'phoneNumber' : self.phoneNumber,
            'email' : self.email,
            'password' : self.password
        }
        my_list.append(new_user)
        return new_user
