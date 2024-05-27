import boto3
import argparse
import yaml

# Initializing client
client_eks = boto3.client("eks")
client_vpc = boto3.client('vpc')
client_ecr = boto3.client('ecr')
client_iam = boto3.client('iam')

with open('config_task.yaml', 'r') as file:
    config = yaml.load(file)

    


def create_eks():
    client_eks.create_cluster(
        name='flask-eks-cluster'
    ),

    client_eks.create_addon(
        
    )

def create_vpc():
    pass

def create_iam():
    pass

def create_ecr():
    pass


def main():
    create_eks()
    create_ecr()
    create_iam()
    create_vpc()