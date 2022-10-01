# Python-WebScraper
TITLE :- PyScraperr


DESCRIPTION :- This Repository contains the Script to legally scrape websites using Python and BeautifullSoup Library.

ABOUT THE PROJECT :- There are 2 projects.
    
   1. HackerNews.py
   
      In this project we will be legally scraping HackerNews website and fetching the news with more than 100 upvotes.

   2. gsoc1.py
   
      In this project we will be legally scraping GSOC website to fetch the organization names of the given years which uses python and all the technologies used by that 
      organizations.
      
      (NOTE:- can change the years in the code as per the choice)
      
      gsoc.txt file contains the data from 2016-2020 
   

THE REQUIRED TOOLS :-
   
   * requests :- The requests module is not a built in module, This module needs to be downloaded. This module is used to make requests to the browser during runtime.
    
            pip install requests
        
   * beautifulsoup :- Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and 
                      modifying the parse tree. It commonly saves programmers hours or days of work.
                      
            pip install beautifulsoup
        
        
   * pprint :- Short for Pretty Printer, pprint is a native Python library that allows you to customize the formatting of your output.
   
            pip install pprint
            
   
WHAT YOU CAN AND WHAT YOU CANT :-
   
   * Most of the websites do not want their websites to be scraped, hence they give us a text file called robots.txt which gives us the information about what we can  scrape and what we cant.
     
   * For ex:- https://news.ycombinator.com/robots.txt this link here takes us to the text file page which has the info about what we can   
     scrape and what we cant from hackernews website.
     
   * Hence it is always better to check robots.txt before scraping any websites so that we can scrape ethically.

API V/S WEB SCRAPING :-
    
   *  There are 2 ways of fetching data from websites, they are using API and web scraping.
   
   *  Many websites have their own API which gives us the access to their websites data, however there are some restrictions.
   
   *  some of the restrictions are you wont get access to all their data and there will be a rate limit.
   
   *  There are 3 types of API's :-
           
        -> Free API for example Password API.
            
        -> Permissive API for example Twitter API.
           
        -> Paid API for example Google Maps API.

   * If the webites does not have API then we can scrape that website to fetch data.
   
   * There are many web scraping libraries in python. some of them are Beautifulsoup, scrapy, selenium etc.
   
   * In both the projects we will be using beautifulsoup library.
   
   * For more information about webscraping libraries please read this Tasty Yummy article :) 
     https://elitedatascience.com/python-web-scraping-libraries 

    
