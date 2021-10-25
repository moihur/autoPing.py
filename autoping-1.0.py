import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '4', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False

# Porbamos la conexión con google
print('Prueba de conexión con google')        
print(myping("www.google.com"))

# Servidores NTTDATA - MAPFRE (se requiere VPN activa)
print('Servidores NTTDATA - MAPFRE (se requiere VPN activa)')
print(myping("plastic"))