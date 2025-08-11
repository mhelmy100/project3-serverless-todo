import uuid
from common import get_table, response
import json

def lambda_handler(event, context):
    body = json.loads(event.get('body') or '{}')
    item_id = str(uuid.uuid4())
    item = {
        'id': item_id,
        'title': body.get('title', 'Untitled'),
        'completed': body.get('completed', False)
    }
    table = get_table()
    table.put_item(Item=item)
    return response(201, item)
