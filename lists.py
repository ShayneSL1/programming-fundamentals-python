#List of EC2 Instance
instanceIds = ['i-1234','i-5678','i-9012']

#List of IPs for a security group
ipAddresses = ['10.0.0.1','10.0.0.2','10.0.0.3']

#List of AZs in a region
availabilityZones = ['us-east-1a','us-east-2b','us-east-3c']

#Print the lists
print(f"EC2 instances to delete: {instanceIds}")
print(f"IP Addresses: {ipAddresses}")
print(f"Number of availability zones: {availabilityZones}")
