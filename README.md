
# Vegan Glasgow #
![Vegan Glasgow Site Mockup](/documentation/images/vg-mockup.png)

*TOC here*

As a vegetarian with a dairy allergy I’m an enforced vegan. However, I love food and am always on the lookout for restaurant recommendations in my local area that can cater to my dietary requirements. I’ll be honest, when dining out vegetarian options can be limited - we’ve all been served a mushy risotto or, my hands-down worst meal, a plate of boiled cauliflower and potatoes (which the restaurant charged £10 for).

These personal experiences inspired me to create *Vegan Glasgow*, for locals and visitors to my home city of Glasgow, to share their experiences and help take the guesswork out of finding a great vegan meal.

[A live preview of Vegan Glasgow is available here](https://vegan-glasgow.herokuapp.com/)

### GOALS ###
#### VISITOR GOALS ####
Target audience:

- Vegans, vegetarians, or people who would like to eat a more plant-based diet. 
- Self-proclaimed ‘foodies’.
- People who live in the Glasgow area.
- People who are visiting Glasgow or are planning a trip to the city.

#### USER GOALS ####
- Have somewhere to find restaurant recommendations. 
- Explore the amazing food scene of the city of Glasgow.
- Be able to leave reviews for other users to help them.

User Specific Goals:

- Find out contact information for individual restaurants.
- Find external links to restaurants' homepages and social media where appropriate.
- See attractive images of the restaurant so I can judge whether I might enjoy the food and atmosphere.
- Find information on the cuisine ie/ Italian, Traditional Scottish, Japanese, Fusion.
- Find out the price range.
- Find what mealtimes restaurants are open.
- Be able to create an account and have an individual profile.
- Be able to leave reviews to help advise others.
- Be able to Edit my reviews if my opinions change.
- Be able to Delete my review if I no longer wish to comment on a restaurant.
- Be able to add restaurants to the website if I find somewhere which is not already listed.

Why does Vegan Glasgow meet these user needs:

- As an enforced vegan dining out can be stressful so I spend a lot of time searching for restaurant menus and possible food options, therefore I have a good understanding of potential users' needs.
- The design of the site is clear and accessible and information is laid out in a user-friendly way.
- The site allows visitors to leave reviews meaning experiences are continuously updated and
remain relevant.
- The website features the designer's favourite recommendations (using the "our recommendation" feature). In future, this would be changed to an average of user ratings.

Admin Specific Goals:

- Be able to edit user reviews if inappropriate.
- Be able to add, edit restaurant info or delete a restaurant should it close
- Be able to receive notifications from users on new restaurants in the area.

#### WEBSITE GOALS ####
- A user-friendly site that allows foodies to find recommendations of places to eat based on their tastes.
- An opportunity for the developer to further develop their frontend programming skills using HTML, CSS, Bootstrap and JavaScript.
- An opportunity for the developer to practice their newfound backend programming skills using Python, MongoDB, Flask and Jinja.

### USER STORIES ### 
Visitor Stories:

As a visitor to Vegan Glasgow I would like:

- To find menu item recommendations quickly and easily.
- To quickly see what type of food is served so I can choose a restaurant based on my tastes. 
- To know where I can buy alcoholic drinks that also cater to my dietary choices.
- To have quick access to price points so I know that I will be dining out within my budget.
- To know where I can grab a "cheap and cheerful" bite to eat while maintaining my dietary choices.
- To know where I can dine out locally when I am too tired to cook a meal at home.
- To quickly find restaurants close to the area of the city I am exploring when hunger hits. 
- To find rough mealtimes of restaurants so I know what will be open when I am looking to dine.
- To be able to find cafe options as well as restaurants for those times I just want coffee and a cake.
- To be able to express my thoughts on a restaurant and its menu.
- To be able to change my mind and update an earlier review if I return to a restaurant and the service and quality of food have changed.
- To be able to contact the site about exciting new restaurants I have discovered.

**The following is covered as a possible future feature**

### BUSINESS STORIES ###

If Vegan Glasgow were to be monetised, businesses may want to:
- Quickly see information about competitors.
- See that the various methods of contacting my restaurant are displayed clearly.
- Have the ability to edit my own restaurant's page to keep all information up to date.
- Use forms to quickly and efficiently log information.
- Be able to advertise special offers and deals.

**End of future feature**

### DESIGN CHOICES ### 
#### FONTS ####
All chosen fonts were taken from [Google Fonts](https://fonts.google.com/?preview.text=Vegan%20Glasgow&preview.text_type=custom)

[Lobster](https://fonts.google.com/specimen/Lobster?preview.text=Vegan%20Glasgow&preview.text_type=custom)
- All Logos, titles, subtitles and headers.
![Google Fonts - Lobster](/documentation/images/lobster.png)

[Muli](https://fonts.google.com/specimen/Muli?query=muli&preview.text=Vegan%20Glasgow&preview.text_type=custom)
- Font used for all other text items.
- *Please note* Since deciding on the font Muli it has been updated in Google Fonts to [Mulish](https://fonts.google.com/specimen/Mulish).  All research suggests this is only a rename and no other changes to the font have been made.
![Google Fonts - Muli](/documentation/images/muli.png)


#### ICONS ####
Thanks to [Font Awesome](https://fontawesome.com/), the website utilises icons to make a large amount of information quickly identifiable and easy to absorb:

e.g/
- Plus sign = Add an item
- Trash can = Delete an item
- Pencil = Edit an item
- Location marker = address
- Telephone = contact number
- Cheese = dairy options Meat(drumstick) = Meat options

#### COLOR ####
After researching color theory, shades of green were selected to suggest nature, freshness and safety.  

Green is synonymous with veganism and, of course, we always want our food to be fresh.  Finally, the origins of the name 'Glasgow' are widely believed to be 'green hollow' or (dear)'green place'.

[Coolors](https://coolors.co/) and [Color Tool Material Design](https://material.io/resources/color/#!/?view.left=0&view.right=0&primary.color=560027&secondary.color=E0E0E0) were used to select the color palette.

![Coolors color palette](/documentation/images/color-palette.png)

1. Navbar, footer, internal sub-headings: #629490. 
    - A green evoking natural and freshness.
2. Main Background: White.
    - Providing contrast and depth.
3. Cards and navbar/footer text: #e0e0e0. 
    - Providing depth and clearly sections information areas. 
4. Card text and borders: #243119.
    - Clearly stands out against all other colors used.

Buttons use the easily identifiable traffic light system:
- Positive actions (e.g. submit/add) - Green
- Editing actions - Amber
- Negative actions (e.g. cancel/delete) - Red

### WIREFRAMES ###

#### HOME ####

![index.html](/documentation/images/wireframes/home.png)

#### CREATE ACCOUNT ####

![create_account.html](/documentation/images/wireframes/create-account.png)

#### LOG IN ####

![login.html](/documentation/images/wireframes/login.png)

#### CONTACT ####

![contact.html](/documentation/images/wireframes/contact.png)

#### ALL RESTAURANTS ####

![restaurants.html](/documentation/images/wireframes/all-restaurants.png)

#### INDIVIDUAL RESTAURANTS ####

![view_restaurant.html](/documentation/images/wireframes/view-restaurant.png)

#### USER PROFILE ####

![user_profile.html](/documentation/images/wireframes/user-profile.png)

#### ADD REVIEW ####

![add_review.html](/documentation/images/wireframes/add-review.png)

#### EDIT REVIEW ####

![edit_review.html](/documentation/images/wireframes/edit-review.png)

#### ADMIN PROFILE ####

![user_profille/admin_profile.html](/documentation/images/wireframes/admin-profile.png)

#### ADD RESTAURANT ####

![add_restaurant.html](/documentation/images/wireframes/add-rest.png)

#### EDIT RESTAURANT ####

![edit_restaurant.html](/documentation/images/wireframes/edit-rest.png)

### FEATURES ###

#### Existing features ####

All pages:

+ Navbar - standard on desktop/tablet. 
+ Burger menu on mobile.
+ Vegan Glasgow logo top left corner as per standard UX design.
+ Footer
+ Flashed messages to confirm actions or give the user additional information.

Users who are not logged in will see the following navbar links: 
- Home
- Restaurants
- Create Account
- Log In

Users who are logged in will see the following navbar links: 
- Home
- Restaurants
- My Profile
- Add Review  
- Log Out

Admin users will see the option to 'Add Restaurant' instead of 'Add Review'.

The footer will contain:
- Copyright information
- Contact link
- Vegan Glasgow socials

Home Page:

- Hero image - aerial shot of the iconic River Clyde sweeping through Glasgow which is an identifiable representation of the city.
- Slogan positioned directly underneath the Hero image to clearly show the purpose of the website
- Top recommendations cards - Users are immediately able to see Vegan Glasgow's top recommendations. Cards will link directly to the individual restaurant's page.
- Cards will feature an image of either the restaurant's interior, exterior, or a dish they serve. Important information about the restaurant will also be displayed such as contact details, price range, mealtime opening hours and a short synopsis of the restaurant written by the admin team.

All Restaurants page:

- As per the Home page restaurants will be displayed on cards that link directly to the individual restaurant's page.
- Information displayed will be the same as on the Home page cards.

Individual Restaurants page:

- The information on the restaurant's cards will be displayed clearly.
- Users will be presented with a button prompting them to 'Add a review'.
- User's are also presented with reviews that have been left for that restaurant.  If the review is written by the logged-in user they also have the opportunity to edit or delete that review.
- The admin team is also able to add reviews, in addition, they are presented with buttons to edit the restaurant's information or delete the restaurant entirely.
- The edit button takes users to the corresponding edit page - most of the data will be prefilled from the database allowing the user to fully update their review or the restaurant information (depending on whether standard user or admin) or extend the information that has already been left.
- The delete button prompts a modal that asks the user to confirm the deletion of that item.  They can close or cancel the request if preferred.

Create Account page:

- When users create an account they will be asked to enter a username, password and to confirm their password via a form.
- The Create Account page utilises the icons user-plus, user-lock and user-check-double to clearly show the input area's purpose.
- The username will be checked to ensure the chosen username does not exist in the database and that it adheres to the chosen username requirements.
- The password will be checked to ensure that it meets the chosen regex requirements.  In addition, the user is required to enter the password again and both passwords are checked to ensure a match.
- Any issues will be flagged via flashed messages as detailed above.
- A 'create account' button makes use of the '+' icon to prompt the user to create their account.  Once clicked this takes the user to their account page, provided there are no issues with their inputted information.
- Should the user have an account already there is an additional link to the 'Log In' page.  When the user hovers over the words 'Log In!' the text becomes underlined to clearly show a clickable element.
- All information is displayed upon a large card which is similar in styling to the restaurant cards for continuity.

Login page:

- A simple Log In page which is similar in style to that of the 'Create Account' page.
- Users are required to enter their Username and Password via a form.
- The Log In page utilises the icons 'user-cog' and 'user-lock' to clearly show the input areas purpose.
- Similar to the Create Account page, the Log In page has a clearly displayed 'Log In' button to prompt the user to log in to their account.  Once clicked this takes the user to their account page, provided there are no issues with their inputted information.
- Should the user not yet have an account there is an additional link to the 'Create Account' page.  When the user hovers over the words 'Sign Up' the text becomes underlined to clearly show a clickable element.
- Any issues will be flagged to the user via flashed messages.

Logout link:

- Once the user has clicked the 'Log Out' button they will be redirected to the Log In page and a flashed message confirms the log out and wishes them well.

My Account page (users):

- A simple Account page which is similar in style to that of the 'Create Account' page.
- On initial Log In the user is presented with a flashed message confirming their username and prompting them to find somewhere to eat.
- At all points during the session user's name is displayed as a header.
- Users are immediately provided with a link to the restaurant's page.
- Users are given a link to the contact page should they have discovered a new restaurant.
* Users can see all their own reviews via a sectioned off 'My reviews' section.  Here they will find:
    * The 'add a review' button, which redirects the user to the add a review form.
    * Details of their existing reviews.
    * Buttons to allow the user to edit and delete their existing reviews - as with all instances of the edit button it redirects the user to the corresponding 'Edit' page where some of the information will have been prefilled via database access.  Clicking the delete button prompts a modal asking the user to confirm the action.

My Account page (admin):

- Similar to regular users, on the initial log in, admin are presented with a flashed message confirming their username and at all points, the Admins username is displayed as the header.
* The first section the admin team are presented with is users messages where admin can see requests of restaurants to be added to the site.  Displayed information is:
    * User who has made the request
    * Name of the restaurant to add
    * The rough location of that restaurant
    * Why the user feels it would be a good addition to the side.
    * A 'Restaurant added' button to remove the message once complete.  Clicking this button prompts a modal display asking the admin team to confirm the restaurant has been added.
- Underneath User Messages the 'Add Restaurant' button is displayed to quickly take the admin to the add restaurant page.
- Finally, the admin team can visit the Restaurants page to edit or delete restaurants information. A future feature would be for the admin team to be able to do this directly from their account page.

Add review page:

- Upon clicking any 'Add a review' link users will be redirected to that page.  The link will be styled link a button.
- On this page users can select the restaurant they would like to review, a rating out of 5 for the restaurant, and leave their thoughts on the restaurant.
- Their review can be added to the database via clicking the 'Add My Review' button or the action can be canceled should they change their mind.
- Once a review has been added a flashed message thanks them for adding a review and the user is redirected to the Add review page in case they wish to review another restaurant.

Edit review page:

- Similar to the Add a review page.
- Upon clicking any 'Edit My Review' button users will be redirected to the edit a review page.
- Previously inputted form information is pulled from the database to allow the review to be easily updated.
- The updated review can be added to the database via clicking the 'Edit My Review' button or the action can be cancelled should they change their mind.
- On clicking the 'Edit My Review' button the user is redirected to their own account page.

Add restaurant page:

- Similar to the 'Add a Review' page but only accessible to admin users.
- A form guides the admin user through adding a restaurant, required inputs include text input, dropdown menus for items such as mealtimes and price points, a checkbox for identifying recommended restaurants and a URL for the admin team to choose the image representing the restaurant.
- In future, an external database would be used for hosting images, such as Cloudinary.
- The restaurant is added by clicking the 'Add Restaurant' button, this flashes a message confirming the addition of that restaurant and redirects admin back to their profile page for easy access to removing tasks.
- Should the admin change their mind about adding the restaurant they can cancel the action.

Edit restaurant page:
- Similar to the 'Edit Review' page but only accessible to admin users.
- The updated restaurants can be added to the database via clicking the 'Edit Restaurant' button or the action can be canceled should they change their mind.
- On clicking the 'Edit Restaurant' button the user is redirected to the restaurant's page and a message is flashed thanking them for editing the information

Contact page:
- The contact page is to allow users to request new restaurants be added to the site.
- The contact page uses a form to harvest data which is stored in the database and posted on the admin account page.
- Form data includes text inputs for the restaurant to be added such as restaurant name and why the user thinks Vegan Glasgow should be aware of the restaurant.  A dropdown menu asks users to select the area of Glasgow where the restaurant is based to ensure the correct restaurant is added (where perhaps more than one restaurant with the same name could exist).
- The green 'send my message' button adds the message to the database and a message is flashed to the user to confirm its submission.  Users also have the option to cancel should they change their mind.

404 page:
- The custom 404 Page shows a cute image of a dropped ice cream, a link is displayed to return the user to the home page.

### FUTURE FEATURES ###
Unfortunately, due to time contraints, the initial design of the website was not able to be fully realised.  The features left to implement are:
- Pagination - The page will display 8 cards (2x4, desktop), 4 cards (2x2, tablet, 1x4, mobile). Users will be able to move through pages using the bottom page function, this minimises information overload, and scroll, on a single page.
- Email authentication.

Vegan Glasgow is currently only for private recommendations, however, there could be future scope to monetise the site and would be a future feature.

If this were the case the target businesses for Vegan Glasgow would be:

- Vegan restaurants in the area.
- Restaurants wanting to reach a wider audience.
- Restaurants advertising that they are fully vegan or have transitioned to fully vegan.
- Restaurants advertising the vegan options on their menu

Business user goals would be:

- A well-designed website that is easy for the public to navigate that will benefit my business to be a part of.
- A design that allows me to input and update my own restaurant's data easily and efficiently.
- Value for money.

Additional future features might be:

- Ability for users to ‘favourite’ restaurants which show on their ‘My Account’ page.
- Ability to add own photographs to reviews.
- Edit profile option, e.g. change password.
- Delete account.
- Map API plotting the location of restaurants.
- Additional information on restaurants
- Have Superuser ability for restaurants to have/host their own page (paid feature). Superusers being able to advertise offers, online ordering and have direct business contact.
- Filter menu option - Users will have the option to filter restaurant results by the most popular filter choices e.g. location, food category, group type, price and average reviews.
- Remove 'our recommendation' option from admin and instead display the top 3 restaurants based on average user rating.

### DATABASE MODEL ###
As this database will be unstructured and additional requirements may be added in the future MongoDB’s non-relational database has been chosen to create this site. In addition, mySQL is recommended for the final project so I am taking the chance to practice using MongoDB just now.

![DB diagram](/documentation/images/db-diagram/db-diagram.png)

Restaurants collection

|Key|Type|Notes|
|---|----|-----|
|_id|ObjectId| |
|name|String| |
|phone_number|String| Research into MongoDB's storage system suggested that telephone numbers should be stored as strings to allow for extra characters, e.g. +44... in area codes.|
|address|String| |
|website|String| |
|price_range|String| This utilises the £ symbol from the keyboard, whilst researching the best data-type for this string was decided upon as char is not listed as a possibility. |
|cuisine|String| |
|open_times|String| |
|summary|String| |
|restaurant_img_url|String| |
|our_recommendation|String| TO BE UPDATED TO BOOLEAN |

Review collection

|Key|Type|Notes|
|---|----|-----|
|_id|ObjectId| |
|restaurant_name|String| |
|restaurant_rating|String| In future this would be listed as an integer,  
|review|String|
|created_by|String|
     

User collection

|Key|Type|
|---|----|
|_id|ObjectId|
|username|String|
|password|String|
|message|String|

Messages collection

|Key|Type|
|---|----|
|_id|ObjectId|
|created_by|String|
|restaurant_name|String|
|location|String|
|message|String|

### Technologies Used ###

This project uses the following programming languages:
- HTML
- CSS
- Python
- JavaScript

This project was built using [Gitpod](https://gitpod.io/).

The creation of this website would not have been possible without:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Balsamiq](https://balsamiq.com/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [MongoDB](https://www.mongodb.com/atlas)
- [PyMongo](https://pypi.org/project/pymongo/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
- [Google Fonts](https://fonts.google.com/) 
- [Font Awesome](https://fontawesome.com/) 
- [AutoPrefixer](http://autoprefixer.github.io/)
- [cdnjs](https://cdnjs.com/)
- [W3C HTML Markup Valication service](https://validator.w3.org/)
- [W3C CSS valication service](https://jigsaw.w3.org/css-validator/)
- [TinyPNG](https://tinypng.com/)
- [Coolors](https://coolors.co/)
- [Color Tool - Material Design](https://material.io/)
- [HTML Formatter](https://webformatter.com/html)
- [Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/index.php)
- [markdown-toc](https://ecotrust-canada.github.io/markdown-toc/)
- [dbdiagram.io](https://dbdiagram.io/home)

### Testing ###

Testing infomation can be found in a separate [TESTING.md document](/documentation/TESTING.md)

### Deployment ###

To run this project you will require your own IDE, e.g [GitPod]((https://gitpod.io/))

You will also need to install the following:

- [PIP](https://pip.pypa.io/en/stable/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)

In addition, you will need an account with [MongoDB Atlas](https://www.mongodb.com/atlas).  You can learn more about setting up an account with the [MongoDb documentation](https://docs.atlas.mongodb.com/).

#### Clone the repo ####

1. Navigate to the 'Vegan Glasgow' repository.
2. Click the Code dropdown menu next to the green Gitpod button.
3. In the dropdown copy the URL displayed under the header CLONE with the HTTPS title underlined (in this instance https://github.com/Cairi-S/vegan-glasgow.git).
4. Open your local IDE and launch Git Bash.
5. Create a new folder or navigate to the folder where you want the clone to be stored.
6. Once opened type 'git clone' and HTTPS URL copied earlier (e.g. git clone https://github.com/Cairi-S/vegan-glasgow.git)
7. Once you press 'enter' the clone will be created.
8. Created a new file to store your environmental variables named env.py.
9. To the env.py file add the following environmental variables:

````console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<secret_key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@myfirstcluster.8s17w.mongodb.net/<db_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<db_name>")
````
10. Add the env.py file to your .gitignore file.  ** THIS IS EXREMELY IMPORTANT TO ENSURE YOUR ENVIRONMENTAL VARIABLES ARE NOT PUSHED PUBLICALLY **.
11. Run your app locally using 
````console
python3 app.py
````

#### Deploy to Heroku ####
1. Create a requirements.txt file by typing the following into the terminal:
````console
pip3 freeze --local > requirements.txt
````
2. Create a Procfile by typing the following into the terminal:
````console
echo web: python app.py > Procfile
````
3. Add these files to GitHub via the usual methods: git add, git commit and git push.
4. Log in to your [Heroku](https://id.heroku.com/login) account.
5. Click the 'New' dropdown menu on your dashboard.
6. Select 'Create New App'
7. Select a unique name for your app.
8. Choose the location closest to you (in the developer's instance this was Europe) and click 'Create App'.
9. From the app dashboard select the 'Deploy' tab and under 'Deployment Method' select GitHub.
10. Navigate to the section 'Connect to GitHub', enter your GitHub and the name of the repository you wish to connect to and click 'search'.
11. Once found click 'Connect'.
12. Return to the top of the Heroku dashboard and click the 'Settings' tab.
13. On the Settings page navigate to 'Config Vars' and then click 'Reveal Config Vars'.
14. Enter the Key Value pairs, matching those created in the previously mentioned env.py file:

|Key|Value|
|---|-----|
|IP|0.0.0.0|
|PORT|5000|
|SECRET_KEY|<secret_key>|
|MONGO_URI|mongodb+srv://<username>:<password>@myfirstcluster.8s17w.mongodb.net/<db_name>?retryWrites=true&w=majority|
|MONGO_DBNAME|<db_name>|
15. Click 'Hide Config Vars' and return to the top of the dashboard navigating back to the 'Deploy' tab.
16. Navigate to the 'Manual Deployment' section.
17. Under 'Select branch to deploy' click 'master' before clicking 'Deploy Branch' and wait for the build to be completed.
18. Once completed return to the top of the dashboard and click 'Open App'.  The site has now been successfully deployed.

### Credits ###

#### Content ####
- I will forever be thankful to [Tim Nelson](https://github.com/TravelTimN) and his Task Manager mini project which is part of the Code Institute coursework.  Elements of this tutorial were used and expanded upon throughout the project.

- Many thanks to [geeksforgeeks.org](https://www.geeksforgeeks.org/) and their guide to [Python pattern matching](https://www.geeksforgeeks.org/pattern-matching-python-regex/).

- Many thanks to [css-tricks.com](https://css-tricks.com) for their [guide to line-clamp](https://css-tricks.com/almanac/properties/l/line-clamp/).

#### Images ####
Individual restaurant images used in this project were found using [Google Images](https://www.google.com/imghp?hl=en) and typing in the restaurants name. These images are used for educational purposes only and full credit goes to the original owner.

**Favicon**
- Taken from [favicon.io](https://favicon.io/) and the open-source project [Twemoji](https://twemoji.twitter.com/).

**Hero**
- The aerial image of the River Clyde winding its way through Glasgow City Center is a [photo by Adam Marikar](https://unsplash.com/photos/7vJX8cIgLao) taken from [Unsplash](https://unsplash.com/).

**Alt img**
- The image of a veggie bowl is a [photo by Luisa Brimble](https://unsplash.com/photos/2RrBE90w0T8) taken from [Unsplash](https://unsplash.com/).

**404**
- The image of a dropped ice-cream cone is a [photo by Sarah Kilian](https://unsplash.com/photos/52jRtc2S_VE) taken from [Unsplash](https://unsplash.com/).

### Acknowledgements ###
As always this project would not have been possible without the fine people of Code Institute and Slack.  In particular:
- My mentor who has been a fantastic guide through this project.
- Slackers BenKav, who has been an exceptional lead, and Christopher Undritz, who has been working on this Python journey at the same time.
- The CI Tutor support team.