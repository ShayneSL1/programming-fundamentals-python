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

#Adding a new Key-Value pair
ec2Instance["AvailabilityZone"] = "us-east-2"
ec2Instance["State"] = "stopped"
print(ec2Instance)

#Removing a Key-Value Pair
#Using pop() method
rmInstanceType = ec2Instance.pop("InstanceType")
print(ec2Instance)

#Del method
del ec2Instance["AvailabilityZone"]
print(ec2Instance)