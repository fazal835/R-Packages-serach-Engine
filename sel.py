import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

title=[]
description=[]
url = "https://cran.r-project.org/web/views/MachineLearning.html"


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
links=[]


links=driver.find_elements_by_xpath("/html/body/ul[1]/li/a")

for link in links:
    urli=link.get_attribute('href')
    driveri = webdriver.Chrome()
    driveri.implicitly_wait(30)
    driveri.get(urli)
    titlei=driveri.find_element_by_xpath("/html/body/h2")
    x1=titlei.text
    title.append(x1)
    descriptioni=driveri.find_element_by_xpath("/html/body/p[1]")
    x2=descriptioni.text
    description.append(x2)
    driveri.quit()

d = {'Title':title,'Description':description}
df=pd.DataFrame(d)
df.to_csv('file4.csv',index=False)     
driver.quit()

