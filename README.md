# Gamers Unite

![Not Logged in Front Page](/static/images/gamers-unite-front-page-no-login.png)
![Logged in Front Page](/static/images/gamers-unite-front-page-login.png)

---

## Live Site
[Gamers Unite](https://gamers-unite-eu.herokuapp.com/)

---

## Contents

- [Gamers Unite](#gamers-unite)
    - [Live Site](#live-site)
    - [Contents](#contents)
    - [Objective](#objective)
    - [Goals](#goals)
    - [User Stories](#user-stories)
        - [First Time Users](#first-time-users)
        - [Returning Users](#returning-users)
        - [Implementing User Stories](#implementing-user-stories)
    - [Website Design](#website-design)
        - [Colour Scheme](#colour-scheme)
            - [Background Colours](#background-colours)
            - [Text Colours](#text-colours)
        - [Font Families](#font-families)
        - [Images](#images)
    - [Features](#features)
        - [Implemented Features](#implemented-features)
        - [Future Features](#future-features)
    - [Testing](#testing)
        - [Bugs](#bugs)
            - [Bugs Found](/BUGS.md#bugs-found)
            - [Bugs Fixed](/BUGS.md#bugs-fixed)
        - [Lighthouse testing](#lighthouse-testing)
            - [What's been tested?](/LIGHTHOUSE.md#whats-been-tested)
                - [Homepage](/LIGHTHOUSE.md#homepage)
                    - [Homepage logged in](/LIGHTHOUSE.md#logged-in)
                    - [Homepage logged out](/LIGHTHOUSE.md#logged-out)
                - [Create a post](/LIGHTHOUSE.md#create-a-post)
                - [Edit a post](/LIGHTHOUSE.md#edit-a-post)
                - [View a post](/LIGHTHOUSE.md#view-a-post)
                    - [View a post logged in](/LIGHTHOUSE.md#logged-in-1)
                    - [View a post logged out](/LIGHTHOUSE.md#logged-out-1)
                - [Edit comment](/LIGHTHOUSE.md#edit-comment)
                - [Login page](/LIGHTHOUSE.md#login-page)
                - [Logout page](/LIGHTHOUSE.md#logout-page)
                - [Signup page](/LIGHTHOUSE.md#signup-page)
                - [Share post page](/LIGHTHOUSE.md#share-post-page)
        - [Manual testing](#manual-testing)
            - [Improvements made](#improvements-made)
        - [Responsive testing](#responsive-testing)
            - [Mobile](#mobile)
            - [Tablet](#tablet)
            - [Laptop](#laptop)
            - [Desktop](#desktop)
        - [HTML Testing](#html-testing)
            - [Webpage Links](#webpage-links)
            - [Textarea](#textarea)
        - [CSS Testing](#css-testing)
    - [Deployment Steps](#deployment-steps)
    - [Credits](#credits)


---
## Objective

Build a Full-Stack site based on business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

[Back to contents](#contents)

---

## Goals

The goal of this website is to provide a place where users can post about games they play, and when they play their games so that other users can play if they wish. The program should:

- Be error free within the program
- Have login/ logout functionality
- Have the ability to like and unlike posts
- Have the ability to create, edit and remove a post
- Have the ability to create, edit and remove comments on posts
- Have the ability to follow another user, putting their posts at the top of the logged in users page

[Back to Contents](#contents)

---
## User Stories

*The user stories created have given me a guide on what to add to the site*

### First Time Users

- >As a **first time user**, I can **view a post** so that **I can see clearly what the site is for**
- >As a **first time user**, I can **view comments** so that **I can see what other people are saying about posts**

---

### Returning Users

- >As a **returning user**, I can **register for an account** so that **I can follow other users**
- >As a **returning user**, I can **like posts** so that **I can show the post creator I like their content** 
- >As a **returning user**, I can **comment on posts** so that **I can show people what I think about a post**
- >As a **returning user**, I can **view user profiles** so that **I can see more about a user, and view all posts by that user**

---

### Implementing User Stories

For this project, I intend to follow the user stories. The requirements based on the user stories for the completion of this project are:

- >Viewing posts
- >Account registration
- >Creating new posts
- >Liking posts
- >Commenting on posts

Based on the user stories, optional additions which I will attempt to add to add to this project are:

- >Following users
- >Creating a user profile
    - >Viewing a user profile
    - >Viewing posts by individual users

All optional additions I will attempt to add to the final product before submission. Anything not added on final submission, will be added to [Future Features](#future-features)

[Back to contents](#contents)

---
## Website Design

The idea on the design of this website is to be viewed as a gaming website, with a pixelated site name, and fun looking headers and paragraphs for the rest of the page.

### Colour Scheme

These are the colours used for the website, separated by each loacation used

#### Background colours
- `#001css` is used as an alternate background colour incase the image doesn't render
- `#0000008a` is used for the header and footer background
- `#f0f8ff` is used as the background colour for each of the cards
- `#ff0000` is used as the background colour for each submit button

---

#### Text Colours
- `#808080` is used for the links to each post created
- `#a9a9a9` is used for a hover effect on each post link
- `#ffffff` is used for each button press, e.g: create post link, submit buttons
- `#000000` is used as a hover effect on each button
- `#212529` is used for the text in every text that isn't colour customized
- `#ff0000` is used as the colour of the like button, for its outline and its solid parts

[Back to Website Design](#website-design)    
[Back to Contents](#contents)

---

### Font Families

There are only 2 external font families used across the site, plus the default font family, and a fallback font for each external font. They are:

- >**Press Start 2P** is used whenever **Gamers Unite** is shown in the browser, which comes from [Google Fonts](https://fonts.google.com/specimen/Press+Start+2P)
- >**Default Font** is used at the footer of the page, which shows who created the website
- >**kalam** is used for every other part of the page, and comes from [Google Fonts](https://fonts.google.com/specimen/Kalam)
- >**Cursive** is used as a fallback font, where either or both of the external fonts don't work on a browser

[Back to Website Design](#website-design)    
[Back to Contents](#contents)

---

### Images

The only image used, is as a background used across the site, which is below

<img src="static/images/pixel-bg.jpg" height="100px" width="100px">

Any other images that are used on the website, are images posted by users, which are stored in [Cloudinary](https://cloudinary.com/)

[Back to Website Design](#website-design)    
[Back to Contents](#contents)

---

## Features

This page contains the features implemented up to the current development stage, plus features to be implemented in future stages. Future features will be ordered by importance, with the most important feature to add at the top of the list.

### Implemented Features

These features are fully implemented

- Registration - Register for an account, which'll eventually allow the user to post, comment, like other's posts and follow other users
    ![Register page](/static/images/gamers-unite-register.png)
- Login - Login to an account as a user to be able to post, comment, like posts and follow other users when implemented
    ![Login page](/static/images/gamers-unite-login.png)
- Logout - Logout of an account so that if a computer is shared, someone else doesn't have access to your account
    ![Logout page](/static/images/gamers-unite-logout-page.png)
- Create a post - Post what game you're playing, and about what you enjoy playing
    ![Create a post](/static/images/gamers-unite-create-a-post-page.png)
- Like/ unlike - Like a post by another user to show you like the game they're playing/ talking about, or unlike it for accidental likes   
    ![Like post](/static/images/gamers-unite-liked-post.png)   
    ![Unlike post](/static/images/gamers-unite-unlike-post.png)
- Viewing Posts - View a posts contents and comments
    ![View post](/static/images/gamers-unite-view-post.png)
- Comment on a post - Comment on posts so you can show what you're thinking
    ![Comment](/static/images/gamers-unite-comment.png)
- Edit a Post/Comment - Edit a Post/Comment that may have a typo or additions that have been forgotten
    ![Edit post](/static/images/gamers-unite-edit-post.png)
    ![Edit comment](/static/images/gamers-unite-edit-comment.png)
- Delete a Post/Comment - Delete a Post/Comment that may have been posted accidentally, or that is no longer wanted
    ![Delete post](/static/images/gamers-unite-delete-post-modal.png)
    ![Delete comment](/static/images/gamers-unite-delete-comment-modal.png)
- Follow/unfollow a user - Follow a user so that you can show your appreciation of their posts, or unfollow if you start not liking them
    ![Follow Users](/static/images/gamers-unite-follow-user.png)
    ![Unfollow Users](/static/images/gamers-unite-unfollow-users.png)
- Delete others comments - Delete a comment by another user, as the post creator, to be able to remove comments that offend you
    ![Delete others comments](/static/images/gamers-unite-delete-others-comment-modal.png)
- Share posts - Share others posts to show others what they're missing or to update others
    ![Share posts](/static/images/gamers-unite-share-post.png)

---

### Future Features

These features are either partially implemented, or to be worked on in the future

- Create a user profile - Create a bio to tell people a little bit about yourself and add a picture of yourself. A profile will also contain each post created by the user
  
[Back to Contents](#contents)

---

## Testing

### Bugs

This website was mostly tested manually. As there is an extensive explanation on how I fixed bugs, I have put all bugs in a separate file, links below:

[Bugs Found](/BUGS.md#bugs-found)   
[Bugs Fixed](/BUGS.md#bugs-fixed)   
[Back to contents](#contents)

---

### Lighthouse testing

I have done a number of lighthouse testing on all pages accessible by the user. These tests are accessible via a separate file, links below:

- [What's been tested?](/LIGHTHOUSE.md#whats-been-tested)
    - [Homepage](/LIGHTHOUSE.md#homepage)
        - [Homepage logged in](/LIGHTHOUSE.md#logged-in)
        - [Homepage logged out](/LIGHTHOUSE.md#logged-out)
    - [Create a post](/LIGHTHOUSE.md#create-a-post)
    - [Edit a post](/LIGHTHOUSE.md#edit-a-post)
    - [View a post](/LIGHTHOUSE.md#view-a-post)
        - [View a post logged in](/LIGHTHOUSE.md#logged-in-1)
        - [View a post logged out](/LIGHTHOUSE.md#logged-out-1)
    - [Edit comment](/LIGHTHOUSE.md#edit-comment)
    - [Login page](/LIGHTHOUSE.md#login-page)
    - [Logout page](/LIGHTHOUSE.md#logout-page)
    - [Signup page](/LIGHTHOUSE.md#signup-page)

[Back to contents](#contents)

---

### Manual testing

All of the testing that has been done has been all manual. All implented features have been tested by me and by other people to make sure everything works, and with each new feature, I tested all previously implemented features to make sure nothing broke with my new implementation.

#### Improvements made

These are the improvements I have made after testing each page manually:

- Changed some of my **views classes** to make sure only **authenticated users** can access *specific pages*
- Changed some of my **views classes** to make sure only the user that created a specific *post* or *comment* can *edit* or *delete* that *post* or *comment*
- For **user experience**, added *if conditions* within some of my *html* to *add* or *remove* specific features from the *page* and change the *sizes* of specific *sections* to compensate

[Back to Contents](#contents)
[Back to testing](#testing)

---

### Responsive testing

I have tested all the different viewport sizes that are possible for the website.

From mobile to desktop, here are the responsive viewpoints in picture form:

#### Mobile

![Gamers Unite Mobile View](/static/images/gamers-unite-mobile.png)

---

#### Tablet

![Gamers Unite Tablet View](/static/images/gamers-unite-tablet.png)

---

#### Laptop

![Gamers Unite Laptop View](/static/images/gamers-unite-laptop.png)

---

#### Desktop

![Gamers Unite Desktop View](/static/images/gamers-unite-desktop.png)

[Back to Contents](#contents)   
[Back to Testing](#testing)

---

### HTML Testing

*Due to how my webpage works, the w3c validator can't check all of my html code via webpage link. Therefore, the top of this section consists of html code that could be checked by the w3c validator via weblink, and the bottom section consists of html code that couldn't be checked via w3c validator weblink, so has been checked via textarea on the validator*

#### Webpage links

My Home page template came back with no errors   
[Home page Testing](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgamers-unite-eu.herokuapp.com%2F#l93c38)   
![Home Page Test Result](/static/images/gamers-unite-home-page-checks.png)

---

My view post template came back with a single error, which relates to base.html. The error shown by the image below has the same h1 element in all my pages, which is the title of my webpage, **Gamers Unite**. This has been tested on multiple posts, and the same error come up.   
[View post testing](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgamers-unite-eu.herokuapp.com%2Fpost%2F35%2F#l93c38)   
![View Post Test Result](/static/images/gamers-unite-view-post-checks.png)   
![View Post Code With Error](/static/images/gamers-unite-view-post-issue.png)

---

My signup page template came back with no errors   
[Signup testing](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgamers-unite-eu.herokuapp.com%2Faccounts%2Fsignup%2F#l93c38)   
![Signup Test Result](/static/images/gamers-unite-register-checks.png)

---

My login page template came back with no errors   
[Login testing](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgamers-unite-eu.herokuapp.com%2Faccounts%2Flogin%2F#l93c38)   
![Login Test Result](/static/images/gamers-unite-login-checks.png)

[Back to Contents](#contents)   
[Back to Testing](#testing)

---

#### Textarea

*Due to the url of the Textarea checks, I haven't left a link to these checks, as the urls all contain #textarea and are not unique*

My new post page template came back with no errors

![New post test result](/static/images/gamers-unite-create-a-post-checks.png)

---

My edit post page template came back with no errors

![Edit post test rseult](/static/images/gamers-unite-edit-post-checks.png)

---

My edit comment page came back with a single error, which is the same error that occurred on the view post page. I have left this as it is, since the error that pops up relates to base.html, and the h1 element is question is the pages main heading element, therefore would need to be a h1 element to represent that

![Edit comment test result](/static/images/gamers-unite-edit-comment-checks.png)
![Edit comment Code with error](/static/images/gamers-unite-edit-comment-issues.png)

---

My logout page came back with no errors

![Logout test result](/static/images/gamers-unite-logout-checks.png)

---

My share post page came back with no errors

![Share post test result](/static/images/gamers-unite-share-post-checks.png)

[Back to Contents](#contents)   
[Back to Testing](#testing)

---

### CSS Testing

The CSS jigsaw validator tested all of my css and all external css. As a result, it checks my style.css, bootstrap and fontawesome CSS stylesheets. I'm only gonna be sharing the results I found for my custom style.css, which came up with no errors

[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgamers-unite-eu.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)   
![Jigsaw validator results](/static/images/gamers-unite-css-checks.png)

[Back to Contents](#contents)   
[Back to Testing](#testing)

---

## Deployment steps

The steps I used for deployment are as follows:

1. Create new app in heroku
2. Create database with ElephantSQL
3. Commit and push to github
4. Create config vars in heroku via settings tab
    1. CLOUDINARY_URL (from cloudinary)
    2. DATABASE_URL (from ElephantSQL)
    3. PORT
    4. SECRET_KEY
5. Go to resources tab and connect heroku app to github repository
6. Deploy from main branch in github

[Back to Contents](#contents)

## Credits

Below are all resources that I used to research some of the code or images in this website

- [Modals](https://getbootstrap.com/docs/5.0/components/modal/)
- [CSRF Token](https://docs.djangoproject.com/en/3.2/ref/csrf/)
- [Static Storage](https://cloudinary.com/)
- [Like and comment icons](https://fontawesome.com/)
- [Bootstrap spacing](https://getbootstrap.com/docs/4.1/utilities/spacing/)
- [Django html if statements](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/)
- [Heading font](https://fonts.google.com/specimen/Press+Start+2P?preview.size=20)
- [Main site font](https://fonts.google.com/specimen/Kalam?preview.size=20)
- [Nav bar active states](https://stackoverflow.com/questions/64244962/django-how-to-change-nav-class-with-change-in-url)
- [Django Redirects](https://www.askpython.com/django/django-redirects)
- [Login required mixin](https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin)
- [ifequal in some html file checks](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#ifequal)
- [Uploading to cloudinary](https://cloudinary.com/documentation/django_image_and_video_upload)
- [Post sharing help](https://github.com/legionscript/socialnetwork/tree/tutorial17/social)
- [Same model foreignkey](https://stackoverflow.com/questions/11214175/can-i-make-a-foreignkey-to-same-model-in-django)

[Back to Contents](#contents)