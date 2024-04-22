import asyncio
from minecraft_launcher.menu import menu_I


async def inicio():
    await menu_I()

if __name__ == '__main__':
    asyncio.run(inicio())