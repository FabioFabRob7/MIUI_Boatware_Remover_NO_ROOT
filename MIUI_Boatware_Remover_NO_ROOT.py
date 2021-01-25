import subprocess

print("//////////////////////////////////\n- MIUI_Bloatware_Remover_NO_ROOT -\n-        By FabioFabRob7         -\n//////////////////////////////////\n")
input("!!!I am not responsible for any damage or malfunction of your device. This app removes some apps of your choice from the MIUI rom. Hit enter to continue. . .")
input("Enable USB debug (ADB) on your smartphone then press enter. . .")

def OS():
    OS_select = input("Select your PC OS:\n1) Windows\n2) Linux\n")
    if OS_select == "1":
        Windows()
    elif OS_select == "2":
        ADB_FASTBOOT_L()
    else:
        OS()

# INSTALL ADB AND FASTBOOT FOR LINUX

def ADB_FASTBOOT_L():
    ADB_FASTBOOT_value = input("Welcome to the universal bootloader unlocking tool for almost all Android smartphones. ADB (Android Debug Bridge) and Fastboot will be downloaded for restarting and unlocking the bootloader, you want to continue Y/N:")
    if ADB_FASTBOOT_value == "y" or ADB_FASTBOOT_value == "Y":
        subprocess.call(["sudo","apt","install","adb","fastboot"])
        Linux()
    elif ADB_FASTBOOT_value == "n" or ADB_FASTBOOT_value == "N":
        exit
    else:
        ADB_FASTBOOT_L()

def Windows():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","shell"])
    print("Enter in ADB SHELL\n")
    select_app()
def select_app():
    program = input("Enter exit for exit\nSelect the bloatware app to remove\nAndroid Bloatware          Google Bloatware          MIUI Bloatware\n\n1) Web Browser             4) Google Docs            11) Mi File Manager\n2) Chrome                  5) Google Maps            12) Mi Health\n3) Ok Google               6) Google Photos          13) Mi Wallet\n                           7) Google Duo             14) MIUI Analytics\n                           8) Gmail                  15) Mi Calculator\n                           9) Gboard                 16) MIUI Compass\n                           10) Youtube               17) MIUI FM\n                                                     18) MIUI Gallery\n                                                     19) Music Player\n                                                     20) MIUI Video player\n                                                     21) Weather app\n\n")
    if program == '1':
        subprocess.call(["pm","uninstall","--user","0","com.android.browser"])
        select_app()
    elif program == '2':
        subprocess.call(["pm","uninstall","--user","0","com.android.chrome"])
        select_app()
    elif program == '3':
        subprocess.call(["pm","uninstall","--user","0","com.android.hotwordenrollment.okgoogle"])
        select_app()
    elif program == '4':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.apps.docs"])
        select_app()
    elif program == '5':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.apps.maps"])
        select_app()
    elif program == '6':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.apps.photos"])
        select_app()
    elif program == '7':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.apps.tachyon"])
        select_app()
    elif program == '8':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.gm"])
        select_app()
    elif program == '9':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.inputmethod.latin"])
        select_app()
    elif program == '10':
        subprocess.call(["pm","uninstall","--user","0","com.google.android.youtube"])
        select_app()
    elif program == '11':
        subprocess.call(["pm","uninstall","--user","0","com.mi.android.globalFileexplorer"])
        select_app()
    elif program == '12':
        subprocess.call(["pm","uninstall","--user","0","com.mi.health"])
        select_app()
    elif program == '13':
        subprocess.call(["pm","uninstall","--user","0","com.mipay.wallet.id"])
        select_app()
    elif program == '14':
        subprocess.call(["pm","uninstall","--user","0","com.miui.analytics"])
        select_app()
    elif program == '15':
        subprocess.call(["pm","uninstall","--user","0","com.miui.calculator"])
        select_app()
    elif program == '16':
        subprocess.call(["pm","uninstall","--user","0","com.miui.compass"])
        select_app()
    elif program == '17':
        subprocess.call(["pm","uninstall","--user","0","com.miui.fm"])
        select_app()
    elif program == '18':
        subprocess.call(["pm","uninstall","--user","0","com.miui.gallery"])
        select_app()
    elif program == '19':
        subprocess.call(["pm","uninstall","--user","0","com.miui.player"])
        select_app()
    elif program == '20':
        subprocess.call(["pm","uninstall","--user","0","com.miui.videoplayer"])
        select_app()
    elif program == '21':
        subprocess.call(["pm","uninstall","--user","0","com.miui.weather2"])
        select_app()
    elif program == 'exit':
        exit
    else:
        select_app()

def Linux():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","shell"])
    print("Enter in ADB SHELL\n")
    select_app()

OS()