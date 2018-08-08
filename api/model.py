import re

class Uber:

    def __init__(self, firstname, surname, phoneNumber, email, password):
        self.firstname = firstname
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.email = email
        self.password = password
    
    def full_name(self):
        # full_name = '{} {}'.format(self.firstname, self.surname)
        
        full_name =f"{self.firstname} {self.surname}"
        print(full_name)
    
    def validate_email(self):
        email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if email_regex.match(self.email):
            print('Valid email')
            return self.email
        print("Invalid email entered")
    
# class Rider:
if __name__ == '__main__':
    transport = Uber('robert', 'ssebintu', '0775222759', 'roxy@gmail.com', '12345678')
    transport.validate_email()