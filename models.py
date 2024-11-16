# from playwright.sync_api import Page, expect

# class PlaceOrder:
#     def __init__(self, page):
#         self.page = page
#         #self.search_term_input = page.locator('[aria-label="Enter your search term"]')

#     def navigate(self,navTitle):
#         self.page.goto("https://www.saucedemo.com/inventory.html")
#         expect(self.page.locator('[class="login_logo"]')).to_have_text(navTitle)
       
#     def search(self, userName,userPassword,item,buttonType,buttonType2,Buyer_FirstName,Buyer_LastName,Buyer_PostalCode):
      


#         self.page.locator('[id="user-name"]').fill(userName)
#         self.page.locator('[id="password"]').fill(userPassword)
#         self.page.locator('[id="login-button"]').click()
    
#         expect(self.page.locator('[id="inventory_container"]').nth(1)).to_be_visible()
   
#         productName = self.page.locator('[data-test="inventory-item"]')
#         productLink = self.page.get_by_role("link",name=item)
#         chooseProduct = productName.filter(has=productLink)
#         chooseProduct.get_by_role("button", name=buttonType).click()
#         shoppingCart = self.page.locator('[id="shopping_cart_container"]')
#         shoppingCart.locator('[class="shopping_cart_link"]').click()
#         self.page.get_by_role("button",name=buttonType2).click()
#     # page.pause()
#         expect(self.page.locator('[id="checkout_info_container"]')).to_be_visible()

#         self.page.locator('[id="first-name"]').fill(Buyer_FirstName)

#         self.page.locator('[id="last-name"]').fill(Buyer_LastName)

#         self.page.locator('[id="postal-code"]').fill(str(Buyer_PostalCode))







from playwright.sync_api import Page, expect

class PlaceOrder:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, nav_title: str):
        """Navigate to the inventory page and verify the title."""
        self.page.goto("https://www.saucedemo.com/inventory.html")
        expect(self.page.locator('[class="login_logo"]')).to_have_text(nav_title)

    def login(self, username: str, password: str):
        """Log in to the application."""
        self.page.locator('[id="user-name"]').fill(username)
        self.page.locator('[id="password"]').fill(password)
        self.page.locator('[id="login-button"]').click()

        # Verify successful login by checking visibility of inventory container
        expect(self.page.locator('[id="inventory_container"]').nth(1)).to_be_visible()

    def search_and_add_to_cart(self, item: str, button_type: str):
        """Search for an item and add it to the cart."""
        product_name = self.page.locator('[data-test="inventory-item"]')
        product_link = self.page.get_by_role("link", name=item)
        choose_product = product_name.filter(has=product_link)
        choose_product.get_by_role("button", name=button_type).click()

    def proceed_to_checkout(self, button_type: str, first_name: str, last_name: str, postal_code: str):
        """Proceed to checkout and fill buyer information."""
        # Go to the shopping cart
        shopping_cart = self.page.locator('[id="shopping_cart_container"]')
        shopping_cart.locator('[class="shopping_cart_link"]').click()

        # Click the checkout button
        self.page.get_by_role("button", name=button_type).click()

        # Verify the checkout information container is visible
        expect(self.page.locator('[id="checkout_info_container"]')).to_be_visible()

        # Fill in buyer details
        self.page.locator('[id="first-name"]').fill(first_name)
        self.page.locator('[id="last-name"]').fill(last_name)
        self.page.locator('[id="postal-code"]').fill(str(postal_code))
