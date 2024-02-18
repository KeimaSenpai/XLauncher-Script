import minecraft_launcher_lib
import os
import subprocess

user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"


# Indicador de por donde va la instalación
current_max = 0

def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}



# Insalación de Minecraft
async def install_minecraft():
    minecraft_version = input('Versió: ')
    minecraft_launcher_lib.install.install_minecraft_version(
        minecraft_version, minecraft_directory, callback=callback)
    print(f'» Instalada la version {minecraft_version}')


# Instalar Forge
async def install_forge():
    print('Dime la Versión')
    forge_ver = input('» ')
    forfe = minecraft_launcher_lib.forge.find_forge_version(forge_ver)
    print(forfe)
    minecraft_launcher_lib.forge.install_forge_version(
        forfe, minecraft_directory, callback=callback)
    print(f'Instalado Forge {forfe}')

async def install_fabric():
    print('Dime la versión')
    fabric_ver = input('» ')
    fabric_supor_ver = minecraft_launcher_lib.fabric.is_minecraft_version_supported(fabric_ver)
    if fabric_supor_ver == False:
        print('No es compatible esa versión')
        await install_fabric()
    else:
        fabric = minecraft_launcher_lib.fabric.install_fabric(fabric_ver, minecraft_directory, callback=callback)

async def play_mine():
    print('Dígame su nombre')
    mine_user = input('» ')
    forts = minecraft_launcher_lib.utils.get_installed_versions(
        minecraft_directory)
    for fort in forts:
        print(fort['id'])
    print('Diagem la versión')
    version = input('» ')

    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',

        "jvmArguments": [
            "-Xmx2G",
            "-Xms2G",
            "-Xmn668m",
            "-XX:+DisableExplicitGC",
            "-XX:+UseConcMarkSweepGC",
            "-XX:+UseParNewGC",
            "-XX:+UseNUMA",
            "-XX:+CMSParallelRemarkEnabled",
            "-XX:MaxTenuringThreshold=15",
            "-XX:MaxGCPauseMillis=30",
            "-XX:GCPauseIntervalMillis=150",
            "-XX:+UseAdaptiveGCBoundary",
            "-XX:-UseGCOverheadLimit",
            "-XX:+UseBiasedLocking",
            "-XX:SurvivorRatio=8",
            "-XX:TargetSurvivorRatio=90",
            "-XX:MaxTenuringThreshold=15",
            "-Dfml.ignorePatchDiscrepancies=true",
            "-Dfml.ignoreInvalidMinecraftCertificates=true",
            "-XX:+UseFastAccessorMethods",
            "-XX:+UseCompressedOops",
            "-XX:+OptimizeStringConcat",
            "-XX:+AggressiveOpts",
            "-XX:ReservedCodeCacheSize=2048m",
            "-XX:+UseCodeCacheFlushing",
            "-XX:SoftRefLRUPolicyMSPerMB=10000",
            "-XX:ParallelGCThreads=10"
            ],  # The jvmArguments
        "launcherVersion": "1.0.0",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        version, minecraft_directory, options)
    subprocess.run(minecraft_command)