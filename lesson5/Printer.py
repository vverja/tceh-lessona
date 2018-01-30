class Printer():
    def log(self,*values):
        print(values)

class FormattedPrinter(Printer):
    def log(self,*values):
        print(5*'*',values,5*'*')

p = Printer()
f = FormattedPrinter()
p.log(5 , 98 , 'Hello')
f.log(5 , 98 , 'Hello')

