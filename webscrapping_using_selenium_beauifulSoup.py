#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


from sqlalchemy import create_engine


# In[5]:


import requests


# In[6]:


url = "https://drive.google.com/uc?export=download&id=1WFt7B84LTHhMueoKmz8W-PRo7xXqmZf3"
response = requests.get(url)
sql_script = response.text


# In[9]:


sql_script


# In[3]:


engine=create_engine("mysql+pymysql://root:@localhost/ipl")


# In[ ]:


import requests
import pandas as pd
import sqlite3
from io import BytesIO
from openpyxl import Workbook

# Step 1: Download the SQL file content
url = "https://drive.google.com/uc?export=download&id=1WFt7B84LTHhMueoKmz8W-PRo7xXqmZf3"
response = requests.get(url)
sql_script = response.text

# Step 2: Set up an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Step 3: Execute the SQL script
conn.executescript(sql_script)

# Step 4: Load each table into a DataFrame
tables = ["invoices", "order_leads", "sales_sql"]
dfs = {table: pd.read_sql_query(f"SELECT * FROM {table}", conn) for table in tables}

# Step 5: Write the data to an Excel file with separate sheets
with pd.ExcelWriter("output_data.xlsx") as writer:
    for table, df in dfs.items():
        df.to_excel(writer, sheet_name=table, index=False)

# Close the database connection
conn.close()

print("Data has been written to 'output_data.xlsx' with each table on a separate sheet.")


# In[8]:


import pandas as pd
with engine.connect() as connection:
    result = pd.read_sql_query(sql_script, connection)

# Display or use the result DataFrame
print(result)


# In[4]:


#reading sql file 
with open("https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1WFt7B84LTHhMueoKmz8W-PRo7xXqmZf3%2Fview%3Fusp%3Dshare_link","r") as sql_file:
    sql_script=sql_file.read()
# Execute SQL script and load data into a pandas DataFrame
with engine.connect() as connection:
    result = pd.read_sql_query(sql_script, connection)

# Display or use the result DataFrame
print(result)


# Go to the site: https://rapidapi.com/wirefreethought/api/geodb-cities. From here, you have to grab the API and have to choose proper routes to get the cities of different countries. After getting the right API, hit that API and create a dataframe of all the cities that you can get by using the API. Then store the dataframe to a SQL. If you need to create an account or have to subscribe, then do that (it has free subscription but has some limitations. Use that free subscription and modify your accordingly to get all the data).

# In[10]:


import requests
import pandas as pd


# In[23]:


import http.client

conn = http.client.HTTPSConnection("wft-geo-db.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c94655ac30msh0bea98c108783e4p1bd123jsn52be5325f750",
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
}

