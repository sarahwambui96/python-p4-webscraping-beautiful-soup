from turtle import ht
from bs4 import BeautifulSoup
import requests

# defining headers helps to remove error that comes because the website may be trying to prevent bots
headers = {'user-agent': 'my-app/0.0.1'}
# grab the html that makes up flatiron school's landing page
html = requests.get("https://flatironschool.com/", headers=headers)
# save the html documnt in a variable that we can work on
doc = BeautifulSoup(html.text, "html.parser")
# printing out doc will give the whole html of that landing page in our terminal
# print(doc)
# use CSS selector to print header that is on the landing page
# printing it like this will bring some dense info
print(doc.select(".heading-primary"))
# to only print the content of that element print like this: you can use strip to remove white space
print(doc.select(".heading-primary")[0].contents)
# want to grab the courses offered and are defined on the landing page
# this will help show how to iterate over elements
html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
# save the elements in a variable
doc = BeautifulSoup(html.text, "html.parser")
# print all the elements
print(doc.select(".heading-25-extrabold.color-black"))
# assign the elements a variable so that we can iterate over that variable using a for loop
courses = doc.select(".heading-25-extrabold.color-black")
for course in courses:
    print(course.contents[0].strip())
# we can get the tag name of the elements
name = doc.select(".heading-25-extrabold.color-black")[0].name
print(name)
# get all the attributes of the first element
attr = doc.select(".heading-25-extrabold.color-black")[0].attrs
print(attr)
