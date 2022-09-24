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
                #buscar endereco
                print(address)
                return address
        else:
            
            address = await address_collection.update_one(
                {"_id" : address["_id"]},
                {
                    "$addToSet" : {
                        "address": new_address[0]
                    }
                })
            
    except Exception as e:
        print(f'create_address.error: {e}')
        
async def get_address_by_user_id(address_collection, user_id):
    try:
        data = await address_collection.find_one({'user._id': ObjectId(user_id)})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')


async def delete_addres_by_id(address_collection, address_id):
    ...
