
'''
    Use Case: Explain the importance of super()
'''
class Bhavana(object):

    def getMeRebBull(self):
        return 'Pay be 100 /- - from class A'



class Hardik(object):

    def getMeRebBull(self):
        return 'Pay be 100 /- from class B'



class Jay(object):

    def getMeRebBull(self):
        return 'Pay be 100 /- from class C'


class PP(object):

    def dontgetMeRebBull(self):
        return 'I dont like RB'


class Arun(PP,Bhavana,Hardik,Jay):pass


# Now Instance of Arun wants a RedBull


# Interpreter will search only in the order given below when you use super() it actually follows this order only ! :-)

'''
[<class 'playground.Arun_Chandramouli.super.Arun'>,
<class 'playground.Arun_Chandramouli.super.PP'>,
<class 'playground.Arun_Chandramouli.super.Bhavana'>,
<class 'playground.Arun_Chandramouli.super.Hardik'>,
<class 'playground.Arun_Chandramouli.super.Jay'>,
<type 'object'>]

'''


# Now answering Kamlesh's question - Arun's instance should take RedBull only from second super class even if first in order has a red bull


def searchOrder(classobject,attrToSearch):
    order = []

    for classes in classobject.mro():

        if attrToSearch in classes.__dict__.keys():
            order.append(classes)
    return order

#"getMeRebBull"

print searchOrder(Arun,"getMeRebBull")

# Now as per your req - you want 2nd in the list

print searchOrder(Arun,"getMeRebBull")[2]

print getattr(searchOrder(Arun,"getMeRebBull")[2],"getMeRebBull")
