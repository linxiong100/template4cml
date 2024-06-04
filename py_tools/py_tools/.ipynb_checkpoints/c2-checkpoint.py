import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple Hello World command-line tool.")
    parser.add_argument('name', type=str, help='The name to greet')
    args = parser.parse_args()
    
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
