from bs4 import BeautifulSoup
import requests
import time

no_skills=[]
print("Enter the job skills which are irrelevant for you. Press -1 to exit")
s="0"
while not s == "-1":
    s=input()
    no_skills.append(s)
else:
    print("\n")
    URL='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

    def jobs():
        f=0
        details= requests.get(URL).text
        html= BeautifulSoup(details,'lxml')
        jobs= html.find_all('li', class_='clearfix job-bx wht-shd-bx')
        for job in jobs:
            post_string= job.find('span', class_='sim-posted').span.text
            if not 'few' in post_string:
                for word in post_string:
                    date="Today"
                    if word.isdigit():
                        date=word
                        break
                name= job.find('h3', class_='joblist-comp-name').text.strip()
                skills= job.find('span', class_='srp-skills').text.strip().replace(" ","")
                list=skills.split(",")
                for skill in no_skills:
                    #title= job.find('strong', class_='b1kclor').text.strip()
                    if skill in list:
                        f=1
                        break
                if f==0:
                    #print(f"Job Title: {title}\n")
                    print(f"Company Name: {name.strip()}\n")
                    print(f"Published Date: {date.strip()} day(s) ago\n")
                    print(f"Skills: {skills}\n")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                f=0

    if __name__=='__main__':
        while True:
            jobs()
            minutes=int(input("Enter time to wait in minutes\n"))
            time.sleep(int(minutes * 60))
