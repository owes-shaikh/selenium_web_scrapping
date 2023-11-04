# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Define the URL of the website
URL = 'https://www.saucedemo.com/v1/'

# Function to open the website and return the driver
def get_url():
    driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    driver.get(URL)  # Navigate to the specified URL
    return driver

# Function to log in to the website
def login(driver):
    login = driver.find_element(By.ID, 'user-name')  # Find the username input field
    login.clear()  # Clear any existing input
    login.send_keys('standard_user')  # Enter the username

    time.sleep(2)  # Wait for 2 seconds

    password = driver.find_element(By.ID, 'password')  # Find the password input field
    password.clear()  # Clear any existing input
    password.send_keys('secret_sauce')  # Enter the password

    time.sleep(2)  # Wait for 2 seconds

    submit_button = driver.find_element(By.ID, 'login-button')  # Find the login button
    submit_button.click()  # Click the login button

    time.sleep(5)  # Wait for 5 seconds for the login to complete

    return driver

# Function to extract product information
def get_text(driver):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")  # Find all product elements
    products_list = []

    for product in products:
        product_description = driver.find_element(By.CLASS_NAME, 'inventory_item_desc')  # Find the product description
        product_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name')  # Find the product name
        product_price = driver.find_element(By.CLASS_NAME, 'inventory_item_price')  # Find the product price
        product_link = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]').get_attribute('href')  # Get the product link

        product_dict = {
            "Name": product_name.text,
            "Description": product_description.text,
            "Price": product_price.text,
            "Link": product_link
        }

        products_list.append(product_dict)  # Add the product information to the list
        time.sleep(1)  # Wait for 1 second before processing the next product

    driver.close()  # Close the WebDriver
    print(products_list)  # Print the list of product information
    return products_list

if __name__ == '__main__':
    driver = get_url()  # Open the website
    driver = login(driver)  # Log in
    products = get_text(driver)  # Extract product information
