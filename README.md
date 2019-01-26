# Logs Analysis Project

This project is intended to provide an internal reporting tool to a newspaper site. The frontend and the database already exist. The database contains articles, authors, and a log of pages visited by readers. The internal reporting tool to be built will query the database on reader activity.

## Table of Contents

* [Description of the Project](#description-of-the-project)
* [Getting Started](#getting-started)
* [Contributing](#contributing)

## Description of the Project

The program that implements the project's functionality interacts with a PostgreSQL database, and features three complex queries, which will are described below:

### What are the most popular three articles of all time?

 This query has been implemented by a left join between the articles and the log tables. The condition of the join is that the articles' slug equals the log's path. Results are grouped by the articles' title, and sorted in descending order by the number of views each title receives. Resulting articles are limited to three occurrences, and both articles' title and number of views per title (via aggregation) are selected.

### Who are the most popular article authors of all time?

This query has been implemented by a join of three tables: authors, articles, and log. The condition of the join is that the articles' slug equals the log's path, and that the authors' id equals the articles' author. Results are grouped by the authors' name, and sorted in descending order by the number of views each author receives. Both authors' name and number of views per author (via aggregation) are selected.

### On which days did more than 1% of requests lead to errors?

This query has been implemented by a join between two subqueries:

* The first subquery retrieves date, and total number of requests per date (via aggregation) from the log table. To this end, results are grouped by date.
* The second subquery does exactly the same as the first subquery, but this time only unsuccessful requests are considered.

The condition of the join is that the date of the first subquery equals the date of the second subquery. In addition, only those results of the join where more than 1% of requests led to errors are chosen. Results are sorted in descending order by date. Both date, and percentage of unsuccessful requests are selected.

## Getting Started

The program built as part of this project, news.py, is run within a Linux-based virtual machine (VM). In order to run this program, you must:

* Install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/).
* Configure the VM. To this end, fork and clone [this Github repository](https://github.com/udacity/fullstack-nanodegree-vm). Then, cd to the newly created directory, and then to the vagrant directory.
* Run `vagrant up` to start the virtual machine, and `vagrant ssh` to log in to it.
* Put the newsdata.sql into the vagrant directory. This directory is outside your VM, but it is shared with it.
* Log in to the VM, cd to the /vagrant directory, and execute `psql -d news -f newsdata.sql`. This command creates and populates the database by executing the commands in the newsdata.sql file.
* That's it! You can now run the news.py file from the command line within the VM, in the /vagrant directory. As a result, its queries  will be executed, and you will be able to see their results.

This project is made up of a number of files. The main ones are:

* news.py: It contains the source code of the Python program that implements the queries which are the main goal of this project.
* newsdata.sql: It contains the commands that create and populate the news database. This file has been provided to the project, and, as a result, has not been developed as part of it.
* output.txt: It contains an example of the output of the program.
* README.md: It contains the documentation file you are viewing right now.

## Contributing

This repository contains all the code that makes up the application. Individuals and I myself are encouraged to further improve this project. As a result, I will be more than happy to consider any pull requests.