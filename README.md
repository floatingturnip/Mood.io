# mood.io

## Inspiration
As students who undergo a lot of stress throughout the year, we are often out of touch with our emotions and it can sometimes be difficult to tell how we are feeling throughout the day. There are days when we might be unsure of how we are really feeling based on our self-talk. Do I feel down, happy, sad, etc? We decided to develop a journal app that interprets the entries we write and quantitatively tracks our mood. This allows us to be more aware of our mental well-being at all times.

## What it does
mood.io takes your daily journal entries and returns a "mood" score for that specific day. This is calculated using Google Cloud's ML Natural Language API, which is then translated into a line graph that tracks your moods over time. The Natural Language API also identifies important subject matter in each entry, known as "entities", which mood.io displays using attractive data visualization tools. This allows you to aim for improvement in your mental health and identify issues you might have in your daily lives.

## How I built it
For our prototype, we built a web app using the Flask framework within Python, which helped with routing and rendering our HTML based homepage. We used Bootstrap to help with the front-end UI look. We also used the Google Cloud Natural Language Processing API to analyze sentiment values and provide the entity data. The data was shown using the matplotlib library within Python.

A concept of our final product was created using Figma and is attached to this submission.


## Challenges I ran into
Our very first challenge was installing python and getting it properly set up so that we didn’t have any errors. When trying to run a simple program.

We then ran into challenges in trying to understand how to interact with the Google Cloud API and how to get it set up and running with Python. After talking to some Google sponsors and mentors, we managed to get it set up properly and work with the code.

Another issue was getting a graph to display properly and making a pretty data visualization, we had tried many different applications to generate graphs but we had issues with each of them until we found one that worked.

Additionally no one in our team had a lack of experience in front end development so making the site look nice and display properly was another issue.

## Accomplishments that I'm proud of
Used a WDM for decision making process process. 
Cool idea! 
Real results! 
Learning to use python. 
Getting an api to work. 
Getting a graph to display properly.

We are proud of the progress we were able to achieve through our first Hackathon experience. Thanks to all the mentors and sponsors that assisted us in our journey

## What I learned
How to program in Python, interact with an API, make a data visualization, how to build a web app from scratch, how to use Google Cloud and its various computing services

## What's next for mood.io
Add users so you can add close friends and family and track their moods.
Adding the entities feature on our prototype
Further improving our UI experience
