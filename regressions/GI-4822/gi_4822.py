import boto3

s3 = boto3.client('s3')
s3.download_file('remote-run-demo', 'grid-run-remote_rpsbrin/object.p', '/tmp/aaa')
