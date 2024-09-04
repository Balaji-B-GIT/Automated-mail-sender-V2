import random
import smtplib
import datetime as dt
from pandas import *

my_mail = "sampleforpythonmail@gmail.com"
# password will be generated through app passwords
password = ""
PLACEHOLDER = "[NAME]"

today = dt.datetime.now()
day = today.day
month = today.month

letters = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
random_letter = random.choice(letters)
with open(random_letter, "r") as file:
    data = file.read()

df = read_csv("birthdays.csv")
for i in range(len(df)):
    if month == df["month"][i]:
        if day == df["day"][i]:

            bd_letter = data.replace(PLACEHOLDER,df["name"][i])

            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(my_mail,password=password)
                connection.sendmail(from_addr=my_mail,
                                    to_addrs=df["email"][i],
                                    msg=f"Subject:Happy Birthday!!!\n\n{bd_letter}")

# This program can be executed every day using "python everywhere"
# First create an account
# Add program files in files tab and folder(same name as in program "letter_templates") in directories
# Create new bash console in "console" tab
# run cmd "python3 main.py" to run our program
# If "smtpAuthenticationError" occurs the copy the link at the end of the message and search it
# Once page loaded, under step 2, click the link "DisplayUnlockCaptcha" and hit "continue"
# run cmd "python3 main.py" again and nothing if displayed, the code executed successfully
# To run this program daily, go to "task" tab
# Type cmd "python3 main.py" in the input field and utc time
# Click "create", CONGRATS!!! this program will run daily at specified utc time.