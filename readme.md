# Bookapp
 ## Table of contents
* [General info](#general-info)
* [Tech info](#tech-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Future Development](#future-development)

## General Info
This is a final project for CODE:ME's Python basics course. 
Bookapp is a book collection manager web app that helps you stay on top of your home library. Adding items is easy thanks to the integration with the ISBN database that includes millions of books. You can delete records and amend them as necessary. Additionally, you can add tags and scores.

## Tech Info
Technology used:
* Python 3
* SQLite module
* Flask framework
* ISBN DB API: https://isbndb.com/apidocs/v2

## Setup
To run this project, install it locally using npm:

```
$ cd ../Bookapp
$ npm install
$ npm start
```

## Features
The current solution features include:
* Adding a book record manually
* Deleting book records
* Amending book records

## Status
Work in progress

## Future Development
Future development of this software includes but is not limited to:

#### Phase 1.1 (in progress)
* Searching the ISBN database by the ISBN number, author or title and adding selected item to the local sql database
* Migrate the console program into a web app using the Flask framework

##### Phase 1.2
The next improvements will include:
* Adding tags/keywords
* Adding scores and comments
* Marking books as read

##### Phase 2
* Creating reading plan/queue with goals/deadlines
* Integration with lubimyczytac.pl and/or goodreads.com
* Recommendations algorithm combining user scores, key words and online ratings
* Creating book shopping lists based on recommendations

##### Phase 3
* Mobile app development
* Adding an OCR-based ISBN scanner

##### Phase 4
* Sharing recommendations with other app users