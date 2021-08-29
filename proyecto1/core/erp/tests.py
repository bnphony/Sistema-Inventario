from config.wsgi import *
from core.erp.models import Type, Employee




"""
t = Type()
t.name = 'Tu puedes 7'
t.save()
"""
"""
try:
    t = Type.objects.get(id=10)
    t.name = 'Hola'
    t.save()
    print(t.name)
except Exception as e:
    print(e)

"""


#t = Type.objects.get(id=10)
#t.delete()

#query = Type.objects.all()
#print(query)

#buscar los registros que el campo nombre contenga una cadena
obj = Type.objects.filter(name__contains='tu puedes')
#Buscar los registros que el campo nombre contenga una cadena sin
#sin importar mayusculas o minisculas
obj = Type.objects.filter(name__icontains='tu puedes')
obj = Type.objects.filter(name__startswith='p')
obj = Type.objects.filter(name__endswith='a')
obj = Type.objects.filter(name__in=['Tu puedes']).count()
print(obj)

consulta = Type.objects.filter(name__icontains='Tu puedes').query
consulta = Type.objects.filter(name__icontains='Tu puedes').exclude(id=18)
#print(consulta)

#for i in Type.objects.filter(name__icontains='Tu puedes'):
#    print(i.name)

obj = Employee.objects.filter(type_id=18)
print(obj)


print("Hola Mundo")

#for i in Type.objects.filter(name__icontains='Tu puedes')[:2]:
#    print(i.name)