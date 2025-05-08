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

--Homework #3--
Task 3: subRabble Detail (and Posts List) View
I asked ChatGPT how to attach comment and like counts to each post if those were 
defined in separate models. It recommended calculating the counts in the view 
and adding them to the context manually, which I did.

Task 4: Post Detail View
Similarly, I asked ChatGPT how to show comments related to a post when the 
Comment model is separate from the Post model. It suggested using 
Comment.objects.filter(post=post) in the view and passing that into the 
template context.

Extra Task: Limiting Actions by User
To enforce login requirements and user-specific editing rights, I asked ChatGPT 
questions like “How can I restrict views to logged-in users in Django?” and 
“How can I show a button in a Django template only if the current user is the 
post's author?” It guided me to use @login_required, request.user, and 
conditional logic in the template. 

--Homework #4--
Task 1-2: Adding API endpoints and Sample Requests
I used ChatGPT to help me debug a 400 Bad Request error while implementing a 
POST endpoint. Specifically I asked: "Why did I get a HTTP 400 Bad Request 
saying the field subrabble is required when I make a POST request?". It 
instructed me to mark the field as read-only in my PostSerializer so the DRF 
doesn't expect it in the request body.

--Homework #5--
Task 1-2: Creating Factories and Writing tests for CRUD views
I used ChatGPT to help me debug issues related to generating unique fake data 
using the Faker library in my factory classes. Specifically, I asked: "How can 
I generate a unique subrabble names for a Django model using factory?" 
ChatGPT suggested using a Sequence (eg. name = Sequence(lambda n: 
f"subrabble-{n}")) to avoid unique constraint errors during batch creation.