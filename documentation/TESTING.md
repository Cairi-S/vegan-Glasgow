# Testing #

All code has been run through validation services such as:
- [W3C HTML Markup Valication service](https://validator.w3.org/) which returned the result:
![HTML validator result](/documentation/images/html-validator.png)

This result was present across all pages despite an h5 element being present within the documented section.

- [W3C CSS valication service](https://jigsaw.w3.org/css-validator/) which returned the result:
![CSS validator result](/documentation/images/css-validator.png)
- [PEP8 Online Checker](http://pep8online.com/checkresult) which returned the result:
![PEP8 check result](/documentation/images/pep8.png)

The most common path through the website would be:

**Guest**
* Home > Restaurants

**New Users**
* Home > Create Account > My Account > Restaurants

**Existing Users**
* Home > Log In > My Account > *then restaurants/add review/edit review as required*

**Admin**
* Home > Log In > My Account > *then add restaurants/edit restaurants/restaurants as required*

### TESTING USER, ADMIN AND DEVELOPER GOALS FROM UX ###

#### User Goals ####
- Have somewhere to quickly find restaurant recommendations.
    - With the Home page of the site displaying 3 'top' recommendations, users are immediately met with restaurant recommendations.  If they don't take their fancy the navbar clearly shows where they will find other restaurant information.
- Explore the amazing food scene of the city of Glasgow.
    - The website showcases the best restaurants that Glasgow has to offer.  To keep on top of newly opened restaurants and menu updates, users are able to request new restaurants are added via the contact page.
- Be able to leave reviews for other users to help them.
    - Users are able to leave a review for a restaurant via each individual restaurants page or their own accounts page.
- Find out contact information for individual restaurants.
    - Every restaurant is initially displayed on a card which includes restaurant contact information such as address and contact telephone number.
- Find exteral links to restaurants homepages and social media where appropriate.
    - On each restaurant card the restaurants web address is displayed.  Within the restaurants full page users are able to access the restaurants social media details.
- See attractive images of the restaurant so I can judge whether I might enjoy the food and atmosphere.
    - Each restaurant features an image of it's interior, exterior or a dish served the user a glimpse of the restaurants theme. 
- Find information on the cuisine ie/ Italian, Traditional Scottish, Japanese, Fusion.
    - Each restaurant card features a short breakdown of the type of food offered.
- Find out the price range.
    - Each restaurant card shows the price range, displayed using the easily recognised and understood £, ££ and £££.
- Find what mealtimes restaurants are open.
    - Each restaurant card displays which mealtimes that eatery would be open at, e.g. brunch/ lunch and dinner etc.
- Be able to create an account and have an individual profile.
    - Users who are not logged in have the Create Account tab clearly displayed in the navbar.  Once an account is created they are automatically directed to their 'My Account' page whose link replaces the 'Create Account' tab.
- Be able to leave reviews to help advise others.
    - All logged in users are able to leave a review quickly and easily by pressing the 'Add a review' button found on both the 'My Account' and individual restaurant pages, there users select a restaurant to review via dropdown menu.  To be clear that this is a positive action the button is green.
- Be able to Edit my reviews if my opinions change.
    - Individual restaurants pages show all the reviews left for that restaurant.  Should the session username match the name of the user who created the review they are greeted by 'Edit' and 'Delete buttons.  These options are also shown on the users reviews displayed on their 'My Account' page.  To be clear that this is an action the button is yellow. 
- Be able to Delete my review if I no longer wish to comment on a restaurant.
    - Logged in users are able to delete reviews that they have written but no longer wish to be seen via the 'Delete' button.  Clicking the delete button triggers a modal to ensure no accidental deletions of items.  To be clear that clicking this button will have a negative effect the button is red.
- Be able to add restaurants to the website if I find somewhere which is not already listed.
    - Users are not yet able to add restaurants themselves, however, users are able to contact the admin team requesting a restaurant be added on their behalf.

#### Admin Goals ####

- Be able to delete user reviews if inappropriate.
    - When logged in admin are met with a 'Delete' button in all areas where they encounter user reviews.  Like in all instances of the delete button it is red to show a negative effect and upon clicking it a modal is triggered to make sure the action is intentional.
- Be able to add, edit restaurant info or delete a restaurant should it close.
    - Admin are able to 'Add' restaurants from their 'My Account' page.  To edit and delete restaurants admin must visit the individual restaurants page which is accessible via the restaurants link on their profile page or navbar.
- Be able to recieve notifications from users on new restaurants in the area.
    - To help the growth of Vegan Glasgow users are able to message the admin via the contact page.  New messages are displayed on the admin profile page and once the admin have finished added the restaurant recommended by the user the message can by deleted by clicking 'Restaurant added'.

MANUAL TESTING

ALL PAGES

Favicon

Check that Favicon shows on all pages

Navigation Bar

Hover over navigation items, and speach bubble/social media icons in the footer ensuring there is no discernable change other than the pointer turning to a hand and the item changing color from off white to dark green.

Logged out users:
*Header*

- Confirm the visible navbar items are Home, Restaurant, Create Account and Log In.
- Clicking the logo and Home items and ensure they reload the Home page.
- Clicking the Restaurant item and ensure it loads the all restaurants page.
- Clicking the Create Account item and ensure it loads the Create account page.
- Clicking the Log In item and ensure it loads the Log In page.

*Footer*

- Clicking the speech bubble icon and ensure it does not load the Contact page, redirecting the user to the Log In screen.



Logged in users:

*Header*

- Confirm the visible navbar items are Home, Restaurant, My Profile, Add Review and Log In.
- Clicking the logo and Home items and ensure they reload the Home page.
- Clicking the Restaurant item and ensure it loads the all restaurants page.
- Clicking the My Profile item and ensure it loads the My Profile page.
- Clicking the Add Review item and ensure it loads the Add Review page.
- Clicking the Log Out item and ensure it loads the Log Out page.

*Footer*

- Clicking the speech bubble icon and ensure it loads the Contact page.

- Change the screen size to various mobile devices using devTools to verify that the navigation bar and footer are responsive.  With the navbar becoming a burger menu and footer items stacking at the appropriate breakpoints.

HOME PAGE

*This page is accessible to all so tests were repeated for when users were both logged in and logged out*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the images and cards are responsive.  With cards stacking at the appropriate breakpoints.
- Click each individual restaurant card to make sure it takes you to the relevant individual restaurant page.
- Cross check with the database to make sure that restaurant's information is being correctly taken from the database.
- Cross check with the database to make sure that the restaurant's listed have "our_recommendation" marked as "on".

RESTAURANTS

*This page is accessible to all so tests were repeated for when users were both logged in and logged out*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the images and cards are responsive.  With cards stacking at the appropriate breakpoints.
- Click each individual restaurant card to make sure it takes you to the relevant individual restaurant page.

CREATE ACCOUNT

- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- BUG reported regarding responsive footer on iPad/iPad Pro devices.
- Complete form filling in the username outside of the username requirements e.g. only 4 characters or over 12 characters, ensuring a warning is flagged on submission.
- Complete form filling in the passwords outside of the password requirements e.g. not including uppercase, lowercase and a number, ensuring a warning is flagged on submission.
- Cross check that attempted account creations using invalid data have not been registered to the database.
- Create an account for a username already in the database 'users' collection, making sure the create account page is reloaded on form submission and a developer written message is flashed notifying the user that that name is not available.
- Create an account for a new username making sure the user is redirected to the My Profile page on form submission and a developer written message is flashed welcoming the user to the site.
- Cross check that the newly created account has been added to the 'users' collection of the database.
- Click the 'Log In' link at the bottom of the page making sure the user is redirected to the 'Log In' page.

BUGS

- *FOOTER* not sticky on bottom of page on iPad/iPad Pro - showing quite a lot of whitespace.
![Footer whitespace](/documentation/images/bugs/footer-bug.png).
    - FIX - Search on Slack directed me towards two resources [css-tricks sticky footer guide](https://css-tricks.com/couple-takes-sticky-footer/) and a [js Bin](https://jsbin.com/wokututopu/1/edit?html,css,output).  Testing both options I settled on the JS Bin, utilising flex, as it fitted with my existing code more succinctly.





