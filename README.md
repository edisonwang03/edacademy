# EdAcademy

https://www.youtube.com/watch?v=nhALP2m-tKM&t=1s 

## Inspiration
I was inspired by Khan Academy's model of providing free, online educational resources to students of all ages. I grew up learning from Khan Academy, and I hope to provide even more learning opportunities on an alternative platform.

## What it does
EdAcademy simplifies Khan Academy's site by creating an intuitive UI that still offers the same learning experience. Users can login to their own personalized dashboard and explore tab. Users can add courses from the explore tab and view them on the dashboard. Once the course is completed, users can remove the course from their dashboard.

## How I built it
I used Flask as a backend to connect to an SQLite database. Flask-SQLAlchemy was an extension used to do so. Jinja acted as a web template engine to organize my HTML templates while also being able to add code. Flask-WTF provided me a way to create simple forms for login, sign-up, and email-recovery. Flask-Login provided a way to encrypt the passwords stored and maintain different user accounts. Bootstrap helped the stylize my HTML. 

## Challenges we ran into
Since I am familiar with primarily using JavaScript in my last web application (a PERN stack To-do list), it was difficult adjusting to a primarily Python-based app. Learning a new framework was very difficult. Additionally, dealing with a relational database made the process a lot more difficult. I had to do research on how to represent a many-to-many relationship, which was done using an association table; that way, I could connect many students to many courses.  I also found it difficult understanding the terminology with logins.

## Accomplishments that I'm proud of
I am proud of creating an app that is very intuitive on the engineering side. All my folders and files are organized so that it makes sense. I am also proud of creating the login system. Having personalized accounts is very important when creating an education service. I am also proud of utilizing my prior knowledge of basic Python and applying it to a more complex program. Before, I used Python and the Pygame module to create simple videogames. Now, I have demonstrated my expertise in Python when creating a web application.

## What I learned
I learned how to use Python, Flask, Bootstrap, Jinja, and SQLite. More importantly, I learned how to do my own research and solve my own problems. Looking up the necessary documentation and using my brain to apply it to my project was very challenging, but an experience I will remember.

## What's next for EdAcademy
I plan to create a search bar on the explore tab that allows users to search for specific courses and filter which courses they specifically want to see (i.e. most people enrolled, highest reviews, alphabetical, etc.). I also plan to make the courses more complex, such as including images, videos, and quizzes.
