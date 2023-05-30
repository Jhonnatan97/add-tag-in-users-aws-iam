# Script to add 'tag_status' tag to IAM users

This Python script uses the Boto3 library to add the 'tag_status' tag to IAM users in an AWS account.

## Prerequisites

- Python 3.x
- Boto3 library

## Settings

Before running the script, make sure you have correctly configured the AWS CLI profile that will be used for authentication. You can configure the profile by running the command:

```
aws configure --profile <your-profile>
```

## How to use

1. Open the terminal and navigate to the directory where the script is located.

2. Run the following command to install the Boto3 library, if it is not already installed:

```
pip install boto3
```

3. Execute o script usando o seguinte comando:
```
python script.py
```
The script will connect to AWS using the 'your-profile' profile and list all IAM users. It will then add the 'tag_status' tag to each user who doesn't already have it.

The 'tag_status' tag is used to track the status of IAM users.

**Note:** Make sure you have the proper permissions to run the script.

