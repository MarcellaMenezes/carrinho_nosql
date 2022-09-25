from src.models.order import (
    create_order,
    get_order_by_id,
    delete_order_by_id
)

from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    
    order = {
        "user":{},
        "price": 0.0,
        "paid": False,
        "address": {} 
    }

    id_order = "633090a9cba890a2f3fb6427"
    
    if option == '1':
        # create order
        order = await create_order(order_collection, order)   
    elif option == '2':
        # get order
        order = await get_order_by_id(
            order_collection,
            id_order
        )
        print(order)
        
    elif option == '3':
        result = await delete_order_by_id(order_collection, id_order)
        print(result)

    await disconnect_db()
