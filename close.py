from selenium import webdriver
# Define the URL's we will open and a few other variables 
main_url = 'https://www.linkedin.com' # URL A
tab_url = 'https://www.google.com' # URL B
chromedriver = 'DESCTINATION_TO_YOUR_CHROME_DRIVER'
# Open main window with URL A
browser= webdriver.Chrome(chromedriver)
browser.get(main_url)
print("Current Page Title is : %s" %browser.title)
# Open a new window
browser.execute_script("window.open('');")
# Switch to the new window and open URL B
browser.switch_to.window(browser.window_handles[1])
browser.get(tab_url)
# …Do something here
print("Current Page Title is : %s" %browser.title)
# Close the tab with URL B
browser.close()
# Switch back to the first tab with URL A
browser.switch_to.window(browser.window_handles[0])
print("Current Page Title is : %s" %browser.title)