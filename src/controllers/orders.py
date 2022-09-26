from src.models.order import (
    create_order,
    get_order_by_id,
    delete_order_by_id,
    update_price_order
)

from src.models.address import (
    get_address_that_is_delivery
)

from src.models.order_item import (
    delete_order_item_by_order_id
)

from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    order_items_collection = db.order_items_collection
    address_collection = db.address_collection
    
    order = {
        "user":{},
        "price": 0.0,
        "paid": False,
        "address": {} 
    }

    email = "marcella@gmail.com"
    id_order = "6330c8d6a2a296dadb408ab1"
    
    if option == '1':
        main_address = await get_address_that_is_delivery(address_collection, email)
        print(main_address)
        if main_address != None:
            order["user"] = main_address['user']
            order["address"] = main_address['address']
        order = await create_order(order_collection, order)   
    elif option == '2':
        # get order
        order = await get_order_by_id(
            order_collection,
            id_order
        )
        print(order)
        
    elif option == '3':
        result = await delete_order_item_by_order_id(order_items_collection, id_order)
        result = await delete_order_by_id(order_collection, id_order)
        print(result)
        
    elif option == '4':
        new_price = 1
        result = await update_price_order(order_collection, id_order, new_price)
        print(result)

    await disconnect_db()
