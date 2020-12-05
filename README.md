## DISCLAIMER

This is some sort of a test web-application. Nothing serious, just having fun, so, some parts can be written POORLY.
Hope it will not give you pain in the lower-back region.

## Making it work

First, you need to create .env file. Its contents for now:

```
SECRET_KEY=<put your key here>
DB_URL=<your db url here>
DB_TRACK_MODIFICATIONS=<true/false>
```

where
* `SECRET_KEY` is any string you want to use as a salt
* `DB_URL` is an url to your db, if you want to specify it
* `DB_TRACK_MODIFICATIONS` is a flag for tracking modifications for sqlalchemy