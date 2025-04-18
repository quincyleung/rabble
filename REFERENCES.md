--Homework #1--
Task 1
I used ChatGPT the way it was suggested in the instructions, 
namely by asking it the following: "In a Django template, how 
could I print one text if the user is logged in, and a different 
one if no user is logged in?". It then instructed me to use the 
{% if user.is_authenticated %} template tag to check if the user 
is logged in and siplay different text based on the result.

Task 2
I asked ChatGPT: "In a Django template, how can I update the 
profile view to display username and email address about a 
logged-in user?". I learned that I didn't need to pass username
and email explicitly since request.user is automatically
available in templates.

Task 3
I asked ChatGPT: "In a Django template, how can I show different
buttons depending on whether the user is logged in". It 
instructed me to use {% if user.is_authenticated %} and add the
different buttons.

--Homework #2--
Task 1: Implementing the models
I wrote User, UserFollower, Community, CommunityMember, and 
SubRabble manually, and prompted ChatGPT the way it was 
suggested in the instructions for the rest, namely by asking it 
the following: "Please write a Django model corresponding to the 
following table:[insert table]". I then made some changes with 
the names and removed extra code. I also asked ChatGPT how to add
custom fields to the existing User model, as well as what an 
error meant when I tried to start the server. It advised me to 
resolve it by adding a unique related_name where two or more 
relationships in a model point to the same model.

Task 2: Enabling the models
I asked ChatGPT: "Can you give me a hint on how to add models to 
the Django admin site using the Django way?" It told me that 
Django expects me to register my models in admin.py and gave me 
a basic template.