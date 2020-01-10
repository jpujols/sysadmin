from tkinter import *

#Header - Menu Buttons
root = Tk()
menu = Menu(root)
root.config(menu=menu)
#SCAN Dropdown Menu
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Import')
filemenu.add_command(label='Export')

#Line Separator to last item under SCAN dropdown menu
filemenu.add_separator()
#EXIT Drop
filemenu.add_command(label='Exit', command=root.quit)

#NETWORK Dropdown Menu
networkmenu = Menu(menu)
menu.add_cascade(label='Network', menu=networkmenu)
networkmenu.add_command(label='Ping')
networkmenu.add_command(label='ARP')
networkmenu.add_command(label='VLAN')
networkmenu.add_command(label='SysInfo')

#AWS Dropdown Menu
awsmenu = Menu(menu)
menu.add_cascade(label='AWS', menu=awsmenu)
awsmenu.add_command(label='EC2')
awsmenu.add_command(label='S3')
awsmenu.add_command(label='Health')
awsmenu.add_command(label='Usage')

#Monitor Dropdown Menu
monitormenu = Menu(menu)
menu.add_cascade(label='Status', menu=monitormenu)
monitormenu.add_command(label='Web Apps')
monitormenu.add_command(label='Servers')
monitormenu.add_command(label='Routers')
monitormenu.add_command(label='Switches')

#HELP tab in the dropdown Menu
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#SysAdmin Dropdown Menu
sysadminmenu = Menu(menu)
menu.add_cascade(label='SysAdmin', menu=sysadminmenu)
sysadminmenu.add_command(label='AD Schema')
sysadminmenu.add_command(label='Permissions')
sysadminmenu.add_command(label='Groups')
sysadminmenu.add_command(label='AD Users')

#widets
var1 = IntVar()
Checkbutton(sysadminmenu, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(sysadminmenu, text='female', variable=var2).grid(row=1, sticky=W)


sysadminmenu.add_command(label='AD Audit')
sysadminmenu.add_command(label='DNS')

mainloop()

