from common import get_table, response
import json

def lambda_handler(event, context):
    table = get_table()
    id = event['pathParameters']['id']
    body = json.loads(event.get('body') or '{}')
    update_expr = 'SET '
    expr_attr = {}
    parts = []
    if 'title' in body:
        parts.append('title = :t')
        expr_attr[':t'] = body['title']
    if 'completed' in body:
        parts.append('completed = :c')
        expr_attr[':c'] = body['completed']
    if parts:
        update_expr += ', '.join(parts)
        res = table.update_item(
            Key={'id': id},
            UpdateExpression=update_expr,
            ExpressionAttributeValues=expr_attr,
            ReturnValues='ALL_NEW'
        )
        return response(200, res.get('Attributes'))
    else:
        return response(400, {'message': 'no fields to update'})
