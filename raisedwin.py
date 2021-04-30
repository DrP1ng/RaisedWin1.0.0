import os
from time import sleep
from colorama import Fore, Back, Style


def main():
    os.system("cls || clear")
    menu()
    sleep(0.5)
    print(Fore.WHITE + "    |\t[MENÚ PRINCIPAL]\t\t\t\t\t\t|")
    print("    |\t\t\t\t\t\t\t\t\t|")
    print("    |\t1 : Windows 7\t\t\t\t\t\t\t|")
    print("    |\t2 : Windows 8\t\t\t\t\t\t\t|")
    print("    |\t3 : Windows 8.1\t\t\t\t\t\t\t|")
    print("    |\t4 : Windows 10\t\t\t\t\t\t\t|")
    print("    |\t5 : Windows Server 2012\t\t\t\t\t\t|")
    print("    |\t6 : Windows Server 2016\t\t\t\t\t\t|")
    print("    |\t7 : Windows Server 2019\t\t\t\t\t\t|")
    print("    |\t\t\t\t\t\t\t\t\t|")
    print("    |\t0 : Salir\t\t\t\t\t\t\t|")
    print("    +===================================================================+")
    sleep(0.5)
    print(Fore.CYAN + "\n    [*] Si no estás seguro de la elección ejecuta " + Fore.RED +
          "\n    systeminfo | findstr /B /C:'Nombre del sistema operativo' /C:'Versión del sistema operativo'" + Fore.CYAN + "\n    para ver información del sistema vulnerado" + Style.RESET_ALL)
    sleep(0.5)
    print("\n    +-------------------------------------------------------------------+")
    choice = input(
        Fore.WHITE + "    [>] Indica tu elección : " + Style.RESET_ALL)
    print("")

    if choice == '1':
        w7()
    elif choice == '2':
        w8()
    elif choice == '3':
        w81()
    elif choice == '4':
        w10()
    elif choice == '5':
        ws12()
    elif choice == '6':
        ws16()
    elif choice == '7':
        ws19()
    elif choice == '0':
        os.system("clear")
        exit()

# Preguntas para saber qué técnica de elevación usar