conn.request("GET", "/v1/geo/cities", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


# In[25]:


data


# In[26]:


string_data=data.decode("utf-8")
string_data


# In[27]:


import json
dict_data=json.loads(string_data)
dict_data


# In[28]:


dict_data["data"]


# In[29]:


pd.DataFrame(dict_data["data"])


# In[13]:


url="https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
res=requests.get(url,headers="x-rapidapi-key: c94655ac30msh0bea98c108783e4p1bd123jsn52be5325f75")
print(res.text)


# In[30]:


import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D/distance"

querystring = {"toPlaceId":"Q60"}

headers = {
	"x-rapidapi-key": "c94655ac30msh0bea98c108783e4p1bd123jsn52be5325f750",
	"x-rapidapi-host": "wft-geo-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


# Problem 3:
# Go to this url: https://www.flipkart.com/search?q=smartphones. This is the url to find phones in flipkart website. You have to extract the below things:
# 
# image url of the phone
# name of the image
# average ratings
# total ratings
# total reviews
# discounted price
# actual price
# Extract all the phones which are available in this website. So you have to use the pagination concept. Also after requesting every page through the url, please wait for a while (minimum 2-3 seconds), otherwise your IP address can be banned to access the flipkart website later.
# 
# After collecting all the data, save that in a JSON file.

# In[34]:


import time
print("dhoni")
time.sleep(4)
print("mahi")


# In[35]:


import requests 
import pandas as pd
from bs4 import BeautifulSoup 


# In[41]:


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
url="https://www.flipkart.com/search?q=smartphones&page=1"


# In[ ]:


<div class="tUxRFH" data-tkid="416a8212-91b8-4ae5-a952-b7fcdb6d45b5.MOBGTAGPTB3VS24W.SEARCH"><a class="CGtC98" target="_blank" rel="noopener noreferrer" href="/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&amp;lid=LSTMOBGTAGPTB3VS24WVZNSC6&amp;marketplace=FLIPKART&amp;q=smartphones&amp;store=tyy%2F4io&amp;spotlightTagId=BestsellerId_tyy%2F4io&amp;srno=s_1_1&amp;otracker=search&amp;fm=organic&amp;iid=416a8212-91b8-4ae5-a952-b7fcdb6d45b5.MOBGTAGPTB3VS24W.SEARCH&amp;ppt=sp&amp;ppn=sp&amp;ssid=ni433czb800000001730976867638&amp;qH=6ea4465d0add4685"><div><div class="UzRoYO CmflSf" style="background: rgb(0, 160, 152);">Bestseller</div></div><div class="Otbq5D"><div class="yPq5Io"><div><div class="_4WELSP" style="height: 200px; width: 200px;"><img loading="eager" class="DByuf4" alt="Apple iPhone 15 (Black, 128 GB)" src="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/h/d/9/-original-imagtc2qzgnnuhxh.jpeg?q=70"></div></div></div><div class="qaR90o"><div class="A8uQAd"><span class="Lni97G"><label class="tJjCVx"><input type="checkbox" class="vn9L2C" readonly=""><div class="XqNaEv"></div></label></span><label class="uu79Xy"><span>Add to Compare</span></label></div></div><div class="oUss6M ssUU08"><div class="+7E521"><svg xmlns="http://www.w3.org/2000/svg" class="N1bADF" width="16" height="16" viewBox="0 0 20 16"><path d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" class="x1UMqG" stroke="#FFF" fill-rule="evenodd" opacity=".9"></path></svg></div></div></div><div class="yKfJKb row"><div class="col col-7-12"><div class="KzDlHZ">Apple iPhone 15 (Black, 128 GB)</div><div class="_5OesEi"><span id="productRating_LSTMOBGTAGPTB3VS24WVZNSC6_MOBGTAGPTB3VS24W_" class="Y1HWO0"><div class="XQDdHH">4.6<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="Rza2QY"></div></span><span class="Wphh3N"><span><span>2,05,243 Ratings&nbsp;</span><span class="hG7V+4">&amp;</span><span>&nbsp;7,149 Reviews</span></span></span></div><div class="_6NESgJ"><ul class="G4BRas"><li class="J+igdf">128 GB ROM</li><li class="J+igdf">15.49 cm (6.1 inch) Super Retina XDR Display</li><li class="J+igdf">48MP + 12MP | 12MP Front Camera</li><li class="J+igdf">A16 Bionic Chip, 6 Core Processor Processor</li><li class="J+igdf">1 year warranty for phone and 1 year warranty for in Box Accessories.</li></ul></div></div><div class="col col-5-12 BfVC2z"><div class="cN1yYO"><div class="hl05eU"><div class="Nx9bqj _4b5DiR">₹58,999</div><div class="yRaY8j ZYYwLA">₹69,900</div><div class="UkUFwK"><span>15% off</span></div></div><div class="k6cAZE dlFt9U"><div><div class="yiggsN" style="color: rgb(0, 0, 0); font-size: 12px; font-weight: 400;">Free delivery</div></div></div></div><div class="_0CSTHy"><img height="21" src="//static-assets-web.flixcart.com/fk-p-linchpin-web/fk-cp-zion/img/fa_62673a.png"></div><div class="M4DNwV"><div class="n5vj9c"><div class="yiggsN O5Fpg8" style="color: rgb(38, 165, 65); font-size: 12px; font-style: normal; font-weight: 700;">Save extra with combo offers</div></div></div><div class="M4DNwV"><div class="n5vj9c"><div class="yiggsN O5Fpg8" style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-weight: 400;">Upto </div><div class="yiggsN O5Fpg8" style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-weight: 700;">₹32,950</div><div class="yiggsN O5Fpg8" style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-weight: 400;"> Off on Exchange</div></div></div></div></div></a></div>


# In[44]:


res=requests.get(url).text
soup=BeautifulSoup(res,'lxml')
soup


# In[45]:


a1=soup.find_all('div',class_="tUxRFH")
print(a1)


# In[46]:


pip install selenium


# In[11]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver (ensure the chromedriver is in your PATH)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode for less detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
driver = webdriver.Chrome(options=options)

url = "https://www.flipkart.com/search?q=smartphones&page=1"
driver.get(url)
time.sleep(3)  # Wait to ensure the page loads completely

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())

driver.quit()


# In[14]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

# Set up the Selenium WebDriver (ensure the chromedriver is in your PATH)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode for less detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
driver = webdriver.Chrome(options=options)
am=[]
for j in range(1,20):
    url = "https://www.flipkart.com/search?q=smartphones&page={}".format(j)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.quit()
    a1=soup.find_all('div',class_="tUxRFH")
# print(a1)
    image_url=[]
    image_name=[]
    phone_rating=[]
    phone_num_ratings=[]
    phone_num_reviews=[]
    cost_without_discount=[] 
    cost_with_discount=[]
    for i in a1:
        try:
            image_url.append(i.find('img',class_="DByuf4")['src'])
        except:
            image_url.append(np.nan)
        try:
            image_name.append(i.find('img',class_="DByuf4")['alt'])
        except:
            image_name.append(np.nan)
        try:
            phone_rating.append(i.find('div',class_="XQDdHH").text.strip())
        except:
            phone_rating.append(np.nan)
        try:
            phone_num_ratings.append(i.find('span',class_="Wphh3N").find_all('span')[1].text.strip())
        except:
            phone_num_ratings.append(np.nan)
        try:
            phone_num_reviews.append(i.find('span',class_="Wphh3N").find_all('span')[3].text.strip())
        except:
            phone_num_reviews.append(np.nan)
        try:
            cost_without_discount.append(i.find('div',class_="yRaY8j ZYYwLA").text)
        except:
            cost_without_discount.append(np.nan)
        try:
            cost_with_discount.append(i.find('div',class_="Nx9bqj _4b5DiR").text)
        except:
            cost_with_discount.append(np.nan)
    df=pd.DataFrame({
        'image_url':image_url,
        'image_name':image_name,
        'phone_rating':phone_rating,
        'phone_num_ratings':phone_num_ratings,
        'cost_without_discount':cost_without_discount,
        'cost_with_discount':cost_with_discount
    })
    am.append(df)
    image_url.clear()
    image_name.clear()
    phone_rating.clear()
    phone_num_ratings.clear()
    cost_without_discount.clear()
    cost_with_discount.clear()
    time.sleep(4)
    
    


# In[17]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

# Set up the Selenium WebDriver (ensure the chromedriver is in your PATH)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode for less detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
driver = webdriver.Chrome(options=options)

# Initialize an empty list to store data from all pages
am = []

try:
    # Loop through pages
    for j in range(1, 20):
        url = f"https://www.flipkart.com/search?q=smartphones&page={j}"
        driver.get(url)  # Open page in the same browser session
        time.sleep(4)  # Wait to avoid IP block

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'lxml')
        a1 = soup.find_all('div', class_="tUxRFH")

        # Initialize lists for the current page
        image_url = []
        image_name = []
        phone_rating = []
        phone_num_ratings = []
        phone_num_reviews = []
        cost_without_discount = [] 
        cost_with_discount = []

        # Extract details from each element
        for i in a1:
            try:
                image_url.append(i.find('img', class_="DByuf4")['src'])
            except:
                image_url.append(np.nan)
            try:
                image_name.append(i.find('img', class_="DByuf4")['alt'])
            except:
                image_name.append(np.nan)
            try:
                phone_rating.append(i.find('div', class_="XQDdHH").text.strip())
            except:
                phone_rating.append(np.nan)
            try:
                phone_num_ratings.append(i.find('span', class_="Wphh3N").find_all('span')[1].text.strip())
            except:
                phone_num_ratings.append(np.nan)
            try:
                phone_num_reviews.append(i.find('span', class_="Wphh3N").find_all('span')[3].text.strip())
            except:
                phone_num_reviews.append(np.nan)
            try:
                cost_without_discount.append(i.find('div', class_="yRaY8j ZYYwLA").text)
            except:
                cost_without_discount.append(np.nan)
            try:
                cost_with_discount.append(i.find('div', class_="Nx9bqj _4b5DiR").text)
            except:
                cost_with_discount.append(np.nan)

        # Append the data for the current page to a DataFrame
        df = pd.DataFrame({
            'image_url': image_url,
            'image_name': image_name,
            'phone_rating': phone_rating,
            'phone_num_ratings': phone_num_ratings,
            'phone_num_reviews': phone_num_reviews,
            'cost_without_discount': cost_without_discount,
            'cost_with_discount': cost_with_discount
        })
        am.append(df)

