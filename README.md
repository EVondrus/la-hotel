# [La Hotel](#la-hotel)

![GitHub contributors](https://img.shields.io/github/contributors/EVondrus/la-hotel)
![GitHub last commit](https://img.shields.io/github/last-commit/EVondrus/la-hotel)
![GitHub language count](https://img.shields.io/github/languages/count/EVondrus/la-hotel)

[Here is a link to the final project]()

This site is a comprehensive hotel reservation system, designed to streamline the operations of both hotel owners and guests alike. This platform is tailored to enhance the user experience for those seeking accommodations, offering a seamless journey from browsing to booking.

This site is fully responsive on all modern screen sizes, and it allows the site users/guests to easily add, edit or delete their profiles, reservations, and the site owner to have the same functionality to handle the hotel and room details.

This site was built using HTML, CSS, Bootstrap, JavaScript, Python, Django, and it uses a SQL database through Code Institute.

![Final project mockup screenshot from Am I Responsive]()

## [Contents](#contents)

- [Icon Key](#icon-key)
- [User Experience](#user-experience)
  - [Initial Discussion](#initial-discussion)
  - [User Stories](#user-stories)
  - [Project Goals](#project-goals)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Home page](#home-page)
    - [User profile registration](#user-profile-registration)
    - [Log in](#log-in)
  - [Room Category page](#room-category-page)
  - [Room Detail page](#room-detail-page)
  - [Booking Page](#booking-page)
    - [Reservation Confirmation](#reservation-confirmation)
  - [Navigation bar](#navigation-bar)
  - [About Section](#about-section)
  - [Contact section](#contact-section)
  - [Future Features](#future-features)
  - [Defensive Design](#defensive-design)
- [Database Design](#database-design)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
  - [Workspace](#workspace)
    - [GitPod & Visual Studio Code](#gitpod---visual-studio-code)
  - [Version Control](#version-control)
    - [Git](#git)
    - [GitHub](#github)
  - [Wireframing](#wireframing)
    - [Balsamiq](#balsamiq)
    - [Database Design](#database-design)
  - [Responsive Design](#responsive-design)
    - [Am I Responsive Design](#am-i-responsive-design)
    - [Responsinator](#responsinator)
  - [Documentation](#documentation)
    - [Shields.io](#shieldsio)
    - [Markdown-toc](#markdown-toc-generator)
    - [Markdownlint extension](#markdownlint-extension)
  - [Site Design](#site-design)
    - [Font Awesome](#font-awesome)
    - [Google Fonts](#google-fonts)
    - [Favicon.io](#faviconio)
  - [Packages](#packages)
  - [Hosting](#hosting)
    - [Heroku](#heroku)
  - [Frameworks, Libraries, and Others](#frameworks--libraries--and-others)
    - [Google DevTools](#google-devtools)
    - [Lighthouse](#lighthouse)
    - [Bootstrap](#bootstrap)
    - [pip](#pip)
- [Deployment](#deployment)
  - [Testing](#testing)
  - [Solved Bugs](#solved-bugs)
  - [Known Bugs](#known-bugs)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

---

## Icon key

&#128272; <-- Superuser only access

&#128100; <-- Logged In Only

&#128683; <-- Logged Out only

&#9989; <-- Yes / Visible

&#10060; <-- No / Not visible

[Back to the top](#la-hotel)

---

## User Experience

### Initial Discussion

- This project is something I wanted to create as I'm a passionate traveler which led me to use plenty of hotel booking sites and I've previously been working in the hotel buisness as well.
- I wanted to create a website linked to a database, which allows users to log in, view hotel information, room details, and make room reservations.
- I wanted the administration to be able to add, edit and delete hotel information, room details and reservations.

### User Stories

_TODO_

### Project Goals

- The main goal is to create an easily editable site to elevate the guest experience and simplify hotel operations.
- Designed with a user-centric approach, the platform should cater the needs of site users, site owners, staff users, and admin users.
- This project also demonstrates my understanding of maintaining a database attached to a website, with full CRUD (Create, Read, Update and Delete) functionality, using CI SQL database, and Cloudinairy Services

[Back to the top](#contents)

---

## Design

### Color Scheme ! TBC !

- The main colors used in this site are Dark Slater Blue, Gold/Beige and Cloudy White.
- These main colors are the colors in the hotels's logo, and they permeate through the site.
- These colors were each selected to embody the serene elegance and natural beauty of a Scandinavia, reflecting the tranquil ambiance and sophisticated charm of the setting.
- A dark green has been used for the sucess messages, to signify that this is a successive action.
- A dark red has been used for all Delete buttons, to signify that this is a destructive action.
- The darker yellow has been used for the hover state of the call-to-action buttons.
- Different color shades have also been used on the hover state of the social media icons on the Contact page to match the icons.

![Color scheme]()

### Typography ! TBC !

- For the fonts, I selected Roboto Slab for headings and Open Sans for body text, both available through Google Fonts.
- These choices were made with a keen focus on readability and accessibility, ensuring a welcoming experience for users with dyslexia and partial visual impairments.
- The elegance and readability of these fonts contribute to the app's overall sophistication and ease of use.
- By utilizing the standard HTML font size of 16px, ensuring to not have any fonts smaller than that, to aid visually impaired users.
- Also, the recommended smallest font size for accessible websites is 12px, so by keeping all font sizes at the HTML standard of (?! 16px) or above, I ensured to be fully compliant with the [Penn State University Accessibility and Usability Guidelines](https://accessibility.psu.edu/fontsizehtml/).
- Font sizes are also able to be zoomed to 200% without losing contrast or functionality, to comply with the [WCAG Guidelines on fonts](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-scale.html).
- Lastly, to prevent the app from appearing overly assertive, I incorporated a mix of uppercase and lowercase text strategically.

![An example of the fonts used]()

### Imagery

- The imagery and logo featured within this hotel reservation app are meticulously crafted using [AI technologies]()
- Integrated to forge a connection between the hotel's brand and the app's interface.
- Subtle box shadows have been artfully applied. These design elements echo the hotel's graphic styling, characterized by neutral, soft colors and refined lines, enhancing the app's aesthetic appeal.
- All links have their underlines removed for stylistic purposes. The links re-gain their underlines when they're hovered over or focused on.
- All interactable objects have hover and focus styles applied to make it clear to the user that those objects are interactable.
- Icons from [Font Awesome](https://fontawesome.com/) have been used on the site to add meaning where relevant and suitable. These icons are accompanied by either visible text or descriptive aria-labels, ensuring inclusivity and accessibility.
- Button and link colors have been used to convey meaning, mainly in the use of the color dark red to convey 'Delete' or 'Cancel' as dangerous actions.

### Wireframes

- [Wireframes for desktop, mobile, and tablet for this project]().
- [ER Diagram for this project]().

[Back to the top](#contents)

---

## Features

### Home page

- This feature allows the user to:
- Get a view of the hotel's ambiance with high-quality images and engaging text, providing visitors with a glimpse of the hotel's offerings.
- Viewing the room types in a carousell - each option linking to a detailed room description page with the choice to make a room reservation.
- View contact information and location.

#### User profile registration

- This feature allows the user to:

  - Register for an account with an email address, first name, last name and password.
  - Ensure no typos by entering the password twice, with the site checking to confirm that the passwords match.
  - _?!?CHECK?!?_ Ensure the correct email address by sending a verification email to the email address the user has supplied.
  - &#128100; Store their details for faster booking.
  - &#128100; Keep a record of their reservation history.

![User's profile, including details update form]()

#### Log in

- This feature allows the user to:

  - Log in to the site with email address and password.
    - Check the box to "remeber me" for upcoming logins.
    - Click the link to reset password if forgotten.
  - Browse their profile page.
    - View, update and delete their profile details.
    - Change password.
  - Browse their room reservations (if they have any).
    - View, update and cancel room reservations.

### Room Category page

- This feature allows the user to:

  - View all room categories of the hotel on the website.
    - Browse room categories through the main navigation bar or carousell from the homepage.
  - Input check in and check out dates to see avaliable room types for the desired stay.
  - Get an overview of what the different room categories offer, including a image, brief description of features and amenities, capacity and price.
  - Click on a room detail card to be redirected to the full room details pages.

![Room Category page with date inputs]()

### Room Detail page

- This feature allows the user to:

  - View comprehensive details about each room category, including:

    - **Category:** The type of room (e.g., Standard, Deluxe, Suite).
    - **Price Per Night:** The cost associated with booking the room for one night.
    - **Capacity:** The maximum number of guests the room can accommodate.
    - **Image Gallery:** High-quality images showcasing the room from various angles and amenities.
    - **Description:** A detailed description of the room's features, amenities, and unique selling points.
    - **User Input for Check-In and Check-Out Dates:** Allows users to input their preferred check-in and check-out dates to see if the room is available during those days.
    - **Availability Status:** Clearly indicates whether the room is available for the selected dates, enhancing the booking process's transparency.

  - **Booking Option:** Users have the option to proceed with booking the selected room by clicking the 'Book' button.
    - This action redirects them to a dedicated page designed for making reservations, where they can finalize their booking details, choose additional services,

![Room Detail page with book button]()

### Booking Page ! TBC !

- This feature allows the user to:
  - Make reservation as a guest user
  - &#128100; The details will be filled from any details given in the user profile.
    - First name, lastname
    - emailadress
    - phonenumber
    - address
  - The details will be filled from any details if given in the room details page.
    - Input/Update check in and check out dates.
    - Edit Number of guests.
    - Edit the quantity of rooms.
    - Edit or delete room category for the the reservation.
  - View the total cost and details of the reservation.

![Reservation form with prefilled user information]()

#### Reservation Confirmation

- If the reservation fails:
  - The user is directed back to the reservation form.
  - The user is shown a message that the payment failed.
- If the payment succeeds:
  - The user will be sent a confirmation email. _?!? CHECK ?!?_
  - The email contains the full order details and order number.
  - The user will be redirected to the success page. _?!? CHECK ?!?_
  - A message will display, informing the user that the payment succeeded, containing the order details and booking ID.
  - &#128100; The order will be added to the user's order history in their profile.

### Navigation bar

The navigation bar changes depending on user status and screen size:

| Nav Link         | &#128683; | &#128100; | &#128272; |
| ---------------- | --------- | --------- | --------- |
| Logo (Homepage)  | &#9989;   | &#9989;   | &#9989;   |
| Home             | &#9989;   | &#9989;   | &#9989;   |
| Rooms            | &#9989;   | &#9989;   | &#9989;   |
| Book             | &#9989;   | &#9989;   | &#9989;   |
| Contact Us       | &#9989;   | &#9989;   | &#9989;   |
| About            | &#9989;   | &#9989;   | &#9989;   |
| Hotel Management | &#10060;  | &#10060;  | &#9989;   |
| Profile          | &#10060;  | &#9989;   | &#9989;   |
| Log Out          | &#10060;  | &#9989;   | &#9989;   |
| Log In           | &#9989;   | &#10060;  | &#10060;  |
| Register         | &#9989;   | &#10060;  | &#10060;  |

- Navigation bar

![Overall navigation bar]()

- Logged in

![Logged in navigation dropdown]()

- Logged out

![Logged out navigation dropdown]()

- An admin

![Admin navigation dropdown]()

- On small screen sizes

![Mobile navigation burger icon]()
![Mobile navigation bar expanded]()

### About Section

- This feature allows the user to:
  - Read about the hotel, it's history and owners.
  - Navigate to the room categories.
  - Navigate to any of the hotel's social media pages.

![The About page]()

### Contact section

- This feature allows the user to:
  - Contact the hotel via email for queries about their stay or reservation.
  - View adress and location including google maps. _?!? CHECK ?!?_
  - View phone number to contact the hotel in a quicker manner.
  - Navigate to any of the hotel's social media pages.

![The Contact Us page]()

### Future Features ! TBC !

### Defensive Design ! TBC !

[Back to the top](#contents)

---

## Database Design ! TBC !

This database uses a SQL database through Code Institute.
[ER Diagram]()

---

## Technologies Used

### Languages Used

#### HTML

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

#### CSS

- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)

#### JavaScript

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

#### Python

- [Python](https://www.python.org/)
- This project uses Python 3.12.3.

### Workspace

#### GitPod & Visual Studio Code

[GitPod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.
[Visual Studio Code](https://code.visualstudio.com/) was used as a local IDE workspace to build the site.

### Version Control

#### Git

[Git](https://git-scm.com/) Git was used for version control. The Gitpod and VS Code terminals were utilized to add, commit to Git and pushed to GitHub.

#### GitHub

[GitHub](https://github.com/) is used to store the code for this project.

### Wireframing

#### Balsamiq

[Balsamiq](https://balsamiq.com/) was used for creating wireframes to plan the layout and structure of the site

#### Database Design

![Lucidcharts](https://lucid.co/) was used to create Entity-Relationship Diagrams (ERDs) to design the database schema.

### Responsive Design

#### Am I Responsive Design

[Am I Responsive Design](http://ami.responsivedesign.is/#) was used to check the site's responsive design and create the final site image.

#### Responsinator

[Responsinator](http://www.responsinator.com/) was used to improve the site's responsive design on a variety of devices.

### Documentation

#### Shields.io

[Shields.io](https://shields.io/) was used to create the GitHub badges for the top of this README.md file.

#### Markdown toc generator

[Markdown-toc](https://ecotrust-canada.github.io/markdown-toc/) was used to create the table of contents.

#### Markdownlint extension

[markdownlint Extension](https://open-vsx.org/vscode/item?itemName=DavidAnson.vscode-markdownlint) was used on GitPod and VS Code to ensure all markdown was correctly formatted.

### Site Design !TBC !

#### Font Awesome

[Font Awesome](https://fontawesome.com/) was used on all pages to add icons.

#### Google Fonts

[Google Fonts](https://fonts.google.com/) was used to select the fonts for the site.

#### Favicon.io

[favicon.io](https://favicon.io/) was used to create the site favicon.

### Packages ! TBC !

| Name                | Purpose                  |
| ------------------- | ------------------------ |
| Django              | Framework                |
| django-allauth      | Authentication           |
| django-crispy-forms | Front End Form Rendering |
| dj-database-url     | Database Configuration   |
| gunicorn            | WSGI HTTP Server         |

### Hosting ! TBC !

#### Heroku

[Heroku](https://www.heroku.com) was used to deploy the live site.

### Frameworks, Libraries, and Others ! TBC !

#### Google DevTools

[Google DevTools](https://developer.chrome.com/docs/devtools/)was used to identify the code corresponding to specific features.

#### Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to ensure the code was performant, followed best practices, and adhered to SEO and accessibility guidelines.

#### Bootstrap

[Bootstrap](https://getbootstrap.com/) was used to create a beautiful, responsive website.

#### pip

[pip](https://pip.pypa.io/en/stable/) was used to install the required dependencies for this site.

[Back to the top](#contents)

---

## Deployment ! TBC !

### Testing ! TBC !

[Click here to view the full testing steps](), which were completed on Google Chrome, Safari and...., and screenshots of testing.

### Solved Bugs ! TBC !

### Known Bugs

[Back to the top](#contents)

---

## Credits

### Code

### Content

### Media

- All media on this site is created by me and my partner Mladen Djurdjevic, using AI technologies.

### Acknowledgments

[Back to the top](#contents)
