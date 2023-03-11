import json

import services.api.OMDB as omdb


def transformData(movie):
    movie = omdb.sendQuery('type=movie&t=' +movie)
    movie = producesBefore2015(movie)
    movie = hasPaulWalker(movie)
    return movie

def producesBefore2015(movie):
    movie['producedBefore2015'] = False
    if (int(movie['Year']) < 2015):
        movie['producedBefore2015'] = True
    return movie

def hasPaulWalker(movie):
    movie['hasPaulWalker'] = False
    arrayActors = movie['Actors'].split(', ')
    for actor in arrayActors:
        if (actor == 'Paul Walker'):
            movie['hasPaulWalker'] = True
    return movie