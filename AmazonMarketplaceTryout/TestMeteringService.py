# Import AWS Python SDK and urllib.parse
import boto3
import urllib.parse as urlparse

# Resolving Customer Registration Token
token_full = 'x-amzn-marketplace-token=MFxWGdn81kSnZ1cl8rY%2FLjOYhgc1OFDK5Kvx9HQlmrqHicgrj5mrYIO5JmC%2Bd1P%2FdMfDUlwLKpng7p5rUK3QdGQTjuNtJWGPKEEyVHZDc73u%2Bwso1yqHHvWdcocqQt8AiJtzZS04cYiTQhlPg%2FpsdoYChBzzhh1JmhcNYLOUEFqfVxk%2BZETkLw%3D%3D'
token_short = 'MFxWGdn81kSnZ1cl8rY/LjOYhgc1OFDK5Kvx9HQlmrqHicgrj5mrYIO5JmC+d1P/dMfDUlwLKpng7p5rUK3QdGQTjuNtJWGPKEEyVHZDc73u+wso1yqHHvWdcocqQt8AiJtzZS04cYiTQhlPg/psdoYChBzzhh1JmhcNYLOUEFqfVxk+ZETkLw=='
formFields = urlparse.parse_qs(token_full)
regToken = formFields['x-amzn-marketplace-token']

# If regToken present in POST request, exchange for customerID
if (regToken):
    marketplaceClient = boto3.client('meteringmarketplace')
    customerData = marketplaceClient.resolve_customer(RegistrationToken=token_short)
    productCode = customerData['ProductCode']
    customerID = customerData['CustomerIdentifier']

print(customerData)

    # TODO: Store customer information
    # TODO: Validate no other accounts share the same customerID