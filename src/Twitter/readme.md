# Twitter Scraper

## Docker Build

```
docker build -t twitterscraper:build .
```

Error

```
Please make sure the libxml2 and libxslt development packages are installed.
```

[ここを見てFix](https://github.com/taspinar/twitterscraper/issues/250)


Done

## How to use

```
docker run --rm -it -v/<PATH_TO_SOME_SHARED_FOLDER_FOR_RESULTS>:/app/data twitterscraper:build <YOUR_QUERY>
```