import sys, time
indent = 0
indentincreases = True 
try:
    while True:
         print(' '*indent + '******')
    time.sleep(0.1)
    if indentincreases:
        indent = indent + 1
        if indent == 20:
            indentincreases = False
     else:
        indent = indent - 1
        if indent == 0:
            indentincreases = True
except KeyboardInterrupt:
    sys.exit()
       
        
  


