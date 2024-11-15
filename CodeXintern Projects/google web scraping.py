import requests
from bs4 import BeautifulSoup
import urllib.parse

def google_search(query, num_results):
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"  # Updated User-Agent
    }
    params = {
        "q": query,
        "num": num_results
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch results. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []


    for result in soup.select(".tF2Cxc"):
        title = result.select_one("h3")
        link = result.select_one("a")
        description = result.select_one(".VwiC3b")

        if title and link and description:
            results.append({
                      "title": title.get_text(),
                      "link": link["href"],
                      "description": description.get_text()
            })
    if not results:
        print("No results found.")


    return results

# Example usage
query = input("Enter your search query: ")
num_results = int(input("Enter the number of results to fetch: "))
results = google_search(query, num_results)


for idx, result in enumerate(results, start=1):
    print(f"{idx}. Title: {result['title']}")
    print(f"   Link: {result['link']}")
    print(f"  Description: {result['description']}\n")