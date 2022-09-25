from bson.objectid import ObjectId

async def create_address(address_collection, user, new_address):
    try:
       
        address = await get_address_by_user_id(
            address_collection,
            user["_id"]
        )
        
        if address == None:       
            address = await address_collection.insert_one({
                    "user" : user,
                    "address": new_address
                })
            if address.inserted_id:
                print(address)
                return address
            
        else:
            #Todo novo endereço irá nascer como delivery false
            new_address[0]["is_delivery"] = False
            address = await address_collection.update_one(
                {"_id" : address["_id"]},
                {
                    "$addToSet" : {
                        "address": new_address[0]
                    }
                }) 
            if address.modified_count:
                return True, address.modified_count

            return False, 0
                 
    except Exception as e:
        print(f'create_address.error: {e}')
        
async def get_address_by_user_id(address_collection, user_id):
    try:
        data = await address_collection.find_one({'user._id': ObjectId(user_id)})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')
        

async def delete_address_by_id(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': ObjectId(address_id)}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')
        
async def get_address_that_is_delivery(address_collection, user_email):
    try:   
        lista = []
        async for user in address_collection.aggregate ([
            {
                "$match":{
                    "user.email": "marcella@gmail.com",
                    "user.is_active": True
                }
            },
            {
                "$unwind": '$address'
            },
            {
                "$match": {
                        'address.is_delivery':True
                    }
            }
        ]): 
            lista.append(user)
        
        print(lista)
        # if data:
        #     return data
    except Exception as e:
        print(f'get_address_delivery.error: {e}')