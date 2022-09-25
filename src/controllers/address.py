from src.models.address import (
    create_address,
    get_address_by_user_id,
    delete_address_by_id
)

from src.models.user import(
    get_user_by_email
)

from src.server.database import connect_db, db, disconnect_db


async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    users_collection = db.users_collection
    address_collection = db.address_collection
    
    address = [{
                "street": "Rua dos Pedras, Numero 0",
                "cep": "8465312",
                "district": "São Paulo",
                "city": "São Paulo",
                "state": "São Paulo",
                "is_delivery": True
            }]
    
    email = "marcella@gmail.com"
    id_user = "632f647bc186b86c9796e48a"
    id_address = "632f80a80b546aebcf15fbfa"
        

    if option == '1':
        # create address for user
        #email = input("Digite o e-mail do usuario: ")
        user = await get_user_by_email(users_collection, email)
        if user != None:
            address = await create_address(address_collection, user, address)   
            
    elif option == '2':
        # get user
        address = await get_address_by_user_id(
            address_collection,
            id_user
        )
        print(address)
        
    elif option == '3':
        result = await delete_address_by_id(address_collection, id_address)
        print(result)

    await disconnect_db()
