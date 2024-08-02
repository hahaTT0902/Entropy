import sys
import time
import random
import openai
import os
import pyfiglet
import rich
from rich.console import Console
import curses
from rich.progress import Progress, track
from os import walk


def hacking_animation(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    chars = ['|', '/', '-', '\\']
    loop = 0
    while loop < 3:
        for i in range(height):
            stdscr.clear()

            line = ''.join(random.choice(chars) for _ in range(width - 1))
            stdscr.addstr(i, 0, line[:width - 1])
            stdscr.refresh()
            time.sleep(0.1)
            loop += 1

        time.sleep(1)


def probing_animation():
    curses.wrapper(hacking_animation)


from rich.live import Live


def loading_bar(total, text, length=50):
    sys.stdout.write(text)
    for i in range(total + 1):
        percent = 100 * (i / float(total))
        bar = '█' * int(percent / 100 * length) + '-' * (length - int(percent / 100 * length))
        sys.stdout.write('\r' + '[' + text + ']' + f' |{bar}| {percent:.2f}%')
        time.sleep(0.1)
    print()


def slow_print(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def very_quick_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def quick_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def game_intro():
    print("\n\n\n\n")
    time.sleep(2)
    print("               ▄████████ ███▄▄▄▄       ███        ▄████████  ▄██████▄     ▄███████▄ ▄██   ▄   ")
    time.sleep(0.05)
    print("              ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███ ███    ███   ███    ███ ███   ██▄ ")
    time.sleep(0.05)
    print("              ███    █▀  ███   ███    ▀███▀▀██   ███    ███ ███    ███   ███    ███ ███▄▄▄███    ")
    time.sleep(0.05)
    print("             ▄███▄▄▄     ███   ███     ███   ▀  ▄███▄▄▄▄██▀ ███    ███   ███    ███ ▀▀▀▀▀▀███    ")
    time.sleep(0.05)
    print("            ▀▀███▀▀▀     ███   ███     ███     ▀▀███▀▀▀▀▀   ███    ███ ▀█████████▀  ▄██   ███    ")
    time.sleep(0.05)
    print("              ███    █▄  ███   ███     ███     ▀███████████ ███    ███   ███        ███   ███    ")
    time.sleep(0.05)
    print("              ███    ███ ███   ███     ███       ███    ███ ███    ███   ███        ███   ███    ")
    time.sleep(0.05)
    print("              ██████████  ▀█   █▀     ▄████▀     ███    ███  ▀██████▀   ▄████▀       ▀█████▀     ")
    time.sleep(0.01)
    print("                                                 ███    ███                                      \n\n\n")
    time.sleep(0.01)
    loading_bar(5, "Powering On")
    loading_bar(5, "Initializing CPU")
    loading_bar(10, "Setting up Bitcoin wallet")
    loading_bar(5, "Generating Private Keys")
    loading_bar(5, "Loading Tor Browser")
    loading_bar(25, "Initializing FlyOS")
    loading_bar(10, "Loading Network")
    os.system('cls')
    slow_print("\rSystem Ready...")
    time.sleep(0.5)
    os.system('cls')
    print("""
    
      _   _                   __  __       _ _    _ 
     | \ | |                 |  \/  |     (_) |  | |
     |  \| | _____      __   | \  / | __ _ _| |  | |
     | . ` |/ _ \ \ /\ / /   | |\/| |/ _` | | |  | |
     | |\  |  __/\ V  V /    | |  | | (_| | | |  |_|
     |_| \_|\___| \_/\_/     |_|  |_|\__,_|_|_|  (_)
                                                    
                                                
    """)
    time.sleep(1)
    os.system('cls')
    quick_print("""
    Hi.
    . . .\n
    This is strange... Stranger than I expected\n     
    I guess I'm supposed to write this in past tense, though I hardly feel like admitting it's over.\n
    My name is Bit, and if you're reading this, I'm already dead.\n
    My Failsafe is active by now if you receive this email, and you can still ask me any question, just think I am still
    alive.\n
    """)
    time.sleep(0.5)
    quick_print("""   
    I don't know you, and I'm sad to say that I never will. \n
    But if you're reading this it means you might be the only person that can make things right.\n
    From the year 2030, the internet world is controlled by a Mega AI known as Entropy.\n
    As a member of the resistance, I was tasked with uncovering the secrets behind Entropy.\n
    Right now I'm trapped. There's no way out, and not enough time, and I need your help.\n
    If you can, or you possibly can, hack into Entropy's proxy server, that will be great.\n
    When you're done, just reply to this email.\n
    Hurry!
    -Bit
    """)


def ai_response(prompt):
    openai.api_key = 'API_KEY'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are Bit. You are a helpful friend for D3f4ult, you will teach him skills to hack "
                        "systems(in a game) and talk with him. If I ask 'how to hack' or how can 'I complete the mission', respond as ' First input ls in the console to check the Files, then do a cat <file> that you want to look, after that, try porthack to scan the ports, after that, do sshcrack, last, do ftpbounce"},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()


# Main Game Function
def main_game():
    quick_print("Bit: Hello, D3f4ult. Long time no See huh! What can I help you?\n")

    while True:
        user_input = input("D4f4ult: ")
        if user_input.lower() in ['exit', 'quit']:
            quick_print("Bit: Goodbye, D3f4lt. Shutting down FlyOS...\n")
            os.system('cls')
            break
        response = ai_response(user_input)
        quick_print(f"Bit: {response}\n")


# Character interactions
def character_interactions():
    os.system('cls')
    slow_print("Bl34ch is online...")
    quick_print("Bl34ch: We need to hack into Entropy's system. Are you ready?")
    choice = input("1. Yes\n2. No\nChoose: ")
    if choice == '1':
        quick_print("Bl34ch: Let's do this!")
        hack_mission()
    else:
        quick_print("Bl34ch: We can't delay. Let me know when you're ready.")


def hack_mission():
    os.system('cls')
    quick_print("Initializing...")
    loading_bar(10, "Connecting to 10.203.10.22")
    FTP_bounced = False
    probed = False
    open_ports = []
    ssh_port = random.choice([22, 2222, 2022])
    ftp_port = random.choice([21, 2121, 2021])

    while True:
        command = input("Enter command: ")
        if command == "ls":
            print("Files:\n- system.log\n- config.sys\n- top_secret.txt")
        elif command.startswith("cat"):
            if command.split()[1] == "top_secret.txt":
                quick_print("EntropyOS main server is located 40.7608° N, 111.8910° W.")
            elif command.split()[1] == "config.sys":
                print("""
                [product]
                version = "1.0"
                machine = "A10-EVB-V13"
                
                [target]
                boot_clock = 1008
                dcdc2_vol = 1400
                dcdc3_vol = 1250
                ldo2_vol = 3000
                ldo3_vol = 2800
                ldo4_vol = 2800
                
                [card_burn_para]
                card_no = 0
                card_line = 4
                card_mode = 0
                sdc_d1 = port:PF00<2><1><default><default>
                sdc_d0 = port:PF01<2><1><default><default>
                sdc_clk = port:PF02<2><1><default><default>
                sdc_cmd = port:PF03<2><1><default><default>
                sdc_d3 = port:PF04<2><1><default><default>
                sdc_d2 = port:PF05<2><1><default><default>
                
                [card_boot]
                logical_start = 40960
                sprite_gpio0 =
                
                [card_boot0_para]
                card_ctrl = 0
                card_high_speed = 1
                card_line = 4
                sdc_d1 = port:PF00<2><1><default><default>
                sdc_d0 = port:PF01<2><1><default><default>
                sdc_clk = port:PF02<2><1><default><default>
                sdc_cmd = port:PF03<2><1><default><default>
                sdc_d3 = port:PF04<2><1><default><default>
                sdc_d2 = port:PF05<2><1><default><default>
                
                [card_boot2_para]
                card_ctrl = 2
                card_high_speed = 1
                card_line = 4
                sdc_cmd = port:PC06<3><1><default><default>
                sdc_clk = port:PC07<3><1><default><default>
                sdc_d0 = port:PC08<3><1><default><default>
                sdc_d1 = port:PC09<3><1><default><default>
                sdc_d2 = port:PC10<3><1><default><default>
                sdc_d3 = port:PC11<3><1><default><default>
                
                [twi_para]
                twi_port = 0
                twi_scl = port:PB00<2><default><default><default>
                twi_sda = port:PB01<2><default><default><default>
                
                [uart_para]
                uart_debug_port = 0
                uart_debug_tx = port:PB22<2><1><1><default>
                uart_debug_rx = port:PB23<2><1><1><default>
                lcd_pwm = port:PB02<2><0><default><default>
                lcd_gpio_0 =
                lcd_gpio_1 =
                lcd_gpio_2 =
                lcd_gpio_3 =
                """)
            elif command.split()[1] == "system.log":
                print("""
                2035-02-13 13:25:31 (900) glide.quota.manager SYSTEM QuotaFinder: Assigning quota
                "TEST PROBLEM FORM" with filter: type=form^urlLIKEsys_id=46fb9e31a9fe198101492060c2a4f8cb^EQ to
                transaction: URL= /problem.do?sys_id=46fb9e31a9fe198101492060c2a4f8cb, THREAD= http-bio-8080-exec-1,
                FG= true, TYPE= 1, STATE= 4, USER= null, TIME= 1,121, MEM= 0, ATTRIBUTES= {}
                
                2035-02-15 13:25:33 (930) glide.quota.manager SYSTEM WARNING *** WARNING ***
                Transaction: Cancelling transaction /problem.do (maximum execution time exceeded):
                Thread http-bio-8080-exec-1
                """)
            else:
                print("Unknown File name")
        elif command == "probehack":
            loading_bar(25, "Probing ports")
            probing_animation()
            open_ports = ["HTTP = 80", "HTTPS = 443", "SSH = " + str(ssh_port), "FTP = " + str(ftp_port)]
            print(f"Open ports: {', '.join(map(str, open_ports))}")
            probed = True
        elif command.startswith("ftpbounce"):
            if not probed:
                print("Error: You must run 'probehack' first.")
            else:
                try:
                    port = int(command.split()[1])
                    if port == ftp_port:
                        slow_print(f"Attempting FTP crack on port {port}...")
                        success = random.choice([True, False])
                        if success:
                            print("FTP crack successful! Requires SSH port")
                            FTP_bounced = True
                        else:
                            print("FTP crack failed! Try again.")
                    else:
                        print(f"Port {port} is not an open FTP port.")
                except (IndexError, ValueError):
                    print("Usage: ftpcrack <port>")
        elif command.startswith("sshcrack"):
            if not probed:
                print("Error: You must run 'probehack' first.")
            elif not FTP_bounced:
                print("Plese do ftpbounce first to crack SSH port!")
            else:
                try:
                    port = int(command.split()[1])
                    if port == ssh_port:
                        loading_bar(25, f"Attempting SSH crack on port {port}")
                        success = random.choice([True, False])
                        if success:
                            print("SSH crack successful! Access granted.")
                            time.sleep(1)
                            os.system('cls')
                            print("""
                            ##    ##  #######  ##     ##    ##     ##    ###    ##     ## ########    ##     ##    ###     ######  ##    ## ######## ########     
                             ##  ##  ##     ## ##     ##    ##     ##   ## ##   ##     ## ##          ##     ##   ## ##   ##    ## ##   ##  ##       ##     ##    
                              ####   ##     ## ##     ##    ##     ##  ##   ##  ##     ## ##          ##     ##  ##   ##  ##       ##  ##   ##       ##     ##    
                               ##    ##     ## ##     ##    ######### ##     ## ##     ## ######      ######### ##     ## ##       #####    ######   ##     ##    
                               ##    ##     ## ##     ##    ##     ## #########  ##   ##  ##          ##     ## ######### ##       ##  ##   ##       ##     ##    
                               ##    ##     ## ##     ##    ##     ## ##     ##   ## ##   ##          ##     ## ##     ## ##    ## ##   ##  ##       ##     ##    
                               ##     #######   #######     ##     ## ##     ##    ###    ########    ##     ## ##     ##  ######  ##    ## ######## ########     
                            """)
                            print("""
                            ######## ##    ## ######## ########   #######  ########  ##    ## ####  ######      ######  ##    ##  ######  ######## ######## ##     ##     
                            ##       ###   ##    ##    ##     ## ##     ## ##     ##  ##  ##  #### ##    ##    ##    ##  ##  ##  ##    ##    ##    ##       ###   ###     
                            ##       ####  ##    ##    ##     ## ##     ## ##     ##   ####    ##  ##          ##         ####   ##          ##    ##       #### ####     
                            ######   ## ## ##    ##    ########  ##     ## ########     ##    ##    ######      ######     ##     ######     ##    ######   ## ### ##     
                            ##       ##  ####    ##    ##   ##   ##     ## ##           ##               ##          ##    ##          ##    ##    ##       ##     ##     
                            ##       ##   ###    ##    ##    ##  ##     ## ##           ##         ##    ##    ##    ##    ##    ##    ##    ##    ##       ##     ## ### 
                            ######## ##    ##    ##    ##     ##  #######  ##           ##          ######      ######     ##     ######     ##    ######## ##     ## ### 
                            """)
                            quick_print("Stolen Files\n- config.sys")
                            time.sleep(5)
                            os.system('cls')
                            break
                        else:
                            print("SSH crack failed! Try again.")
                    else:
                        print(f"Port {port} is not an open SSH port.")
                except (IndexError, ValueError):
                    print("Usage: sshcrack <port>")
        elif command == "exit":
            print("Mission aborted.")
            os.system('cls')
            break
        else:
            print("Unknown command. Try 'ls', 'cat <file>', 'probehack', 'sshcrack <port>', 'ftpcrack <port>', "
                  "or 'exit'.")


def secondary_menu():
    while True:
        print("""
        +------------------------------+
        | Menu:                        |
        |                              |
        | 1. Chat with Bit             |
        |                              |
        | 2. Hack in Entropy           |
        |                              |
        | 3. Exit Game                 |
        |                              |
        +------------------------------+
        """)
        choice = input("Choose: ")
        if choice == '1':
            os.system('cls')
            main_game()
        elif choice == '2':
            os.system('cls')
            character_interactions()
        elif choice == '3':
            quick_print("Exiting game...")
            break
        else:
            print("Invalid choice. Try again.")


game_intro()
secondary_menu()
