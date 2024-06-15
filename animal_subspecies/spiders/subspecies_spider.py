import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

def download_images(query, num_images, output_dir):
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Set the headers to mimic a browser visit
    headers = {
        "User-Agent": "Safari/537.36"
            }
    
    # Format the query for URL encoding
    query = urllib.parse.quote(query)
    
    downloaded = 0
    page = 0
    
    while downloaded < num_images:
        # Construct the Google Image search URL with pagination
        search_url = f"https://www.google.com/search?q={query}&tbm=isch&start={page*20}"
        
        # Get the HTML content of the search page
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image elements
        img_tags = soup.find_all('img')[1:]  # Skip the first image which is usually the Google logo
        
        if not img_tags:
            break
        
        for i, img in enumerate(img_tags):
            if downloaded >= num_images:
                break
            try:
                img_url = img.get('src') or img.get('data-src')
                if not img_url or not img_url.startswith('http'):
                    continue
                img_data = requests.get(img_url).content
                with open(os.path.join(output_dir, f"{query}_{downloaded}.jpg"), 'wb') as handler:
                    handler.write(img_data)
                print(f"Downloaded {query}_{downloaded}.jpg")
                downloaded += 1
            except Exception as e:
                print(f"Could not download image {downloaded}: {e}")
        
        # Increase page count to move to the next set of images
        page += 1
        time.sleep(5)  # Pause to avoid overwhelming the server

# Start the crawling process with error handling

download_images("Turkish Hamster", 1000, "data/Turkish Hamster")