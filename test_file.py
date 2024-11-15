import re
from playwright.sync_api import Page, expect
from enum import Enum

def test_login_feature(page:Page):

    class Buyer(Enum):
        firstName = 'Alsaggaf'
        lastName = 'Obi'
        postalCode = 20987




    navTitle = "Swag Labs"
    userName = "standard_user"
    userPassword = "secret_sauce"
    item = "Sauce Labs Backpack"
    buttonType = "Add to cart"
    buttonType2 = "Checkout"
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[class="login_logo"]')).to_have_text(navTitle)
    page.locator('[id="user-name"]').fill(userName)
    page.locator('[id="password"]').fill(userPassword)
    page.locator('[id="login-button"]').click()
    # expect(page.locator('[id="inventory_container"]')).to_be_visible()
    expect(page.locator('[id="inventory_container"]').nth(1)).to_be_visible()
    # page.locator('Ok').click()
    productName = page.locator('[data-test="inventory-item"]')
    productLink = page.get_by_role("link",name=item)
    chooseProduct = productName.filter(has=productLink)
    chooseProduct.get_by_role("button", name=buttonType).click()
    shoppingCart = page.locator('[id="shopping_cart_container"]')
    shoppingCart.locator('[class="shopping_cart_link"]').click()
    page.get_by_role("button",name=buttonType2).click()
    # page.pause()
    expect(page.locator('[id="checkout_info_container"]')).to_be_visible()

    page.locator('[id="first-name"]').fill(Buyer.firstName.value)

    page.locator('[id="last-name"]').fill(Buyer.lastName.value)

    page.locator('[id="postal-code"]').fill(str(Buyer.postalCode.value))





# def test_login_feature():
#     with sync_playwright() as p:
#         # Launch the browser in slow motion for easier observation
#         browser = p.chromium.launch(headless=False, slow_mo=300)
#         page = browser.new_page()
        
#         # Navigate to the login page
#         page.goto("https://www.saucedemo.com/inventory.html")
        
#         # Check that the login logo contains "Swag Labs"
#         expect(page.locator('[class="login_logo"]')).to_have_text("Swag Labs")
        
#         # Fill in the username and password fields
#         page.locator('[id="user-name"]').fill('standard_user')
#         page.locator('[id="password"]').fill('secret_sauce')
#         page.locator('[id="login-button"]').click()
#         # Check that the app logo is visible after logging in
#         expect(page.locator('[id="inventory_container"]')).to_be_visible()
        
#         # Close the browser after the test
#         # browser.close()







                 

def test_multiple_order_feature(page: Page):
    # Test data
    nav_title = "Swag Labs"
    user_name = "standard_user"
    user_password = "secret_sauce"
    multiple_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Onesie"]

    # Go to the login page and verify page title
    page.goto("https://www.saucedemo.com/")
    expect(page.locator('.login_logo')).to_have_text(nav_title)

    # Log in to the application
    page.locator('#user-name').fill(user_name)
    page.locator('#password').fill(user_password)
    page.locator('#login-button').click()

    # Verify that the inventory page loads
    # expect(page.locator('#inventory_container')).to_be_visible()

    # Locate all products on the inventory page
    #product_container = page.locator('[data-test="inventory-item"]')

    # Loop over each item in the inventory and add selected items to the cart
    for item_name in multiple_items:
        product_container = page.locator('[data-test="inventory-item"]')
        for i in range(product_container.count()):
            product_name_locator = product_container.nth(i).locator('.inventory_item_name')
            product_name = product_name_locator.text_content()

            # If the product matches an item in multiple_items, add it to the cart
            if product_name == item_name:
                product_container.nth(i).locator('button:has-text("Add to cart")').click()
                break  # Exit inner loop on

            

             
             



    # for i in productCount:
    #     productContainer = page.locator('[data-test="inventory-item"]').filter(has=productName).nth(i)
    #     productInfo =  productContainer.locator('.inventory_item_name').textContent()

    #     if productInfo == "Sauce Labs Backpack":
    #         productContainer.get_by_role("button",name="Add to cart").click()
