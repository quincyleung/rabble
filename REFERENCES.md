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