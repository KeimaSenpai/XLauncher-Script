![minecraft_title](https://github.com/KeimaSenpai/X-Launcher/assets/98184310/7add7162-ec81-45a9-bf23-d182655b655f)

# Minecraft Launcher
Launcher de minecraft que hice para un video de YouTube

### 🔩Instalacion
- Clonar repositorio
```console
git clone https://github.com/KeimaSenpai/Script-launcher-Minecraft.git
```
- Crear entorno de desarrollo
```console
pip install virtualenv
virtualenv env
```
- Instalar dependencias
```console
pip install -r requirements.txt
```

🔩Instalación para los usuarios de Cuba
> Para que no gasten megas en la instalacion del paquete pueden usar este comando
> Solo funciona para CUBA este comando
```console
python -m pip install -r requirements.txt --index-url http://nexus.prod.uci.cu/repository/pypi-proxy/simple/ --trusted-host nexus.prod.uci.cu
```

### 📦Para empaquetar
```console
pyinstaller main.py --noconfirm --onedir --console --icon icon_windows.ico --name "XLauncher"
```

>Link de la documentacion [LINK](https://minecraft-launcher-lib.readthedocs.io/en/stable/)

## 📺Video de YouTube
[CREA TU PROPIO LAUNCHER de MINECRAFT](https://youtu.be/5FmjSubDRyw?si=9brYY9OnENftZgft)
