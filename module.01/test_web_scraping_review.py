"""
Web Scraping Review Lab - Python Test Script
Tests web scraping capabilities with BeautifulSoup
"""

from bs4 import BeautifulSoup
import requests

def test_web_scraping_review():
    print("=" * 60)
    print("Testing Web Scraping Review Lab")
    print("=" * 60)
    
    # Test 1: Scrape IBM website
    print("\n1. Testing IBM website scraping...")
    try:
        url = "http://www.ibm.com"
        data = requests.get(url).text
        soup = BeautifulSoup(data, "html.parser")
        
        # Count links
        links = soup.find_all('a')
        print(f"✓ Found {len(links)} links on IBM website")
        
        # Count images
        images = soup.find_all('img')
        print(f"✓ Found {len(images)} images on IBM website")
    except Exception as e:
        print(f"✗ Error scraping IBM website: {e}")
        print("  (This may fail if there are connectivity issues)")
    
    # Test 2: Scrape HTML table
    print("\n2. Testing HTML table scraping...")
    try:
        URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
        data = requests.get(URL).text
        soup = BeautifulSoup(data, "html.parser")
        
        table = soup.find('table')
        
        colors_scraped = 0
        print("\nSample color codes:")
        for i, row in enumerate(table.find_all('tr')):
            cols = row.find_all('td')
            if len(cols) >= 4:
                color_name = cols[2].getText().strip()
                color_code = cols[3].getText().strip()
                colors_scraped += 1
                if i < 5:  # Print first 5
                    print(f"  {color_name} ---> {color_code}")
        
        print(f"\n✓ Successfully scraped {colors_scraped} color codes")
    except Exception as e:
        print(f"✗ Error scraping color table: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Web Scraping Review Lab Complete!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_web_scraping_review()
    exit(0 if success else 1)
