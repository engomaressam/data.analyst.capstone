"""
Web Scraping Lab - Python Test Script
Scrapes programming language salary data from a webpage
"""

from bs4 import BeautifulSoup
import requests
import csv

def test_web_scraping():
    print("=" * 60)
    print("Testing Web Scraping Lab")
    print("=" * 60)
    
    # URL containing the data
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
    
    # Step 1: Download the webpage
    print("\n1. Downloading webpage...")
    try:
        data = requests.get(url).text
        print("✓ Webpage downloaded successfully")
    except Exception as e:
        print(f"✗ Error downloading webpage: {e}")
        return False
    
    # Step 2: Create soup object
    print("\n2. Creating soup object...")
    try:
        soup = BeautifulSoup(data, 'html.parser')
        print("✓ Soup object created successfully")
    except Exception as e:
        print(f"✗ Error creating soup object: {e}")
        return False
    
    # Step 3: Scrape language names and salaries
    print("\n3. Scraping language names and salaries...")
    try:
        table = soup.find('table')
        
        languages = []
        salaries = []
        
        for row in table.find_all('tr'):
            # Try to find td tags first
            cols = row.find_all('td')
            # Skip header rows
            if not cols:
                continue
            if len(cols) >= 2:
                language = cols[0].getText().strip()
                salary = cols[1].getText().strip()
                # Skip empty rows
                if language and salary:
                    languages.append(language)
                    salaries.append(salary)
        
        print(f"✓ Scraped {len(languages)} programming languages")
        print("\nSample data:")
        for i in range(min(5, len(languages))):
            print(f"  {languages[i]}: {salaries[i]}")
    except Exception as e:
        print(f"✗ Error scraping data: {e}")
        return False
    
    # Step 4: Save to CSV
    print("\n4. Saving data to popular-languages.csv...")
    try:
        with open('popular-languages.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Language', 'Average Annual Salary'])
            for i in range(len(languages)):
                writer.writerow([languages[i], salaries[i]])
        print("✓ Data saved successfully to popular-languages.csv")
    except Exception as e:
        print(f"✗ Error saving CSV: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Web Scraping Lab Complete!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_web_scraping()
    exit(0 if success else 1)
