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

database schema

![Database_schema](/docs/images/gamer_library_database_schema.png)

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
