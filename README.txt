# Item Catalog Application - Udacity

The item catalog application is the fourth project in Udacity's  [Full Stack Web Development Nanodegree ](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004) curriculum. 


## Project Overview

The aim of this project is to deploy skills such as developing **RESTful**  web applications that utilize python framework **Flask** along with OAuth authentication and implementation of **CRUD** based utilities to provide user friendly services.  The code provided in this repository runs on a local server and employs all the above techniques.

## Requirements

The project utilizes a host of dependencies which have already been made available in the **Vagrant file** provided by Udacity. Therefore, users are not required to install the aforementioned tools separately. To test this project install the following requirements :

 - [Python 3](https://www.python.org/download/releases/3.0/)
 - [Vagrant](https://www.vagrantup.com/)
 - [Udacity's Vagrant Folder](https://github.com/udacity/fullstack-nanodegree-vm)
 - [VirtualBox](https://www.virtualbox.org/)
 - [Git](https://git-scm.com/)

## How to run the project?

 1. If you don't already have the latest version of python download it from the link in requirements.
 2. Download and install Vagrant and VirtualBox.
 3. Download the Udacity vagrant [folder](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)  with preconfigured vagrant settings.
 4. Navigate to the Udacity folder in your bash interface and inside that cd into the vagrant folder.
 5. Open Git Bash and launch the virtual machine with`vagrant up`
 6. Once Vagrant installs necessary files use  `vagrant ssh`  to continue.
 7. Navigate to Udacity's vagrant folder on your file system in the computer.
 8. Inside folder visit the folder named */vagrant*.There is an empty folder *catalog* there with a Readme file that you can delete.
 9. Clone this repository and shift its folder inside vagrant where you deleted catalog.
 10. In *git bash* navigate to the repository folder. Once inside that folder first type the command `python database_setup.py` . This command will setup the database required to run the application
 11. After setting the database type `python lotsofitems.py` . This will populate your database with dummy categories, items and users for testing purposes.
 12. Finally type in `python application.py` . This command will start the server. Once this is done, open your browser and type in **localhost:8000**
 to see the application's home page.


## Navigation in the App

The application has the following links for navigation:

 - *localhost:8000* or *localhost:8000/categories/* for the homepage that displays all categories in the database.
 - -*localhost:8000/categories/new* for the page that helps users create new categories in the database.
 - *localhost:8000/categories/<int:category_id>/edit/* for the edit page that helps users edit existing categories created by them.
 - *localhost:8000/categories/<int:category_id>/delete/* leads to a page that helps users delete categories they created.
 - *localhost:8000/categories/<int:category_id>/* or *localhost:8000/categories/<int:category_id>/items* will display all the items created under a category.
 - *localhost:8000/categories/<path:category_name>/<path:item_name>/* takes users to a page that gives the selected items detailed description.
 - *localhost:8000/categories/<path:category_name>/item/new* is a page that helps users create new items under categories they created.
 - *localhost:8000/categories/<int:category_id>/item/<path:item_name>/edit* is a link to a page that lets users edit items they created.
 - *localhost:8000/categories/<int:category_id>/item/<path:item_name>/delete* will let users delete items that were created by them.
 - *localhost:8000/login* will enable users to log into the application with their google account.
## JSON Endpoints

The application has JSON endpoints for users to access the database info for development and testing purposes. These endpoints are as follows:

 1. *localhost:8000/categories/json* displays the output from the homepage in JSON
 `{
	  "Category": \[
	    {
	      "id": 1, 
	      "name": "Cakes", 
	      "picture": "https://i.imgur.com/Uf6TYcx.jpg"
	    }, 
	    {
	      "id": 2, 
	      "name": "Cookies", 
	      "picture": "https://i.imgur.com/l72wRjn.jpg"
	    }, 
	    {
	      "id": 3, 
	      "name": "Pies", 
	      "picture": "https://i.imgur.com/ZG4H6mZ.jpg"
	    }, 
	    {
	      "id": 4, 
	      "name": "Breads", 
	      "picture": "https://i.imgur.com/E7Vyu24.jpg"
	    }
	  \]
}`
2. *localhost:8000/categories/<path:category_name>/items/json* will display all items in a category in JSON

   `{
  "Items": \[
    {
      "category": "Cookies", 
      "description": "The cookie with lots of chips", 
      "id": 3, 
      "image": "https://i.imgur.com/tCiXG6k.jpg", 
      "name": "Choco-chip cookie", 
      "price": "$2.50"
    }
  \]
}`
3. *localhost:8000/categories/items/json* will display all items from the catalog.
4. *localhost:8000/categories/<path:category_name>/<path:item_name>/json* will like the web application give details on aspecific item in JSON.

## Troubleshooting
In some computers running Windows for OS the command `vagrant ssh` may not work correctly. For those systems please try `winpty vagrant ssh`