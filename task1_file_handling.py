try:
    # Step 4: Open the file in read mode
    with open("sample.txt", "r") as file:
        
        # Step 5: Read and print lines one by one
        for line in file:
            print(line.strip())  # strip() removes trailing newline
except FileNotFoundError:
    # Step 6: Handle file not found error
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    # Step 7: Handle any other unexpected errors
    print("An unexpected error occurred:", e)
