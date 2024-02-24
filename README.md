# The Gamer Library

---

## Site Overview

---
Immerse yourself in your passion for gaming with The Gamer Library, an app meticulously crafted to unite your gaming journey across generations and platforms. As a fellow gamer, my gaming odyssey began with the early days of Sonic 2 on the Sega Mega Drive and has continued, spanning up to the latest adventure in Baldur's Gate III.

Understanding the challenges of hardcore gamers in keeping track of their extensive gaming history, The Gamer Library aims to provide a comprehensive solution. In today's digital era, games are available in various formats and scattered across different platforms, each maintaining an independent record. This challenge becomes evident, for example, when attempting to reconcile games played on Game Pass with those in the Steam library. With the rise of cloud gaming, titles frequently shift between platforms, making it easy to lose track of your gaming history.

Adding a game to The Gamer Library goes beyond mere organization; it enhances your gaming satisfaction. There's a unique sense of achievement in conquering the final boss and proudly recording your triumph in the library. Moreover, it takes users on a nostalgic journey, linking specific games to significant moments. I vividly recall playing Digimon World 3 on PS1 when my sister was born, conquering Ornstein and Smough in Dark Souls during my Master's degree, exploring the City of Tears in Hollow Knight with my first job, and immersing myself in Baldur's Gate III builds while crafting this very project.

Embark on a new chapter of gaming with The Gamer Library to celebrate your games! Join The Gamer Library and redefine how you experience and share your love for gaming!

