import boto3

client = boto3.client('marketplace-entitlement')

response = client.get_entitlements(
    ProductCode='36bhyxe8r4udkhe1zl1kp8bac',
    Filter={
        'CUSTOMER_IDENTIFIER': ['9GfvGB7aUGW'],
    },
    MaxResults=20
)
print(response)

