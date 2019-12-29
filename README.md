# kinder_project
A second year, First semester project

1) So, basically when you clone the code and run the server and enter information/ perform any action it will change the pycache and the 
	database. So, the next time you write "git status" wll obviously show you tons of changes to commit before working on the file again. 
	You can freely work on the project and add all the changes and commit them together and need not worry about the unfamiliar changes. 
	It took me some time to figure this out. So, I thought it would be better to share it early.

2 )Django officially supports the following databases:

PostgreSQL
MariaDB
MySQL
Oracle
SQLite 
After a thorough research, I found SQLite to be the compatible and easy one. So, we'll be using SQLite.


3) The only thing remaining in sign up is the id-checking procedure which will be done after the databases are handled. The default user model in django could not be changed.
So, I have extended it by adding another form.