Live link to [The Gamer Library](https://the-gamer-library-a2d80d9a63a6.herokuapp.com/)

![intro page](./docs/images/the_gamer_library_viewport.png)

## Table of Contents

- [The Gamer Library](#the-gamer-library)
  - [Site Overview](#site-overview)
  - [Table of Contents](#table-of-contents)
  - [Planning phase](#planning-phase)
    - [Strategy plane](#strategy)
      - [Aims](#aims)
      - [Opportunities](#opportunities)
    - [Scope](#scope)
    - [Structure](#structure)
      - [User stories](#user-stories)
    - [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
      - [Database schema](#database-schema)
    - [Surface](#surface)
      - [Colors](#colors)
      - [Typography](#typography)
  - [Features](#features)
    - [Intro](#intro)
    - [Get in touch](#get-in-touch)
    - [Info](#info)
    - [Login](#login)
    - [Register](#registration)
    - [Home](#home)
    - [Add Platform](#add-platform)
    - [Platform Detail](#platform-detail)
    - [Edit Platform](#edit-platform)
    - [Add Game](#add-game)
    - [Game Detail](#game-detail)
    - [Edit Game](#edit-game)
    - [Add Wishlist Game](#add-wishlist-game)
    - [Wishlist Game detail](#wishlist-game-detail)
    - [Edit WishList Game](#edit-wishlist-game)
    - [Delete modals](#delete-modals)

  - [Bugs](#bugs)
  - [Diary](#diary)

---

## Planning phase

---

### Strategy

---

#### Aims

The Gamer Library efficiently catalogues all played games and the diverse platforms users have experienced. In today's gaming landscape, options include PCs, streaming services, consoles, and cloud gaming platforms.

The core objective of The Gamer Library is to empower gamers by facilitating meticulous tracking of their gaming history and the corresponding platforms. Beyond this, the platform acknowledges that each gaming service, console, or PC carries its own cost. With The Gamer Library, users can effortlessly monitor the number of games played on each platform, enabling them to evaluate the continued value of associated fees.

Furthermore, The Gamer Library enhances user experience by offering the ability to curate a wish list. Users can add desired games and even analyze the wish-listed titles on each platform. This functionality aids in strategic decision-making, helping users identify the most convenient platform based on the quantity and priority of wish-listed games.

#### Opportunities

In the table and plot below, you'll find a comprehensive list of features that emerged during the brainstorming step.

| Opportunity/Problem                                 | Importance | Feasibility/Viability |
|-----------------------------------------------------|------------|-----------------------|
| Keep track of games                                 | 5          | 4                     |
| Keep track of platforms                             | 5          | 4                     |
| Create wishlists                                    | 4          | 4                     |
| Allow user to login                                 | 5          | 5                     |
| Provide instructions on how to use the app          | 4          | 5                     |
| Allow other developers to get in touch              | 3          | 5                     |
| Import data from Metacritics and Game database APIs | 2          | 3                     |
| Share game, platforms and wish list with friends    | 3          | 2                     |
| Allow friends users to exchange messages            | 1          | 1                     |
| Allow friends users to create posts, clips, streams | 2          | 1                     |

![Strategy plan chart](./docs/images/strategy_plan_plot.png)

### Scope

---

Due to the limited time available, I will focus on implementing features where Importance (I) + Feasibility (F) has the highest value:

- UX **must** address:
  - Allow user to login  
  - Keep track of games
  - Keep track of platforms

- UX **should** address:
  - Create wishlists
  - Provide instructions on how to use the app
  - Allow other developers to get in touch
  - Allow friends users to exchange messages

- UX **could** address:
  - Import data from Metacritics and Game database APIs
  - Share game, platforms and wish list with friends

- UX **wont** address:
  - Allow friends users to create posts, clips, streams
  - Allow friends users to exchange messages

### Structure

---
The graphic below illustrates the steps a user should take to use The Gamer Library app. I created it using `Lucidchart`.

![Strategy plan chart](./docs/images/the_gamer_library_flow_chart.png)

#### User Stories

I developed The Gamer Library project by following Agile principles. I worked in sprints of 2 weeks each, and at the end of each sprint, I introduced new user stories or rescheduled previous user stories following the MoSCoW rules.

##### Sprint 1

##### 18/12/2023 - 25/12/2023

- **Must have**
  - As a **Developer** I can**access the project on the cloud** so that I **can view and navigate the app on Heroku, just as I do locally**.
  - As a **Admin** I can **create, read, update, and delete platform instances** so that I **can perform CRUD operations on platforms**.
  - As a **Admin** I can **create, read, update, and delete games instances** so that I **can perform CRUD operations on games**.

- **Should have**
  - As a **Admin** I can **See the list of platforms added outside the admin panel** so that I **can verify the platform list view and home page perform as expected**.
  - As a **Admin** I can **See the list of games added outside the admin panel** so that I **can verify the game list view and html template perform as expected**.

##### Sprint 2

##### 25/12/2023 - 08/01/2024

- **Must have**
  - As a **User** I can **add a platform to the app** so that I **can keep track of the platforms I use**.
  - As a **User** I can**add Games to a Platform** so that I **can keep track of the games played on each platform**.

- **Should have**
  - As a **User** I can **log into the app** so that I **can see only my list of platforms and games**.
  - As a **Developer** I can **showcase who I am and my history** so that I **can empathize with the user**.
  
- **Could have**
  - As a **Developer** I can **get in touch with recruiters or other developers** so that I **can receive offers to work on new projects or receive feedback**.

##### Sprint 3

##### 08/01/2024 - 22/01/2024

- **Must have**
  - As a **User** I can **edit a platform instance** so that **I can update the platform or correct mistakes added during creation**.
  - As a **User** I can **delete a platform instance** so that **I can remove platforms from the app**.

- **Could have**
  - As a **Developer** I can **test that a platform is created and its details are visible** so that **I can perform platform CRUD testing without manual intervention**.
  - As a **Developer** I can **verify that the 'Get in Touch' content is displayed without manual testing** so that I can **save time during app testing**.

##### Sprint 4

##### 22/01/2024 - 05/02/2024

- **Must have**
  - As a **User** I can **see game details** so that **I can get information and details on the games I have played**.
  - As a **User** I can **add images to my games** so that **I can customize the game instances I add**.

- **Should have**
  - As a **User** I can **edit my game details** so that **I can customize my games instances**.
  - As a **User** I can **delete a game instance** so that **I can remove unwanted games from my game list**.

##### Sprint 5

##### 05/02/2024 - 19/02/2024

- **Must have**
  - As an **Admin** I can **add wishlist instances** so that **I can manage and view wishlist items from the admin panel**.
  - As a **User** I can **add wishlist items** so that **I can plan and keep track of the games I want to buy**.

- **Should have**
  - As a **User** I can **edit a wishlist item** so that **I can update details such as price and priority**.
  - As a **User** I can **delete wishlist items** so that **I can remove a game I no longer want to buy**.

- **Could have**
  - As a **User** I can **access instructions on how to use the app** so that **I do not feel lost when navigating the home page**.
  - As a **User**, I can **understand what the purpose of the app is** so that **I can decide if it fits my needs**.
  - As a **Developer** I can **test creating, reading, updating, and deleting Platform instances** so that **I can test Platform CRUD without manual input**.
  - As a **Developer** I can **test creating, reading, updating, and deleting Game instances** so that **I can test Game CRUD without manual input**.
  - As a **Developer** I can **test creating, reading, updating and deleting WishListGames instances** so that **I can test WishListGame CRUD without manual input**.
  - As a Developer I can test forms' validity without manual input so that I can speed up and automate the app testing.

##### Sprint 6

##### 19/02/2024 - 29/02/2024

- **Must have**
  - As a **User** I can **access all the details on the app's purpose, planning, and functions** so that **I can make an informed decision on whether it meets my needs**.

- **Should have**
  - As a **Developer** I can **analyze the test coverage percentage for views and forms** so that **I can prioritize manual testing efforts on uncovered areas**.

  - As a **User** I can **seamlessly access the game store directly from the wishlist section of the app** so that **I can conveniently purchase desired games without switching between platforms**.

##### Backlog

- **Wont have**
  - As a **User** I can **add friends to the app** so that **I can share games, platforms and wishlists with them**.
  - As a **User** I can **get Metacritic score, released date, developer and genres fields automatically filled** so that **I can speed up the adding game step**.
  - As a **User** I can **add posts, streams, and game clips** so that **I can share them with friends**.

### Skeleton

---

#### Wireframes

Below are the wireframes I used to create the .html templates for the app.
![Wireframe home](./docs/images/wireframe_home.png)
![Wireframe game detail](./docs/images/wireframe_game_detail.png)
![Wireframe platform detail](./docs/images/wifreframe_platform_detail.png)
![Wireframe wish list game detail](./docs/images/wifreframe_platform_detail.png)

#### Database schema

Below is the schema I used to implement the main model of The Gamer Library
![Database_schema](./docs/images/gamer_library_database_schema.png)

### Surface

---

#### Colors

Gamers are the primary target audience for The Gamer Library; therefore, I have chosen colours that immerse users in the gaming world. Indeed, an RGB border surrounds the Navbar that continuously changes colour.

![Navbar blue](./docs/images/navabr_green.png)
![Navbar_green](./docs/images/navbar_blue.png)

Each gaming console/brand has a distinct colour: red for Nintendo Switch, green for Xbox, and blue for PlayStation 5. Therefore, I allowed the users to personalize the background colour for each platform. This colour choice influences the platform box colour on the home page and serves as the background colour on the platform detail page. If a user selects a dark colour as the background, the font in the platform box and platform detail page will not be visible. Therefore, users can change the font colour for the platform box on the home page and the platform detail page

![Platforms box colors](./docs/images/platforms_box_colors.png)

![Platforms background colors](./docs/images/platform_background_color.png)
For more information, refer to the [Edit platform](#edit-platform) section.

#### Typography

As font I chose a font which reminds of gaming `Press Start 2 Play`to create the logo and one which combined accordingly `Roboto` for the main content of the app

---

## Features

---

### Navbar

#### Logo

The logo bears the name of the web app surrounded by RGB lights. Both the font, `Press Start 2 Play`, and the RGB lights transport users to the gaming world, establishing a strong connection with gamers.

![logo](./docs/images/gamerlibrary_logo.png)

On small screens, the navbar displays as a hamburger menu.
![hamburger menu](./docs/images/closed_hamburger_menu.png)

When clicked, the hamburger menu shows all the available options.
![hamburger menu open](./docs/images/open_hamburger_menu.png)

#### Navbar links

The navbar allows not logged-in users to access the following pages:

- [Intro](#intro)
- [Get in touch](#get-in-touch)
- [Info](#info)
- [Login](#login)
- [Register](#registration)

Logged users instead get access to additional pages:

- [Home](#home)
- [Add Platform](#add-platform)
- [Platform Detail](#platform-detail)
- [Edit Platform](#edit-platform)
- [Add Game](#add-game)
- [Game Detail](#game-detail)
- [Edit Game](#edit-game)
- [Add Wishlist Game](#add-wishlist-game)
- [Wishlist Game detail](#wishlist-game-detail)
- [Edit WishList Game](#edit-wishlist-game)
- [Delete modals](#delete-modals)

### Intro

Users who are not logged in will be redirected to the intro page initially. The page showcases three hero images illustrating the main purposes of the app: keeping track of platforms, monitoring game activity, and planning the game wish list. At the bottom, there are two buttons allowing the user to either log in or sign up.
![Intro page](./docs/images/intro_page.png)

### Get in touch

The Get in Touch page contains a brief user description. The description is not hardcoded in the HTML page. Instead, the admin can update and modify the message through the admin panel. Positioned at the centre of the page is a hero image serving as a gateway to the gaming world. At the bottom, a collaboration button enables other developers to contact me or provide feedback on the app.

![Get in touch page](./docs/images/get_in_touch.png)

### Info

The Info page provides instructions on how to use the app. After logging in, the user should initially add a platform. Then, the user can edit or delete it. Additionally, he can add games to their collection or wishlist only if he already added a platform.

![Info page](./docs/images/info.png)

### Login

The login page enables registered users to log in. Once logged in, users can access the main features of the app, including adding, removing, and editing platforms, games, and wish list items. If a user is not already logged in, the login page provides a link to the registration page, which users can also access directly from the navbar.

![Login page](./docs/images/login_page.png)

### Registration

Users can log in only if they have registered first. To register, users need to provide a valid username and password, with the email address being optional. The page also displays the password constraints.
![Sign up page](./docs/images/register.png)

### Home

Only logged-in users can access the home page. The home page displays a list of added platforms, showcasing each platform's name and the number of associated games. Clicking on a platform's name redirects the user to the platform page. Below the platform details, two buttons are available. The blue button expands the platform details, revealing the list of games added, including the game name, image, and a user-assigned score ranging from 0 to 100. The red button serves as the delete button, allowing the user to remove the platform. Upon clicking, a modal will appear, prompting the user to confirm the deletion, as this action cannot be undone.

![Home page](./docs/images/home.png)

### Add platform

Logged-in users can select the Add Platform link on the navbar to create a new platform. On this page, users can provide a platform name and category, with the image being optional. Both the name and category are mandatory fields. Most of the additional platform details can be edited on the platform detail page.
Verification is performed on the uploaded image. Only the following formats are supported: .png, .webp, .jpg, .jpeg, and .gif.

![Add platform](./docs/images/add_platform_form.png)

### Platform detail

Once the user adds a platform, it becomes visible on the home page. The user can click on the platform name to be redirected to the platform detail page. On the platform detail page, the platform image is displayed, with a placeholder shown if none has been chosen. Below, there is the platform name, along with two buttons one to edit the platform details (redirecting to the edit platform form) and a delete button that triggers a modal to confirm platform deletion.

Following the platform details, additional information is displayed based on the chosen category. Each category presents different details. Subsequently, the page lists the games and those added to the wish list. In the game list, the game image is shown, with a placeholder displayed if none is available. Below the image, the game name and user-assigned score (ranging from 0 to 100) are presented. Clicking on the game name redirects the user to the game detail page.

In the wish list games list, each entry displays the chosen game image or a placeholder if none has been selected. Additionally, a priority is shown, represented by an integer value where a lower value indicates a higher priority.

![Platform detail part 1](./docs/images/platform_detail_page_part_1.png)

![Platform detail part 1](./docs/images/platform_detail_part_2.png)

### Edit Platform

Logged-in users can click on the blue button to edit platform details, which redirects to a form for editing based on the platform category. Among other options, users can choose a background color and font color. To set both colors, users must enter a HEX code for the selected color.

The background color will determine the color of the platform box on the home page and the background on the platform detail page. By default, the background color is black, and the font color is white. If the user selects a light color as the background, the font might not be visible. Therefore, the form provides the option to change the font color as well. This alteration affects the font color in the platform box on the home page and the platform details on the platform details page.

Furthermore, users have the option to change the category of the platform. However, the attributes of the new category become visible only after saving the new category and clicking the edit button again.

![Edit platform form](./docs/images/edit_platform_form.png)

### Add Game

Logged-in users, after adding a platform, can click on the Add Game link in the navbar to associate a game with a platform. They will be redirected to the Add Game form, where only a few attributes are available: Name, Platform, Image, and User Score. Name and Platform are mandatory, while Image and User Score are optional. If no image is added, a placeholder will be displayed.

![Add game form](./docs/images/add_game_form.png)

### Game Detail

After filling out the "Add Game" form, the game becomes visible on the home page after clicking the expand button, and in the platform details page in the game list section. Both the game name on the home page and the game name in the platform detail, by clicking on them, redirect the user to the game detail page.

The game detail page displays the game image or a placeholder if none is chosen, along with the "Edit Game" and "Delete Game" buttons. Clicking the "Edit Game" button redirects to the edit game form page, while the "Delete Game" button prompts a modal for confirming game deletion. Upon confirmation, the game is deleted.

Below, there is a list of game details, including the game review, where a user can express their opinion on the played game.

![Game Detail](./docs/images/game_detail_page.png)

### Edit Game

On the Game Detail page, the user can click on the Edit Game button to be redirected to the Edit Game page. Here, the user has access to additional attributes such as Developer, Genres, Completion Date, and Hours Spent. Furthermore, there is a text area for the user to write a review for the game.

![Edit game form part 1](./docs/images/edit_game_form_part1.png)

![Edit game form part 2](./docs/images/edit_game_form_part2.png)

### Add Wishlist Game

After adding a platform, the user can also add a Wish List game by clicking on the Add Wishlist button in the navbar. Similar to the Add Game and Add Platform pages, only a few attributes are available on the Add Wishlist Game form. The majority of the attributes are accessible in the Edit Wishlist Game form.

In the Add Wishlist Game form, the following attributes are available: Name, Platform, Image, Priority, Currency Cost, and Store. Only the Platform and Name fields are mandatory.

Wish List games will be visible only on the platform detail page in the Wish List Games section. Details of a Wish List game can be viewed by clicking on the Wish List game name in the platform detail page.

![Add Wishlist game form](./docs/images/add_wishlist_game_form.png)

### Wishlist Game detail

The Wish list game detail will display the image of the wish-listed game; if none is chosen, a placeholder is displayed. Below, there are the game name, and the Edi" and Delete buttons. The Edit button redirects to the Edit Wish List Game page, while the Delete button prompts a modal to confirm the deletion of the game from the wish list. At the bottom, all the wish-listed game attributes are displayed.

![Wishlist game detail page](./docs/images/wish_list_game_detail_page.png)

### Edit Wishlist Game

On the Wish List Game detail page, users can click on the Edit button to modify various attributes associated with a game added to the wishlist. It's important to note that when updating the date attribute, it must follow the Django format 'YYYY-MM-DD'.

The Priority field is specific to wish-listed games, where users input an integer. The lower the value, the higher the priority for the game. Games in the wishlist with lower priority values will be displayed first.

![Wishlist game detail page part1](./docs/images/edit_wishlist_game_part1.png)

![Wishlist game detail page part2](./docs/images/edit_wishlist_game_part2.png)

### Delete Modals

Every delete button once clicked will show a similar modal the one on the picture below and the platform, game or wishlist game will be deleted only if the user selects confirm.

![Delete modals](./docs/images/delete_modal.png)

## Future development

Future development includes user stories that have been left in backlog following agile principles:

- Utilize API integration to fetch data from the video games database IGDB and Metacritics. This approach enables users to pre-fill most of the data when adding a Game or Wishlisted Game by accessing the APIs.

- Implement the capability for users to add friends. Friends will be able to view each other's platforms, games, and wish lists. This feature proves useful when a user wants to purchase the same platform as a friend. They can view their friend's PC build, including GPU, CPU, and RAM, and make informed decisions. Additionally, friends can gift games from the wish list as birthday presents!

- Introduce a messaging system, enabling users to exchange messages. This feature can facilitate setting up multiplayer sessions or simply chatting about their favorite games.

- Enable users to share game clips, game content, and potentially even stream live content. This way, the app could foster a community of gamers, allowing them to connect and engage with each other.

## Bugs

1. **Error**:
  
    ```cmd
    File "<frozen importlib._bootstrap_external>", line 1074, in get_code
    File "<frozen importlib._bootstrap_external>", line 1004, in source_to_code
    File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
    File "C:\Users\Mary9\OneDrive\Documenti\angelo\The-Gamer-Library\gamer_library\settings.py", line 21
      TEMPLATES_DIR os.path.join(BASE_DIR, 'templates')
    SyntaxError: invalid syntax
    ```

    **Cause** missing = in:

    ```python

      SECRET_KEY os.environ.get('SECRET_KEY')
    ```

    **Solution** added = in setting .py , code is now:

    ```python

    SECRET_KEY = os.environ.get('SECRET_KEY')
    ```

1. **Error**:

   ```cmd
    File "C:\Users\Mary9\OneDrive\Documenti\angelo\The-Gamer-Library\env.py", line 6, in <module>
      os.environ["LOCALHOST"]= ["127.0.0.1"]
      ~~~~~~~~~~^^^^^^^^^^^^^
    File "<frozen os>", line 684, in __setitem__
    File "<frozen os>", line 744, in check_str
   TypeError: str expected, not list
   ```
  
    **Cause**: variable LOCALHOST was set as a list rather than as a string

      ```python
      os.environ["LOCALHOST"]= ["secret_string"]
      ```

    **Solution**: turned list into string

      ```python
      os.environ["LOCALHOST"]= "secret_string"
      ```

1. **Error**:

   ```bash
    django.core.exceptions.ImproperlyConfigured: In order to use cloudinary storage, you need to provide CLOUDINARY_STORAGE dictionary with CLOUD_NAME, API_SECRET and API_KEY in the settings or set CLOUDINARY_URL variable (or CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET variables).
    !Error while running '$ python manage.py collectstatic --noinput'.
    See traceback above for details.
    You may need to update application code to resolve this error.
    Or, you can disable collectstatic for this application:
   ```

    **Cause**: Cloudinary settings were set as

      ```python
      os.environ["CLOUDINARY_URL"]= "my_cloudinary_url"
      ```

    **Solution**: added in settings.py :

    ```python
        CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }
    ```

    and the related key in env.py

    ```python
    os.environ["CLOUDINARY_CLOUD_NAME"] = "my_cloud_name"
    os.environ["CLOUDINARY_API_KEY"] = "my_API_key"
    os.environ["CLOUDINARY_API_SECRET"] = "my_API_secret_key"
    ```

1. **Error**:

    ```bash
        File "/app/.heroku/python/lib/python3.12/site-packages/cloudinary/utils.py", line 740, in build_distribution_domain
              raise ValueError("Must supply cloud_name in tag or in configuration")
          ValueError: Must supply cloud_name in tag or in configuration
    !     Error while running '$ python manage.py collectstatic --noinput'.
          See traceback above for details.
          You may need to update application code to resolve this error.
          Or, you can disable collectstatic for this application:
              $ heroku config:set DISABLE_COLLECTSTATIC=1
          https://devcenter.heroku.com/articles/django-assets
    !     Push rejected, failed to compile Python app.
    !     Push failed
    ```

    **Cause**: DISABLE_COLLECTSTATIC was named incorrectly in heroku, it was DISABLE_COLLEC
    STATIC =1

    **Solution**: deleted config var DISABLE_COLLEC
    STATIC =1 and added  DISABLE_COLLECTSTATIC=1

1. **Error**:
    many to many relation is not visible in admin panel

   **Cause**:
    many to many rleation have been created using cross-tables
    user-games, user-wishlist

    **Solution**:
      used ManyToManyField rather than cross table

1. **Error**:
    Many to many relation does not take into consideration game custom fields such as user score and user review

    **Cause**:
    Use of many-to-many relation rather than one-to-many

    **Solution**:
    changed many to many relation into one to many in the following:
    user-games is now one to many
    user-wishlists is now one to many
    added plaltform table
    user-platform is one to many
    platform-games is one to many
    platform-wishlists os one to man

1. **Error**:

    ```cmd
      ERRORS:
      <class 'library.admin.PlatformAdmin'>: (admin.E020) The value of 'filter_horizontal[0]' must be a many-to-many field.
      <class 'library.admin.PlatformAdmin'>: (admin.E020) The value of 'filter_horizontal[1]' must be a many-to-many field.
      <class 'library.admin.UserProfileAdmin'>: (admin.E013) The value of 'filter_horizontal[0]' cannot include the ManyToManyField 'friends', because that field manually specifies a relationship model.
      <class 'library.admin.UserProfileAdmin'>: (admin.E020) The value of 'filter_horizontal[1]' must be a many-to-many field.
      <class 'library.admin.UserProfileAdmin'>: (admin.E020) The value of 'filter_horizontal[2]' must be a many-to-many field.
      <class 'library.admin.UserProfileAdmin'>: (admin.E020) The value of 'filter_horizontal[3]' must be a many-to-many field.
      library.Platform.games: (fields.E303) Reverse query name for 'library.Platform.games' clashes with field name 'library.Game.platform'.
              HINT: Rename field 'library.Game.platform', or add/change a related_name argument to the definition for field 'library.Platform.games'.
      library.Platform.wishlists: (fields.E303) Reverse query name for 'library.Platform.wishlists' clashes with field name 'library.WishList.platform'.
              HINT: Rename field 'library.WishList.platform', or add/change a related_name argument to the definition for field 'library.Platform.wishlists'.
   ```

   **Cause**
   filter orizontal was set in `UserProfile` for `games`, `whishlists` and `platforms` model although they the releation between user profile and  `games`, `whishlists` and `platforms` was one to many.
   filter orizontlal was set also for `FriendList` model but friendlist model has trough attribute

    ```python
    filter_horizontal = ('friends', 'games', 'wishlists', 'platforms')
    ```
  
    The error also complaints about a clash between the foreign key used in the `Platform model`

    ```python
    class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    platform_name = models.CharField(max_length=255)
    platform_image = models.ImageField(null=True,  blank=True)
    games = models.ForeignKey('Game', on_delete=models.CASCADE, blank=True)
    wishlists = models.ForeignKey('WishList', on_delete=models.CASCADE,  blank=True)
    ```
  
    **Solution**
    filrer orizantal was removed in `admin.py` for `UserProfile` model
    related name attribute added to platform model for the foreign keys

    ```python
    class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    platform_name = models.CharField(max_length=255)
    platform_image = models.ImageField(null=True,  blank=True)
    games = models.ForeignKey('Game', on_delete=models.CASCADE, blank=True, related_name='games' )
    wishlists = models.ForeignKey('WishList', on_delete=models.CASCADE,  blank=True, related_name='wish_list')
    ```

1. **Error**:

   ```cmd
    IntegrityError at /admin/library/platform/add/
    null value in column "games_id" of relation "library_platform" violates not-null constraint
    DETAIL:  Failing row contains (c64c5653-4b10-4f1c-a68d-cf1754346e90, Game Pass, , null, null, null).
    Request Method:POST
    Django Version:5.0
    Exception Type:IntegrityError
    Exception Value:
    null value in column "games_id" of relation "library_platform" violates not-null constraint
    DETAIL:  Failing row contains (c64c5653-4b10-4f1c-a68d-cf1754346e90, Game Pass, , null, null, null).
    Exception Location:
   ```

   **Cause**:
    Games is Foreign key for platfrom and is not set to null=true

    **Solution**:
    Added null= True to the game and wish list ForeignKey

    ```python
    games = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    ```

1. **Error**:
    The template platform_list.html does not show platform created

    **Cause**:
    Platform attributes were called incorrectly in .html template

    ```html
      <h1>Platforms list</h1>
      {% for platform in object_list %}
        <h2>{{platform.name}}</h2>
        <p>{{plaform.model}}</p>
      {% endfor %}
    ```

    **Solution**:
    Corrected platform instance attribute name in .html template

    ```html
     <h1>Platforms list</h1>
      {% for platform in object_list %}
        <h2>{{platform.platform_name}}</h2>
        <p>{{platform.platform_model}}</p>
      {% endfor %}
    
    ```

1. **Error**

   ```cmd
      TemplateDoesNotExist at /add_platform/
      add_platform.html
      Request Method:GET
      Django Version:5.0
      Exception Type:TemplateDoesNotExist
      Exception Value:
      add_platform.html
   ```

   **Cause**
   Template file name was missing from add `platform view`

   **Solution**
   Added add platform template to add platform view:

   ```python
      def add_platform(request):
        platform_form = AddPlatformForm()

        if request.method == 'POST':
            platform_form = AddPlatformForm(request.POST)
            if platform_form.is_valid():
                platform_form.save()
                # Add any additional logic or redirect here
                return redirect('')

        return render(request,
                      'library/add_platform.html',
                      {'platform_form': platform_form})
   ```

1. **Error**

   ```cmd
    django.db.utils.ProgrammingError: Problem installing fixture ': Could not load library.Platform(pk=00000000-0000-0000-0000-000000000001): column "user_id" of relation "library_platform" does not exist
    LINE 1: ...g', "box_color" = NULL, "font_color" = '#fafafa', "user_id" ...
   ```

   **Cause**
   Database was corrupted

   **Solution**
   reset database on elephant sql

1. **Error**

   ```cmd
   django.urls.exceptions.NoReverseMatch: Reverse for 'collaborate' not found. 'collaborate' is not a valid view function or pattern name.
   ```

   **Cause**
   url was missing in url.py

   **Solution**

   ```python
      path('collaborate/', views.collaborate, name='collaborate'),
   ```

1. **Error**

   ```cmd
    UnboundLocalError at /game-pass/edit_platform/00000000-0000-0000-0000-000000000001/
    cannot access local variable 'platform' where it is not associated with a value
    Request Method:GET
    Request URL:http://127.0.0.1:8000/game-pass/edit_platform/00000000-0000-0000-0000-000000000001/
    Django Version:5.0
    Exception Type:UnboundLocalError
    Exception Value:
    cannot access local variable 'platform' where it is not associated with a value
    Raised during:library.views.edit_platform
    Python Version:3.11.4
   ```

    **Cause**
    In view.py form was named `edit_platform_form` but variable `form` was called in html template

    **Solution**
    named form as `edit_platfotm_form` in views.py and called variable `edit_platfotm_form` in html

    ```html
    <form method="post"  class='white-text' action="{% url 'edit_platform' platform.slug platform.id%}">
      {% csrf_token %}
      {{ edit_platform_form|crispy }}
      <button type="submit">Save</button>
    </form>
    ```
  
1. **Error**

    ```cmd
    Page not found (404)
    No Platform matches the given query.
    Request Method:GET
    Request URL:http://127.0.0.1:8000/steam/undefined
    Raised by:library.views.platform_detail
    ```

    **Cause**
    `platform.id` was assigned as a attribute to the modal button rather than to the delete button

    **Solution**
    added `platform.id` to the delete button element

    ```html
    <div class="text-center white-text">
      <button class="btn btn-delete btn-danger white-text" data-platformid="{{ platform.id }}" id="deleteButton">Delete</button>
    </div>
    ```

1. **Error**

    ```cmd
    library\Lib\site-packages\django\utils\module_loading.py", line 25, in import_string
    module_path, class_name = dotted_path.rsplit(".", 1)
                              ^^^^^^^^^^^^^^^^^^
    AttributeError: 'tuple' object has no attribute 'rsplit'
    ```

    **Cause**
    Application of pep8 rule in `setting.py`:

    ```python
        AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': ('django.contrib.auth.password_validation.'
                    'UserAttributeSimilarityValidator'),
        },
        {
            'NAME': ('django.contrib.auth.password_validation.'
                    'MinimumLengthValidator'),
        },
        {
            'NAME': ('django.contrib.auth.password_validation.'
                    'CommonPasswordValidator'),
        },
        {
            'NAME': ('django.contrib.auth.password_validation.'
                    'NumericPasswordValidator',)
        },
    ]
    ```

    **Solution**
    To restore default in settings.py solved the issue:

    ```python
      AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
    ]
    ```

1. **Error**
     Adding a new platform returns error:

    ```cmd
      django.db.utils.IntegrityError: null value in column "user_id" of relation "library_platform" violates not-null constraint
      DETAIL: Failing row contains (4b4415a6-8d18-47c0-addf-9d15235bdb82, test, test, pc, placeholder, null, #fafafa, null).
    ```

   **Cause**
    Platform model has been update so that user is a foreign key of platform, therefore when a new platform is added a user is required

    **Solution**
    `login_required` decorator has been added to the view and user is passed during the form save function

    ```python
      @login_required
      def add_platform(request):
      if request.method == 'POST':
          add_platform_form = AddPlatformForm(request.POST)
          if add_platform_form.is_valid():
              add_platform_form.save(user=request.user)
              messages.add_message(request, messages.SUCCESS,
                                  'new platform added')
              return redirect('home')
          else:
              messages.error(request, 'Error adding the platform. Please check'
                            'the form.')
      else:
          add_platform_form = AddPlatformForm()

      return render(request,
                    'library/add_platform.html',
                    {'add_platform_form': add_platform_form})
    
    ```
  
1. **Error**

     ```cmd
     TypeError at /3r23r23r/delete_platform/6463b2fe-6a98-43ec-9817-9bbc33b30222/
     delete_platform() got an unexpected keyword argument 'slug'
     ```

   **Cause**
   Url to delete platform required 'slug' as parameter but slug was removed from delete_platform view

   **View**
   Added url back to delete_platform view

1. **Error**
  Expand button is expanding on `index.html` is expanding but collapsing

   **Cause**
    Interference between bootstrap imported in `base.html`

    ```html
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
      <script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
    ```

    **Solution**
    kept Boostrap bundle which includes popper and Bootstrap and removed lines the other two lines

   ```html
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
   ```
  
1. **Error**
     If a user tries to add a `platform` with the same name of the platform of another user gets error:

     ```cmd
     IntegrityError at /add_platform/
    duplicate key value violates unique constraint "library_platform_slug_key"
      DETAIL:  Key (slug)=(test) already exists.
    ```

    **Cause**
    URL for `platform details`, `add platform` and `remove platform` is designed to include only slug, which will be the same if two user Add the same platform name.

    **Solution**
    Added `user id` to the url for `platform details`, `add platform` and `remove platform`

    ```python
    urlpatterns = [
        path('', views.PlatformList.as_view(), name='home'),
        path('add_game/', views.add_game, name='add_game'),
        path('add_platform/', views.add_platform, name='add_platform'),
        path('<int:user_id>/<slug:slug>/', views.platform_detail,
            name='platform_detail'),
        path('<int:user_id>/<slug:slug>/edit_platform/<uuid:platform_id>/',
            views.edit_platform, name='edit_platform'),
        path('<int:user_id>/<slug:slug>/delete_platform/<uuid:platform_id>/',
            views.delete_platform, name='delete_platform'),
    ]
    ```

1. **Error**
   Different users can see platforms of other users, when adding a game to platform

   **Cause**
   Platforms were not filtered in forms.py for add game form

   **Solution**
   Added a filter to restrict view to only user owned platform in add_game form

   ```python
   def __init__(self, user, *args, **kwargs):
        super(AddGameForm, self).__init__(*args, **kwargs)
        # Filter platforms based on the current user
        self.fields['platform'].queryset = Platform.objects.filter(user=user)
   ```

1. **Error**
   Images are not uploaded to Cloudindary when uploaded via form

   **Cause**
  Form in html template and view were missing relevant fields

   **Solution**

    ```python
    @login_required
    def add_platform(request):
        if request.method == 'POST':
            add_platform_form = AddPlatformForm(request.POST, request.FILES)
            if add_platform_form.is_valid():
                platform_name = add_platform_form.cleaned_data['name']
    ```

    ```html
      <form method="post" class="white-text" enctype="multipart/form-data" action="{% url 'add_platform' %}">
        {% csrf_token %}
        {{ add_platform_form|crispy }}
        <button type="submit" class="btn btn-primary">Add Platform</button>
    </form>

    ```

1. **Error**
    When creating the edit game form got error:

    ```cmd
    from .forms import (AddPlatformForm, EditPlatformForm, AddGameForm,)
    raise FieldError(
    django.core.exceptions.FieldError: 'completion_date' cannot be specified for Game model form as it is a non-editable field)

    ```

    **Cause**
    Field `auto_now_add=True` was added to the `Game` model if this is added the field is not editable

    **Solution**
    Changed `auto_now_add=True` to `default=models.functions.Now` to set current date as default and allow to edit the completion date

1. **Error**
   got the following error when creating the creating the `edit game` view

   ```cmd
   NoReverseMatch at /1/games-pass/test2/
   Reverse for 'edit_game' with arguments '(1, '', 'test2')' not found. 1 pattern(s) tried: ['(?P<user_id>[0-9]+)/(?P<platform_slug>[-a-zA-Z0-9_]+)/(?P<game_slug>[-a-zA-Z0-9_]+)/edit_game/\\Z']
   ```
  
   **Cause**
   The edit game button is added on the `game_detail.html` and to form the url the platform.slug attribute is required.
   Nevertheless, the `game_detail` view does not return the instance of the platform

   **Solution**
   Added the instance of platform in the return of `game_detail` view

   ```python
    user = request.user
      platform = get_object_or_404(Platform, user=user, slug=platform_slug)
      game = get_object_or_404(Game, platform=platform, slug=game_slug)

      return render(
          request,
          "library/game_detail.html",
          {
          "platform": platform,
          "game": game},
      )
   ```

1. **Error**
   Platform and Gamer slug does not change after edits and the url use the slug

    **Cause**
    After instance editing slug attribute does not get updated

    **Solution**
    Url use platform, game, and wishlist_game id rather than slug in the urls

## Diary

- ### Sprint 1

  - **11/12/2023**
    Add user stories template
    add labels
    add user stories
    add sprint 1
    add wireframe
    update feasibility importance plot
    start django project

  - **12/12/2023**
    set up early deployment
    documented bugs
    created and connected to postgresql
    connect to cloudinary
    successfull deployment on heroku

  - **15/12/2023**
    database schema creation
    database implementation

  - **16/12/2023**
    add manytomany relation on database
    deletion and recreation of database

  - **17/12/2023**
    changed many to many relation into one to many in the following:
    user-games is now one to many
    user-wishlists is now one to many
    added plaltform table
    user-platform is one to many
    platform-games is one to many
    platform-wishlists os one to many

  - **19/12/2023**
     add basic view and url
     allows to see the list of platforms available
     added template html to visualize platforms list

  - **20/12/2023**
     add summernote
     add fixture

  - **21/12/2023**
    reshape model adding platform subclasses

  - **25/12/2023**
     created base.html
     add boostrap
     add fontawesome

- ### Sprint 2

  - **26/12/2023**
  - add index.html
  - add javascript and jquery

- **27/12/2023**
  - add game list to index.html
  - remove foreign key from platform model

- **28/12/2023**
  - move static files from cloudinary to collectstic
  - add whitenoise
  
- **29/12/2023**
  - add view function for platform detail.html
  - add platform detail .html
  - add slug field to platforms
  - add style to platform detail.html
  - updates fixtures

- **30/12/2023**
  - add about app
  - add about url, views, settings model
  - add about template
  - style about template
  
- **31/12/2023**
  - add authentication
  - add authentication templates
  - add authentication draft style

- **01/01/2024**
  - Part C of crud
  - add form.py
  - add form templates, urls and views to add platforms and games
  
- **02/01/2024**
  - add User foreign key to platform model

- **06/01/2024**
  - add collaborate form

- ### Sprint 3

- **09/01/2024**
  - add edit platform url and view draft
  
- **10/01/2024**
  - allow platform editing
  - allow platform deleting

- **12/01/2024**
  - add modal for platform deletion

- **13/01/2024**
  - adapt code to pep8

- **14/01/2024**
  - add cloudinary for media storage
  - start draft testing unit

- **17/01/2024**
  - add unit testing for about and library app

- **18/01/2024**
  - fix platform addition and deletion after adding user

- **21/01/2024**
  - reshape index.html

- ### Sprint 4
  
- **22/01/2024**
  - fix delete button on index.html
  - fix expand button on index.html

- **27/01/2024**
  - removed subclasses from platform model
  - improved platform_detail.html

- **31/01/2024**
  - reshape user stories

- **01/02/2024**
  - add image form for game
  - add game detail view
  - add game detail template
  - add game detail url

- **03/02/2024**
  - add delete game view, url and javascript

- **04/02/2024**
  - add currency attribute to platform
  - improve general layout of platform detail

- ### Sprint 5

- **06/02/2024**
  - fix delete game button
  - improve forms layout
  - improve game detail layout

- **07/02/2024**
  - fix null platform for game
  - update wishlist model
  - add wishlist form
  - C of wishlist crud complete

- **08/02/2024**
  - add wish list game detail view, url, and template

- **09/02/2024**
  - add edit game detail view and url
  - add delete game view and javascript
  - sort game, wish list and platforms

- **10/02/2024**
  - add intro page
  - style sign in sign up

- **11/02/2024**
  - add info page
  - rename about into get in touch
  - add get in touch form

- **12/02/2024**
  - set restriction for images files

- **13/02/2024**
  - add tests for all platform views

- **14/02/2024**
  - urls use platform.id game.id and wishlist_game.id rather than slugs
  - add test for game and wishlist game views
  - add test for Platform, Game and Wishlist forms

- **17/02/2024**
  - improve games expanding on index.html

- **18/02/2024**
  - add overflow to index.html
  - reduce image size in get_in_touch.html
  - improve accessibility on index.html
  - add docstring to all views

- ### Sprint 6

- **20/02/2024**
  - complete docs intro

- **21/02/2024**
  - complete docs scope, strategy, structure
  - add user stories up to sprint 2

- **23/02/2024**
  - completed planning phase in docs

- **24/02/2024**
  - completed features in docs
