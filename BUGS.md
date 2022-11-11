### Bugs found
These are the bugs found whilst programming 

1. **Custom styles** not working on the website.
2. **Navbar** moving upwards when there was a **large number of comments**.
3. **Posts** wouldn't load when clicked on.
4. **Leave a comment** card extended down past **comments** card.
5. **Admin page** wouldn't load **post or comment** for adjustments.
6. **Comments** wouldn't load in the *Leave a comment:* section of the page when clicking *Edit comment*.
7. **Delete** function would just return to the home page without deleting a post.
8. The **delete** function wouldn't allow me to stop other users that didn't create the given post/ comment to *delete* the post/comment.

--- 

### Bugs Fixed
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

[Back to Bugs Found](#bugs-found)   
[Back to Testing](/README.md#testing)   
[Back to Contents](/README.md#contents)