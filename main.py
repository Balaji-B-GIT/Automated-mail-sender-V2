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
