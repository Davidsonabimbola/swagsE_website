import re
# from playwright.sync_api import expect

# def test_has_title(page):
#     page.goto("https://www.saucedemo.com/inventory.html")
#     expect(page.locator('[class="login_logo"]')).to_have_text("Swag Labs")
#     page.locator('[id="user-name"]').fill('standard_user')
#     page.locator('[id="password"]').fill('secret_sauce')



   

from playwright.sync_api import sync_playwright

def test_has_title():
    with sync_playwright() as p:
        # Launch the browser in slow motion with a delay of 100 milliseconds
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com/inventory.html")
        page.locator('[class="login_logo"]').wait_for()  # Ensure element loads
        page.locator('[id="user-name"]').fill('standard_user')

        
            
        # for i in range(4):
        #     page.locator('[id="login-button"]').click()

        
        browser.close()
