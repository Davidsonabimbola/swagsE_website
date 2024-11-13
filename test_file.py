import re
from playwright.sync_api import Page, expect

def test_login_feature(page:Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[class="login_logo"]')).to_have_text("Swag Labs")
    page.locator('[id="user-name"]').fill('standard_user')
    page.locator('[id="password"]').fill('secret_sauce')
    page.locator('[id="login-button"]').click()
    # expect(page.locator('[id="inventory_container"]')).to_be_visible()
    expect(page.locator('[id="inventory_container"]').nth(1)).to_be_visible()
    # page.locator('Ok').click()
    productName = page.locator('[data-test="inventory-item"]')
    productLink = page.get_by_role("link",name="Sauce Labs Backpack")
    chooseProduct = productName.filter(has=productLink)
    chooseProduct.get_by_role("button", name="Add to cart").click()
    page.pause()




   

# from playwright.sync_api import sync_playwright

# def test_has_title():
#     with sync_playwright() as p:
#         # Launch the browser in slow motion with a delay of 100 milliseconds
#         browser = p.chromium.launch(headless=False, slow_mo=300)
#         page = browser.new_page()
        
#         page.goto("https://www.saucedemo.com/inventory.html")
#         page.locator('[class="login_logo"]').wait_for()  # Ensure element loads
#         page.locator('[id="user-name"]').fill('standard_user')
#         page.locator('[id="password"]').fill('secret_sauce')
#         page.locator('[id="login-button"]').click()
#         expect(page.locator('[id="inventory_container"]')).to_be_visible()
#         page.pause()
        

        
            
        # for i in range(4):
        #     page.locator('[id="login-button"]').click()

        
        # browser.close()



        # from playwright.sync_api import sync_playwright, expect

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

