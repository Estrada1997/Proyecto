import datetime
class Empresa:
    def __init__(self,seguro ="Seguro", ID = "001-AD", nombre = "Computon", jefe = "Ing. Anderson Estrda", ruc ="0921171617001", telf ="0982971849", direc ="Bucay (Ganl. Antonio Elizalde"):
        self.nombre = nombre 
        self.ruc = ruc 
        self.jefe = jefe 
        self.telefono = telf 
        self.direccion = direc 
        self.seguro = seguro
        self.ID = ID
    def Departamento(self):
        print("Empresa: {} \nJefe: {:30} Ruc:{}  \nDirecc: {}".format(self.nombre, self.jefe, self.ruc,  self.direccion))
        print("Departamento: {:22} Codigo: {}".format(self.seguro, self.ID))
# hora = datetime.datetime.now()
# print(hora)
# emp = Empresa()
# emp.Departamento()
# print(Empresa())
class Empleado:
    def __init__(self, nom ="Anderson Estrada" , ced ="0921171617", telf ="0982971849", sueldo ="390", Fe_Ingreso= "25/08/2021", comision ="si"):
        self.nombre = nom 
        self.cedula = ced 
        self.telefono = telf
        self.sueldo = sueldo
        self.Fe_Ingreso = Fe_Ingreso
        self.comision = comision
    def comision(self, comi):   # va co sueldo del empleado o al iess
        self.comisiones = comi
        if comision == "si":
            comi = int(input("Ingrese su comision: "))
        elif comision == "no":
            print("Usted no tiene comision")
class Nuevo_Obrero(Empleado): 
    def __init__(self,  nom ="Anderson Estrada" , ced ="0921171617", telf ="0982971849", sueldo ="390", Fe_Ingreso= "25/08/2021", comision ="si",  contrato =None):  
        super().__init__(nom, ced, telf, sueldo, Fe_Ingreso, comision)
        self.contrato = contrato
        if contrato == None:
            "Su contrato es de 3 Meses"
        else:
            "Ya se finalizo su contrato"
class Trabajador(Empleado):
    def __init__(self, nom ="Anderson Estrada" , ced ="0921171617", telf ="0982971849", sueldo ="390", Fe_Ingreso= "25/08/2021", comision ="si", estado = "si", ): 
        super().__init__(nom, ced, telf, sueldo, Fe_Ingreso, comision)
        self.estado = estado 
        if estado == "si":
            self.estado="Activo"
        else:
            return "No Activo"
    def mostrar(self):
        print("Nombre: {:28} C.L.: {:30} \nSueldo BAsico $: {:20} Estado: {} \nFecha Ingreso:{}".format(self.nombre, self.cedula, self.sueldo,self.estado, self.Fe_Ingreso))        
# empl = Empleado()
# empl = Nuevo_Obrero()
# empl = Trabajador()
# empl.mostrar()
# print(Empleado())
class Pago_Salario:
    def __init__(self, sueldo="390.00", h_ord="8", ext_diur="4", ext_noct="3", ext_dom="5"):
        self.h_ord = h_ord
        self.sueldo = sueldo
        self.ext_diur = ext_diur
        self.ext_noct = ext_noct
        self.ext_dom = ext_dom
    # def salario(self):
    #     sueldo = float(input("Ingrese su sueldo: "))
    #     h_ord = int(input("Ingrese la catidad de horas orrdinarias: "))
    #     ext_diur = int(input("Horas extras: "))
    #     ext_noct = int(input("Horas nocturnas: "))
        ext_dom = int(input("Horas Dominicanas: "))de

    def calcular(self):
        salario_ord = 8 * 390.00
        salario_ext = (4 * 390.00) * 1.25 + (3 * 390.00)*1.5 + (5 * 390.00)*1.75
        retencion = salario_ext * 0.1   #para el Iess
        pagar = salario_ord + salario_ext - retencion
        print("Total Ingreso $:{} ".format(pagar))
        print("La retencio Para el seguro (IESS) es: ",retencion)
pago = Pago_Salario()
pago.calcular()
print(Pago_Salario())

class Prestamo(Trabajador):
    def __init__(self, nom ="Anderson Estrada" , ced ="0921171617", sueldo ="390", comision ="si", fecha="3/08/2021", monto ="1000", meses="5", interes="0.10"):
        super().__init__(nom, ced, sueldo, comision)
        self.fecha = fecha
        self.monto = monto
        self.meses = meses
        self.interes = interes 
        # meses = int(input("Ingrese Nro de Meses : "))
    def calculo(self):  
        intereses = 1000 * 5 * 0.10
        total_pago = 1000 + intereses                             # revisar
        print("Nombre: {:22} C.L.: {:20} \nEstado: {:22} Fecha del Prestamo:{}".format(self.nombre, self.cedula, self.estado, self.fecha))    # revisar estado 3 veces     
        print("El valor del Prestamo es $:{:20} Interes: {} Pago Total: {}".format(self.monto, intereses, total_pago))
# pres = Prestamo()
# pres.calculo()
# print(Prestamo())         
        
# hora = datetime.datetime.now()
# print(hora)
# print("******* Nomina Del Trabajador ******")
# emp = Empresa()
# emp.Departamento()
# print(Empresa())
# print("--------------------------------------")
# empl = Empleado()
# empl = Nuevo_Obrero()
# empl = Trabajador()
# empl.mostrar()
# print(Empleado())
# print("******Prestamo de Mil dolares*******") 
# pres = Prestamo()
# pres.calculo()
# print(Prestamo())
