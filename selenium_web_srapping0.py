# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

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
        product_description = product.find_element(By.CLASS_NAME, 'inventory_item_desc')  # Find the product description
        product_name = product.find_element(By.CLASS_NAME, 'inventory_item_name')  # Find the product name
        product_price = product.find_element(By.CLASS_NAME, 'inventory_item_price')  # Find the product price
        
        # Create a dictionary to store product information
        product_dict = {
            "Name": product_name.text,
            "Description": product_description.text,
            "Price": product_price.text
        }

        products_list.append(product_dict)  # Add the product information to the list
        time.sleep(1)  # Wait for 1 second before processing the next product

    driver.close()  # Close the WebDriver

    # Create a Pandas DataFrame and save it as a CSV file
    selenium_dataframe = pd.DataFrame(products_list)
    selenium_dataframe.to_csv('Selenium_DataFrame.csv')

    print(selenium_dataframe)
    return products_list

if __name__ == '__main__':
    driver = get_url()  # Open the website
    driver = login(driver)  # Log in
    products = get_text(driver)  # Extract product information
