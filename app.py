def main():
    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Use your AWS region
    table = dynamodb.Table('Order')  # Replace with your actual table name

    # Scan the table
    try:
        response = table.scan()
        items = response.get('Items', [])
        print("Data from DynamoDB Table 'Order':")
        for item in items:
            print(item)
    except Exception as e:
        print("Failed to read from DynamoDB:", str(e))

if _name_ == "_main_":
    main()