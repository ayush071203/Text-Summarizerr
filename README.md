This Django-project runs on a bart based model, so to setup the project we need to :

Step 1: Run the following commands on the terminal a) pip install transformers. b) from transformers import pipeline (use this in views.py file for importing pipeline functionality which is a part of transformers from Hugging Face model). c)Install the Hugging face model for text summarization based on bart.

Step 2: Run "python manage.py runserver" to run the project successfully.

or else , first run these 2 commands as : "python manage.py makemigrations" "python manage.py migrate"

and then finally run type "python manage.py runserver" on the terminal to run the project.

Happy Coding...
