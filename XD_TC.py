"""
MIT License
Copyright (c) [2024] [XD TEAM]

@XDrobotch - @yeh_XD
"""
from colorama import init, Fore, Style
import requests
import os

if __name__ == '__main__':
    init()

    def main_menu():
        # Logo script
        print(Fore.RED+r""" 
    ____  _________     ________      
    __  |/ /__  __ \    ___  __/______
    __    /__  / / /    __  /  _  ___/
    _    | _  /_/ /     _  /   / /__  
    /_/|_| /_____/      /_/    \___/

    XD Token Cracker 3.0"""+Fore.YELLOW+"""

    • Choose an option:"""+Fore.CYAN+"""
     [1] Start Crack
     [2] Exit
    """)
        try:
            choice = input(Fore.RESET+"Enter your choice (1-2): ")
            if choice == "1":
                Crack_menu()
            elif choice == "2":
                print(Fore.RED +" OK, the tool is closed", end="")
                return
        except KeyboardInterrupt:
            print(Fore.RED +"Error executing the script")
            return
    
    def Crack_menu():
        print_count = 0

        while True:
            print(Fore.YELLOW + r""" Submit your command below:""" + Fore.CYAN + """
            parameters:
              t_in  = Token list (txt)
              t_out = Token output
            Sample : 
              t_in=tokenlist.txt-t_out=output.txt
            """)

            try:
                user_input = input(Fore.RESET + "your command : ")

                if "-" not in user_input:
                    print(Fore.RED + "The input format is incorrect. Must be separated by -.")
                    continue

                t_in, t_out = user_input.split("-")

                if "=" not in t_in or "=" not in t_out:
                    print(Fore.RED + "The input format is incorrect. It should be in the form of t_in=filename.txt-t_out=filename.txt.")
                    continue

                url = 'https://api.telegram.org/bot{}/getMe'

                t_in_string = t_in.split("=")[0]
                t_out_string = t_out.split("=")[0]

                t_in_filename = t_in.split("=")[1]
                t_out_filename = t_out.split("=")[1]
    
                t_in_format = os.path.splitext(t_in_filename)[1]
                t_out_format = os.path.splitext(t_out_filename)[1]
    
                if t_in_string != "t_in" and t_out_string != "t_out":
                    print(Fore.RED + "The input format is incorrect. It should be in the form of t_in=filename.txt-t_out=filename.txt.")
                    continue
                
                if t_in_format != ".txt" and t_out_format != ".txt":
                    print(Fore.RED + "The format of the input files is not correct (they must be txt)")
                    continue
                
                if not os.path.isfile(t_in_filename):
                    print(Fore.RED + f"We could not find your list token file, File name: {t_in_filename}")
                    continue
                
                if os.path.isfile(t_out_filename):
                    os.remove(t_out_filename)
    
                if print_count == 0:

                    true_tokens = 0
                    false_tokens = 0
    
                    with open(t_in_filename, 'r') as f:
                        tokens = f.readlines()
    
                    for token in tokens:
                        token = token.strip()
                        response = requests.get(url.format(token))
                        if response.status_code == 200:
                            result = response.json()
                            if result['ok']:
                                with open(t_out_filename, 'a') as output_file:
                                    output_file.write(token + '\n')
                                true_tokens += 1
                                print(Fore.GREEN + f"  [+] True  : {token}")
                            else:
                                false_tokens += 1
                                print(Fore.RED + f"  [-] False : {token}")
                        else:
                            false_tokens += 1
                            print(Fore.RED + f"  [-] False : {token}")
    
                    all_tokens = true_tokens + false_tokens
    
                    print(Fore.GREEN + "\n The operation was completed successfully \n    " + Fore.RESET + f"Number of tokens: {all_tokens} \n    Correct tokens: {true_tokens} \n    Broken tokens: {false_tokens} \n   ")
                    break
                
                break
            
            except FileNotFoundError:
                print(Fore.RED + f"Input file not found: {t_in_filename}")
            except PermissionError:
                print(Fore.RED + "Insufficient permissions to access the files.")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Network error: {e}")
            except Exception as e:
                print(Fore.RED + f"An unexpected error occurred: {e}")

    main_menu()