def preguntas():
    print("    +-------------------------------------------------------------------+")
    print("    |\t\t\t\t\t\t\t\t\t|")
    print("    |  ¿Está el SO desactualizado?\t\t\t\t\t|")
    respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                      " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)
    if respuesta == "s":
        print("    +-------------------------------------------------------------------+")
        print("    |  ¿Es vulnerable el kernel?\t\t\t\t\t|")
        respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                          " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

        if respuesta == "s":
            print(
                Fore.CYAN + "\n    [*]Las vulnerabilidades en el kernel de Windows se publican de vez \n    en cuando,muchas de las cuales se pueden usar para escalar privilegios")
            print(Fore.CYAN +
                  "\n    [>] Busca exploits públicos en " + Fore.RED + "https://www.exploit-db.com/" + Fore.CYAN + "\n    para conseguir la elevación de privilegios.\n    También puedes utilizar alguno de los siguientes :" + Style.RESET_ALL)
            sleep(2)
            exploits()
            sleep(10)
            exit()
        elif respuesta == "n":
            print(
                "    +-------------------------------------------------------------------+")
            print("    |  ¿Has encontrada aplicaciones vulnerables?\t\t\t|")
            respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                              " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

            if respuesta == "s":
                print(Fore.CYAN +
                      "\n    [>] Busca exploits públicos en " + Fore.RED + "https://www.exploit-db.com/" + Fore.CYAN + "\n    para conseguir la elevación de privilegios." + Style.RESET_ALL)
                sleep(10)
                exit()
            elif respuesta == "n":
                print(
                    "    +-------------------------------------------------------------------+")
                print("    |\t\t\t\t\t\t\t\t\t|")
                print("    |" + Fore.RED +
                      "  [!] Vas a tener que buscar otro camino" + Fore.WHITE + "\t\t\t\t|")
                print("    |" + Fore.RED +
                      "  Volvamos a comenzar de nuevo" + Fore.WHITE + "\t\t\t\t\t|")
                print("    |\t\t\t\t\t\t\t\t\t|")
                sleep(2)
                preguntas()

    elif respuesta == "n":
        print("    +-------------------------------------------------------------------+")
        print("    |  ¿Hay servicios inseguros?\t\t\t\t\t|")
        respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                          " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

        if respuesta == "s":
            print(
                "    +-------------------------------------------------------------------+")
            print("    |  ¿Has encontrado permisos de archivos de configuración\t\t|")
            print("    |  o ejecutables de servicios débiles?\t\t\t\t|")
            respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                              " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

            if respuesta == "s":
                print(
                    "    +-------------------------------------------------------------------+")
                print(Fore.CYAN + "\n    [*] Los servicios ejecutan el archivo definido en su ruta de archivo.\n    Si el archivo puede ser modificado, puedes reemplazarlo por un archivo malicioso propio.\n    Además, los servicios a veces cargan archivos de configuración.\n    Dependiendo del programa, es posible que dicho archivo de configuración\n    se pueda utilizar para ejecutar un archivo arbitrario.\n    Si existen permisos de escritura para dicho archivo de configuración,\n    los privilegios se pueden escalar" + Style.RESET_ALL)
                sleep(10)
                exit()
            elif respuesta == "n":
                print(
                    "    +-------------------------------------------------------------------+")
                print(
                    "    |  ¿Has encontrado rutas de algún servicio con espacios en blanco?\t|")
                respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                                  " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

                if respuesta == "s":
                    print(
                        "    +-------------------------------------------------------------------+")
                    print(Fore.CYAN +
                          "    [>] El modo de escalar privilegios es mediante 'Unquoteed service paths'")
                    print(Fore.CYAN + "\n    [*]Esta es otra forma de escalar los privilegios es explotar el orden\n    en el que Windows busca ejecutables según el valor definido\n    en el parámetro ImagePath de un servicio cuando\n    este valor contiene espacios y no está incrustado entre\n    comillas dobles" + Style.RESET_ALL)
                    sleep(10)
                    exit()
                elif respuesta == "n":
                    print(
                        "    +-------------------------------------------------------------------+")
                    print(
                        "    |  ¿Has encontrado permisos de servicio débiles?\t\t\t\t\t|")
                    respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                                      " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

                    if respuesta == "s":
                        print(
                            "    +-------------------------------------------------------------------+")
                        print(Fore.CYAN +
                              "\n    [>] Puedes usar esta técnica modificando la ruta binaria en el\n    servicio y, de este modo, ejecutar archivos arbitrarios" + Style.RESET_ALL)
                        sleep(10)
                        exit()
                    elif respuesta == "n":
                        print(
                            "    +-------------------------------------------------------------------+")
                        print(
                            "    |  ¿Has encontrado algún servicio que intenta cargar una DLL que falta?\t|")
                        respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                                          " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

                        if respuesta == "s":
                            print(
                                "    +-------------------------------------------------------------------+")
                            print(Fore.CYAN +
                                  "\n    [>] El método de escalada a utilizar es DLL Hijacking")
                            print(Fore.CYAN + "\n    [*]Las aplicaciones de Windows generalmente cargan archivos DLL\n    cuando se inician. Puede suceder que un archivo DLL no exista\n    y la aplicación no pueda cargarlo.\n    Sin embargo, una aplicación continuará ejecutándose\n    mientras no se necesite la DLL que falta." + Style.RESET_ALL)
                            sleep(10)
                            exit()
                        elif respuesta == "n":
                            print(
                                "    +-------------------------------------------------------------------+")
                            print(
                                "    |  ¿Hay permisos de clave de registro débiles?\t\t\t\t\t|")
                            respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                                              " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

                            if respuesta == "s":
                                print(
                                    "    +-------------------------------------------------------------------+")
                                print(Fore.CYAN + "\n    [>] Para cada servicio, existe una clave de registro en\n    HKLM\SYSTEM\CurrentControlSet\Services. Las subclaves de la clave\n    de un servicio contienen información sobre la ruta\n    del archivo ejecutable, los parámetros y las opciones\n    de configuración. Si un servicio está configurado para comenzar\n    desde el contexto de seguridad de una cuenta en particular,\n    las subclaves también contienen el nombre de usuario" + Style.RESET_ALL)
                                sleep(10)
                                exit()
                            elif respuesta == "n":
                                print(
                                    "    +-------------------------------------------------------------------+")
                                print("    |\t\t\t\t\t\t\t\t\t|")
                                print(
                                    "    |" + Fore.RED + "  [!] Vas a tener que buscar otro camino" + Fore.WHITE + "\t\t\t\t|")
                                print(
                                    "    |" + Fore.RED + "  Volvamos a comenzar de nuevo" + Fore.WHITE + "\t\t\t\t\t|")
                                print("    |\t\t\t\t\t\t\t\t\t|")
                                sleep(2)
                                preguntas()

        elif respuesta == "n":
            print(
                "    +-------------------------------------------------------------------+")
            print(
                "    |  ¿Existe un servicio que se puede utilizar\t\t\t|\n    |   para encontrar contraseñas?\t\t\t\t\t|")
            respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                              " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

            if respuesta == "s":
                print(
                    "    +-------------------------------------------------------------------+")
                print(
                    Fore.CYAN + "\n    [>] Puedes elevar privilegios aprovechando las credenciales encontradas" + Style.RESET_ALL)
                sleep(10)
                exit()
            elif respuesta == "n":
                print(
                    "    +-------------------------------------------------------------------+")
                print(
                    "    |  ¿Has encontrado contraseñas de texto sin cifrar\t\t\t|\n    |   en ficheros o en el registro?\t\t\t\t\t|")
                respuesta = input(Fore.WHITE + "       Sí" + Fore.GREEN +
                                  " [s] " + Fore.WHITE + " No" + Fore.RED + " [n]" + Fore.WHITE + " : " + Style.RESET_ALL)

                if respuesta == "s":
                    print(
                        "    +-------------------------------------------------------------------+")
                    print(Fore.CYAN +
                          "\n    [>] Úsalas para escalar privilegios")
                    print("\n    [*]En el proceso de automatización de diferentes tareas, los\n    administradores del sistema a menudo, a sabiendas\n    o sin saberlo, escriben contraseñas de texto\n    sin cifrar en archivos o en el registro de cuentas,\n    que se utilizan para autenticarse en diferentes servicios" + Style.RESET_ALL)
                    sleep(10)
                    exit()
                elif respuesta == "n":
                    print(
                        "    +-------------------------------------------------------------------+")
                    print("    |\t\t\t\t\t\t\t\t\t|")
                    print(
                        "    |" + Fore.RED + "  [!] Vas a tener que buscar otro camino" + Fore.WHITE + "\t\t\t\t|")
                    print(
                        "    |" + Fore.RED + "  Volvamos a comenzar de nuevo" + Fore.WHITE + "\t\t\t\t\t|")
                    print("    |\t\t\t\t\t\t\t\t\t|")
                    sleep(2)
                    preguntas()


