import greetings

def main():
    print("--- System Login ---")
    
    
    user_name = input("samaelking")
    
    
    message = greetings.generate_greeting(user_name)
    
    
    print(message)

if __name__ == "__main__":
    main()
