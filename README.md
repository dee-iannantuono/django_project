Dee Iannantuono  - She Codes News Project

## About This Project

The project was to create a website for She Codes News that allows users to read news stories, and authors to create them.


## How To Run This Code
To run this code, please follow the following steps: 

1. Clone the repo from Github onto your local machine. 
2. Use the terminal to navigate to the folder which contains the project. 
3. Run the following command to create a virtual environment 'python -m venv venv' 
4. Run `git init` 
5. Run `code .`
6. Create 2 new files in VS Code - one called requirements.txt and one called .gitignore
7. Add the following code to the requirements.txt file: requirements.txt Django==4.2.2
8. Copy this https://github.com/github/gitignore/blob/main/Python.gitignore into the `.gitignore` file. 
9. Go to the folder which has your requirements.txt in it and run ` . venv/Scripts/activate` which activates your virtual environment. 
10. Go to the folder that has the manage.py file in it and then run `python manage.py runserver`
11. Go to http://127.0.0.1:8000/news/ to see the She Codes News page. 


## Database Schema

    (./django_project/readme_images/dbschema.png)

## Project Features
- [X] Order stories by date

    These two images show the latest news ordered by date and then all stories ordered by date:
    
    (./django_project/readme_images/allnewsbydate.png)
    (./django_project/readme_images/latestnewsbydate.png)

- [X] Styled "new story" form
- [X] Story images

    This is my new story form. I ran out of time and did was not able to style it as I prioritised other parts of the project which were django focussed, not CSS. I added in an option to get the img url though which will show the story images. I also updated my images so they were in colour rather than grayscale.

    (./django_project/readme_images/newstoryform.png)

- [X] Log-in/log-out
- [X] "Create Story" functionality only available when user is logged in
- [X] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in

    These images show when a user is logged in and when a user is logged out. The create story fucntion will not show unless a user is logged in. The login button is only visible when no user is logged in and logout button is only visible when a user is logged in. 

    (./django_project/readme_images/loggedin.png)
    (./django_project/readme_images/loggedout.png)

- [X] "Account view" page

    When a user is logged in, they can click their name in the top right hand corner and it takes them to this account view page. 

    (./django_project/readme_images/accountviewpage.png)

- [X] "Create Account" page

    When a user clicks login, they are taken to a login screen where they can select that they want to create an account, this takes them to the create new account page. 

    (./django_project/readme_images/createnewuserform.png)

- [X] View stories by author

    I created a seperate search page where someone can search for a username or it also shows even if they just type a letter, so if they typed 'B' it would still show all the stories by 'bob' but none from 'dee' so that it works even when users don't type the full username. When submitted it takes users to a results page. 

    (./django_project/readme_images/searchpage.png)
    (./django_project/readme_images/searchresultspagebob.png)


## Additional Features:

    No additional features were completed due to lack of time. 

- [ ] Add categories to the stories and allow the user to search for stories bycategory.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )