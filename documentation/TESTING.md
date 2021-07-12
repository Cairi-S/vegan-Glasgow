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