finally:
    # Ensure the driver quits after the loop finishes
    driver.quit()

# Concatenate all data frames into a single data frame
all_data = pd.concat(am, ignore_index=True)
all_data['cost_without_discount']=all_data['cost_without_discount'].str.replace('â‚¹', '₹')
all_data['cost_with_discount']=all_data['cost_with_discount'].str.replace('â‚¹', '₹')

# Optional: save the data to a CSV or JSON file
all_data.to_csv("D:/flipkartsmartphones_data1.csv", encoding='utf-8', index=False)


# In[18]:


#We were getting error in the previous code because we had written driver.quit() within the outer loop as a result of which the
#the driver was getting quit immediately during the first loop...hence we have written driver.quit() after the end of the loop
#and used a driver.quit() within a try finally block so that the resources get quit even if there is a error...if resources are
#held up then that can lead to the computer slowing down


# In[12]:


j1=21
"ms d is a great warrior {}".format(j1)


# Div class below

# In[9]:


import numpy as np
a1=soup.find_all('div',class_="tUxRFH")
# print(a1)
image_url=[]
image_name=[]
phone_rating=[]
phone_num_ratings=[]
phone_num_reviews=[]
cost_without_discount=[] 
cost_with_discount=[]
for i in a1:
    try:
        image_url.append(i.find('img',class_="DByuf4")['src'])
    except:
        image_url.append(np.nan)
    try:
        image_name.append(i.find('img',class_="DByuf4")['alt'])
    except:
        image_name.append(np.nan)
    try:
        phone_rating.append(i.find('div',class_="XQDdHH").text.strip())
    except:
        phone_rating.append(np.nan)
    try:
        phone_num_ratings.append(i.find('span',class_="Wphh3N").find_all('span')[1].text.strip())
    except:
        phone_num_ratings.append(np.nan)
    try:
        phone_num_reviews.append(i.find('span',class_="Wphh3N").find_all('span')[3].text.strip())
    except:
        phone_num_reviews.append(np.nan)
    try:
        cost_without_discount.append(i.find('div',class_="yRaY8j ZYYwLA").text)
    except:
        cost_without_discount.append(np.nan)
    try:
        cost_with_discount.append(i.find('div',class_="Nx9bqj _4b5DiR").text)
    except:
        cost_with_discount.append(np.nan)
        
        
        
