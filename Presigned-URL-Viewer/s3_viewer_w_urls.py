#!/usr/bin/env python3

import boto3
from flask import Flask, render_template, request, Response

app = Flask(__name__)

# AWS S3 Configuration
S3_BUCKET = "cloudnost"
S3_PREFIX = "testing"
EXPIRATION = 3600  # URL expiration time in seconds

# Initialize S3 client
s3 = boto3.client('s3')

def list_s3_files():
    """List files under the specified S3 prefix."""
    try:
        response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
        if "Contents" in response:
            return [obj["Key"] for obj in response["Contents"]]
        return []
    except Exception as e:
        print(f"Error listing S3 files: {e}")
        return []

@app.route('/')
def index():
    """Main page that lists files."""
    files = list_s3_files()
    return render_template('index.html', files=files)

@app.route('/view/<path:key>')
def view_file(key):
    """Fetch file from S3 and display it inline."""
    try:
        s3_response = s3.get_object(Bucket=S3_BUCKET, Key=key)
        content = s3_response['Body'].read()
        content_type = s3_response['ContentType']  # Get MIME type

        return Response(content, content_type=content_type)
    except Exception as e:
        return f"Error fetching file: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

