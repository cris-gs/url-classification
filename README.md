# Url Classification

## Authors

| <img src="https://avatars.githubusercontent.com/u/61507252?v=4" alt="profile image" width="140px"> | <img src="https://avatars.githubusercontent.com/u/61550370?v=4" alt="profile image" width="140px" />  |  <img src="https://avatars.githubusercontent.com/u/59376626?v=4" alt="profile image" width="140px" />  |
| :------------: | :------------: |:------------: |
|  *Breiner Carranza* | *Cristopher González*  | *Derian Rodríguez*  | 

<br/>

## What does it consist of

> ### Web Scrapping

<br/>

> ### Multiprocess

<br/>

> ### Bayes theorem

<br/>

> ### Sample data on the web

<br/>

## Instalation

> ### How to clone

`git clone https://github.com/cris-gs/url-classification.git`
<br/>

> ### Install dependencies
> 
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

- First we must execute the `main.py` in which the web scraping will be applied to the urls, evaluating the words and saving the results in the json file `datos.json`
<br/>

- Second, we are going to run `urlClassification.py`, it applies Bayesian analysis and saves the results to the json file `dataCategories.json`
<br/>

- Third and last, we are going to execute `dashboard.py`, it interprets the data in graphs, and gives us a url in the console, which we must open with the browser
<br/>

<div style="text-align: justify">
This is executed in this sequence of steps so that the interaction time with the data is not so long due to the large number of urls that are analyzed, however, if we want to execute everything in the same step, we can call the functions directly in `main.py` and only run once.
</div>
<br/>

## Time Comparative