def w7():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS 7" +
          Style.RESET_ALL + "\t\t\t\t\t\t\t|")
    preguntas()


def w8():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS 8" +
          Style.RESET_ALL + "\t\t\t\t\t\t\t|")
    preguntas()


def w81():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS 8.1" +
          Style.RESET_ALL + "\t\t\t\t\t\t\t|")
    preguntas()


def w10():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS 10" +
          Style.RESET_ALL + "\t\t\t\t\t\t\t|")
    preguntas()


def ws12():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS SERVER 2012" +
          Style.RESET_ALL + "\t\t\t\t\t\t|")
    preguntas()


def ws16():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS SERVER 2016" +
          Style.RESET_ALL + "\t\t\t\t\t\t|")
    preguntas()


def ws19():
    os.system("cls || clear")
    menu()
    print("    |\t" + Fore.GREEN + ":: WINDOWS SERVER 2019" +
          Style.RESET_ALL + "\t\t\t\t\t\t|")
    preguntas()


def exploits():
    print("\n    " + Fore.GREEN +
          ":: LISTA DE EXPLOITS PARA ELEVAR PRIVILEGIOS" + Style.RESET_ALL)
    print(Fore.CYAN +
          "\n    [1] Microsoft Address Book 6.00.2900.5512")
    print(Fore.GREEN + "        > CVE-ID :\t" + Fore.CYAN + "CVE-2010-3147")
    print(Fore.GREEN + "        > Score :\t" + Fore.RED + "9.3")
    print(Fore.GREEN + "        > URL :\t\t" + Fore.CYAN +
          "https://www.exploit-db.com/exploits/14745")
    print(Fore.GREEN + "\n        [+] Info : " + Fore.WHITE + "Untrusted search path vulnerability in wab.exe 6.00.2900.5512 in Windows Address \n    Book allows local users to gain privileges via a Trojan horse wab32res.dll file in the current \n    working directory, as demonstrated by a directory that contains a Windows Address Book (WAB), \n    VCF (aka vCard), or P7C file")
    sleep(1)
    print(Fore.CYAN +
          "\n    [2]Microsoft Remote Desktop Services")
    print(Fore.GREEN + "        > CVE-ID :\t" + Fore.CYAN + "CVE-2015-0016")
    print(Fore.GREEN + "        > Score :\t" + Fore.RED + "9.3")
    print(Fore.GREEN + "        > URL :\t\t" + Fore.CYAN +
          "https://www.exploit-db.com/exploits/35983")
    print(Fore.GREEN + "\n        [+] Info : " + Fore.WHITE +
          "Directory traversal vulnerability in the TS WebProxy (aka TSWbPrxy) allows remote \n    attackers to gain privileges via a crafted pathname in an executable file, as demonstrated by \n    a transition from Low Integrity to Medium Integrity")
    sleep(1)
    print(Fore.CYAN +
          "\n    [3] Microsoft Windows - Class Handling")
    print(Fore.GREEN + "        > CVE-ID :\t" + Fore.CYAN + "CVE-2010-2744")
    print(Fore.GREEN + "        > Score :\t" + Fore.YELLOW + "7.2")
    print(Fore.GREEN + "        > URL :\t\t" + Fore.CYAN +
          "https://www.exploit-db.com/exploits/15894")
    print(Fore.GREEN + "\n        [+] Info : " + Fore.WHITE + "The kernel-mode drivers do not properly manage a window class, which allows local \n    users to gain privileges by creating a window, then using (1) the SetWindowLongPtr function \n    to modify the popup menu structure, or (2) the SwitchWndProc function with a switch window \n    information pointer, which is not re-initialized when a WM_NCCREATE message is processed")
    sleep(1)
    print(Fore.CYAN +
          "\n    [4] Microsoft Windows - HWND_BROADCAST")
    print(Fore.GREEN + "        > CVE-ID :\t" + Fore.CYAN + "CVE-2013-0008")
    print(Fore.GREEN + "        > Score :\t" + Fore.YELLOW + "7.2")
    print(Fore.GREEN + "        > URL :\t\t" + Fore.CYAN +
          "https://www.exploit-db.com/exploits/24485")
    print(Fore.GREEN + "\n        [+] Info : " + Fore.WHITE +
          "win32k.sys in the kernel-mode drivers does not properly handle window broadcast \n    messages, which allows local users to gain privileges via a crafted application")
    sleep(1)
    print(Fore.CYAN +
          "\n    [5] NTUserMessageCall Win32k Kernel Pool Overflow 'schlamperei.x86.dll'")
    print(Fore.GREEN + "        > CVE-ID :\t" + Fore.CYAN + "CVE-2013-1300")
    print(Fore.GREEN + "        > Score :\t" + Fore.YELLOW + "7.2")
    print(Fore.GREEN + "        > URL :\t\t" + Fore.CYAN +
          "https://www.exploit-db.com/exploits/33213")
    print(Fore.GREEN + "\n        [+] Info : " + Fore.WHITE +
          "win32k.sys in the kernel-mode drivers does not properly handle window \n    broadcast messages, which allows local users to gain privileges via a crafted application")
    sleep(1)
    print(Fore.CYAN +
          "\n    [6] Microsoft Windows - TrackPopupMenu Win32k Null Pointer Dereference")
    print(Fore.GREEN + "        > CVE-ID :\t" + Fore.CYAN + "CVE-2014-4113")
    print(Fore.GREEN + "        > Score :\t" + Fore.YELLOW + "7.2")
    print(Fore.GREEN + "        > URL :\t\t" + Fore.CYAN +
          "https://www.exploit-db.com/exploits/35101")
    print(Fore.GREEN + "\n        [+] Info : " + Fore.WHITE +
          "win32k.sys in the kernel-mode drivers allows local users to gain privileges via a \n    crafted application, as exploited in the wild in October 2014")


