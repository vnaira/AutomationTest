from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(driver):

    login = LoginPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
        """ 
        comment
         """
    )

    inventory = InventoryPage(driver)

    assert inventory.get_title() == "Products"
