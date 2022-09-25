from src.models.product import (
    create_product,
    get_product_by_id,
    delete_product_by_id
)

from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    product_collection = db.product_collection
    
    product = {
        "name" : "Barra de Chocolate HERSHEY'S Special Dark Menta 60% Cacau - 85g",
        "description" : "O delicioso chocolate Hershey's 60% cacau em um combinação perfeita com a menta, faz deste um dos nossos grandes sucessos. Feito especialmente para todos.",
        "price" : 11.99,
        "image" : "https://static3.tcdn.com.br/img/img_prod/779654/hershey_s_special_dark_sabor_menta_60_cacau_85g_5429_1_20200817134448.jpg",
        "code" : 97882
    }
    
    id_product = "633090a9cba890a2f3fb6427"
    
    if option == '1':
        # create product
        product = await create_product(product_collection, product)   
    elif option == '2':
        # get product
        product = await get_product_by_id(
            product_collection,
            id_product
        )
        print(product)
        
    elif option == '3':
        result = await delete_product_by_id(product_collection, id_product)
        print(result)

    await disconnect_db()
