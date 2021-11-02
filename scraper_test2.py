
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from google.cloud import storage

def main( ):

    capabilities = webdriver.DesiredCapabilities.CHROME.copy()

    url_one = "https://ca.indeed.com/jobs?q=%22Computer+Forensic+Investigator%22&l=Nova%20Scotia&filter=0&start=0"
    # paste the IP address of the cluster from step 1
    url = "/wd/hub"

    driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=capabilities
    )

    driver.get(url_one)

    html_page = driver.page_source

    print("saving the source page to docker")

    with open("page_source.html", "w") as f:
        f.write(html_page)
    


if __name__ == "__main__":
    main( )
    cwd = os.getcwd()
    arr = os.listdir()
    print(cwd)
    print(arr)
    print("saving the data to google cloud")
    client = storage.Client()
    bucket = client.get_bucket('scraper_ictc')
    blob = bucket.blob('page_source.html')
    blob.upload_from_filename(filename='page_source.html')
    
