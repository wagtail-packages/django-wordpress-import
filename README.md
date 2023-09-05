# Django Wordpress Import

## Install dependencies

```bash
poetry install
```

Activate the virtual environment

```bash
poetry shell
```

## Wordpress demo site

### Running the Wordpress demo site

The Wordpress demo site uses a docker container that can be started with the following command:

```bash
wp build
wp up
wp load
```

It will be available at <http://localhost:8888> and the admin at <http://localhost:8888/wp-admin> and populated with some default content.

You can login with the following credentials:

- Username: `admin`
- Password: `password`

The API root can be seen here: <http://localhost:8888/wp-json/wp/v2>

- [Posts](http://localhost:8888/wp-json/wp/v2/posts)
- [Pages](http://localhost:8888/wp-json/wp/v2/pages)
- [Media](http://localhost:8888/wp-json/wp/v2/media)
- [Categories](http://localhost:8888/wp-json/wp/v2/categories)
- [Tags](http://localhost:8888/wp-json/wp/v2/tags)
- [Users](http://localhost:8888/wp-json/wp/v2/users)
- [Comments](http://localhost:8888/wp-json/wp/v2/comments)

### To stop the demo site

```bash
wp down
```

### To remove the demo site

```bash
wp destroy
```

### List of wordpress commands

```bash
wp --help
```

## Django import site

### Running an import

```bash
dj authors
dj categories
dj tags
dj posts
dj pages
dj media
dj comments
```

or to run all of them

```bash
dj complete
```

### To run the Django site

```bash
dj runserver
```

### Management commands

With the virtual environment activated you can run the following commands:

```bash
./manage.py [command]
```

## Requiremnts

- [x] Spin up a wordpress example site to import from
- [x] Import form the Wordpress JSON API
- [x] Create comparable records in Django models
- [x] Make admin a usable app for at least viewing the importred content
- [ ] Expose an API that can be used to import into Wagtail
