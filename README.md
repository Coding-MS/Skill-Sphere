# Skill-Sphere
This is my final capstone project for Code Institute. Skill Sphere is a full stack project that aims to create a website so that a user can post a request for a task/ project and be connected with an experienced freelancer.  The purpose of Skill Sphere is to allow users to post their requests for a project so that they can get in contact with an expert freelancer and complete the designated task/project. Skill Sphere will also highlight freelancer giving them exposure for their varied talents and skills as their portfolio and profile will display their previous projects and its associated customer feedback with an image of the final project this will highlight the freelancers and give them a platform for their business.

## Target Audience 
The target audience for Skill Sphere is any user who wants help with a project or task. The audience of the website is varied as each user would want something different from the website. Skil Sphere is a more of a community board that signposts and connects our users to their desired freelancer so that they can complete their project or task. It also has a second target audience being the freelancers themselves as Skill Sphere provides freelances with a platform to display their talent and skills to a potiential customer through their profile which acts as portfillo to advertise their services.  

## User stories 
Skill Sphere aims to address the following user stories: 

User Story 1: As a user I want to find a trustworthy freelancer to walk my dog. 
Acceptance Citeria: Create a post that allows the user to find a reliable freelance who walks dogs. 

User Story 2: As a user I want to hire a freelance experienced painter to paint my door red. 
Acceptance Criteria: Create a post that allows users to connect with a freelance painter. 

User Story 3: As a user I want to hire a freelance that is available to work certain hours and days as I have a busy schedule. 
Acceptance Criteria: Show the available times of the freelancer so that the user can talk to the freelancer to arrange a suitable time to complete the project. 

User Story 4: As a user I want to hire an experience freelance hair dresser to cut my hair at home. 
Acceptance Criteria: Create a post that enables the user to connect with an experienced hairdresser. (Add a section to the freelancer page so that they can contact them). 

User Story 5: As a user I want to create a job request so that I can get in contact with freelancers. 
Acceptance Criteria: Functionality in the Workboard page which allows the user to create a job request and be redirected to a suitable freelancer. 

User Story 6: As a user I want the option to meet with the freelancer virtually to talk to him about the project. 
Acceptance Criteria: Add their contact information to their profile and include any virtual platforms they use. 

## Wire Frame and design 
I have created a wireframe for Skill Sphere this application focusses on connection users to experienced and qualified freelancers to complete their designated task or project. So I have started the design process with visualising the Home Page which is the initial page that the user will visit. The wire frame design can be seen below. 

![Home page design](https://github.com/Coding-MS/Skill-Sphere/assets/144471859/119b6a74-83bf-4e73-a975-3ffcb62d4eab)

I have then created the Wireframe for the Workboard page. This page will allow the user to add a post to request a freelancer for their specific project/task. The freelancer will be categorised by speciality this will allow the user to be connected with an expert who has experience in the field that they require as when the user clicks the button "Connect with a freelancer", they will be redirected to the freelancer page. The user`s post will be available to view publically on the workboard below the display will be paginated by six requests per page which everyone can view. The user can also filter the requests by a certain speciality or date to view all requests that meet these conditions. The design of Workboard page can be seen below. 

![Workboard design](https://github.com/Coding-MS/Skill-Sphere/assets/144471859/75b3f3a4-592b-4d4b-8935-c7f76c3cc605)


I have created the Wireframe for the Freelancer page. This page will allow all users to view all freelancers that are available for work. Freelancer can be filtered by specific Speciality or a date range. In this wireframe the user has filtered by the Speciality: Hair dresser, the page will then display all available Hairdressers. The initial structure of the freelancer profile will be repeated throughout this project.   

![Freelancer page design](https://github.com/Coding-MS/Skill-Sphere/assets/144471859/cff894d3-38d1-4712-99f0-f1d1d4c65731)


The Sign-Up page will require the user to fill in a simple form to create a new account as illustrated below. 

![Sign-up design](https://github.com/Coding-MS/Skill-Sphere/assets/144471859/6ca9ee0b-4135-4639-a24f-af87b9101c2a)


The Sign-in page will require the user to fill in their credientials of an existing user to login to Skill Sphere. The Sign-in page can be seen below. 

![Sign in page design](https://github.com/Coding-MS/Skill-Sphere/assets/144471859/a4b8bed1-14b9-4b9c-bc9f-dae2b68a89ad)




## User flow diagram 
The User Flow diagram illustrates the process a user would go through in my application from visting the page to performing a specific action. The User flow Diagram is illustrated below. 


## Description of user flow 
The User would first be at the Home page of Skill Sphere. They would then have the option to sign in if they have an existing account. Once they have logged in to Skill Sphere they would have authorization to create a post in the Workboard page. The user would then submit their post to the workboard and have the option to contact a freelancer for the job. 


## ERD diagram the structure of the database 





## Core functionality 
The Core functionality of my project will be focussed on the WorkBoard page to ensure that I have CRUD functionality so the user one authenticated can create a post requesting help from a freelancer to complete a certain task or odd job. Once the user has submitted this post they will be able to see it on the Workboard below and on their own separate section this will be implemented to avoid confusion. It is also essential that authentication is implemented on this page to ensure that only logged in users can create posts and that only the user who created the post itself can edit or delete their own post from the workboard. So my inital design approach is to have build the Minium Viable Project first to ensure the core functionality of Skill Sphere then depending on the time I will focus on implementing as much as possible in the other sections.

## Possible features 
During my design phase and ideation of the project I came up with many good ideas for functionality and possible design choices. However due to the time constraints of the project I didn`t have enough time to fully realize the inherent potiential of these features. The list below outlines the ideas for additional functionality which could be added in the future: 

Search functionality: 
In the future I plan to make a search functionality that will enable the user to search for related content on page. 


Speciality checkbox: 
I initially planned to have a drop down list on the workboard page that would allow the user to filter all jobs by a certain speciality. This would enable the user to quickly find all jobs related to a certain speciality. 



### UX 
Skill Sphere design is focussed on simplicity as I have used the same colour plate to maintain consistency across all pages. The colour scheme is broken down below: 

1: 012622 (dark green) 

This dark green colour is being used to display a text section with a contrasting text colour of white. 

2: E98A15 (orange)

This orange colour is being used to display text in the hero image. 

3: 59114D (Palatinate)

This Palatinate colour is being used in the footer as it stands out. 

4: ECE5F0 (Magnolia)

This Magnolia colour is being used as the default background colour of the pages. 

5: 003B36 (Dark green)

This Dark green colour is being used in the forms that the user will use. 

### Existing features 
- Navbar 

  - The Navbar has been made through bootstrap 5 templates. 
  - The Navbar has linked the 
