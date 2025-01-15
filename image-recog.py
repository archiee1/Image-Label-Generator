import boto3

# Function to detect labels in an image using Amazon Rekognition
def detect_labels(photo, bucket):
    # Initialize the Rekognition client
    client = boto3.client('rekognition', region_name='ap-south-1')

    # Call Rekognition to detect labels
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, MaxLabels=10)

    print(f"Labels detected for {photo}:")
    for label in response['Labels']:
        print(f" - {label['Name']} (Confidence: {label['Confidence']:.2f}%)")

def main():
    # Provide your bucket name and image file name here
    bucket_name = "image-recogbucket"
    image_file = "img2.jpg"

    # Call the detect_labels function
    detect_labels(image_file, bucket_name)

if __name__ == "__main__":
    main()
