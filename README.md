# The Gamer Library

---

## Site Overview

---
Immerse yourself in your passion for gaming with The Gamer Library, an app meticulously crafted to seamlessly unite your gaming journey across generations and platforms. As a fellow gamer, I embarked on my gaming odyssey from the early days of Sonic 2 on the Sega Mega Drive and have continued the adventure, spanning up to the latest Baldur's Gate III.

As a hardcore gamer, I understand the struggle to keep track of all the games played. In today's digital era, games come in various formats, scattered across different platforms, each maintaining an independent record. This challenge becomes apparent when attempting to reconcile games played on Game Pass with those in the Steam library, or vice versa. Especially with the advent of cloud gaming, titles shuffle in and out of platforms, making it easy to lose track of your gaming history.

Adding a game to The Gamer Library isn't merely about organization; it's about enhancing your gaming satisfaction. There's a unique sense of achievement in conquering the final boss and proudly adding your triumph to the library. Furthermore, it takes the user on a nostalgic journey, linking specific games to significant moments in their life. I vividly recall playing Digimon World 3 on PS1 when my sister was born, conquering Ornstein and Smough in Dark Souls during my Master's degree, exploring the City of Tears in Hollow Knight with my first job, and immersing myself in Baldur's Gate III builds while crafting this very project.

But why limit this experience to personal reminiscence? The Gamer Library goes beyond, allowing you to share and connect with friends. Discover what games your friends are playing and unveil shared affinities, transforming your gaming endeavor into a social adventure.

The Gamer Library isn't just a solo venture; it's a platform for building communities, especially for multiplayer games. Often, the hesitation to delve into multiplayer experiences arises from not having a group to play with. With The Gamer Library, you can find like-minded individuals, creating communities that evolve multiplayer gaming from a solitary pursuit into a shared, social adventure.

Embark on a new chapter of gaming with The Gamer Library — where your gaming history is celebrated, connections are forged, and communities thrive. Join The Gamer Library and redefine the way you experience and share your love for gaming!

## Table of Contents

- [The Gamer Library](#the-gamer-library)
  - [Site Overview](#site-overview)
  - [Table of Contents](#table-of-contents)
  - [Planning phase](#planning-phase)
    - [Strategy plane](#strategy-plane)
    - [Scope plane](#scope-plane)
  - [Bugs](#bugs)
  - [Diary](#diary)

---

## Planning phase

### Strategy plane

he Gamer Library, a dynamic web app, distinguishes itself by providing a culturally rich and relevant gaming experience. Users can intuitively track and catalog their gaming journey through a web app interface designed for modern gamers. What sets The Gamer Library apart is the fusion of intuitive tracking features and a user-friendly web app interface, offering more than a traditional game library; it provides a comprehensive gaming experience.

Tech considerations encompass responsive design, integration capabilities with various gaming platforms, and a robust backend infrastructure for scalability. Its technology aligns seamlessly with the preferences of modern gamers accustomed to web apps.

Users engage with the platform not just for organization but to enhance and cherish their gaming lifestyle. Beyond tracking games, it offers a space where users can connect, share, and immerse themselves in the vast world of gaming.

Through competitor analysis, gaps and opportunities have been identified, with a focus not only on competition but on excellence. Many existing libraries only consider games purchased on their specific services. For example, on Steam, you can only track games from Steam, and the same applies to Game Pass. Furthermore, when a title leaves the Game Pass service, you lose track of it entirely.

The primary audience is the diverse gaming community — gamers of all ages, backgrounds, and interests. The platform aims to be the nexus connecting gamers worldwide, providing a space that transcends boundaries and resonates with varied gaming interests. It is especially useful for aged gamers who played on old consoles, where games are challenging to retrieve and catalog, as well as for gamers using a variety of platforms seeking a single place to track all their games.

In a landscape filled with competitors, The Gamer Library distinguishes itself by offering a holistic experience that goes beyond being a repository of games, making it a unique and indispensable part of the gaming landscape.

| Opportunity/Problem                              | Importance | Feasibility/Viability |
|---------------------------------------------------|------------|-----------------------|
| Keep track of games                               | 5          | 5                     |
| Import data from Metacritics and Game database API| 3          | 4                     |
| Share game list with friends                      | 5          | 1                     |
| Create wishlists                                  | 3          | 4                     |

![Strategy plan chart](/docs/images/strategy_plan_plot.png)

### Scope plane

This project harnesses the power of Agile development methodologies. Given the solitary nature of development, GitHub emerges as the platform of choice for efficiently managing user stories, epics, and issues.

**Sprint 1 Objectives**:
In the inaugural sprint, the focus is on empowering users with fundamental features:

- **User-Friendly Game Addition**:

    Introduce a seamless form submission process, allowing users to effortlessly add their favorite games to the library.

- **Relational Database Implementation**:

    Establish the foundation of a robust relational database, meticulously designed to handle user and game data. This step is crucial for laying the groundwork that supports future functionalities and enhances data management.

By prioritizing these objectives in the initial sprint, the project sets a strong foundation for subsequent phases, ensuring a streamlined development process and a user-centric gaming experience.

- **Structure plane**

How is the coentent organized in menus
consinstency in colors, labels,
apply changes only when releavant
add error feedback, page not found
provide link to take user back to safety
Stucturre non strictly linear
Information architecture Nested list

- **Skeleton plane**

DO not put too much elements in one page
add searching fpr leywprds
divide content in multiple pages
nanvigation trough icons
create wireframe

![Wireframe](/docs/images/Wireframe.png)

- **Surface plane**
font contrast
contrast font and background
contrast between different section in colors
keep consitancy

---

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

    **Solution** deleted config var DISABLE_COLLEC
    STATIC =1 and added  DISABLE_COLLECTSTATIC=1
  
## Diary

- **11/12/2023**
  Add user stories template
  add labels
  add user stories
  add sprint 1
  add wireframe
  update feasibility importance plot
  start django project

- **12/12/2023**
  