import boto3
import argparse


client_eks = boto3.client('eks')
client_vpc = boto3.client('vpc')