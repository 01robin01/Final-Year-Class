# Todo for Khojne Sathi
## tasks 
[x] create forgot password page that asks users for their username 

[x] create "Email has been sent to your email address. please check spam folder"

[x] create "reset password" page that asks user for new password and confirm new password 

[x] create "Password reset success" page that shows user the password has been reset & Should contain a link to login page 

[x] Separate css from all pages into styles.css to be used in base.html & keep page specific CSS as it is

[x] UI for Claim approval/rejection by the Admin

[x] Claim page for User 

[x] Admin sidebar all pages using template inheritance

[x] login page using authenticate function

[x] Add actual Images

[x] Have dummy items to toggle with JS in user dashboard

[x] All linking should be with URL tags

[x] Implement signup With Google using Django-allauth

[x] Do templating inheritance for non-admin pages (admin pages are finished)

[x] Add actual images in my_lost_items.html & my_found_items.html

[x] make it so that all cards are same size & images shouldnt be cropped in either, if image is too big just make it object-fit = contain 
 
[x] make it mobile friendly, cards should be 4 columns in desktop, 3 in tablets, 2 in big phones, 1 in phones using col-md classes

[x] Different Search Page matching UI

[x] Implement View for Report Lost Items. (payload keys already match model fields)

[x] make the media files as internet links

[x] Send dummy data to templating engine through views instead of hardcoding it

[x] Do report_found view in style of report_lost

[x] Details page for individual items

[x] Claim page image size, when user uploads an image. a preview is shown in the dropdown area(also in found & lost pages;) & the image upload field should be able to handle multiple images uploads, Add a 10 MB image max size and a cutoff resolution where anything above gets resized to a specific resolution without changing aspect ratio. 

[x] localhost:8000/lost/items should show database data in lost posts and found posts.

[x] Only Allow 10 Images to be posted. 

[x] make Item Details page Dynamic .If an item has multiple images, make them scrollable like in daraz desktop individual item view

[x] Edit page for Lost/Found Items. for Images, show current images & give an option to delete the image though a new Url that deletes the image. & new images uploaded will be added to the items will be looped through and added 

[x] Image is blurred on the server and saved as a base64 encoded string that is served on the frontend.

[x] make dashboard.html dynamic

[x] make index.html have dynamic and working anchor tags

[x] User can only update their own item. if not owned by them, show a 403 forbidden page

[x] Claim Page make it dynamic and working. 

[x] automated emailing if lost item matches a newly found one. do this on post_save signal.

[x] confirm_delete.html missing while deleting lost item

[x] email and password for real smtp server 

[x] Handle POST request in claim endpoint.

[x] See the docs and change name field on password-reset.html & forgot-password.html page (Use the already provided Django Form if possible)

[x] Make registration/password_reset_email.html & registration/password_reset_subject.txt make sure to comply with html email rules.

[x] Make "password_reset_done.html" file to show user to check their email.

[ ] Admin pages.

[x] Make daraz like UI for multiple images of a single Item



<!-- [ ] try to blur the image using js canvas API. for admin, make it toggleable using floating action button inside of the image preview  -->
<!-- [ ] For sensitive image, save it to the database as is_private & also create a blurry version of them that will also be saved to the database as non private.
 Also make it so that "item.images.all" will only list public images and not private images.  --> 