cost_with_discount
    
    


# In[ ]:


<div class="Nx9bqj _4b5DiR">₹11,499</div>


# In[8]:


a1[9].find('div',class_="Nx9bqj _4b5DiR").text


# In[ ]:


<span class="Wphh3N"><span><span>52,279 Ratings&nbsp;</span><span class="hG7V+4">&amp;</span><span>&nbsp;1,705 Reviews</span></span></span>


# In[ ]:


<div class="yRaY8j ZYYwLA">₹15,499</div>


# In[6]:


a1[9].find('div',class_="yRaY8j ZYYwLA").text


# In[4]:


a1[9].find('span',class_="Wphh3N").find_all('span')


# In[5]:


a1[9].find('span',class_="Wphh3N").find_all('span')[1].text


# In[6]:


a1[9].find('span',class_="Wphh3N").find_all('span')[1].text.strip()


# In[7]:


a1[9].find('span',class_="Wphh3N").find_all('span')[3].text.strip()


# In[33]:


#\xa0 is a non-breaking space which is meant to keep some texts in the same line.


# In[22]:


print(a1[15])


# In[ ]:


<div class="XQDdHH">4.4<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="Rza2QY"></div>


# In[27]:


a1[9].find('div',class_="XQDdHH").text.strip()


# In[16]:


