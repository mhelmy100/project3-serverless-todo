from common import get_table, response
import json

def lambda_handler(event, context):
    table = get_table()
    res = table.scan()
    items = res.get('Items', [])
    return response(200, items)
