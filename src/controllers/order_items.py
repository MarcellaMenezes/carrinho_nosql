from src.models.order_item import (
    create_order_item,
    get_order_item_by_id,
    delete_order_item_by_id,
    update_price_order_item
)

from src.models.order import (
    get_order_by_id,
    update_price_order
)

from src.models.product import (
    get_product_by_id
)

from src.server.database import connect_db, db, disconnect_db

async def order_items_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    order_items_collection = db.order_items_collection
    product_collection = db.product_collection
    
    
    order_items = {
        "orders": {},
        "products": {}
    }
    
    id_order = "6330c8d6a2a296dadb408ab1"
    id_product = "6330e8c60f0a24e1645c4d10"
    id_order_item = "6330ffafd24640bbd7f0dd32"
    
    if option == '1':
        order = await get_order_by_id(order_collection, id_order)
        product =await get_product_by_id(product_collection, id_product)
   
        if order != None and product != None:
            order_items["orders"] = order
            order_items["products"] = product
            
            result = await create_order_item(order_items_collection, order_items) 
            
            #Atualizando o valor total do carrinho
            new_price = order["price"] + product["price"]
            
            if result != None:
                result = await update_price_order(order_collection, id_order, new_price)
                result = await update_price_order_item(order_items_collection, id_order, new_price)
        
    elif option == '2':
        # get order
        main_address = await get_order_item_by_id(order_items_collection, id_order_item)
        print(main_address)
        
    elif option == '3':
        order_item = await get_order_by_id(order_items_collection, id_order_item)
        if order_item != None:
            result = await delete_order_item_by_id(order_items_collection, id_order_item)
            new_price =  order_item["orders"]["price"] - order_item["products"]["price"]
        
            if result != None:
                result = await update_price_order(order_collection, id_order, new_price)
                result = await update_price_order_item(order_items_collection, id_order, new_price)
        

    await disconnect_db()
