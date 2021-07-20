- [VALIDATION](#validation)
- [TESTING USER, ADMIN AND DEVELOPER GOALS FROM UX](#testing-user--admin-and-developer-goals-from-ux)
  * [User Goals](#user-goals)
  * [Admin Goals](#admin-goals)
- [MANUAL TESTING](#manual-testing)
  * [ALL PAGES](#all-pages)
  * [HOME PAGE](#home-page)
  * [RESTAURANTS](#restaurants)
  * [INDIVIDUAL RESTAURANTS (view_restaurant.html)](#individual-restaurants--view-restauranthtml-)
  * [CREATE ACCOUNT](#create-account)
  * [LOG IN](#log-in)
  * [LOG OUT](#log-out)
  * [CONTACT](#contact)
  * [404](#404)
  * [MY PROFILE - *USER*](#my-profile----user-)
  * [ADD REVIEW](#add-review)
  * [EDIT REVIEW](#edit-review)
  * [MY PROFILE - *ADMIN*](#my-profile----admin-)
  * [ADD RESTAURANT - *ADMIN ONLY*](#add-restaurant----admin-only-)
  * [EDIT RESTAURANT - *ADMIN ONLY*](#edit-restaurant----admin-only-)
  * [DELETE RESTAURANT - *ADMIN ONLY*](#delete-restaurant----admin-only-)
- [ADDITIONAL TESTING](#additional-testing)
  * [Home](#home)
  * [All Restaurants](#all-restaurants)
  * [Individual Restaurants](#individual-restaurants)
  * [Create Account](#create-account)
  * [Log In](#log-in)
  * [Contact](#contact)
  * [Profile Page - User](#profile-page---user)
  * [Add Review](#add-review)
  * [Edit Review](#edit-review)
  * [Profile Page - Admin](#profile-page---admin)
  * [Add Restaurant](#add-restaurant)
  * [Edit Restaurant](#edit-restaurant)
- [BUGS](#bugs)
- [FURTHER TESTING](#further-testing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


### VALIDATION ### 
All code has been run through validation services such as:
- [W3C HTML Markup Valication service](https://validator.w3.org/) which returned the result:
![HTML validator result](/documentation/images/validation/html-validator.png)

This result was present across all pages despite an h5 element being present within the documented section.

- [W3C CSS valication service](https://jigsaw.w3.org/css-validator/) which returned the result:
![CSS validator result](/documentation/images/validation/css-validator.png)
- [PEP8 Online Checker](http://pep8online.com/checkresult) which returned the result:
![PEP8 check result](/documentation/images/validation/pep8.png)

### TESTING USER, ADMIN AND DEVELOPER GOALS FROM UX ###

The most common path through the website would be:

**Guest**
* Home > Restaurants

**New Users**
* Home > Create Account > My Account > Restaurants

**Existing Users**
* Home > Log In > My Account > *then restaurants/add review/edit review as required*

**Admin**
* Home > Log In > My Account > *then add restaurants/edit restaurants/restaurants as required*

#### User Goals ####
- Have somewhere to quickly find restaurant recommendations.
    - With the Home page of the site displaying 3 'top' recommendations, users are immediately met with restaurant recommendations.  If they don't take their fancy the navbar clearly shows where they will find other restaurant information.
- Explore the amazing food scene of the city of Glasgow.
    - The website showcases the best restaurants that Glasgow has to offer.  To keep on top of newly opened restaurants and menu updates, users are able to request new restaurants are added via the contact page.
- Be able to leave reviews for other users to help them.
    - Users are able to leave a review for a restaurant via each individual restaurants page or their own accounts page.
- Find out contact information for individual restaurants.
    - Every restaurant is initially displayed on a card which includes restaurant contact information such as address and contact telephone number.
- Find external links to restaurants' homepages and social media where appropriate.
    - On each restaurant card the restaurant's web address is displayed, in future this would be a clickable link.  
    - Within the restaurants page users are able to access the restaurant's social media details.
- See attractive images of the restaurant so I can judge whether I might enjoy the food and atmosphere.
    - Each restaurant features an image of its interior, exterior or a dish served there, giving the user a glimpse of the restaurants theme. 
- Find information on the cuisine ie/ Italian, Traditional Scottish, Japanese, Fusion.
    - Each restaurant card features a short breakdown of the type of food offered.
- Find out the price range.
    - Each restaurant card shows the price range, displayed using the easily recognised and understood £, ££ and £££.
- Find what mealtimes restaurants are open.
    - Each restaurant card displays which mealtimes that eatery would be open at, e.g. brunch/ lunch and dinner etc.
- Be able to create an account and have an individual profile.
    - Users who are not logged in have the Create Account tab clearly displayed in the navbar.  Once an account is created they are automatically directed to their 'My Account' page whose link replaces the 'Create Account' tab.
- Be able to leave reviews to help advise others.
    - All logged-in users can leave a review quickly and easily by pressing the 'Add a review' button found on both the 'My Account' and individual restaurant pages, there users select a restaurant to review via a dropdown menu.  To be clear that this is a positive action the button is green.
- Be able to Edit my reviews if my opinions change.
    - Individual restaurants pages show all the reviews left for that restaurant.  Should the session username match the name of the user who created the review they are greeted by 'Edit' and 'Delete buttons.  These options are also shown on the user's reviews displayed on their 'My Account' page.  To be clear that this is an action the button is yellow. 
- Be able to Delete my review if I no longer wish to comment on a restaurant.
    - Logged-in users can delete reviews that they have written via the 'Delete' button.  Clicking the delete button triggers a modal to ensure no accidental deletions of items.  To be clear that clicking this button will have a negative effect the button is red.
- Be able to add restaurants to the website if I find somewhere which is not already listed.
    - Users are not yet able to add restaurants themselves, however, users are able to contact the admin team requesting a restaurant be added on their behalf.

#### Admin Goals ####

- Be able to add, edit restaurant info or delete a restaurant should it close.
    - Admin can 'Add' restaurants from their 'My Account' page.  To edit and delete restaurants admin must visit the individual restaurant's page which is accessible via the 'Restaurant' link on their profile page or navbar in future they will be able to do this directly from their profile page.
- Be able to recieve notifications from users on new restaurants in the area.
    - To help the growth of Vegan Glasgow users are able to message the admin via the contact page.  New messages are displayed on the admin profile page and once the admin have finished adding the user recommended restaurant the message can by deleted by clicking 'Restaurant added'.

### MANUAL TESTING ###

#### ALL PAGES ####

Favicon

Check that Favicon shows on all pages

Navigation Bar

Hover over navigation items, contact page link and social media icons in the footer ensuring there is no discernable change other than the pointer turning to a hand and the item changing color from off white to dark green.

Logged out users:
*Header*

- Confirm the visible navbar items are Home, Restaurant, Create Account and Log In.
- Clicking the logo and 'Home' items and ensure they reload the Home page.
- Clicking the 'Restaurant' item and ensure it loads the all restaurants page.
- Clicking the 'Create Account' item and ensure it loads the Create account page.
- Clicking the 'Log In' item and ensure it loads the Log In page.

*Footer*

- Clicking the contact link text and ensure it does not load the Contact page, redirecting the user to the Log In screen.

Logged in users:

*Header*

- Confirm the visible navbar items are Home, Restaurant, My Profile, Add Review and Log In.
- Clicking the logo and 'Home' items and ensure they reload the Home page.
- Clicking the 'Restaurant' item and ensure it loads the all restaurants page.
- Clicking the 'My Profile' item and ensure it loads the My Profile page.
- Clicking the 'Add Review' item and ensure it loads the Add Review page.
- Clicking the 'Log Out' item and ensure it loads the Log Out page.

*Footer*

- Clicking the contact link text and ensure it loads the Contact page.

- Change the screen size to various mobile devices using devTools to verify that the navigation bar and footer are responsive.  With the navbar becoming a burger menu and footer items stacking at the appropriate breakpoints.

#### HOME PAGE ####

*This page is accessible to all so tests were repeated for when users were both logged in and logged out*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the images and cards are responsive.  With cards stacking at the appropriate breakpoints.
- Click each individual restaurant card to make sure it takes you to the relevant individual restaurant page.
- Cross-check with the database to make sure that the restaurant's information is being correctly taken from the database.
- Cross-check with the database to make sure that the restaurants listed have "our_recommendation" marked as "on".

#### RESTAURANTS ####

*This page is accessible to all so tests were repeated for when users were both logged in and logged out*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the images and cards are responsive.  With cards stacking at the appropriate breakpoints.
- Click each individual restaurant card to make sure it takes you to the relevant individual restaurant page.

#### INDIVIDUAL RESTAURANTS (view_restaurant.html) ####

*This page is accessible to all so tests were repeated for when users were both logged in and logged out*

- Change the screen size manually and to various mobile device sizes using devTools to verify that the images and cards are responsive.  With cards stacking at the appropriate breakpoints.
- Click all social links to ensure open in a seperate tab (Future feature will include restaurants individual social pages).
- Click 'Add Review' button and check it redirects to 'Add a Review' page when logged in and to 'Log In' page with an appropriate flashed message if user not in session.
- Check reviews are displayed clearly with all information displayed appropriately.

*For logged in users only:*

- Check that the 'Edit' button is only visible for user's own reviews.
- In the review section click 'Edit' button and check in redirects to the edit review button with the correct restaurant name and review body displayed.
- Check that the 'delete a review' link is only visible for logged-in users.  If no user or admin user are logged in the link is not displayed.

*For admin users only:*

- Check that the edit and delete restaurant buttons are visible for logged-in admin users.
- Click the 'Edit Info' button in the Edit/Delete restaurant section checking that admin are redirected to the edit info page and the information from the corresponding page is auto-generated.
- Checks modal for deleting restaurants using the same methods as previously mentioned.


#### CREATE ACCOUNT ####

- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- Complete form filling in the username outside of the username requirements e.g. only 4 characters or over 12 characters, ensuring a warning is flagged on submission.
- Complete form filling in the passwords outside of the password requirements e.g. not including uppercase, lowercase and a number, ensuring a warning is flagged on submission.
- Cross-check that attempted account creations using invalid data have not been registered to the database.
- Create an account for a username already in the database 'users' collection, making sure the create account page is reloaded on form submission and a developer written message is flashed notifying the user that that name is not available.
- Create an account for a new username making sure the user is redirected to the My Profile page on form submission and a developer written message is flashed welcoming the user to the site.
- Cross-check that the newly created account has been added to the 'users' collection of the database.
- Click the 'Log In' link at the bottom of the page making sure the user is redirected to the 'Log In' page.

#### LOG IN ####

- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- Complete form with a username that is not registered in the 'users' collection ensuring a developer written message is flashed notifying the user that that username or password does not exist.
- Complete form where the username uses all lowercase letters ensuring that on form completion the username is recognised and the user is redirected to their profile page. 
- Complete form filling using the incorrect password.  When an incorrect format is used a warning is flagged, if an incorrect password is used a developer written message is flashed notifying the user that that username or password does not exist 
- Complete the form using the admin login details ensuring that they are redirected to the admin specific profile page.
- Click the 'Sign Up' link at the bottom of the page making sure the user is redirected to the 'Create Account' page.

#### LOG OUT ####

- Click 'Log Out' navbar item ensuring the user is redirected to the 'Log In' page and a developer written message is flashed confirming that the user has been logged out.

#### CONTACT #### 

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Load the contact page via the link in the footer and 'Let us know' link on the user profile.
- Click the location dropdown and ensure all expected options are available and able to be selected.
- Leave the location dropdown blank and ensure a warning is triggered when the 'Send Message' button is clicked.
- Check other required form fields trigger a warning when the 'Send message' button is clicked if not completed.
- Complete the form as expected and click cancel to ensure the page reloads - cross-check with 'messages' collection in the database to make sure the message has not been sent.
- Complete the form as expected and click 'Send message' to ensure the page reloads and a developer written message is flashed confirming the message has been sent - cross-check with 'messages' collection in the database to make sure the message was successfully sent.

#### 404 ####

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Hover over the 'home' link to ensure a change of color and cursor turns to a hand.
- Click the 'home' link to ensure the user is returned to index.html.


#### MY PROFILE - *USER* ####

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- On the initial log in ensure a message is flashed welcoming the user to the site.
- Make sure the username is displayed at the top of the page confirming that user's profile.
- Click the 'Let's find somewhere to eat' link and ensure it redirects the user to the restaurant's page.
- Click the 'Let us know' link and ensure it redirects the user to the contact page.
- Click the 'Add a review' button and ensure it redirects the user to the Add a review page.
- Check that the user's existing reviews are visible, cross-referencing with the database 'reviews' collection to make sure that none are missing.
- Click the 'Edit' button in the existing review section ensuring it redirects the user to the edit a review page and that the restaurant name and review body is pre-completed.
- Click the 'Delete' button in the existing review section ensuring it triggers a modal prompting the user to confirm that they want to delete that review.
- Re-open the 'Delete' modal and click the 'x' and 'Close' buttons to ensure that the modal is closed and no action is taken.
- Re-open the 'Delete' modal and click the 'Delete' button making sure the user is redirected back to their profile page and the review has been removed.
- Cross-check on the 'reviews' collection that the review no longer exists.
- When the user has no written reviews check that a suitable message is displayed in the Existing Reviews section.
- Click the visible 'leave a review' link and ensure it redirects the user to the 'Add a review' page.
- Try force way on to admin account making sure only the user's own profile page is displayed or the custom 404 page is displayed.

#### ADD REVIEW ####

- Test that only logged in users can access the add review page by manually typing in the route e.g. /review/add
- Change the screen size manually and to various mobile device sizes using devTools to verify that the form is responsive.
- Click the 'select restaurant' dropdown and ensure all restaurants in the database 'restaurants' collection are listed. Selecting each restaurant individually.
- Click the 'select rating' dropdown and ensure all options are available and able to be selected.
- Add text to the 'What do you think?' box ensuring that the box size is adjustable for larger reviews.
- Leave the 'select restaurant' and 'select rating' boxes blank and ensure a warning is triggered when the 'Add review' button is clicked.
- Fill in all details correctly and click the 'Add review' button making sure the 'Add a review' page reloads and a developer written message is flashed confirming the action.
- Write a review and click the 'Cancel' button making sure that the page reloads and the form is blank.

#### EDIT REVIEW ####

- Test that only logged in users can access the edit review page by manually typing in the route e.g. /review/edit
- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Check that clicking edit buttons on individual restaurant page and My Profile page re-routes user to the 'Edit Review' page and that the restaurant name and review body are auto-filled.
- Click the 'select restaurant' dropdown and make sure only the active restaurant is selectable.
- Click the 'select rating' dropdown.  Bug reported as not yet able to pre-fill this information.
- Edit text in the 'What do you think?' box ensuring that the box size is adjustable for larger reviews.
- Edit review details and click the 'Cancel' button making sure that the user is redirected to their profile page and that the review remains unchanged.
- Edit review details and click 'Edit my review' ensuring the user is redirected to their profile page and the corresponding review has been updated.

#### MY PROFILE - *ADMIN* ####

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- On the initial log in ensure a message is flashed welcoming the admin to the site.
- Make sure the admin username is displayed at the top of the page confirming that admin profile.
- In the 'User Messages' section check that all current messages are displayed - cross-checked with the 'messages' collection in the database.
- Send a new message via the contact page checking that the message is newly displayed in the 'User Messages' section.
- Click the 'Add a Restaurant' button and ensure admin is redirected to the 'Add a Restaurant' page.
- Click the 'Restaurant Added' button to ensure it triggers a modal prompting the admin to confirm that they have added that restaurant.
- Re-open the 'Restaurant Added' modal and click the 'x' and 'Close' buttons to ensure that the modal is closed and no action is taken.
- Re-open the 'Restaurant Added' modal and click the 'Restaurant Added' button making sure the user is redirected back to their profile page and the message has been removed - cross-check with the 'messages' collection in the database.
- Click the 'Restaurants' link to ensure the admin is redirected to the restaurant's page when wanting to edit/delete a restaurant.
- Try forcing way on to a user profile page making sure only the admin profile page is displayed or the custom 404 page is displayed.

#### ADD RESTAURANT - *ADMIN ONLY* ####

- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Log in as a standard user and attempt to navigate to the add restaurant page by manually adding /restaurant/add to the address.  Ensure that the user is not able and an appropriate response is given.
- Check that admin can access the 'Add Restaurant' page via the navbar link and button on their profile page.
- Click the 'how expensive' and 'mealtime' dropdowns and ensure all expected options are available and able to be selected.
- Leave the 'how expensive' and 'mealtime' dropdowns blank and ensure a warning is triggered when the 'Add restaurant' button is clicked.
- Complete the form ensuring that the form requires all fields to be completed, except the URL, before the form can be submitted. If a required field is left blank the user is given a prompt.
- On form submission ensure admin is redirected to their own profile page and a message is flashed confirming the addition of the restaurant.
- Check the successful addition of the new restaurant on the 'restaurants' page.
- Complete the form and hit the cancel button ensuring the admin user is redirected to their home page.

#### EDIT RESTAURANT - *ADMIN ONLY* ####

- Test that only admin users can access the edit page by manually typing in the route e.g. /restaurant/edit STILL TO TEST WITH FAKE REST_ID
- Change the screen size manually and to various mobile device sizes using devTools to verify that the page is responsive.
- Check that clicking edit buttons on individual restaurant pages re-routes user to the 'Edit Restaurant' page and that the majority of form information is auto-filled.  See bugs for exception to this.
- Edit restaurant details and click the 'Cancel' button making sure that the user is redirected to their profile page and that the restaurant information remains unchanged.
- Edit restaurant details and click 'Edit' ensuring the user is redirected to the all restaurants page and the corresponding restaurant info has been updated.

#### DELETE RESTAURANT - *ADMIN ONLY* ####

- Check that clicking the 'delete' button on individual restaurant pages triggers the 'Delete Restaurant' modal.
prompting the user to confirm that they want to delete that review.
- Re-open the 'Delete' modal and click the 'x' and 'Close' buttons to ensure that the modal is closed and no action is taken.
- Re-open the 'Delete' modal and click the 'Delete' button making sure the user is redirected back to the admin profile page.
- Cross-check in the database that the restaurant has been deleted.
- *PLEASE NOTE* it is intentional that reviews for the deleted restaurant remain in the database. Should the restaurant be re-added to the site, e.g. the restaurant re-opens after a brief spell of closure, the existing reviews will automatically be generated for the listing.

### ADDITIONAL TESTING ###

Throughout production this site has been tested using [Google Chrome's DevTools](https://developer.chrome.com/docs/devtools/).

In addition the Lighthouse feature has been used to test the Performance, Accessibility, Best Practices and SEO.  The following results were returned for laptop devices.

#### Home ####

![Lighthouse Home Page Desktop results](/documentation/images/lighthouse/home-desk.png)

#### All Restaurants ####

![Lighthouse Restaurants Page Desktop results](/documentation/images/lighthouse/restaurants-desk.png)

#### Individual Restaurants ####

![Lighthouse Individual Restaurants Page Desktop results](/documentation/images/lighthouse/indrest-desk.png)

#### Create Account ####

![Lighthouse Create Account Page Desktop results](/documentation/images/lighthouse/create-desk.png)

#### Log In ####

![Lighthouse Log In Page Desktop results](/documentation/images/lighthouse/login-desk.png)

#### Contact ####

![Lighthouse Contact Page Desktop results](/documentation/images/lighthouse/contact-desk.png)

#### Profile Page - User ####

![Lighthouse User Profile Page Desktop results](/documentation/images/lighthouse/user-prof-desk.png)

#### Add Review ####

![Lighthouse Add Review Page Desktop results](/documentation/images/lighthouse/add-review-desk.png)

#### Edit Review ####

![Lighthouse Edit Reivew Page Desktop results](/documentation/images/lighthouse/edit-review-desk.png)

#### Profile Page - Admin ####

![Lighthouse Admin Profile Page Desktop results](/documentation/images/lighthouse/admin-prof-desk.png)

#### Add Restaurant ####

![Lighthouse Add Restaurant Page Desktop results](/documentation/images/lighthouse/add-rest-desk.png)

#### Edit Restaurant ####

![Lighthouse Edit Restaurant Page Desktop results](/documentation/images/lighthouse/edit-rest-desk.png)

### BUGS ###

- *FOOTER* not sticky on the bottom of the page on iPad/iPad Pro - showing quite a lot of whitespace.
![Footer whitespace](/documentation/images/bugs/footer-bug.png).
    - FIX - Search on Slack directed me towards two resources [css-tricks sticky footer guide](https://css-tricks.com/couple-takes-sticky-footer/) and a [js Bin](https://jsbin.com/wokututopu/1/edit?html,css,output).  Testing both options I settled on the JS Bin, utilising flex, as it fitted with my existing code more succinctly.

- *EDIT REVIEW* and *EDIT RESTAURANT* pages, dropdown menus are not pre-filling the previously selected rating.
    - FIX - Not yet found.  For now, the text has been added reminding the user of their previous rating and prompting them to confirm their rating or select another.

### FURTHER TESTING ###

All pages were tested using [Google Chromes DevTools](https://developer.chrome.com/docs/devtools/) and the inbuilt mobile sizing -  all pages were tested across all available mock devices except Galaxy Fold.

As well as testing across the in-built mobile sizing on devTools I invited friends and family to view the site on their devices and report any issues.  Devices included:

- MacBook Pro
- MacBook Air
- iPad
- iPad Pro
- Pocophone F1 Mio
- Xiaomi Mi 10T Lite

There were no bugs or glitches reported from these tests.