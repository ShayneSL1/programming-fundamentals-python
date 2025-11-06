""" Dictionaries
Store and retrieve information
Key and Values """

#EC2
ec2Instance = {
    "InstanceId": "i-123abc",
    "InstanceType": "t2-micro",
    "State": "running",
    #"PublicIpAddress": "203.0.111.2"
}

instanceType = ec2Instance["InstanceId"]
print(instanceType)

publicIp = ec2Instance.get("PublicIpAddress", "No Public IP Address here.")
print(publicIp)