def full_name(fir_name, last_name):
    try:
        if(fir_name.isalpha() == True) and (last_name.isalpha() == True):
            return fir_name + " " +last_name
    except:
        return None

#f_n = "Chenyu"
#l_n = "Song"
#result = full_name(f_n, l_n)
#print("result: ",result)