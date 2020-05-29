# **BookLiker**

A visitor-maintained book list with information about the books. Users can sort/or filter the books using premade functions.

## Table of content

- [**BookLiker**](#--bookliker--)
  * [Table of content](#table-of-content)
  * [UX design](#ux-design)
    + [Design wire-frames / mock-ups:](#design-wire-frames---mock-ups-)
    + [User stories](#user-stories)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Menu Area](#menu-area)
      - [Book-cards area](#book-cards-area)
      - [Not area related features](#not-area-related-features)
      - [Future ideas](#future-ideas)
    + [Features left to implement](#features-left-to-implement)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Acknowledgement](#acknowledgement)
    + [License](#license)


## UX design

The design primarily focus on simplicity, usability responsiveness to provide good user experience to young and old people using wide range of devices.

The navigation system has been changed during development as the initial design did not give the same easy to use experience to all users.

### Design wire-frames / mock-ups:

- [Importance-to-Viability](docs/ImportanceToViability.pdf)
- [Strategy Plane](docs/StrategyPlane.pdf)
- [Scope Plane](docs/ScopePlane.pdf)
- [Structure Plane](docs/StructurePlane.pdf)
- [Skeleton for Mobile](docs/skeletonMobile.pdf)
- [Skeleton for Desktop](docs/SkeletonDesktop.pdf)

### User stories

As the app does not use user accounts or session storage, there is no difference between new users or returning users.

- User A would like to know more about the app or how to use it. As user landing on the Home page, where the welcome and how to message can be found, this shows up straight away for every visitors. 
- User A does not know how to use the app, but not on the Home page, can click on the Home button to redirect to the Home page.
- User B would like to sort the books by author/title, this can be done by clicking on the sort/filter button, and selecting the desired sort function. This will be rendered in alphabetic order for the user.
- User B would like to filter the books by genre, this can be done by clicking on the sort/filter button and selecting the desired genre.
- User B would like to see the most liked books, this can be done by clicking on the sort/filter button and selecting the most liked option.
- User C would like to see more details about one book, this can be reached by clicking o n the more info button on the book card.
- User C would like to check the online book-store to buy the book, this can be reached by clicking on the where to buy button on the book card.
- User D would like to add new book to the collection, this can be done by clicking on the add new book button. From there the form has a description how to and following that the user can add a new book.
- User D would like to update an existing book. This can be done by clicking on the more info on the book card and from there clicking on the edit book button. From the edit form either the user can navigate to some other pages or by clicking on the update book button can update the document in the collection.
- User D would like to delete an existing book. this can be done by choosing the edit option on the book card and clicking on the delete book button. This will bring up an alert to confirm and then need to click on the confirm button to delete the documents from the collection.
- User E would like to like/dislike a book. This can be done by clicking on the book card like/dislike icons. This can be done on any page where the user does see the like/dislike icons. This includes, the any sort/filter and about book pages.

## Features

### Existing Features

#### Menu Area

- Home button to go back to welcome screen
- Sort/filter dropdown to use premade queries on the collection
- Adding new document to the collection
- The navbar is responsive, clear and straightforward

#### Book-cards area

- The book cards are responsive templates, including the book cover, the title and author of the book, a buy online and more info buttons and like/dislike icons

#### Not area related features

- The user can do CRUD on the books collection there is no authentication or restriction on this as this is not the aim of the project
- When clicking on the like/dislike icons the app updates the document and returns to the same page(flask) same position(jQuery)

#### Future ideas

In order to achieve these ideas need to create user authentication as simply storing information in the browser cache would not fully fill the requirements.

User account to follow user actions

User permissions to create groups from users and prevent certain actions(e.g delete)

Users should be able to like/dislike one book only once



### Features left to implement

A genre request page, so the admin can see what is missing but to avoid duplicates.

## Technologies Used

[Python](https://www.python.org): The main programming language

[Flask](https://www.flask.org): A python based templating language

[Html](https://whatwg.org/) : To display the document in the web browser

[SCSS](https://sass-lang.com/documentation/syntax) : To customise the document layout.

[jQuery](https://jquery.com/) : To simplify DOM manipulation.

[Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) : To use jQuery and actions on the page

[Git](https://git-scm.com/) : For version control.

[Github](https://github.com/) : To publish the website's code

[GitPod](https://gitpod.io/) : For code editing.

[Office](https://www.Office.com): For creating initial planes.

[Typora](https://typora.io/): To edit the markdown files.

[Heroku](https://heroku.com): To publish the app.

## Testing

Test documentation can be found [here](docs/tests.md)

## Deployment

The deployment process was the following:

- created the [repository](https://github.com/varroz56/BookLiker) on GitHub. [Guidance](https://help.github.com/en/github/getting-started-with-github/create-a-repo)
- created the app on Heroku. [Guidance](https://devcenter.heroku.com/articles/getting-started-with-python)
- created BookReview DB on mongo atlas and created Books and Genres collections 
- On the app settings tab, set the environmental variables: IP, PORT, MONGO_URI (the connection string what can be set up using this [Guidance](https://docs.mongodb.com/guides/cloud/connectionstring/))
- Created Procfile to specify the commands executed by the app on startup, this is required by heroku
- Created requirements.txt file using the "pip3 freeze >> requirements.txt" command as Heroku automatically look for this to install the required depedencies
- On the Heroku app dashboard Deploy section connected the app to the github repository(as previously authenticated myself it was not necessary) by selecting Github in the Deployment methods
- Heroku has the option to choose branch to deploy, in the beginning used the master branch, for production, used the customsort branch.
- In Heroku after selecting the branch the app can be deployed by clicking on the deploy button.
- If there was no problem with the deployment, the app can be opened on the following link: <app name>.herokuapp.com, in this case Bookliker.herokuapp.com

For local testing:
As the code does not include the mongo connection string, in order to test it a connection string must be set up correctly

- create atlas account and follow the [Guidance](https://docs.atlas.mongodb.com/getting-started/) to set up the database as follows:
  DB:
    Books:
        "title": string,
        "author": string,
        "description": string,
        "url_to_buy": string,
        "image_url": string,
        "likes": int,
        "dislikes": int,
        "genre": string
    Genres:
        "genre": string

- the connection string what can be set up using this [Guidance](https://docs.mongodb.com/guides/cloud/connectionstring/)

- clone the repo from [Github](https://github.com/varroz56/BookLiker) using the "git clone https://github.com/varroz56/BookLiker.git" command in the desired directory
- install(sudo apt-get install python3-pip) or update pip3(pip3 install --upgrade pip)
- install requirements from the requirements.txt using the "pip3 install -r requirements.txt" command
- save the mongo connection string as MONGO_URI in the env variables:
- - sudo nano ~/.bashrc
- - export MONGO_URI=<connection string>
- - save and exit the text editor, close the terminal or use the source ~/.bashrc command to refresh cached bashrc document

- start the app using "python3 app.py"  command
- open a web browser and search for localhost:8080




## Credits

### Content

The content mainly used for the book cards are from [Wikipedia](https://www.wikipedia.org/). 
Other content have been uploaded from various websites
[Table of contents generated with markdown-toc](http://ecotrust-canada.github.io/markdown-toc/)


### Acknowledgement
Special thanks to the tutors at Code Institute, they helped a lot to overcome some difficulties during the project
Platforms used to get help and to test the application:
- Stack Overflow
- Slack
- Python, flask and mongo documentation

### License

The BookLiker app have been created by [Zoltan Varro](https://www.linkedin.com/in/zoltanlvarro/) and it is subject to the [MIT license](https://opensource.org/licenses/MIT).