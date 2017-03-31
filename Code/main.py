"""Menu principal"""

from Worker import *

from Subscriber import *

def Test():

    worker1=Worker(000,"Jean",19,"Jean98vb@hotmail.com","asdfasdfa",1)

    if worker1.tipoTrabajador == 1:
        print("Tipo de trabajador: "+"Admin")
    else:
        print("Tipo de trabajador:"+ "User")

    print("Nombre: "+worker1.nombre)
    print("Email: "+worker1.email)



Test()