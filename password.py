def take_inputs():
    create_or_ret = int(input("Selct an option:\n1.Create\n2.Retrive"))
    if create_or_ret == 1:
        pass_len = int(input("Enter length you need for your password: "))
        num_chars = int(input("Enter no of numeric chars: "))
        spec_chars = int(input("Enter no of special chars: "))
        aplpha_chars = int(input("Enter no of alphs chars: "))
        random_pass = "%$^1YUH2562()"
        display_or_store = int(input("Selct an option:\n1.Display\n2.Store"))
        
take_inputs()