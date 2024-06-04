# La Hotel

![GitHub contributors](https://img.shields.io/github/contributors/EVondrus/la-hotel)
![GitHub last commit](https://img.shields.io/github/last-commit/EVondrus/la-hotel)
![GitHub language count](https://img.shields.io/github/languages/count/EVondrus/la-hotel)

[Here is a link to the final project]()

This site is a comprehensive hotel reservation system, designed to streamline the operations of both hotel owners and guests alike. This platform is tailored to enhance the user experience for those seeking accommodations, offering a seamless journey from browsing to booking.

This site is fully responsive on all modern screen sizes, and it allows the site users/guests to easily add, edit or delete their profiles, reservations, and the site owner to have the same functionality to handle the hotel and room details.

This site was built using HTML, CSS, Bootstrap, JavaScript, Python, Django, and it uses a SQL database through Code Institute.

![Final project mockup screenshot from Am I Responsive]()

## Contents

TODO

## User Experience

### Initial Discussion

- This project is something I wanted to create as I'm a passionate traveler which led me to use plenty of hotel booking sites and I've previously been working in the hotel buisness as well.
- I wanted to create a website linked to a database, which allows users to log in, view hotel information, room details, and make room reservations.
- I wanted the administration to be able to add, edit and delete hotel information, room details and reservations.

### User Stories

TODO

### Project Goals

- The main goal is to create an easily editable site to elevate the guest experience and simplify hotel operations.
- Designed with a user-centric approach, the platform should cater the needs of site users, site owners, staff users, and admin users.
- This project also demonstrates my understanding of maintaining a database attached to a website, with full CRUD (Create, Read, Update and Delete) functionality, using CI SQL database, and Cloudinairy Services

[Back to the top](#)

---

## Design

### Color Scheme

TBC

- The main colors used in this site are Dark Slater Blue, Gold/Beige and Cloudy White.

* These main colors are the colors in the hotels's logo, and they permeate through the site.

- These colors were each selected to embody the serene elegance and natural beauty of a Scandinavia, reflecting the tranquil ambiance and sophisticated charm of the setting.
- A dark green has been used for the sucess messages, to signify that this is a successive action.
- A dark red has been used for all Delete buttons, to signify that this is a destructive action.
- The darker yellow has been used for the hover state of the call-to-action buttons.
- ?! Different color shades have also been used on the hover state of the social media icons on the Contact page to match the icons.

![Color scheme]()

### Typography

TBC

- For the fonts, I selected Roboto Slab for headings and Open Sans for body text, both available through Google Fonts.
- These choices were made with a keen focus on readability and accessibility, ensuring a welcoming experience for users with dyslexia and partial visual impairments.
- The elegance and readability of these fonts contribute to the app's overall sophistication and ease of use.
- By utilizing the standard HTML font size of 16px, ensuring to not have any fonts smaller than that, to aid visually impaired users.
- Also, the recommended smallest font size for accessible websites is 12px, so by keeping all font sizes at the HTML standard of (?! 16px) or above, I ensured to be fully compliant with the [Penn State University Accessibility and Usability Guidelines](https://accessibility.psu.edu/fontsizehtml/).
- Font sizes are also able to be zoomed to 200% without losing contrast or functionality, to comply with the [WCAG Guidelines on fonts](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-scale.html).
- Lastly, to prevent the app from appearing overly assertive, I incorporated a mix of uppercase and lowercase text strategically.

![An example of the font used]()

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

## Features

### Home page

- This feature allows the user to:
- Get a view of the hotel's ambiance with high-quality images and engaging text, providing visitors with a glimpse of the hotel's offerings.
- Viewing the room types in a carousell - each option linking to a detailed room description page with the choice to make a room reservation.
- View contact information and location

### Room Category page

- This feature allows the user to:

  - View all room categories of the hotel on the website.
  - Browse rooms category through the main navigation bar or carousell from the homepage.
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
  
  - **Booking Option:** Users have the option to proceed with booking the selected room by clicking the 'Book' button. <br>
  This action redirects them to a dedicated page designed for making reservations, where they can finalize their booking details, choose additional services,


![Room Detail page with book button]()
