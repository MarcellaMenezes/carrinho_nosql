from bson.objectid import ObjectId

async def create_order(order_collection, order):
    try:
       
        order = await order_collection.insert_one(order)
        if order.inserted_id:
            print(order)
            return order  
    except Exception as e:
        print(f'create_order.error: {e}')
        
async def get_order_by_id(order_collection, order_id):
    try:
        data = await order_collection.find_one({'_id': ObjectId(order_id)})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}')


async def delete_order_by_id(order_collection, order_id):
    try:
        order = await order_collection.delete_one(
            {'_id': ObjectId(order_id)}
        )
        if order.deleted_count:
            return {'status': 'order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')