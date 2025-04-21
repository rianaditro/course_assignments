import argparse
import logging
import sys
import requests
import json
import csv
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor, as_completed


logging.basicConfig(level=logging.DEBUG, force=True, filename="book_toscrape.log")

def save_to_file(output:str, filename:str , data:list[dict]) -> None:
    if output == "json":
        with open(f"{filename}.{output}", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    elif output == "csv":
        with open(f"{filename}.{output}", "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    else:
        logging.error("error invalid output file format")
        return
    logging.info("success save to file")


def fetch_page(session, url):
    """ Mengambil halaman dengan session untuk HTTP keep-alive """
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None


def scrape_books(session, base_url, limit):
    """ Scraping daftar buku dari semua halaman """
    data = []
    urls = [base_url if i == 1 else f"{base_url}/catalogue/page-{i}.html" for i in range(1, limit+1)]
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(fetch_page, session, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            html = future.result()
            if html:
                soup = bs(html, 'html.parser')
                books = soup.find_all('article', class_='product_pod')
                for book in books:
                    title = book.h3.a.get_text()
                    price = book.find('p', class_='price_color').get_text()
                    book_url = book.h3.a['href']
                    book_url = f"{base_url}{book_url}" if "/catalogue/" in book_url else f"{base_url}catalogue/{book_url}"

                    data.append({
                        'title': title,
                        'price': price,
                        'book_url': book_url,
                        'cover_image_url': None,
                        'product_description': None,
                        'upc': None,
                        'product_type': None,
                        'price_before_tax': None,
                        'price_after_tax': None,
                        'tax': None,
                        'stock': None,
                        'number_of_reviews': None
                    })
    return data


def scrape_book_details(session, book):
    """ Scraping detail buku untuk satu buku """
    try:
        response = session.get(book['book_url'], timeout=10)
        response.raise_for_status()
        soup = bs(response.text, "html.parser")

        p_tag = soup.find_all('p')
        product_description = p_tag[3].get_text() if len(p_tag) > 3 else "No description"

        img_url = soup.find('img')['src'].replace('../..', book['book_url'])

        table = soup.find('table', class_='table table-striped')
        td_data = table.find_all('td')

        book['product_description'] = product_description
        book['cover_image_url'] = img_url
        book['upc'] = td_data[0].get_text()
        book['product_type'] = td_data[1].get_text()
        book['price_before_tax'] = td_data[2].get_text()
        book['price_after_tax'] = td_data[3].get_text()
        book['tax'] = td_data[4].get_text()
        book['stock'] = td_data[5].get_text().replace('In stock (', '').replace(' available)', '')
        book['number_of_reviews'] = td_data[6].get_text()

        return book
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching details for {book['title']}: {e}")
        return book


def main():
    parser = argparse.ArgumentParser(description='Web Scraping program')
    parser.add_argument('--url', help='URL to scrape', required=True)
    parser.add_argument('--output', help='Output format', choices=['csv', 'json'], default='csv')
    parser.add_argument('--filename', help='Output filename', default='output')
    parser.add_argument('--limit', help='Page limit', type=int, default=1)

    args = parser.parse_args()
    logging.info(f"SCRAPING on URL: {args.url}, OUTPUT: {args.output}, FILENAME: {args.filename}, LIMIT: {args.limit}")

    with requests.Session() as session:
        session.headers.update({'User-Agent': 'Mozilla/5.0'})

        logging.info("START SCRAPING BOOK LIST")
        books = scrape_books(session, args.url, args.limit)
        logging.info(f"SCRAPED {len(books)} BOOKS")

        logging.info("START GETTING BOOK DETAILS")
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(scrape_book_details, session, book): book for book in books}
            for future in as_completed(futures):
                book = future.result()

        logging.info("SAVE TO FILE")
        save_to_file(args.output, args.filename, books)
        logging.info("SCRAPING DONE")


sys.argv = ['script.py', '--url', 'https://books.toscrape.com/', '--output', 'csv', '--filename', 'output', '--limit', '50']

if __name__ == "__main__":
    main()
