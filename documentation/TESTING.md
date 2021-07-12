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