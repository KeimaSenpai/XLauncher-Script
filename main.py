import asyncio
import os
import json
import time
# Importaciones locales
from minecraft_launcher.minecraft import install_fabric, install_forge, install_minecraft, play_mine


VERSION = ('1.0.2')
user_windows = os.environ['USERNAME']
ruta_json = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher//configuracion.json"
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"

async def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists(minecraft_directory):
        os.makedirs(minecraft_directory)
    print(
        f'''
                    ██╗  ██╗ ██╗    ██╗   ██╗ ████    ██╗
                    ╚██╗██╔╝░██║░░░░██║░░░██║░██║██░░░██║
                    ░╚███╔╝░░██║░░░░██║░░░██║░██║░██░░██║
                    ░██╔██╗░░██║░░░░██║░░░██║░██║░░██░██║
                    ██╔╝╚██╗░██████╗████████║░██║░░░████║
                    ╚═╝░░╚═╝░╚═════╝╚═══════╝ ╚═╝   ╚═══╝ {VERSION}

▐Play Minecraft (1)
▐Instalar Versiones (2)
▐Instalar Forge (3)
▐Instalar Fabric (4)
▐Configurar Launcher (5)
▐Editar Configuación (6)
▐Para info (7)
▐---------------------------
▐Si quiere salir escriba (0)
''')

    select = input('▐Escribe la opcion: ')
    if select == "1":
        await play_mine()
    if select == "2":
        await install_minecraft()
    if select == "3":
        await install_forge()
    if select == "4":
        await install_fabric()
    if select == '5':
        await confi()
    if select == '6':
        await cambiar_dato()
    if select == "7":
        await info_app()
    if select == "0":
        exit
    if select == "":
        await menu()



async def confi():
    print('▐Digame su Nombre')
    nombre = input('» ')
    print('▐Digame la RAM en MB')
    ram = input('» ')
    print('▐Digame la ruta del Java')
    java_ruta = input('» ')

    data = {
        "Nombre": nombre,
        "RAM": ram,
        "Java": java_ruta
    }

    with open(ruta_json, 'w') as file:
        json.dump(data, file)
    print("◈ Guardando... ◈")
    time.sleep(2)
    await menu()

# Esto es para cambiar los ajustes
async def cambiar_dato():
    with open(ruta_json, 'r') as file:
        data = json.load(file)

    print("▨ Valores actuales ▨")
    for key, value in data.items():
        print(f"▸ {key}: {value}")
    print('\n▐¿Qué dato desea cambiar? \n  (Nombre/RAM/Java)')
    opcion = input('» ')
    if opcion in data:
        print(f'▐Ingrese el nuevo valor para {opcion}')
        nuevo_valor = input('» ')
        data[opcion] = nuevo_valor

        with open(ruta_json, 'w') as file:
            json.dump(data, file)

        print(f"◈ Actualizando... ◈")
        time.sleep(2)
        await menu()
    else:
        print("Opción no válida. Por favor elija entre Nombre, RAM o Java.")
        await cambiar_dato()


# -----------------------------------------------------
async def info_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(ruta_json, 'r') as file:
        data = json.load(file)

    print("\n   ▨ Info de Perfil ▨")
    for key, value in data.items():
        print(f"▸ {key}: {value}")
    print(
        f'''
        Info de XDLink
»Simple scipt par ejecutar Minecraft
 y jugar de manera no premium.

» Desarrollado por KeimaSenpai.

»Telegram - https://t.me/KeimaSenpai
»YouTube - https://www.youtube.com/@KeimaSenpaiYT
»GitHub - https://github.com/KeimaSenpai/XLauncher-Script
»Version: {VERSION}\n
''')
    print('Escribe (0) para volver')
    sel = input('» ')
    if sel == "0":
       await menu()




if __name__ == '__main__':
    asyncio.run(menu())