import json
import sys 

def main():
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    json_file = open(input_file_path, "r")
    data = json.load(json_file)
    output_file = open(output_file_path, "w+")
    for entry in data:
        output_file.write(entry["domain"] + "\n")
        print(entry["domain"])

if __name__ == "__main__":
    main()