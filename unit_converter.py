from sys import argv
from final_staging import *

def main():

    if len(argv)==1:
        print(help_message)
        return
    elif argv[1]=="-h":
        print(help_message)
        return
    elif len(argv)==2 or len(argv)>=4:
        print("ERR: incorect number of arguments -> see help")
        print(help_message)
        return
        
    try:
        print(unified_conversion_func_map.get(argv[1],unknown_option_error_string)(float(argv[2])))
        return
    except:
        print("ERR: cannot parse number / unit amount")
        print(help_message)
    
if __name__ == "__main__":
    main()