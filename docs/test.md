ests for the Bookliker app

The following tests has been done:

- Test users

- Unittest
- Test during development using the site itself and checking behaviour using print function

Users tested both the layout and the business logic, the customsort branch holds the production layout and the added sort and filter options following the feedbacks.

What has been changed since the initial plans:

- Navigation layout
- background of the site and the book cards
- card layout and bootstrap settings
- cards layout( jquery to adapt for screen sizes and resize)



Unittest test codes can be found in the tests.py file, also coverage report:

app.py                                                                                           70     15    79%

As nothing can be tested 100% using the Pareto Principle 80%-20% I believe this is sufficient.

Unittest covers the business logic and the index page loading.

