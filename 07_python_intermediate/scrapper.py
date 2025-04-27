import sys
import argparse

def main() -> None:
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A simple web scraper.")

    # Add an argument for the target URL
    parser.add_argument("--url", required=True, help="The URL to scrape")

    # Parse the arguments
    args = parser.parse_args()

    # Access the URL argument
    print(f"Scraping URL: {args.url}")

if __name__ == "__main__":
    main()
