# Assignment 2 - SERC Website
A website for a SERC Research Lab.

## Dependencies for Running Locally
* python 3
* pip3
  * `sudo apt install python3-pip`
* pipenv
  * `pip3 install --user pipenv`

## Basic Build Instructions

 ```bash 
      cd 2021202022/
      pipenv install
      pipenv run python3 app.py
  ```
Open http://127.0.0.1:5000/

## Admin Mode

In all admin pages, the  [CK editor]([https://ckeditor.com/), a WYSIWYG rich text editor that allows you to write content directly inside web pages, is used.
The modifications are permanently saved in the sqlite database. 
* http://127.0.0.1:5000/admin-about 
* http://127.0.0.1:5000/admin-news
* http://127.0.0.1:5000/admin-focus
* http://127.0.0.1:5000/admin-posters

The page will be redirected and the modifications will be displayed immediately after hitting the `update` button. 

