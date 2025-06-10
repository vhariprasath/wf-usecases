import os

def main():
    # Read environment variable
    bucket_name = os.getenv("BUCKET_NAME", "default-bucket")

    # Use the variable
    print(f"Using S3 bucket: {bucket_name}")

if __name__ == "__main__":
    main()
