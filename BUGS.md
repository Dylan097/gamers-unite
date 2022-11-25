# Bugs

## Contents

- [Gamers Unite](/README.md#gamers-unite)
    - [Live Site](/README.md#live-site)
    - [Contents](#contents)
    - [Objective](/README.md#objective)
    - [Goals](/README.md#goals)
    - [User Stories](/README.md#user-stories)
        - [First Time Users](/README.md#first-time-users)
        - [Returning Users](/README.md#returning-users)
        - [Implementing User Stories](/README.md#implementing-user-stories)
    - [Website Design](/README.md#website-design)
        - [Colour Scheme](/README.md#colour-scheme)
            - [Background Colours](/README.md#background-colours)
            - [Text Colours](/README.md#text-colours)
        - [Font Families](/README.md#font-families)
        - [Images](/README.md#images)
    - [Features](/README.md#features)
        - [Implemented Features](/README.md#implemented-features)
        - [Future Features](/README.md#future-features)
    - [Testing](/README.md#testing)
        - [Bugs](/README.md#bugs)
            - [Bugs Found](#bugs-found)
            - [Bugs Fixed](#bugs-fixed)
        - [Lighthouse testing](/README.md#lighthouse-testing)
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
        - [Manual testing](/README.md#manual-testing)
            - [Improvements made](/README.md#improvements-made)
        - [Responsive testing](/README.md#responsive-testing)
            - [Mobile](/README.md#mobile)
            - [Tablet](/README.md#tablet)
            - [Laptop](/README.md#laptop)
            - [Desktop](/README.md#desktop)
        - [HTML Testing](/README.md#html-testing)
            - [Webpage Links](/README.md#webpage-links)
            - [Textarea](/README.md#textarea)
        - [CSS Testing](/README.md#css-testing)
    - [Deployment Steps](/README.md#deployment-steps)
    - [Credits](/README.md#credits)

## Bugs found
These are the bugs found whilst programming 

1. **Custom styles** not working on the website.
2. **Navbar** moving upwards when there was a **large number of comments**.
3. **Posts** wouldn't load when clicked on.
4. **Leave a comment** card extended down past **comments** card.
5. **Admin page** wouldn't load **post or comment** for adjustments.
6. **Comments** wouldn't load in the *Leave a comment:* section of the page when clicking *Edit comment*.
7. **Delete** function would just return to the home page without deleting a post.
8. The **delete** function wouldn't allow me to stop other users that didn't create the given post/ comment to *delete* the post/comment.
9. **Images** would always default to *placeholder* whether an image was added or not.
10. **Following** wasn't working, and would always redirect me to 404 error page

[Back to Contents](#contents)   
[Back to Testing in README.md](/README.md#testing)

--- 

## Bugs Fixed
These are the fixes for each bug, in the same order as each bug found in [bugs found](#bugs-found)

1. In **settings.py**, I found 
    ```python
    STATICFILES_DIR = [os.path.join(BASE_DIR, 'static')]
    ```
    instead of 
    ```python
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    ```
    Once this had been fixed, my custom styles started to work

2. In **base.html**, change
    ```html
    <nav class="navbar sticky-top navbar-expand-lg navbar-dark dark-bg">
    ```
    to
    ```html
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark dark-bg">
    ```
    after that change, the navbar stays at the top of the page whenever the user scrolls down, making it easier for the user to navigate to the home page, or login/out

3. Changed the file name from **post_details.html** to **post_detail.html**
4. In **post_detail.html**, changed from 
    ```html
    <div class="col-md-4 card md-4 mt-3">
    ```
    to
    ```html
    <div class="col-md-4 card mb-4 mt-3">
    ```
    This minor change added a bottom margin to the **Leave a comment** card, which made this card in line with the **comments** card.
5. I found out, with the help of **Jack Wachira**, that there was a migration issue, where I had attempted to add a **uuid** to my **Post** model. This was fixed by doing the below command:
    ```
    python3 manage.py migrate gamers_unite zero
    ```
    After this command was run, I deleted previous migrations, then I ran:
    ```
    python3 manage.py makemigrations
    ```
    and then:
    ```
    python3 manage.py migrate
    ```
    This had fixed the issue, and the website was once again running normally.
6. In **views.py**, I found that I had added a *request.POST* to my *commentForm()* when I was defining *get* in my *EditComment* class. 
    ```python
    edit_comment = CommentForm(data=request.POST, instance=comment)
    ```
    Once I had removed *data=request.POST*, the **comment** was then showing in the **Leave a comment:** section of my page
7. *When testing the **delete** function, I was testing with post deletion, as I was using the same class for comment deletion, therefore, the same bug would've been in comment deletion. Comment deletion was tested after I had fixed the post deletion issue and tested post deletion fully.*
    
    When calling the *.delete()* function, I had forgotten to add parentheses to *.delete()*. This was causing the function to not be called.
8. When trying to add:
    ```python
    if post.author_id == self.request.user.id:
        {Code Block}
    if comment.creator_id == self.request.user.id:
        {Code Block}
    ```
    my website would come up with an error telling me that I didn't have an argument for *request*.

    I found that, as my *delete* class was originally a function, I was unable to use self and request at the same time. I therefore changed from:
    ```python
    def Delete(self, request, id, model):
    ```
    to:
    ```python
    class Delete(View):
    ```
    and added:
    ```python
    def get(self, request, id, model):
    ```
    After this, my delete button worked fine for both posts and comments, and also prevented people typing in the delete url to delete any post they wanted.
9. With the help of **Jack Wachira**, I found that I need my form tag to look like this:
    ```html
    <form method="post" enctype="multipart/form-data">
    ```
    instead of this:
    ```html
    <form method="post">
    ```
    After this issue had been resolved in *edit_post.html* and *new_post.html*, images could be posted by any user
10. I found that the reason for the follow button not working properly, was because the user profiles weren't being added to the profiles section in the admin panel to follow another user. So far, I am having to manually add new users to the profiles section whenever a new account is created so that other users can follow them, but hope to fix this so that whenever a user registers, they'll be added to the profiles section as well, so that they can be followed.

[Back to Bugs Found](#bugs-found)     
[Back to Contents](#contents)   
[Back to Testing in README.md](/README.md#testing)