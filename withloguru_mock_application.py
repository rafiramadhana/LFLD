from loguru import logger
import sys
import random
from time import sleep

logger.remove()
logger.add(sys.stdout, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
logger.add("lfld.log", serialize=True)

books = [
    "Harry Potter and the Prisoner of Azkaban",
    "Tangkaplah Daku Kau Kujitak",
    "Narnia"
]

def main():
    rd = random.randint(0, 100)
    if rd < 30:
        check_book_availability()
    else:
        add_book_to_wishlist()

def check_book_availability():
    lg = logger.bind(service="warehouse_service")
    rd = random.randint(0, 100)
    book = books[rd%3]
    lg = lg.bind(book_name=book)
    if rd < 30:
        lg.debug(f'{book} is available')
    else:
        err_msg = f'{book} is not available'
        lg = lg.bind(error=err_msg)
        lg.error(f'Fail to check book availability: {err_msg}')

def add_book_to_wishlist():
    lg = logger.bind(service="whitelist_service")
    rd = random.randint(0, 100)
    book = books[rd%3]
    lg = lg.bind(book_name=book)
    if rd < 30:
        lg.debug(f'{book} is added to whitelist')
    else:   
        err_msg = "whitelist is full"
        lg = lg.bind(error=err_msg)
        lg.error(f'Fail to add book to whitelist: {err_msg}')
        

if __name__ == "__main__":
    for _ in range(0,30):
        sleep(30/1000)
        main()