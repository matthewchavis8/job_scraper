from bs4 import BeautifulSoup
import requests
import time
print("put your weakest skills")
unfamiliar_skill = input('Enter: ')
print(f"filtering out {unfamiliar_skill}")




def find_jobs():
    #creating a url to the website
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

    #this requests the html text from the website
    content = requests.get(url, headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"})

    #this parses the html content using the lxml parser
    soup = BeautifulSoup(content.text, 'lxml')

    #this method extracts all the job listings that have that class attribute
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    #this method finds the job name

    #this for loop loops through all job postings
    for index, job in enumerate(jobs): 
        #this method post the date
        post_date = job.find('span', class_= "sim-posted").span.text
        #this condition checks for few days to filter out older post
        if 'few' in post_date:
            company_name = job.find('h3', class_= "joblist-comp-name").text.strip().replace('','')
            #this method finds the skill needed for the job
            skill = job.find('span', class_="srp-skills").text.strip().replace('','')
            #this method finds a css selector of job location
            location = job.select('span[title="Kolkata"]')
            location_content = [loc.text.strip() for loc in location]
            #this method finds the tag with more info for each job listing
            more_info = job.header.h2.a['href']
            #this filters out users unfamiliar skills and only prints out skills familiar
            if unfamiliar_skill not in skill:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company name: {company_name}\n")
                    f.write(f"Location: {location_content}\n")
                    f.write(f"Required Skills: {skill}\n")
                    f.write(f"Post date: {post_date}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f'File saved: {index}')

#this creates a loop that will refresh the feed every hour
if __name__ == '__main__':
    while True:
        find_jobs()
        refresh = time.sleep(3600)
        print(f"Waiting {refresh} hour...")
            
        




