# S3 File Viewer

Flask (not for production) version of S3 Bucket File Viewer.

Will start a server locally on default port (5000) and list s3 objects for the specified bucket.

Clicking on the object/file links will expand to display the contents of the file

## Run the program

s3_viwer_w_urls.py starts flask

  - the bucket name needs to be specified
  - optionally, you can specify the bucket prefix if you just want to view files with the given prefix
  - us-east-1 is the default region but you can override it and use a different region with --region
  - by default the expiration on a pre-signed url is on hour (3600 s) but this can be changed using --expiration 
```
$: ./s3_viewer_w_urls.py

    usage: s3_viewer_w_urls.py [-h] [--prefix PREFIX] [--region REGION] [--expiration EXPIRATION] bucket
    s3_viewer_w_urls.py: error: the following arguments are required: bucket
```

## Screenshot

[Presigned-URL-Viewer/assets/images/screenshot01.jpeg]
![s3-file-viewer screenshot01.jpg](https://github.com/au79stein/python-s3-buckets/tree/main/Presigned-URL-Viewer/assets/images/screenshot)
![s3-file-viewer screenshot01.jpg](/assets/images/screenshot)
