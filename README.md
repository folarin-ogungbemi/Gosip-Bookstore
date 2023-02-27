# e-commerce Bookstore for all age groups

[Gosip](https://flo-gosip.herokuapp.com/) e-commerce bookstore is an online store that specializes in selling books. The website is designed to be user-friendly, allowing customers to browse through a wide selection of books and make purchases easily. To ensure secure payment transactions, the ecommerce bookstore has integrated Stripe as its payment gateway.

![](/media/readme-images/mockup.jpg)

## Table of contents

* [Purpose](#purpose)

* [UX Design](#ux-design)

* [Design](#design)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Graphics and Layout](#graphics-and-layout)

* [Architecture](#Architecture)
    * [Database](#database)
    * [Entities](#entities)

* [Features](#Features)
    * [Non Admin User](#non-admin-user)
        * [Sign In](#sign-in)
        * [Sign Up](#sign-up)
        * [Homepage](#homepage)
        * [Navbar](#navbar)
        * [Search Query](#search-query)
        * [Search Bar](#search-bar)
        * [Sorting By Query](#sorting-by-query)
        * [User Profile](#user-profile)
        * [Books](#books)
        * [Books in cart](#books-in-cart)
        * [Books in Wishlist](#books-in-wishlist)
        * [Checkout Book](#checkout-book)
        * [Transaction Success](#transaction-success)
        * [Team Page](#team-page)
        * [About Page](#about-page)
        * [Contact Page](#about-page)
        * [Privacy Policy](#privacy-policy)
        * [Footer and Newsletter](#footer-and-newsletter)
        * [404 Error Page](#404-error-page)

    * [Admin User](#non-admin-user)
        * [Admin Bookstore Crud Function](#admin-bookstore-crud-function)
        * [Author Management](#author-management)
        * [Books Management](#books-management)

* [Web Marketing](#web-marketing)

* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Unit Testing](#unit-testing)
    * [Python unit tests](#python-unit-tests)
  * [Automated Testing](#automated-testing)
      * [Code Validation](#code-validation)
      * [Lighthouse](#lighthouse)

* [Deployment](#Deployment)
    * [Project Creation](#project-creation)
    * [Heroku Deployment](#heroku-deployment)

* [Technologies](#Technologies)
  * [Languages](#languages)
  * [Programs, Frameworks, Libraries](#programs-frameworks-libraries)

* [Credits](#Credits)
    * [Code](#code)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgement](#acknowledgement)

# Purpose

[Gosip Bookstore](https://flo-gosip.herokuapp.com/ "visit website") demonstrates the functionalities of an E-commerce website specifically with a **B2C**(Business to Customer) relationship. Buyers can view a list of books within the Bookstore, select an individual book from the list to view its details, choose to add the book to their wishlist for later purchase or decide to add the book to their shopping cart at a certain quantity from where they can proceed to checkout the Item(s) using a secure payment system [Stripe](https://stripe.com/en-de "visit stripe"). 
Moreover, the Store Administrator also has the possibility of **CRUD**ing book's authors and books in the bookstore from the front end. Overall, the website provides the ability to make a complete online business transaction between the Store Owner and Buyers/Users seamlessly. Gosip Bookstore was built with a Frontend(HTML, CSS, [Bootstrap](https://getbootstrap.com/ "visit Bootstrap"),  [Javascript](https://www.javascript.com/ "visit Javascript"), [Jquery](https://jquery.com/ "visit Jquery")) and Backend ([Python](https://www.python.org/ "visit Python"),  [Django framework](https://www.djangoproject.com/ "visit django")) Software with an **Agile** Mindset.

[Link to live website](https://flo-gosip.herokuapp.com/ "visit website") 


---

# UX-Design

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

    

# UX Design

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

### Graphics and Layout
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
    pip3 install django-allauth 
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
| Key                       | image_url             | blank=True        | URLField
| Key                       | image                 | blank=True        | ImageField
| Key                       | Created_on            | auto_now_add=True | DateTimeField

* The Slug field is a slugified data of the title field.
---
# Features

## Non Admin User

### Sign In
![](/media/readme-images/sign-in-form.jpg)

### Sign Up
![](/media/readme-images/sign-up-form.jpg)

### Homepage
![](/media/readme-images/homepage.jpg)

### Navbar
![](/media/readme-images/navbar.jpg)

### Search Query
![](/media/readme-images/search-query.jpg)

### Search Bar
![](/media/readme-images/offcanvas.jpg)

### Sorting By Query
![](/media/readme-images/sorting-by-query.jpg)

### User Profile
![](/media/readme-images/profile.jpg)

### Books
![](/media/readme-images/books-mockup.jpg)

### Books in cart
![](/media/readme-images/Books-in-cart.jpg)

### Books in Wishlist
![](/media/readme-images/wishlist-books.jpg)

### Checkout Book
![](/media/readme-images/checkout.jpg)
![](/media/readme-images/checkout.jpg2)

### Transaction Success
![](/media/readme-images/transaction-success.jpg)

### Team Page
![](/media/readme-images/team-page.jpg)

### About Page
![](/media/readme-images/about-section.jpg)

### Contact Page
![](/media/readme-images/contact-section.jpg)

### Privacy Policy
![](/media/readme-images/privacy-policy.jpg)

### Footer and Newsletter
![](/media/readme-images/footer-and-newsletter.jpg)

### 404 Error Page
![](/media/readme-images/error-404.jpg)

## Admin User

### Admin Bookstore Crud Function
![](/media/readme-images/admin-crud.jpg)
![](/media/readme-images/admin-crud-2.jpg)
![](/media/readme-images/edit-author.jpg)

### Author Management
![](/media/readme-images/author-mgt.jpg)

### Books Management
![](/media/readme-images/book-mgt.jpg)

# Web Marketing
The website is using Facebook to improve its online presence, increase web marketing efforts and improve SEO. By doing so, it hopes to reach a wider audience of people interested in the variety of books offered by Gosip Bookstore. [Gosip Bookstore](https://www.facebook.com/profile.php?id=100089052437606 "Visit facebook page")

![](/media/readme-images/facebook-gosip.jpg)

# Testing

Testing procedures carried out for the success of the website were partly **Automated** using the included feature of django TestCase and in other cases **Manual** testing. Besides the pages of the website were through validation test.

## Manual Testing

![](/media/readme-images/MT01.jpg)
![](/media/readme-images/MT02.jpg)
![](/media/readme-images/MT03.jpg)

## Unit Testing

### Python unit tests

For clarity, tests were sectioned for each app and each test were named according to their case.
Each app contains a test folder called **tests**
to run this test

``` bash
    python3 manage.py test appname.tests
```

to check the status of testig required for the project. coverage was installed

`pip3 install coverage`
`pip3 freeze > requirements.txt`

``` bash
    coverage run --source=home manage.py test home.tests
```
To view a report of the test

``` bash
    coverage report
```
* Home App
![](/media/readme-images/home-app-testcase.jpg)

* Books App
![](/media/readme-images/books-app-testcase.jpg)
## Automated Testing

### Code Validation

The pages of the website were run through [W3 HTML Validator](https://validator.w3.org/nu/#textarea "Link to W3 HTML checker main-page") from the source page. 
The process for testing was going through each page of the website to check if they pass W3 HTML validation.
Errors detected in instances of duplicated `id` during population of items to template. The decision taken at this time was to replace `id` attributes to `class` attributes and in other cases modals causing it were removed in order for the template to pass validation.

Current status: No errors were detected.
* All HTML pages report 
![](/media/readme-images/html-validator.jpg)

The Static CSS files were validated through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator "Link to W3 CSS main-page"). No errors were detected
* All CSS files report 
![](/media/readme-images/css-validator.jpg)

### Lighthouse

![](/media/readme-images/Lighthouse-test.jpg)

Fix Bug 
Redirect url returns no match found. Removed the quotes around it. it works

# Deployment
Before Deployment, It is important that in the django project settings, **Debug** is set to **False** majorly for the security of the project.

## Project Creation

To start this project, It is recommended to use the [template](https://github.com/Code-Institute-Org/gitpod-full-template "Link to Code Institute template") already created by Code Institute. By using this template, necessary plugins for your project are downloaded for you. After clicking this link, the following steps are to be followed.
1. Navigate to "Use this template" on the page.
    * click on the button
1. Navigate to "repostory name"
    * Enter a name for your repository to continue (e.g my-project)
    * You may enter a description for the project. (Not mandatory)
    * keep your repository checked "public" for assessment purposes.
    * Then click on the button "Create repository from template".
1. Are you registered with gitpod by now?
    1. If No ? 
        * Visit the [Gitpod](https://www.gitpod.io "Click to visit gitpod") webiste and Login your details.
        * there after navigate back to Github and continue the steps after login.
    1. If yes ?
        * Navigate to the green button titled **Gitpod**
        * The creation of an environment might take a while. wait for gitpod to set up your environment.
        * It is important to pin your worksheet in Gitpod Dashboard and load subsequent opening of this project from the dashboard in order to keep all installed creds intact.
    1. Here we have Visual Studio code as IDE.
        * By default, on the left side-bar is the respository we created in github including an already made README.md file, package.json, requirements.txt and run.py etc.
            * A mouse right click in this panel area gives us option to create new files and or folders in this repository.
            * Finally, the bash terminal for interacting with github and writing our python code is located right below this window. We can right click on the terminal option to move terminal to right panel
        * To upload changes made in our repository to github in this IDE, the following commands are to be enetered after the $ sign in the bash terminal.
            * To check the status of your repository if any changes have been made.
                 ``` bash
                    git status
            *  To stage changes made 
                ``` bash
                    git add . 
            * To commit changes made 
                ```bash
                    git commit -m "commit message in between this quotes"
            * To push changes made to github
                ```bash
                    git push
            * View files that have been uploaded to github
                ```bash
                    git ls-files
                ```

## Heroku Deployment 

Heroku is the hosting platform for the project and to deploy, The following steps were strictly taken:
[Heroku Address](https://id.heroku.com/ "visit heroku address")
* Sign in to Heroku, otherwise create an account
* From Heroku Dashboard, 
    * click **Create new app**
    * Enter a unique App name
    * create app after selecting region.
* Navigate to settings on Heroku.
    * Navigate to Config Vars
        The config vars should contain the following keys and their corresponding values:
        * DATABASE_URL
        * SECRET_KEY
        * AWS_ACCESS_KEY_ID
        * AWS_SECRET_ACCESS_KEY
        * STRIPE_PUBLIC_KEY
        * STRIPE_SECRET_KEY
        * STRIPE_WEBHOOK_SECRET
        * USE_AWS should be set to **True**
        * Make sure DISABLE_COLLECTSTATIC is removed before production.
* Navigate back to Deploy section
    * Select Github to connect to Github
        * Search for github repository using the name of the repository
        * click connect
    * scroll down to Deploy branch
        * Select **deploy branch** to deploy manually. Clicking on this button may take a while
        * After completion, There is a *View* button below it. Click to view live website
[Live website here](https://flo-gosip.herokuapp.com/ "visit live website")


## Demonstrated Data and Account

| Email                     | username           | Password         | Description
|---------------------------|--------------------|------------------|-------------------------------
| gosip@blog.com            | flo-admin          | myGosip!!        | Admin account



---

# Technologies

## Languages

* HTML
    * Hyper Text Markup Language(HTML) is the main text writer used for this website.
* CSS
    * Cascading Style Sheets(CSS) is the technology used for styling the website.
* [Javascript](https://www.javascript.com/ "Link to Javascript")
    * Javascript frontend programming language.
* [Python](https://www.python.org/ "Link to python")
    * Python is a programming language that lets you work quickly and integrate systems more effectively.

## Programs, Frameworks, Libraries

* [Django](https://docs.djangoproject.com/ "Link to Django Docs")
    * Django makes it easier to build better web apps more quickly and with less code.
* [Bootstrap](https://getbootstrap.com/ "Link to Bootstrap main-page")
    * A free and open-source CSS framework directed at responsive, mobile-first front-end web development.
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
* [AWS](https://aws.amazon.com/ "Link to AWS")
    * Provides cloud based images and video management services.
* [elephantSQL](https://www.elephantsql.com/ "Link to elephantSQL")
    * The postgreSQL Database used for the program.

---

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
