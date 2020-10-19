import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

title=[]
description=[]
url = "https://cran.r-project.org/web/views/Bayesian.html"


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
titles=[]
package=[]
description=[]
functions=[]
function_descs=[]
count={}

titles=driver.find_elements_by_xpath("/html/body/ul[1]/li/a")
g=0
error=0
for title in titles:
    '''if g==4:
        break
    g=g+1'''
    urli="https://www.rdocumentation.org/packages/"
    urli=urli+title.text
    driveri = webdriver.Chrome()
    driveri.implicitly_wait(30)
    driveri.get(urli)
    print(title.text)
    #package.append(title.text)

    z=driveri.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/section[1]/p")
    #description.append(z.text)

    x=[] #list of all functions
    x=driveri.find_elements_by_xpath("/html/body/div[2]/div[1]/section/div/section[2]/table/tbody/tr/td[1]/a")
    if x==[]:
        x=x=driveri.find_elements_by_xpath("/html/body/div[2]/div[1]/section/div/section[3]/table/tbody/tr/td[1]/a")
    index=0
    for function in x:
        print(function.text)
        functions.append(function.text)
        index=index+1
        package.append(title.text)
        description.append(z.text)
    y=[] #list of all desc_functions
    y=driveri.find_elements_by_xpath("/html/body/div[2]/div[1]/section/div/section[2]/table/tbody/tr/td[2]")
    if x==[] and y==[]:
        error=error+1
        
    if y==[]:
        y=y=driveri.find_elements_by_xpath("/html/body/div[2]/div[1]/section/div/section[3]/table/tbody/tr/td[2]")
    for function_desc in y:
        function_descs.append(function_desc.text)
        
    count[title]=index
    #package.append(index)
    index=0
    driveri.quit()
print(error)
d = {'Title':package,'Description':description,'functions':functions,'functions_descriptions':function_descs}
df=pd.DataFrame(d)
print(df)
df.to_csv('fle1.csv',index=False)  

driver.quit()

