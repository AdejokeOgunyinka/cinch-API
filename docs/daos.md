## Introduction

Data Access Objects (DAOs) are classes that defines query methods for fetching data from and inserting into the database. Note that using this pattern means that we are adding another layer on top of our actual data layer and doing this ensures that updates to the defined methods' implementations on how data should be fetched or inserted does not break the application at large when and hence promotes replacability of our data layer

The data layer that implementations in the DAOs are based on, is the default Django ORM using the models defined in the `db` folder. If we want to use another data layer in future, all we need to do is replace the `db` folder and update the implementations of the methods in the DAOs with changing the names and arguments of the methods.

Methods defined in our DAOs should be very concise and only describes that needs to be inserted or fetched, and also only return serialized data ready for transmission.

```python

# >> Assume a module at : daos/artists_dao.py

from models import Artist
from serializers import ArtistSerializer


class ArtistsDAO:
    @classmethod
    def fetch_all_artists(cls):
        artists = Artist.objects.all()
        return ArtistSerializer(artists, many=True).data
    
    @classmethod
    def fetch_top_artists(cls):
        artists = Artist.objects.filter(...)
        return ArtistSerializer(artists, many=True).data
    
    @classmethod
    def create_author(cls, first_name, last_name):
        artist = Artist.create(first_name=first_name, last_name=last_name)
        return ArtistSerializer(artists).data

```

## Notes & Caveats

- DAO classes must depend only on contents defined in the db folder
- Watch out for changes to the methods signatures as doing that might break the system
- Updates to method implementations will not break the system as long as their signatures remain the same
