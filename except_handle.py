def except_handle():
    ''' ctrl + d to handle EOF exception and


    ctrl + c to handle KeyboardInterrupt. '''    

    try:
       text = raw_input('Enter something --> ')
    except EOFError:
       # print message for EOF error
       print 'Why did you EOF on me !'
    except KeyboardInterrupt:
       # print message for keyboard interrupt
       print 'Why did you cancel me !'
    else:
       print 'You entered {}'.format(text)                	

# print docstring
print except_handle.__doc__
except_handle()    