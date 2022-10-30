# Url Classification

## Authors

| <img src="https://avatars.githubusercontent.com/u/61507252?v=4" alt="profile image" width="140px"> | <img src="https://avatars.githubusercontent.com/u/61550370?v=4" alt="profile image" width="140px" />  |  <img src="https://avatars.githubusercontent.com/u/59376626?v=4" alt="profile image" width="140px" />  |
| :------------: | :------------: |:------------: |
|  *Breiner Carranza* | *Cristopher González*  | *Derian Rodríguez*  | 

<br/>

## What does it consist of

> ### Web Scrapping
<div style="text-align: justify">
This performs a tour of the text found in each of the urls, in case the url is invalid, it identifies it as such. This text extraction is done through BeautifulSoup, with which you can go through the tags found in the body of the page and extract the string data found in them, finally, all this is stored in a JSON file.
</div>
<br/>

> ### Multiprocess
<div style="text-align: justify">
Multiprocessing is of great importance in this app, due to the large amount of information that must be processed to obtain an effective result and it is necessary to distribute the workload in more than one process and thus obtain a more effective result. The multiprocess is implemented in two parts of the app, first it is used in the execution of web scrapping, in which 4 processes are used which apply web scrapping to 4 urls simultaneously. The second multiprocess application is in the analysis of the text previously extracted from the url, in the same way 4 processes are used to identify the words of each category per web page.
</div>
<br/>

> ### Bayes theorem
<div style="text-align: justify">
To apply this analysis we must use the 4 main data, which are: total games, total computation, total invalid pages and total links. Now we are going to be able to calculate the prior probability of the computer and games categories, this consists of dividing between the total of the category and the total of links, then by dividing between the total of words of each category and the total of this category (example: total game words/total games), the incidence probability of the categories is calculated. With the multiplication of the prior probability and the incidence probability, we obtain the probability of each category, with this we can compare who is greater and categorize it, in case their probabilities are equal, it is categorized as invalid. Another case in which it is categorized as invalid is that the number of words in both categories is less than 7.
</div>
<br/>

> ### Sample data on the web
<div style="text-align: justify">
A bar graph is created in which it shows us the amount identified in all the urls of the three categories, in this way the results obtained are shown much more clearly, other than that it is shown on the web being easier to access.
</div>
<br/>

## Instalation

> ### How to clone

`git clone https://github.com/cris-gs/url-classification.git`
<br/>

> ### Install dependencies
 
 - **Multiprocessing**
 `pip install multiprocessing` 
 <br/> 

 - **Pandas**
 `pip install pandas`
 <br/>

 - **Requests**
 `pip install requests`
 <br/>

 - **Bs4**
 `pip install bs4`
 <br/>

 - **Dash**
 `pip install dash`
 <br/>

 - **Plotly**
 `pip install plotly`
 <br/>

> ### How to run it

- First we must execute the `web_scraping.py` in which the web scraping will be applied to the urls, extracting the text and saving it in the json file `datos.json`
<br/>

- Second we must execute the `main.py` in which the words of each page will be evaluated, grouping them by category in the json file `datos.json`
<br/>

- Third, we are going to run `urlClassification.py`, it applies Bayesian analysis and saves the results to the json file `dataCategories.json`
<br/>

- Fourth and last, we are going to execute `dashboard.py`, it interprets the data in graphs, and gives us a url in the console, which we must open with the browser
<br/>

This is executed in this sequence of steps so that the interaction time with the data is not so long due to the large number of urls that are analyzed, however, if we want to execute everything in the same step, we can call the functions directly in `main.py` and only run once.
<br/>

## Time Comparative

**Web Scraping**

Sequential time: 16126.5082452297 seconds.

Parallel time: 4278.2422530651 seconds.

**Identify the words of each category by web page**

Sequential time: 4.5470371246 seconds.

Parallel time: 1.9183907509 seconds.