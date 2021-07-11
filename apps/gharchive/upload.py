from util import get_client


def upload_s3(body, bucket, file):
    s3_client = get_client()
    res = s3_client.put_object(
        Bucket=bucket,
        Key=file,
        Body=body
    )
    return res
