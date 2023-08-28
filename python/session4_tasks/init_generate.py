
ls = []
for i in range(0,8):
    mode = str(input (f"enter Bit {i} mode: "))
    
    if mode == "in" :
        ls.append('0')
    elif mode == 'out':
        ls.append('1')

ls.reverse()
ls=''.join(ls)
f = open("init.c",'x')
f.write("void Init_porta_dir(void)\n")
f.write(" { \n    DDRA = 0b"+ls + '; \n }')
#f.write('}')
f.close()
            
    
