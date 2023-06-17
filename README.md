# clothing-rental

## Table of contents
* [General info](#general-info)
  * [Current stage](###current-stage)
  * [Functionalities](###Functionalities)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is the beginning of an online clothing rental service. People are used to buying clothes, even if they only use the items once.
However, this project is about creating a website where they can rent the clothes for a certain period of time and then return them.

This project will help create a database of people who want to rent clothes for everyday situations and not just for special occasions.

### Current stage

The plan is to build up this project so that it allows users to provide their own items for rental, exchange pieces with other users and subscribe for a month of regular rental.
However, at this point it provides a choice of items from the store owner's selection.

Although Items can be added to cart the order functionality is not available yet.
	
## Technologies
Project is created with:
* Python 3           (3.11.0)
* python-dotenv      1.0.0
* Pillow             9.5.0
* Django             4.2.1
* PyMySQL            1.0.3

Requirements.txt provided.
	
## Setup
To run this project, you need to clone this repository:
```
$ git clone
$ cd clothing_rental
```
Virtual environment:
```
$  pip install virtualenv
$  python<version> -m venv <virtual-environment-name>
```

Install dependencies :
```
$ pip install -r requirements.txt
$ cd clothing_rental
```

### Functionalities

#### Home
* Home
* How does it work
* About us

#### Accounts
* Sign up
* Log in
* Log out

#### Clothes and Clothing Items
The terminology regarding clothing is quite limited and, for this reason, it is necessary to understand the models.

* Categories (general types of clothing: pants, shirts, dresses, etc.)
* Clothes are all types or models of the categories (Pants capri, cargo, skinny types)
* Clothing items are specific types of clothes, meaning for example: Capri pants with specific details, let's say capri pants designed by XY with gold elements are different from capri pants designed by ZX regular.
* Clothing items can have different sizes, colors or are made from different materials.

Not registered users can only browse through the items but cannot see availability or make reservations.

#### For admin and staff: 

Most functionalities are for admin and staff.
The admin panel provides access to all models.

Views and templates block certain functionalities to regular users and are allowed only to staff and admin users.
There are also some functionalities available for everyone who visits the site, without the need to sing up and log in.

Every user can check the clothes types and every version of that style.
If they want to add them to favourites or add the to the cart, they need to log in. 

##### Add, update, delete and read:
* clothes
* clothing items
* categories
* clothing configurations options
* Variation types
* Variations options

* orders
* order lines 

##### Create: order status

* Logged in users can add items to favourites or to cart. 
  * Coming up: add to order and create order
* Browse and check available clothing items
* Add items of their preference to favorites or directly to cart. 