a1[9].find('img')


# In[7]:


"https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/w/3/4/-original-imahyytukhkky5ew.jpeg?q=70" in image_url


# In[ ]:


<img loading="eager" class="DByuf4" alt="vivo T3x 5G (Crimson Bliss, 128 GB)" src="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/w/3/4/-original-imahyytukhkky5ew.jpeg?q=70">


# In[5]:


len(image_url)


# In[ ]:


<div class="tUxRFH" data-tkid="416a8212-91b8-4ae5-a952-b7fcdb6d45b5.MOBGTAGPTB3VS24W.SEARCH"><a class="CGtC98" target="_blank" rel="noopener noreferrer" href="/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&amp;lid=LSTMOBGTAGPTB3VS24WVZNSC6&amp;marketplace=FLIPKART&amp;q=smartphones&amp;store=tyy%2F4io&amp;spotlightTagId=BestsellerId_tyy%2F4io&amp;srno=s_1_1&amp;otracker=search&amp;fm=organic&amp;iid=416a8212-91b8-4ae5-a952-b7fcdb6d45b5.MOBGTAGPTB3VS24W.SEARCH&amp;ppt=sp&amp;ppn=sp&amp;ssid=ni433czb800000001730976867638&amp;qH=6ea4465d0add4685"><div><div class="UzRoYO CmflSf" style="background: rgb(0, 160, 152);">Bestseller</div></div><div class="Otbq5D"><div class="yPq5Io"><div><div class="_4WELSP" style="height: 200px; width: 200px;"><img loading="eager" class="DByuf4" alt="Apple iPhone 15 (Black, 128 GB)" src="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/h/d/9/-original-imagtc2qzgnnuhxh.jpeg?q=70"></div></div></div><div class="qaR90o"><div class="A8uQAd"><span class="Lni97G"><label class="tJjCVx"><input type="checkbox" class="vn9L2C" readonly=""><div class="XqNaEv"></div></label></span><label class="uu79Xy"><span>Add to Compare</span></label></div></div><div class="oUss6M ssUU08"><div class="+7E521"><svg xmlns="http://www.w3.org/2000/svg" class="N1bADF" width="16" height="16" viewBox="0 0 20 16"><path d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" class="x1UMqG" stroke="#FFF" fill-rule="evenodd" opacity=".9"></path></svg></div></div></div><div class="yKfJKb row"><div class="col col-7-12"><div class="KzDlHZ">Apple iPhone 15 (Black, 128 GB)</div><div class="_5OesEi"><span id="productRating_LSTMOBGTAGPTB3VS24WVZNSC6_MOBGTAGPTB3VS24W_" class="Y1HWO0"><div class="XQDdHH">4.6<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="Rza2QY"></div></span><span class="Wphh3N"><span><span>2,05,243 Ratings&nbsp;</span><span class="hG7V+4">&amp;</span><span>&nbsp;7,149 Reviews</span></span></span></div><div class="_6NESgJ"><ul class="G4BRas"><li class="J+igdf">128 GB ROM</li><li class="J+igdf">15.49 cm (6.1 inch) Super Retina XDR Display</li><li class="J+igdf">48MP + 12MP | 12MP Front Camera</li><li class="J+igdf">A16 Bionic Chip, 6 Core Processor Processor</li><li class="J+igdf">1 year warranty for phone and 1 year warranty for in Box Accessories.</li></ul></div></div><div class="col col-5-12 BfVC2z"><div class="cN1yYO"><div class="hl05eU"><div class="Nx9bqj _4b5DiR">₹58,999</div><div class="yRaY8j ZYYwLA">₹69,900</div><div class="UkUFwK"><span>15% off</span></div></div><div class="k6cAZE dlFt9U"><div><div class="yiggsN" style="color: rgb(0, 0, 0); font-size: 12px; font-weight: 400;">Free delivery</div></div></div></div><div class="_0CSTHy"><img height="21" src="//static-assets-web.flixcart.com/fk-p-linchpin-web/fk-cp-zion/img/fa_62673a.png"></div><div class="M4DNwV"><div class="n5vj9c"><div class="yiggsN O5Fpg8" style="color: rgb(38, 165, 65); font-size: 12px; font-style: normal; font-weight: 700;">Save extra with combo offers</div></div></div><div class="M4DNwV"><div class="n5vj9c"><div class="yiggsN O5Fpg8" style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-weight: 400;">Upto </div><div class="yiggsN O5Fpg8" style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-weight: 700;">₹32,950</div><div class="yiggsN O5Fpg8" style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-weight: 400;"> Off on Exchange</div></div></div></div></div></a></div>