def menu():
    print(Fore.WHITE + """\n
    +===================================================================+
    |\t	                   __		                  \t|
    |\t	              ,-~Â¨^  ^Â¨-,           _,           \t|
    |\t	             /          / ;^-._...,Â¨/             \t|
    |\t	            /          / /         /               \t|
    |\t	           /          / /         /                \t|
    |\t	          /          / /         /                 \t|
    |\t	         /,.-:''-,_ / /         /                  \t|
    |\t	         _,.-:--._ ^ ^:-._ __../                   \t|
    |\t	       /^         / /Â¨:.._Â¨__.;                  \t|
    |\t	      /          / /      ^  /                     \t|
    |\t	     /          / /         /                      \t|
    |\t	    /          / /         /                       \t|
    |\t	   /_,.--:^-._/ /         /                        \t|
    |\t	  ^            ^Â¨Â¨-.___.:^                       \t|
    |\t                _              _            _            \t|
    |\t               (_)            | |          (_)           \t|
    |\t      _ __ __ _ _ ___  ___  __| | __      ___ _ __       \t|
    |\t     | '__/ _` | / __|/ _ \/ _` | \ \ /\ / / | '_ \      \t|
    |\t     | | | (_| | \__ \  __/ (_| |  \ V  V /| | | | |     \t|
    |\t     |_|  \__,_|_|___/\___|\__,_|   \_/\_/ |_|_| |_|     \t|
    |\t                                                         \t|
    +-------------------------------------------------------------------+
    |\t     By : Adraho & Dr. P1ng                     v1.0      \t|
    +-------------------------------------------------------------------+
    |\t     Choose your own windows privesc technique      \t\t|
    +===================================================================+
    """ + Style.RESET_ALL)


if __name__ == "__main__":
    main()
