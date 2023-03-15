import boto3
from os import chdir as cd
import os
import subprocess

#Change the current directory
os.chdir('/home/devops/hdd/release/WKDY/xs-dev/mt6890/openwrt/')
#print the current directory path
print("Current working directory: {0}".format(os.getcwd()))

#Run the sh script and store the output into output veriable
output = os.popen('./scripts/create_xs_revision.sh').read()
#add the bin in the last of reterived output
f_name=(output.rstrip() + '.bin')
#print the filename with bin extension
print(f_name)

#Now find the file as above reterived file name from the given location
import io
f = io.StringIO()
for root, dirs, files in os.walk("/home/devops/hdd/release/WKDY/xs-dev/mt6890/openwrt"):
      for file in files:
          if file.endswith(f_name):
              print(os.path.join(root, file),file=f)
              a = f.getvalue()
              print(a) 
              f.close()

# Create an S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id='******************************',
    aws_secret_access_key='***********************************'
)


filename = a.rstrip()
bucket_name = 'bucket name'

#upload the file on AWS S3
s3.upload_file(filename, bucket_name, f_name)
print('Latest version of file uploaded successfully')
