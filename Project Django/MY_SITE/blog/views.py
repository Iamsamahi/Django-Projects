from django.shortcuts import render
from datetime import date
from operator import itemgetter
dict_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "seabeach.jpg",
        "author": "Saif",
        "date": date(2021, 7, 21),
        "title": "Sea Shore",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "Recent-Marvel-Movie",
        "image": "spiderman.jpg",
        "author": "Saif",
        "date": date(2022, 3, 10),
        "title": "Giving some self time",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday. Thats why I went out with friends to have some recreation b...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Saif",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_Date(date):
    return date["date"]

# Create your views here.

def homepage(request):
  sorted_Post = sorted(dict_posts,key=get_Date) #returning a new sorted list accorrding to the key value of the previous list 
  latest_Post = sorted_Post[-3:] #List slicing - taking the value of the last one starting from the righttmost
  return render(request,"blog/index.html", {
     "post" : latest_Post 
  })


def posts(request) :
    return render(request, "blog/all-posts.html",{
        "all_post" : dict_posts
    } )

def post_details(request,slug) :
   specifiedLink = []
   for posts in dict_posts : 
      if posts['slug'] == slug :
         specifiedLink = posts
   return render(request, "blog/post-details.html" , {
      
      "post" : specifiedLink
   } )