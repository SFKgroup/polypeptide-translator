import tkinter as tk
import encode
def run():
    res = encode.encoding(datain.get())
    tdna.set('DeoxyriboNucleic Acid:' +  str(res['DeoxyriboNucleic Acid'][0]))
    tsdna.set('                      '+  str(res['DeoxyriboNucleic Acid'][1]))
    tmrna.set('Messenger Ribonucleic Acid:' + str(res['Messenger Ribonucleic Acid']))
    tpr.set('polypeptide:' +   str(res['polypeptide']))
    tchem.set('Chemical formula:' + str(res['Chemical formula']))

root = tk.Tk()
root.title('IP Find')
root.geometry('680x400')
try:root.iconbitmap('./icon/favicon.ico')
except:pass
ttitle = tk.StringVar()
ttitle.set('IP Find')
tk.Label(root, textvariable=ttitle,bd=5,font=('consolas',30)).pack(side=tk.TOP)

tdna = tk.StringVar()
tdna.set('DeoxyriboNucleic Acid      :')
tk.Label(root, textvariable=tdna ,bd=5,font=('consolas',20)).pack(side=tk.TOP)
tsdna = tk.StringVar()
tsdna.set('                      ')
tk.Label(root, textvariable=tsdna ,bd=5,font=('consolas',20)).pack(side=tk.TOP)
tmrna = tk.StringVar()
tmrna.set('Messenger Ribonucleic Acid :')
tk.Label(root, textvariable=tmrna,bd=5,font=('consolas',20)).pack(side=tk.TOP)
tpr = tk.StringVar()
tpr.set('polypeptide                :')
tk.Label(root, textvariable=tpr  ,bd=5,font=('consolas',20)).pack(side=tk.TOP)
tchem = tk.StringVar()
tchem.set('Chemical formula           :')
tk.Label(root, textvariable=tchem,bd=5,font=('consolas',20)).pack(side=tk.TOP)

datain = tk.StringVar()
tk.Label(root, text="Text:",bd=5,font=('consolas',20)).pack(side=tk.LEFT)
tk.Entry(root,textvariable=datain,font=('consolas',20), width = 30).pack(side=tk.LEFT)
tk.Button(root,text='Encode',command=run,width=14).pack(side=tk.LEFT)

root.mainloop()