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

### MANUAL TESTING ###

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

INDIVIDUAL RESTAURANTS (view_restaurant.html)

*This page is accessible to all so tests were repeated for when users were both logged in and logged out*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the images and cards are responsive.  With cards stacking at the appropriate breakpoints.
- Click all social links to ensure open in seperate tab (Future feature will include restaurants individual social pages).
- Click 'Add Review' button and check it redirects to 'Add a Review' page when logged in and to 'Log In' page with appropriate flashed message if user not in session.
- Check reviews are displayed clearly with all information displayed appropriately.

*For logged in users only:*

- Check that edit/delete buttons are only visible for users own reviews.
- In review section click 'Edit' button and check in redirects to the edit review button with the correct restaurant name and review body displayed.
- In review section click 'Delete' button and check it triggers a modal prompting the user to confirm that they want to delete that review.
- Re-open the 'Delete' modal and click the 'x' and 'Close' buttons to ensure that the modal is closed and no action is taken.
- Re-open the 'Delete' modal and click the 'Delete' button making sure the user is redirected back to their profile page and the review has been removed.

*For admin users only:*

- Check that the delete review button is visible for logged in admin users.  Repeat the modal checks for deleting reviews.
- Check that the edit and delete restaurant buttons are visible for logged in admin users.
- Click the 'Edit Info' button in the Edit/Delete restaurant section checking that admin are redirected to the edit info page and the information from the corresponding page is auto generated.
- Repeat the modal checks for deleting restaurants.


CREATE ACCOUNT

- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- Complete form filling in the username outside of the username requirements e.g. only 4 characters or over 12 characters, ensuring a warning is flagged on submission.
- Complete form filling in the passwords outside of the password requirements e.g. not including uppercase, lowercase and a number, ensuring a warning is flagged on submission.
- Cross check that attempted account creations using invalid data have not been registered to the database.
- Create an account for a username already in the database 'users' collection, making sure the create account page is reloaded on form submission and a developer written message is flashed notifying the user that that name is not available.
- Create an account for a new username making sure the user is redirected to the My Profile page on form submission and a developer written message is flashed welcoming the user to the site.
- Cross check that the newly created account has been added to the 'users' collection of the database.
- Click the 'Log In' link at the bottom of the page making sure the user is redirected to the 'Log In' page.

LOG IN

- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- Complete form with a username that is not registered in the 'users' collection ensuring a developer written message is flashed notifying the user that that username or password does not exist.
- Complete form where the username uses all lowercase letters ensuring that on form completion the username is recognised and user is redirected to their profile page. 
- Complete form filling using the incorrect password.  When an incorrect format is used a warning is flagged, if an incorrect password is used a developer written message is flashed notifying the user that that username or password does not exist 
- Complete the form using the admin log in details ensuring that they are redirected to the admin specific profile page.
- Click the 'Sign Up' link at the bottom of the page making sure the user is redirected to the 'Create Account' page.

LOG OUT

- Click 'Log Out' navbar item ensuring the user is redirected to the 'Log In' page and a developer written message is flashed confirming that the user has been logged out.

MY PROFILE - *USER*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- On initial log in ensure a message is flashed welcoming the user to the site.
- Make sure the username is displayed at the top of the page confirming that users profile.
- Click the 'Let's find somewhere to eat' link and ensure it redirects the user to the restaurants page.
- Click the 'Let us know' link and ensure it redirects the user to the contact page.
- Click the 'Add a review' button and ensure it redirects the user to the Add a review page.
- Check that the users existing reviews are visible, cross referencing with the database 'reviews' collection to make sure that none are missing.
- Click the 'Edit' button in the existing review section ensuring it redirects the user to the edit a review page and that the restaurant name and review body is pre-completed.
- Click the 'Delete' button in the existing review section ensuring it triggers a modal prompting the user to confirm that they want to delete that review.
- Re-open the 'Delete' modal and click the 'x' and 'Close' buttons to ensure that the modal is closed and no action is taken.
- Re-open the 'Delete' modal and click the 'Delete' button making sure the user is redirected back to their profile page and the review has been removed.
- Cross check on the 'reviews' collection that the review no longer exists.
- When the user has no written reviews check that a suitable message is displayed in the Existing Reviews section.
- Click the visible 'leave a review' link and ensure it redirects the user to the 'Add a review' page.
- Try editing the site address to exclude the users username and instead inputting admin, e.g. /profile/?username=admin or /profile/admin, making sure only the users own profile page is displayed or the custom 404 page is displayed.

