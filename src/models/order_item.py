from bson.objectid import ObjectId

async def create_order_item(order_item_collection, order_item):
    try:
        order_item = await order_item_collection.insert_one(order_item)
        if order_item.inserted_id:
            print(order_item)
            return order_item  
    except Exception as e:
        print(f'create_order_item.error: {e}')
        
async def get_order_item_by_id(order_item_collection, order_item_id):
    try:
        data = await order_item_collection.find_one({'_id': ObjectId(order_item_id)})
        if data:
            return data
    except Exception as e:
        print(f'get_order_item.error: {e}')


async def delete_order_item_by_id(order_item_collection, order_item_id):
    try:
        order_item = await order_item_collection.delete_one(
            {'_id': ObjectId(order_item_id)}
        )
        if order_item.deleted_count:
            return {'status': 'order_item deleted'}
    except Exception as e:
        print(f'delete_order_item.error: {e}')
        
async def delete_order_item_by_order_id(order_item_collection, order_id):
    try:
        order_item = await order_item_collection.delete_one(
            {'orders._id': ObjectId(order_id)}
        )
        if order_item.deleted_count:
            return {'status': 'order_item deleted'}
    except Exception as e:
        print(f'delete_order_item.error: {e}')


async def update_price_order_item(order_item_collection, order_id, new_price):
    order_item = await order_item_collection.update_many(
        {"orders._id" : ObjectId(order_id)},
        {
            "$set" : {"orders.price": new_price}
        })
    
    if order_item.modified_count:
        return True, order_item.modified_count

    return False, 0