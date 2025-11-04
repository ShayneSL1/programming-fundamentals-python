print ('Hello, World!')


print ('Hello, Cloud Engineer!')
if True:
    print('This is indented')
    print('this is also in the if block')
    print('this is a third line that is indented')
print('This is not idented, so it is outside the if block')
print('This is a second line that is not indented.')

#Define the account ID
accountID = '12345'
#Define the project name
projectName = 'myS3Bucket'
#Concatenate the strings to form a unique name
bucketID = accountID + '-' + projectName + '-Bucket'
#Print the resulting name
print(f'The bucket name is {bucketID}')
