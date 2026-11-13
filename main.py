from extractor import extract_all_data
from colored import Fore, Back, Style

def main():
    print("=" * 55)
    print(" REGEX DATA EXTRACTION RESULTS")
    print("=" * 55)

    # Read the raw text from sample_input.txt
    try:
        with open("sample_input.txt", "r", encoding="utf-8") as file:
            raw_text = file.read()
    except FileNotFoundError:
        print("Error: 'sample_input.txt' not found. Make sure it's in the same directory.")
        return

    results = extract_all_data(raw_text)

    for category, matches in results.items():
        formatted_title = category.replace("_", " ").title()
        print(f"\n[{formatted_title}] ({len(matches)} matches found):")
        for item in matches:
            if category == "emails":
                print(f"  - {Fore.blue}{item}{Style.reset}")
            elif category == "urls":
                print(f"  - {Fore.turquoise_4}{item}{Style.reset}")
            elif  category == "phone_numbers":
                print(f"  - {Fore.green}{item}{Style.reset}")
            elif  category == "credit_cards":
                 print(f"  - {Fore.yellow_3a}{item}{Style.reset}")    
            elif  category == "time":
                 print(f"  - {Fore.orange_3}{item}{Style.reset}")
            elif  category == "html_tags":
                print(f"  - {Fore.blue_3a}{item}{Style.reset}")
            elif  category == "hashtags":
                print(f"  - {Fore.dark_red_1}{item}{Style.reset}")
            elif  category == "currency":
                print(f"  - {Fore.dark_green}{item}{Style.reset}")
                 
            else:
                print(f"  - {item}")
                    

if __name__ == "__main__":
    main()