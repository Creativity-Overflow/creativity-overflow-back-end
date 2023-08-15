from azure.storage.blob import BlobServiceClient

# Your Azure Blob Storage settings
AZURE_STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=creativeart;AccountKey=Z0fWkHBSc6+Vyoz4+yW8MrP8r6CbwsU0M+bjXa8ZHVEj3yb3QVLJtHfucs/lt5ymBp7Pku7qh1yq+ASta7mGmw==;EndpointSuffix=core.windows.net'
AZURE_CONTAINER = 'media'

# Create a BlobServiceClient instance
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
