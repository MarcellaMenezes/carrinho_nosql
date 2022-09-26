import asyncio

from src.controllers.users import users_crud
from src.controllers.address import address_crud
from src.controllers.products import products_crud
from src.controllers.orders import orders_crud
from src.controllers.order_items import order_items_crud
# from src.controllers.carrinho import carrinho_crud

loop = asyncio.get_event_loop()
option = input("Insira a sua opcao.\n1 - Usuario\n2 - Endereco\n3 - Produtos\n4 - Pedidos\n5 - Items do Pedido\nR:")

match option:
    case "1":
        loop.run_until_complete(users_crud())
    case "2":
        loop.run_until_complete(address_crud())
    case "3":
        loop.run_until_complete(products_crud())
    case "4":
        loop.run_until_complete(orders_crud())
    case "5":
        loop.run_until_complete(order_items_crud())


