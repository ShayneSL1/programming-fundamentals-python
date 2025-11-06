#use ctrl + / to add # to multiple lines

#List of EC2 Instance
instanceIds = ['i-1234','i-5678','i-9012']

#List of IPs for a security group
ipAddresses = ['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.0']

#List of AZs in a region
availabilityZones = ['us-east-1a','us-east-2b','us-east-3c']

""" #Print the lists
print(f"EC2 instances to delete: {instanceIds}")
# print(f"IP Addresses: {ipAddresses}")
# print(f"Number of availability zones: {availabilityZones}")

#Add new EC2 instance id 
instanceIds.append('i-3456')
print(instanceIds)

#Check if list includes an item
if "10.0.0.4" in ipAddresses:
    print("Yes 10.0.0.4 is allowed")
else:
    print("10.0.0.4 is not in the allowed list")
 """

# #Slicing a List
# #First two availability zones
# firstTwoAzs = availabilityZones[:2]
# print("First two AZs:",firstTwoAzs)

# #Last availability zone
# lastAZ = availabilityZones[2:]
# print(lastAZ)

# #.sort method sorts by ascending order
# ipAddresses.sort()
# print(ipAddresses)

#Finding the length of a list
numberOfIps = len(ipAddresses)
print(numberOfIps)