import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-commerce Product Scraper")
        self.root.geometry("400x200")

        self.url_label = tk.Label(root, text="Enter Flipkart Search URL:")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        self.scrape_button = tk.Button(root, text="Scrape Products", command=self.scrape_and_save)
        self.scrape_button.pack(pady=10)

    def scrape_and_save(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding  # Ensure response is handled as UTF-8
            soup = BeautifulSoup(response.text, 'html.parser')

            products = []
            for product in soup.find_all('a', class_='CGtC98'):
                name_tag = product.find('div', class_='KzDlHZ')
                price_tag = product.find('div', class_='Nx9bqj _4b5DiR')
                rating_tag = product.find('div', class_='XQDdHH')

                if name_tag and price_tag:
                    name = name_tag.text.strip()
                    # Handle price formatting
                    price_text = price_tag.text.strip()
                    price = ''.join(filter(str.isdigit, price_text))  # Extract only digits

                    rating = rating_tag.text.strip() if rating_tag else 'No rating'

                    products.append({
                        'Name': name,
                        'Price': price,
                        'Rating': rating
                    })

            if products:
                self.save_to_csv(products)
                messagebox.showinfo("Success", "Products scraped and saved to 'products.csv'.")
            else:
                messagebox.showinfo("No Products", "No products found on the page.")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error scraping data: {str(e)}")

    def save_to_csv(self, products):
        with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow(product)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
