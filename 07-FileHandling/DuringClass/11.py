film_titles = ["beter call soul","breaking bad","docktor house", "drive","idkł"]
file = open('C:/Study/pp1/07-FileHandling/During class/films.txt','a')
for title in film_titles:
    file.write(f"{title}\n")