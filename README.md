# Memopolis

A fullstack django project, with the aim to create, browse, comment, update and delete memes.

The project is hosted under https://www.memopolis.pl/.

## Upvote System

This site features a system which allows to vote and unvote for a specific meme. Additionally, each user may see their own page that shows their five memes with the largest number of upvotes. This data is shown using chart.js.

![alt text](https://i.imgur.com/Yqtc0xA.png?1 "User upvotes")

# Django REST framework

![alt text](https://i.imgur.com/8UKKiuv.png?1 "Django REST framework")

# API documentation:
## Resources:
### Meme objects:
#### GET
 https://www.memopolis.pl/api/memopolis/meme
#### Description
 Memes are displayed on the main page for example.
#### Properties
        {
           "author": string,
           "title": string,
           "num_vote_up": integer,
           "tags": list of integers,
           "image": string,
           "date_posted": string,
           "accepted": boolean
        }
        
        
        
### Comment objects:
#### GET
 https://www.memopolis.pl/api/memopolis/comment
#### Description
 Comments are displayed on individual meme pages (detail views).
#### Properties
        {
           "author": integer,
           "content": string,
           "num_vote_up": integer,
           "date_posted": string,
           "belongs_to": integer
        }
### Tag objects:
#### GET
 https://www.memopolis.pl/api/memopolis/tag
#### Description
 Tags are bound to memes and describe them.
#### Properties
        {
        "name": string
        }
### Profile objects:
#### GET
 https://www.memopolis.pl/api/users/profile
#### Description
 A profile is a combination of a user and an image, which is used as an avatar.
#### Properties
        {
        "user": integer,
        "image": string 
        }



