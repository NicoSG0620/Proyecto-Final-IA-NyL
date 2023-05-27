import datetime

# Horarios de atención de la empresa
horarios = {
    "Lunes": ["8:30 AM", "12:00 PM", "2:00 PM", "6:00 PM"],
    "Martes": ["8:30 AM", "12:00 PM", "2:00 PM", "6:00 PM"],
    "Miércoles": ["8:30 AM", "12:00 PM", "2:00 PM", "6:00 PM"],
    "Jueves": ["8:30 AM", "12:00 PM", "2:00 PM", "6:00 PM"],
    "Viernes": ["8:30 AM", "12:00 PM", "2:00 PM", "6:00 PM"]
}

# Cupos disponibles por día
citas_disponibles = {
    "Lunes": 5,
    "Martes": 5,
    "Miércoles": 5,
    "Jueves": 5,
    "Viernes": 5
}

def solicitar_informacion():
    cliente = {}
    cliente["nombres"] = input("Ingrese sus nombres: ")
    cliente["apellidos"] = input("Ingrese sus apellidos: ")
    cliente["cedula"] = input("Ingrese su cédula: ")
    cliente["telefono"] = input("Ingrese su número de teléfono: ")
    
    print("Horarios disponibles:")
    for dia, horario in horarios.items():
        print(f"{dia}: {horario}")
    
    cita = {}
    cita["dia"] = input("Ingrese el día de la cita (en formato Lunes/Martes/Miércoles/Jueves/Viernes): ")
    cita["hora"] = input("Ingrese la hora de la cita (en formato HH:MM AM/PM): ")
    
    return {"cliente": cliente, "cita": cita}

def validar_horario(cita):

    dia = cita["dia"]
    hora = datetime.datetime.strptime(cita["hora"], "%I:%M %p").time()
    horario = horarios[dia]
    
    if hora < datetime.datetime.strptime(horario[0], "%I:%M %p").time() or hora >= datetime.datetime.strptime(horario[-1], "%I:%M %p").time():
        print("Lo siento, la hora especificada no está dentro del horario de atención de la empresa.")
        return False
    
    for i in range(1, len(horario), 2):
        if hora >= datetime.datetime.strptime(horario[i-1], "%I:%M %p").time() and hora < datetime.datetime.strptime(horario[i], "%I:%M %p").time():
            return True
    
    print("Lo siento, la hora especificada no está dentro del horario de atención de la empresa.")
    return False

def validar_cupos(cita):
    dia = cita["dia"]
    if citas_disponibles[dia] > 0:
        return True
    else:
        print("Lo siento, no hay cupos disponibles para el día especificado.")
        return False

def agendar_cita(cliente, cita):
    dia = cita["dia"]
    citas_disponibles[dia] -= 1
    
    print("Informacion Cita:")
    print("Cliente:")
    print(f"Nombres: {cliente['nombres']}")
    print(f"Apellidos: {cliente['apellidos']}")
    print(f"Cédula: {cliente['cedula']}")
    print(f"Teléfono: {cliente['telefono']}")
    print("Cita:")
    print(f"Día: {cita['dia']}")
    print(f"Hora: {cita['hora']}")
