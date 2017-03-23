import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        randomlist = ["Beauty and the Beast","Finding Nemo","Aladdin","Lion King","Little Mermaid"]
        # TODO: randomly choose one of the movies, and return it
        choice = randomlist[random.randrange(len(randomlist))]
        return choice

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        movie2 = self.getRandomMovie()
        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        content += "<br><br><h1>Tomorrow's movie of the day</h1>"
        content += "<p>" + movie2 + "</p>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
