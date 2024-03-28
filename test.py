from selenium import webdriver
from selenium. webdriver.chrome.service import Service
from selenium. webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

<<<<<<< HEAD
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service (ChromeDriverManager().install()),
                          options=options)
                                                                       
driver.get("http://127.0.0.1:8000/createposts")
=======
driver = webdriver.Chrome()
>>>>>>> 6b34438a7cab788745049dafd2732326dd262563



baho kag igit