ADD REVIEW

- Test that only logged in users can access the add review page by manually typing in the route e.g. /review/add STILL TO TEST WITH FAKE REST_ID
- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- Click the 'select restaurant' dropdown and ensure all restaurants in the database 'restaurants' collection are listed. Selecting each restaurant individually.
- Click the 'select rating' dropdown and ensure all options are available and able to be selected.
- Add text to the 'What do you think?' box ensuring that the box size is adjustable for larger reviews.
- Leave the 'select restaurant' and 'select rating' boxes blank and ensure a warning is triggered when the 'Add review' button is clicked.
- Fill in all details correctly and click the 'Add review' button making sure the 'Add a review' page reloads and a developer written message is flashed confirming the action.
- Write a review and click the 'Cancel' button making sure that the page reloads and the form is blank.

EDIT REVIEW

- Test that only logged in users can access the add review page by manually typing in the route e.g. /review/edit STILL TO TEST WITH FAKE REST_ID
- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Check that clicking edit buttons on individual restaurant page and My Profile page re-routes user to the 'Edit Review' page and that the restaurant name and review body are autofilled.
- Click the 'select restaurant' dropdown and make sure only the active restaurant is selectable.
- Click the 'select rating' dropdown.  Bug reported as not yet able to pre-fill this information.
- Edit text in the 'What do you think?' box ensuring that the box size is adjustable for larger reviews.
- Edit review details and click the 'Cancel' button making sure that the user is redirected to their profile page and that the review remains unchanged.
- Edit review details and click 'Edit my review' ensuring the user is redirected to their profile page and the corresponding review has been updated.

MY PROFILE - *ADMIN*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- On initial log in ensure a message is flashed welcoming the admin to the site.
- Make sure admin username is displayed at the top of the page confirming that admin profile.
- In 'User Messages' section check that all current messages are displayed - cross checked with the 'messages' collection in the database.
- Send a new message via the contact page checking that the message is newly displayed in the 'User Messages' section.
- Click the 'Add a Restaurant' button and ensure admin are redirected to the 'Add a Restaurant' page.
- Click the 'Restaurant Added' button to ensure it triggers a modal prompting the admin to confirm that they have added that restaurant.
- Re-open the 'Restaurant Added' modal and click the 'x' and 'Close' buttons to ensure that the modal is closed and no action is taken.
- Re-open the 'Restaurant Added' modal and click the 'Restaurant Added' button making sure the user is redirected back to their profile page and the message has been removed - cross check with the 'messages' collection in the database.
- Click the 'Restaurants' link to ensure the admin are redirected to the restaurants page when wanting to edit/delete a restaurant.
- Try editing the site address to exclude the admin username and instead inputting an existing username, e.g. /profile/?username=test01 or /profile/test01, making sure only the users own profile page is displayed or the custom 404 page is displayed.

ADD RESTAURANT - *ADMIN ONLY*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Log in as a standard user and attempt to navigate to the add restaurant page by manually adding /restaurant/add to the address.  Ensure that the user is not able and an appropriate response is given.
- Check that admin are able to access the 'Add Restaurant' page via the navbar link and button on their profile page.
- Click the 'how expensive' and 'mealtime' dropdowns and ensure all options are available and able to be selected.
- Leave the 'how expensive' and 'mealtime' dropdowns blank and ensure a warning is triggered when the 'Add restaurant' button is clicked.
- Complete the form ensuring that the form requires all fields to be completed, except the URL, before the form can be submitted. If a required field is left blank the user is given a prompt.
- On form submission ensure admin is redirected to their own profile page and a message is flashed confirming the addition of the restaurant.
- Check the successful addition of the new restaurant on the 'restaurants' page.
- Complete the form and hit the cancel button ensuring the admin user is redirected to their home page.

BUGS

- *FOOTER* not sticky on bottom of page on iPad/iPad Pro - showing quite a lot of whitespace.
![Footer whitespace](/documentation/images/bugs/footer-bug.png).
    - FIX - Search on Slack directed me towards two resources [css-tricks sticky footer guide](https://css-tricks.com/couple-takes-sticky-footer/) and a [js Bin](https://jsbin.com/wokututopu/1/edit?html,css,output).  Testing both options I settled on the JS Bin, utilising flex, as it fitted with my existing code more succinctly.

- *EDIT REVIEW* page, 'select rating' dropdown is not pre-filling the previously selected rating.
    - FIX - Not yet found.  For now text has been added reminding the user of their previous rating and prompting them to confirm their rating or select another.