# In[51]:


a1="<div class="phone-details"><span class="_2_R_DZ"><span><span>Rating: 4.5 stars</span></span><span><span>200 reviews</span></span></span></div>"


# In[52]:


from bs4 import BeautifulSoup

# Parse the HTML with BeautifulSoup
html_content = """
<div class="phone-details">
    <span class="_2_R_DZ">
        <span>
            <span>Rating: 4.5 stars</span>
        </span>
        <span>
            <span>200 reviews</span>
        </span>
    </span>
</div>
"""


# In[79]:


soup=BeautifulSoup(html_content,'lxml')
a1=soup.find_all('span',class_="_2_R_DZ")[0].find_all('span')[3].text.strip()
print(a1)


# In[53]:


soup=BeautifulSoup(html_content,'lxml')
a1=soup.find_all('span',class_="_2_R_DZ")
a1


# In[55]:


a1=soup.find_all('span',class_="_2_R_DZ")[0]
a1


# In[57]:


a1=soup.find_all('span',class_="_2_R_DZ")[0].find_all('span')
a1


# In[69]:


a1=soup.find_all('span',class_="_2_R_DZ")[0].find_all('span')[0].find_all('span')
a1


# In[70]:


a1=soup.find_all('span',class_="_2_R_DZ")[0].find_all('span')[0].find_all('span')[0]
a1


# In[71]:


a1=soup.find_all('span',class_="_2_R_DZ")[0].find_all('span')[0].find_all('span')[0].text
a1


# In[59]:


soup=BeautifulSoup(html_content,'lxml')


# In[60]:


span_with_class = soup.find_all('span', class_='_2_R_DZ')[0]
first_nested_span = span_with_class.find_all('span')[0]
text_value = first_nested_span.find_all('span')[0].text.strip()


# In[65]:


span_with_class1 = soup.find_all('span', class_='_2_R_DZ')
print(span_with_class1)


# In[66]:


first_nested_span1 = span_with_class.find_all('span')
print(first_nested_span1)


# In[67]:


text_value1 = first_nested_span.find_all('span')
print(text_value1)


# In[68]:


text_value2 = first_nested_span.find_all('span')[0]
print(text_value2)


# In[ ]:





# In[62]:


print(span_with_class)
# print(first_nested_span)
# print(text_value)


# In[63]:


print(first_nested_span)


# In[64]:


print(text_value)


# In[ ]:




