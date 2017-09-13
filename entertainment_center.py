import media
import fresh_tomatoes

premam=media.Movie("premam","It is an malayalam movie..","http://media3.picsearch.com/is?eTi43KizYLCuodyQlb3laIs14R_8R96uEArma3M2IJM&height=255","https://www.youtube.com/watch?v=i6TSrhiuSJA")

rajarani=media.Movie("rajarani","A love story of the international movie writen by atli","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwvyvAiMUerwLu_qfxAAcn_OcEnQpJ-uBeWrZjf9C9WY-1sI4gHV8nyxs","https://www.youtube.com/watch?v=wZm38_0aIXk")

jungle_book=media.Movie("junglebook","It is an animation movie","http://cdn.collider.com/wp-content/uploads/2016/04/the-art-of-the-jungle-book-cover.jpg","https://www.youtube.com/watch?v=5mkm22yO-bs")


#premam.show_trailer()
movies=[premam,rajarani,jungle_book]
fresh_tomatoes.open_movies_page(movies)


