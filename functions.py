import random

""" def functionName(parameter1, parameter2):
    #function body has code to be executed with inputs/parameters
return result #optional """

def generateBucketName(projectName):
    randomSuffix = random.int(1,9999)
    bucketName = f"{projectName}-bucket-{randomSuffix}"
    return bucketName

superBucket = generateBucketName("S3Bucket")
print(superBucket)  