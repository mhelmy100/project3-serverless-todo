from common import get_table, response

def lambda_handler(event, context):
    table = get_table()
    id = event['pathParameters']['id']
    table.delete_item(Key={'id': id})
    return response(204, {})
