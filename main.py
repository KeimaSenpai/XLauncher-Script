import asyncio
import os
# Importaciones locales
from minecraft_launcher.minecraft import install_fabric, install_forge, install_minecraft, play_mine


VERSION = ('1.0.1')
user_windows = os.environ['USERNAME']
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
▐Para info de del script (5)
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
    if select == "5":
        await info_app()
    if select == "0":
        exit
    if select == "":
        await menu()


async def info_app():
    os.system('cls' if os.name == 'nt' else 'clear')
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