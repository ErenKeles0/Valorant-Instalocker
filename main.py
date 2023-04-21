import valclient
import tkinter as tk
import time


root=tk.Tk()
root.geometry("500x600")





reyna="a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"
jett="add6443a-41bd-e414-f6ad-e58d267f4e95"
cypher="117ed9e3-49f3-6512-3ccf-0cada7e3823b"
raze="f94c3b30-42be-e959-889c-5aa313dba261"
neon="bb2a4828-46eb-8cd1-e765-15848195d751"
chamber="22697a3d-45bf-8dd7-4fec-84a9e28c69d7"
yoru="7f94d92c-4234-0a36-9646-3a87eb8b5c89"
pho="eb93336a-449b-9c1b-0a54-a891f7921d69"


client = valclient.Client(region="eu")
client.activate()







while True:
    try:
        x=client.pregame_fetch_match()
        break
    except:
        print("Maç Bekleniyor")
        time.sleep(2)
        continue





def jettagentselect():
    client.pregame_lock_character(jett)
def reynaagentselect():
    client.pregame_lock_character(reyna)
def cypheragentselect():
    client.pregame_lock_character(cypher)
def razeagentselect():
    client.pregame_lock_character(raze)
def neonagentselect():
    client.pregame_lock_character(neon)
def chamberagentselect():
    client.pregame_lock_character(chamber)
def yoruagentselect():
    client.pregame_lock_character(yoru)
def phoagentselect():
    client.pregame_lock_character(pho)







jettbutton=tk.Button(text="Jett",command=jettagentselect,font="Verdana 28")
jettbutton.pack()
reynabutton=tk.Button(text="Reyna",command=reynaagentselect,font="Verdana 28")
reynabutton.pack()
reynabutton=tk.Button(text="Cypher",command=cypheragentselect,font="Verdana 28")
reynabutton.pack()
reynabutton=tk.Button(text="Raze",command=razeagentselect,font="Verdana 28")
reynabutton.pack()
reynabutton=tk.Button(text="Neon",command=neonagentselect,font="Verdana 28")
reynabutton.pack()
reynabutton=tk.Button(text="Chamber",command=chamberagentselect,font="Verdana 28")
reynabutton.pack()
reynabutton=tk.Button(text="Yoru",command=yoruagentselect,font="Verdana 28")
reynabutton.pack()
reynabutton=tk.Button(text="Pho",command=phoagentselect,font="Verdana 28")
reynabutton.pack()





root.mainloop()

