import os 
import subprocess as sp

sp.getoutput('aws ec2 run-instances --image-id ami-0ad704c126371a549 --instance-type t2.micro --count 1 --subnet-id subnet-47316b0b --security-group-ids sg-09b30f041bad3c325 --key-name win1')
print("Instance is running")
a = str(sp.getoutput('aws ec2 describe-instances --filters Name=instance-state-name,Values=pending --query "Reservations[*].Instances[*].InstanceId" --output text'))
print(a)
print("Filtering and select instance that create latest...")
sp.getoutput('aws ec2 create-volume --availability-zone ap-south-1b --size 5')
print("Volume is creating...")
b= str(sp.getoutput('aws ec2 describe-volumes --filters Name=size,Values=5 --query "Volumes[*].VolumeId" --output text'))
print(b)
c= f" aws ec2 attach-volume --volume-id  {b}   --instance-id  {a}  --device /dev/sdg "
print(c)
sp.getoutput(c)
print("Volume attach to the os ...")

