class Contact:
    def __init__(this,name,email):
        this.name = name
        this.email = email

contact = Contact("John Miller","johnmiller@example.com")
toString = lambda name,email : name+"'s email address is "+email
print(toString(contact.name,contact.email))