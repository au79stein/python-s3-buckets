#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
import boto3


app = Flask(__name__)

# AWS S3 Configuration
S3_BUCKET = "cloudnost"
S3_PREFIX = "testing"
EXPIRATION = 3600  # 1 hour

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

def generate_presigned_url(key):
    """Generate a pre-signed URL for a given S3 object."""
    try:
        return s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': S3_BUCKET, 'Key': key},
            ExpiresIn=EXPIRATION
        )
    except Exception as e:
        print(f"Error generating pre-signed URL: {e}")
        return None

@app.route('/')
def index():
    """Main page with file list (but NO pre-signed URLs initially)."""
    files = list_s3_files()
    return render_template('index.html', files=files)

@app.route('/get_url')
def get_url():
    """Generate a pre-signed URL when requested."""
    key = request.args.get("key")
    if not key:
        return jsonify({"error": "Missing file key"}), 400
    
    url = generate_presigned_url(key)
    if url:
        return jsonify({"url": url})
    return jsonify({"error": "Failed to generate URL"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

