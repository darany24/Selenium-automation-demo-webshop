#playwright.sync_api is a module in the Playwright library that provides synchronous APIs for browser automation.
#sync_playwright is a function that allows us to use Playwright in a synchronous manner, meaning that the code will wait for each operation to complete before moving on to the next one.
import select
from playwright.sync_api import sync_playwright 
from playwright.sync_api import expect 
#login_page is a module that contains the LoginPage class, which is a Page Object Model (POM) representation of the login page of the application.
from login_page import LoginPage
#re is a module that provides support for regular expressions in Python
import re

def saucedemo_flow():  
    #with is a context manager in python that ensures proper resource management
    with sync_playwright() as p:
        #creating a browser instance
        #brow=p.chromium.launch(channel="msedge",headless=False,slow_mo=100)
        brow = p.firefox.launch(headless=False,slow_mo=100)
        #creating a new browser context and page
        #context represents an fresh browser session, and page represents a single tab within that session
        #isolated browser context allows us to run tests in parallel without interference, as each context has its own cookies, cache, and session storage.
        context =brow.new_context()
        #page opens a new tab in the browser 
        page=context.new_page() 
        #login_pom is an instance of the LoginPage class, which is used to interact with the login page of the application
        login_pom = LoginPage(page)

    #negative login 
    #calling the methods of login page class to perform negative login and validate the error message
        login_pom.goto()
        login_pom.login("standard_", "secret_sauce")
        error_text = login_pom.expect_error_visible()
        print("Negative login error message:", error_text)  
        context.close() 
        
    
    #fresh start
        context=brow.new_context()
        page=context.new_page()
        #login_pom is an instance of the LoginPage class, which is used to interact with the login page of the application
        login_pom = LoginPage(page)

    #positive login
        login_pom.goto() 
        login_pom.expect_password_masked()
        login_pom.login("standard_user","secret_sauce") 
        login_pom.expect_successful_login()  
        expect(page.locator(".inventory_list")).to_be_visible()     
        title=page.title()
        print(title)
            

    #sorting products
        page.locator(".product_sort_container").select_option(index=2)

        price_locator = page.locator("[data-test='inventory-item-price']")

        price_locator.first.wait_for(state="visible",timeout=5000)
        prices_ui = [float(price.text_content().replace("$", ""))for price in price_locator.all()]

        assert prices_ui == sorted(prices_ui), "the prices are not sorted"
        print("prices got sorted successfully")

        searchbar =page.locator("//input[@id='twotabsearchtextbox']").fill("bag")
        contains=page.locator(//div[@class='autocomplete-results-container']).all_text_contents()
        for i in contains:
            if contains.text_content=="bag men"
             contains.is_checked("bag men")
    #first product     
        page.get_by_alt_text("Sauce Labs Backpack").is_visible()
        page.locator("div.inventory_item_name", has_text='Sauce Labs Backpack').click()
        name_item1=page.locator("[data-test='inventory-item-name']").text_content()
        price_item1 = page.locator("[data-test='inventory-item-price']").text_content()
        print("name of the item "+name_item1+ " price = " +price_item1)
        expect(page.get_by_text("Add to cart")).to_be_enabled(timeout=50000)
        page.get_by_text("Add to cart").click()
        page.get_by_role("button",name="Back to products").click()
    #second product
        page.get_by_text("Sauce Labs Fleece Jacket").is_visible()
        page.get_by_text("Sauce Labs Fleece Jacket").click()
        name_item2=page.locator("div.inventory_details_name").text_content()
        price_item2=page.locator("[data-test='inventory-item-price']").text_content()
        print("name of the item "+name_item2+ " price = " +price_item2)
        expect(page.locator("#add-to-cart")).to_be_enabled()
        page.locator("#add-to-cart").click()
        page.get_by_role("button",name="Back to products").click()
    #third product
        page.get_by_text("Sauce Labs Onesie").is_visible()
        locator_item3=page.get_by_alt_text("Sauce Labs Onesie")
        locator_item3.click()
        name_item3=page.locator("div.inventory_details_name").text_content()
        price_item3=page.locator(".inventory_details_price").text_content()
        print("name of the item "+name_item3+ " price = " +price_item3)
        expect(page.locator("#add-to-cart")).to_be_enabled()
        page.locator("#add-to-cart").click()
        page.get_by_role("button",name="Back to products").click()
    #fourth product
        page.get_by_alt_text("Sauce Labs Bolt T-Shirt").is_visible()
        page.get_by_alt_text("Sauce Labs Bolt T-Shirt").click()
        name_item4=page.locator("div.inventory_details_name").text_content()
        price_item4=page.locator(".inventory_details_price").text_content()
        print("name of the item "+name_item4+ " price = " +price_item4)
        expect(page.locator("#add-to-cart")).to_be_enabled()
        page.locator("#add-to-cart").click()
        page.get_by_role("button",name="Back to products").click()
    #navigating to cart
        page.locator("a.shopping_cart_link").click()
        print("Cart quantity before removing an item:  " +page.locator("[data-test='shopping-cart-badge']").text_content())
        expect(page.locator("#remove-sauce-labs-bolt-t-shirt")).to_be_enabled()
        page.click("#remove-sauce-labs-bolt-t-shirt")
        print("Cart quantity after removing an item:  " +page.locator("[data-test='shopping-cart-badge']").text_content())
        page.get_by_role("button",name="Open Menu").click()
    #navigating back to main page
        page.get_by_role("link",name="All Items").click()
    #adding another item to cart
        page.get_by_text("Sauce Labs Bike Light").click()
        name_of_new_item=page.text_content("[data-test='inventory-item-name']")
        price_of_new_item=page.text_content("[data-test='inventory-item-price']")
        expect(page.locator("#add-to-cart")).to_be_enabled()
        page.click("#add-to-cart")
        print("Name of the item " +name_of_new_item +" price = " +price_of_new_item)
        page.get_by_role("button",name="Back to products").click()
    #navigating to cart
    
        expect(page.locator("a.shopping_cart_link")).to_be_enabled()
        page.locator("a.shopping_cart_link").click()
        print("Cart quantity after adding new item:  " +page.locator("[data-test='shopping-cart-badge']").text_content())
    #checkout
        page.click("#checkout")
        page.fill("#first-name","Dharanii")
        page.get_by_role("textbox",name="Last Name").fill("Muniappan")
        page.get_by_placeholder("Zip/Postal Code").fill("638006")   
        continueb=page.get_by_role("button",name="Continue")
        expect(continueb).to_be_enabled()
        page.get_by_role("button",name="Continue").click()
    #price validation
        count_cart_items=page.locator("[data-test='inventory-item-price']").count()
        expect(page.locator("[data-test='inventory-item-price']")).to_have_count(4)
        cart_c=page.locator("[data-test='shopping-cart-badge']").text_content()
        cart_count=int(cart_c)
        assert cart_count==count_cart_items,"the cart quantity and carts product quantity are not same "
        total = 0
        #loops through each item in the cart, extracts the price, and calculates the total price of the items in the cart.
        for i in range(count_cart_items):
            #nth(i) is used to access the specific item in the list of items, and text_content() is used to extract the text content of the price element.
            text_items=page.locator("[data-test='inventory-item-name']").nth(i).text_content()
            price_items=page.locator("[data-test='inventory-item-price']").nth(i).text_content()
            price=float(price_items.replace("$","").strip())
            total=total+price     
        print("Total", total)
        t_tax=page.locator("[data-test='tax-label']").text_content()
        tax=float(re.sub(r"[^0-9.]","",t_tax))
        Item_totalui=page.locator("[data-test='total-label']").text_content()
        total_ui = float(re.sub(r"[^0-9.]","", Item_totalui))
        total_with_tax=total+tax 
        assert total_ui==total_with_tax,"mistake in total"  
        print("Payment_information:  " +page.locator("[data-test='payment-info-value']").text_content())
        print("Shipping_information:  " +page.locator("[data-test='shipping-info-value']").text_content())
        print("Total with tax=  ", total_with_tax)
        expect(page.locator("#finish")).to_be_enabled()
        page.locator("button:has-text('Finish')").click()
        success_msg=page.locator(".complete-header")
        expect(success_msg).to_have_text("Thank you for your order!")
        expect(page.locator(".complete-text")).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
        print(success_msg.text_content())
        page.get_by_role("button",name="Back Home").click()

#if the script is run directly, the name variable will be set to "__main__", 
# and the saucedemo_flow function will be called to execute the test flow.
if __name__ == "__main__":
    #calling the main function to execute the test flow
    saucedemo_flow()

