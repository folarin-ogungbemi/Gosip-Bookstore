# Gosip

## Introduction

[Gosip Bookstore](https://flo-gosip.herokuapp.com/ "visit website") demonstrates the functionalities of an E-commerce website specifically with a **B2C**(Business to Customer) relationship. Buyers can view a list of books within the Bookstore, select an individual book from the list to view its details, choose to add the book to their wishlist for later purchase or decide to add the book to their shopping cart at a certain quantity from where they can proceed to checkout the Item(s) using a secure payment system [Stripe](https://stripe.com/en-de "visit stripe"). 
Moreover, the Store Administrator also has the possibility of **CRUD**ing book's authors and books in the bookstore from the front end. Overall, the website provides the ability to make a complete online business transaction between the Store Owner and Buyers/Users seamlessly. Gosip Bookstore was built with a Frontend(HTML, CSS, [Bootstrap](https://getbootstrap.com/ "visit Bootstrap"),  [Javascript](https://www.javascript.com/ "visit Javascript"), [Jquery](https://jquery.com/ "visit Jquery")) and Backend ([Python](https://www.python.org/ "visit Python"),  [Django framework](https://www.djangoproject.com/ "visit django")) Software with an **Agile** Mindset.

[Link to live website](https://flo-gosip.herokuapp.com/ "visit website") 


# User Experience Design

* As a user,
    * I can register for an account so that I can have a profile linked to my account
    * I can log in and(or) log out of the website so that I can always easily access my account information on the website's page
    * I can reset my password incase I forget it so that I can recover access to my account.
    * I can receive an email confirmation after Registration so that I can verify that my account registration was successful
    * I can have a personal User Profile so that I can keep track of my Orders and have my personal information saved for easy payment purposes.
    * I can be able to reach out to the organization via their current contact address and contact them if in need of more information.
    * I can be able to sign for newsletters in order to keep up to date with news and special oofers of the Organization.
    * I can be able to visit the website on my Mobile device as well as my tablet or computer when necessary.

* As a Buyer,
    * I can view a list of books in the bookstore so that I can select the books to purchase
    * I can view details of an individual book so that I can identify information about the book's image, price, genre, description and author etc.
    * I can view the bookstore specials so that I can plan my shopping and be guided on books to purchase.
    * I can view the specific details of the book such as the Year of Publication, Pages, dimension, and language so that I can know if its a book i can read.
    * I can view the information about the author of a book so that I can be aware of the writer of the book I like to Purchase.
    * I can sort the list of books in the bookstore so that I can easily identify the books based on their price, genres, and best ratings.
    * I can search for a book by its name or description so that I can easily identify a particular book for purchase
    * I can see what i have searched for and the number of books matching my search so that I can decide quickly whether the book in search is in the bookstore.
    * I can easily select the quantity of a book for purchase so that I can match my planned budget.
    * I can view Books i have selected for purchase so that I can know the total cost of the Books I am purchasing
    * I can adjust the number of Items in my shopping cart to match my Shopping budget
    * I can easily select a book that I like and have it stored in my wishlist so that I can add them for purchase at a later date
    * I can unlike a book in my wishlist so that I know the books I still wish to purchase at a later date
    * I can easily provide my billing and shipping information so that I can checkout quickly
    * I can feel my personal and payment information is safe and secure so that I can confidently provide the information needed to complete my purchase
    * I can view an order confirmation after transaction is complete so that I confirm the Books I have purchased are the right ones.
    * I can receive an email confirmation after a completed transaction so that I can confirm the Books I should be expecting on Delivery.

* As the Website administrator,
    * I can add a new author and her information so that I can be able to update Books to be added to the Store
    * I can edit/update the author and her information so that I can change or add to the authors information.
    * I can delete an existing author so that I can manage the Books in the Store
    * I can add newly arrived Books to the Bookstore so that I can increase the books available in the Bookstore
    * I can edit/update Books within the Bookstore so that I can update the Price, and informations about the Book.
    * I can delete Books existing in the Bookstore so that I can manage the Books that are no longer available to customers.

    

## Design

### Colour Scheme
The Colour scheme for this project took ideas from [Gosip](https://folarin-ogungbemi.github.io/Portfolio-Project-1/ "visit gosip") a blog post created initially as a first project in Code Institute and from which births Gosip Bookstore.
Gosip depends on its three important colors which are significant to the values of the Organization.

* A dark-blue colour - #022138 , rgba(2, 33, 56)
* A light cream colour - #fffaf6, rgba(240, 44, 44)
* A redish colour - #f02c2c, rgb(255, 250, 246)

Additional colors:
* White - #fff, rgb(255, 255, 255)
* Bootsrap Info color - #17a2b8
* Bootsrap Danger color - #dc3545
* Bootsrap Success color - #28a745
* Bootsrap Primary color - #007bff
* Bootsrap Secondary color - #6c757d


### Typography

The Website adopted the default font from bootstrap as it aids visual comprehension of the text and the website contents.
* font faimily: '"Helvetica Neue", Helvetica, sans-serif'

### graphics & Layout
The Website was pre-designed on a graphical paper. A pictogram of what the landing page could look like in order to accomodate informations helpful for the user.

---


# Architecture

## Database 

* A postgreSQL database offered by elephantSQL was the choice of database connected with the django framework during project development. 

### Entities 
* User
    * Allauth account formed the basis for creation of account. a standard account implemented with the program.
    * All auth provides a step by step documentation for successful installation. [Django All Auth](https://django-allauth.readthedocs.io/en/latest/installation.html "visit gosip")

    ``` bash
    pip install django-allauth 
    ```
    and imported for use in django models.
    ```
    django.contrib.auth.models
    ```

* Author

| KEY                       | ATTRIBUTE             | VALIDATION       | FIELD_TYPE
|---------------------------|-----------------------|------------------|-------------------------------
| Key                       | name                  | max_length=100   | CharField
| Key                       | book_titel            | max_length=100   | CharField
| Key                       | about                 | required         | TextField

* Genre

| KEY                       | ATTRIBUTE             | VALIDATION       | FIELD_TYPE
|---------------------------|-----------------------|------------------|-------------------------------
| Key                       | name                  | max_length=100   | CharField

* Special

| KEY                       | ATTRIBUTE             | VALIDATION       | FIELD_TYPE
|---------------------------|-----------------------|------------------|-------------------------------
| Key                       | name                  | max_length=100   | CharField


* Books
    * All attributes on the book table are required except **special**

| KEY                       | ATTRIBUTE             | VALIDATION        | FIELD_TYPE
|---------------------------|-----------------------|-------------------|-------------------------------
| key                       | title                 | unique            | CharField
| slug                      | slug                  | unique            | CharField
| Foreign Key(Genre)        | genre                 | Genre             | FK
| Foreign_key(Author)       | author                | Author            | FK
| ManyToMany(Special)       | special               | Special           | MTM
| Key                       | publication_year      | required          | IntegerField
| Key                       | pages                 | required          | IntegerField
| Key                       | language              | max_length=100    | CharField
| Key                       | isbn                  | unique            | IntegerField
| Key                       | dimension             | max_length=100    | CharField
| Key                       | price                 | max_digits=6      | DecimalField
| Key                       | rating                | choices=RATING    | PositiveIntegerField
| Key                       | description           | required          | TextField
| Key                       | image                 | required          | CloudinaryField
| Key                       | Created_on            | auto_now_add=True | DateTimeField



# Technologies
* HTML
    * Hyper Text Markup Language(HTML) is the main text writer used for this website.
* CSS
    * Cascading Style Sheets(CSS) is the technology used for styling the website.
* [Bootstrap](https://getbootstrap.com/ "Link to Bootstrap main-page")
    * A free and open-source CSS framework directed at responsive, mobile-first front-end web development.
* Javascript
    * Javascript web program was used isn writing the codes that brings interactivity to the game.
* [Google Clouds](https://console.cloud.google.com/ "Link to Google Clouds main-page")
    * Access Google maps API
* [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template "Link to Gitpod-template")
    * A coding school for learning Software Development provides template for gitpod necessary libraries.
* [Github](https://github.com "Link to Github main-page")
    * Github is the site used for the deployment and hosting of this website.
* [Gitpod](https://www.gitpod.io "Link to Gitpod main-page")
    * Gitpod is the open-source developer platform used in tandem with github for the deployment of the website source code.
* [Visual Studio code](https://code.visualstudio.com "Link to visual studio code main-page")
    * The Integrated development environment(IDE) used for the writing of source code.
* [TinyJPG](https://tinyjpg.com/ "Link to TinyJPG main-page")
    * Website used for the compression of images used in the website.
* [Pexels](https://www.pexels.com "Link to pexels main-page")
    * Website used to source images used in the website.
* [Techsini](https://techsini.com/multi-mockup/index.php "Link to website main-page")
    * The Mock-up generator website used for creating the website mock-up image.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator "Link to W3 CSS main-page")
    * CSS validator used to validate the website's CSS in comparison to standard CSS writing.
* [W3 HTML Checker](https://validator.w3.org/nu/#textarea "Link to W3 HTML main-page")
    * HTML validator used to validate the website's HTML in comparison to standard HTML writing.
* [Image resizer](https://imageresizer.com/resize/download/632541ad11b49d00123e785e "Link to main-page")
    * For resizing of images to desired output
* [Cloudinary](https://cloudinary.com/ "Link to cloudinary")
    * Provides cloud based images and video management services.
* [elephantSQL](https://www.elephantsql.com/ "Link to elephantSQL")
    * The postgreSQL Database used for the program.


# Credits

## Code
* The turorial from [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainfullstacksoftwarecommoncurriculum "Visit Code Institute") was the most helpful link from the writing of code to the deployment of the program.
* Helpful Documentation  [Django models](https://docs.djangoproject.com/en/4.1/ "Visit django documentation") on how to set up and build with django.
* Helpful Documentation  [Stripe Docs](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout#set-up-stripe "Visit Stripe documentation") on how to set up and build stripe payment.

## Content
 * Book Images, Description and about author were taken from Google and wikipedia

## Media
* The Landing page images used in the website [Pexels](https://www.pexels.com/ "visit Pexels") were products of pexels.

## Acknowledgement 
My sincere appreciation goes to :
* To the always active Code Institute Tutor assistants that always came up with helpful tips and guide, it would not have been possible without your help.
* To my partner, Mo, for giving her attention at the time of need.