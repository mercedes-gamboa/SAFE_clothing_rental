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
	
### Functionalities

Sign up
Log in
Log out

Not registered users can only browse through the items but cannot see availability or make reservations.

#### For admin and staff: 

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

* Logges in users can
* browse and check available clothing items
* add items of their preference to favorites or directly to cart. 
* create orders

## Technologies
Project is created with:
* Python 3           (3.11.0)
* python-dotenv      1.0.0
* Pillow             9.5.0
* Django             4.2.1
* PyMySQL            1.0.3

Requirements.txt provided.
	
## Setup
To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```