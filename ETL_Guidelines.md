# Guidelines for ETL Project

This document contains guidelines, requirements, and suggestions for the ETL Project. 

These guidelines have been customized for class `UCF-LKM-DATA-PT-11-2019-U-C`.

## Team Effort

Due to the short timeline, teamwork will be crucial to the success of this project! Work closely with your team through all phases of the project to ensure that there are no surprises at the end of the week.

Working in a group enables you to tackle more difficult problems than you'd be able to working alone. In other words, working in a group allows you to **work smart** and **dream big**. Take advantage of it!

Since it's only a week, you will _not_ have a presentation for this project.

## Project Proposal

Before you start writing any code, remember that you only have one week to complete this project. View this project as a typical assignment from work. Imagine a bunch of data came in and you and your team are tasked with migrating it to a production data base, then creating a means for your customers to consume this data.

Take advantage of your Instructor and TA support during class project work time. They are a valuable resource and can help you stay on track.

## Finding Data

Your project must use 2 or more sources of data (it is okay to break one large (~15+ columns) csv into two, but you should normalize or perform some data cleaning on it). We recommend the following sites to use as sources of data:

* [data.world](https://data.world/)

* [Kaggle](https://www.kaggle.com/)

* [Google Dataset Search](https://datasetsearch.research.google.com/)

You can also use APIs or data scraped from the web. However, get approval from your instructor first. Again, there is only a week to complete this!

## Data Cleanup & Analysis

Once you have identified your datasets, perform ETL on the data. Make sure to plan and document the following:

* The sources of data that you will extract from.

* The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).

* The type of final production database to load the data into (relational or non-relational).

* The final tables or collections that will be used in the production database.

## API with documentation

Once you have loaded your data into a database, the results should be served via an API for users to consume.

* Create a minimum of _one_ API endpoint that serves some subset of data from your database.

* If something goes wrong at the endpoint (either because of user error or an issue with your server), return an error to your user. 

    It may be helpful to review HTTP Status Code meanings when designing your returns: [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)
    
    * Server errors should be reported with a 500 HTTP Status Code.
    * User errors should be reported with a 400, 403, or 404 HTTP Status Code. 

* Create a responsive homepage (your `/` Flask root route), styled using Bootstrap, with API documentation to demonstrate how to use your API:

    * Document your return types:
        * Returned object should be a list of JSON objects (i.e. Python dictionaries) or a single JSON object.
        * Also document returned attributes: 
        
            `name`: `type` - `description`
          
            e.g. `ChicagoCrimes.CreateDate`: `DATETIME` - datetime crime was entered in the database
            
    * *(If you have user parameters)* User parameter meanings and acceptable values
    * Explain errors that can be returned by your API and how the user can fix their query to avoid them.

* Choose carefully; what uses would your endpoint have to a potential consumer?

You will be required to submit a final technical report with the above information, the steps required to reproduce your ETL process, and your API documentation and design reasoning.

## Extra Credit

If you finish early, take some time to polish your work so you can easily include it in your portfolios ...

... by deploying it online!

You can use:

* ***Recommended:*** Github Pages 
    * (It won't be able to connect to your database, but you should include your static pages like the API documentation, a page for your Final Report, and optionally a static sample of what your API return might look like.)
    
* Heroku/ PythonAnywhere to actually host your Flask server and database, as well as your Flask-served API documentation. (We'll teach this formally later on).

## Project Report

At the end of the week, your team will submit a Final Report (via your Github README.md) that describes the following:

* ETL Work:

    * **E**xtract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).
    * **T**ransform: what data cleaning or transformation was required.
    * **L**oad: the final database, tables/collections, and why this was chosen.

* API Documentation - you can copy-paste this into a word document, or provide a link to the index.html page on your github (if your API documentation is on static pages).

* Why did you choose the endpoint(s) you did for your API? For example: 

    * Give users the ability to select just the subset of your data they need? 
    * Were you aiming to provide a full export of your dataset for others to consume? 
    * Optionally, include a few examples of how to make use of your API.

Please upload the report to Github and submit a link to Bootcampspot.

- - -

### Copyright

Coding Boot Camp © 2019. All Rights Reserved.
