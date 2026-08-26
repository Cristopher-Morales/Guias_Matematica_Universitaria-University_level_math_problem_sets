def PrintTable(header,n,a,b,x_sol,error):
    print(header)
    print('---------------------------------------------------------')
    for n,a,b,x_sol,error in zip(n,a,b,x_sol,error):
        print('%.0f'%n,'|%.7f'%a,'|%.7f'%b,'|%.7f'%x_sol,'|%.7f'%error)
        print('---------------------------------------------------------')