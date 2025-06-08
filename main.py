import valclient
import tkinter as tk
import time


root=tk.Tk()
root.geometry("830x600")
icon = tk.PhotoImage(file="https://img.icons8.com/?size=100&id=4e6jaJRUzaF9&format=png&color=000000") 
root.iconphoto(True, icon) 
root.title("Valorant Instalocker")

gekko = "e370fa57-4757-3604-3648-499e1f642d3f"
fade = "dade69b4-4f5a-8528-247b-219e5a1facd6"
breach = "5f8d3a7f-467b-97f3-062c-13acf203c006"
deadlock = "cc8b64c8-4b25-4ff9-6e7f-37b4da43d235"
tejo = "b444168c-4e35-8076-db47-ef9bf368f384"
raze = "f94c3b30-42be-e959-889c-5aa313dba261"
chamber = "22697a3d-45bf-8dd7-4fec-84a9e28c69d7"
kayo = "601dbbe7-43ce-be57-2a40-4abd24953621"
skye = "6f2a04ca-43e0-be17-7f36-b3908627744d"
cypher = "117ed9e3-49f3-6512-3ccf-0cada7e3823b"
sova = "320b2a48-4d9b-a075-30f1-1f93a9b638fa"
killjoy = "1e58de9c-4950-5125-93e9-a0aee9f98746"
harbor = "95b78ed7-4637-86d9-7e41-71ba8c293152"
vyse = "efba5359-4016-a1e5-7626-b1ae76895940"
viper = "707eab51-4836-f488-046a-cda6bf494859"
phoenix = "eb93336a-449b-9c1b-0a54-a891f7921d69"
astra = "41fb69c1-4189-7b37-f117-bcaf1e96f1bf"
brimstone = "9f0d8ba9-4140-b941-57d3-a7ad57c6b417"
iso = "0e38b510-41a8-5780-5e8f-568b2a4f2d6c"
clove = "1dbf2edd-4729-0984-3115-daa5eed44993"
neon = "bb2a4828-46eb-8cd1-e765-15848195d751"
yoru = "7f94d92c-4234-0a36-9646-3a87eb8b5c89"
waylay = "df1cb487-4902-002e-5c17-d28e83e78588"
sage = "569fdd95-4d10-43ab-ca70-79becc718b46"
reyna = "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"
omen = "8e253930-4c05-31dd-1b6c-968525494517"
jett = "add6443a-41bd-e414-f6ad-e58d267f4e95"


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



def gekkoagentselect():
    client.pregame_lock_character(gekko)

def fadeagentselect():
    client.pregame_lock_character(fade)

def breachagentselect():
    client.pregame_lock_character(breach)

def deadlockagentselect():
    client.pregame_lock_character(deadlock)

def tejoagentselect():
    client.pregame_lock_character(tejo)

def razeagentselect():
    client.pregame_lock_character(raze)

def chamberagentselect():
    client.pregame_lock_character(chamber)

def kayoagentselect():
    client.pregame_lock_character(kayo)

def skyeagentselect():
    client.pregame_lock_character(skye)

def cypheragentselect():
    client.pregame_lock_character(cypher)

def sovaagentselect():
    client.pregame_lock_character(sova)

def killjoyagentselect():
    client.pregame_lock_character(killjoy)

def harboragentselect():
    client.pregame_lock_character(harbor)

def vyseagentselect():
    client.pregame_lock_character(vyse)

def viperagentselect():
    client.pregame_lock_character(viper)

def phoenixagentselect():
    client.pregame_lock_character(phoenix)

def astraagentselect():
    client.pregame_lock_character(astra)

def brimstoneagentselect():
    client.pregame_lock_character(brimstone)

def isoagentselect():
    client.pregame_lock_character(iso)

def cloveagentselect():
    client.pregame_lock_character(clove)

def neonagentselect():
    client.pregame_lock_character(neon)

def yoruagentselect():
    client.pregame_lock_character(yoru)

def waylayagentselect():
    client.pregame_lock_character(waylay)

def sageagentselect():
    client.pregame_lock_character(sage)

def reynaagentselect():
    client.pregame_lock_character(reyna)

def omenagentselect():
    client.pregame_lock_character(omen)

def jettagentselect():
    client.pregame_lock_character(jett)








buttons = [
    ("Gekko", gekkoagentselect),
    ("Fade", fadeagentselect),
    ("Breach", breachagentselect),
    ("Deadlock", deadlockagentselect),
    ("Tejo", tejoagentselect),
    ("Raze", razeagentselect),
    ("Chamber", chamberagentselect),
    ("KAY/O", kayoagentselect),
    ("Skye", skyeagentselect),
    ("Cypher", cypheragentselect),
    ("Sova", sovaagentselect),
    ("Killjoy", killjoyagentselect),
    ("Harbor", harboragentselect),
    ("Vyse", vyseagentselect),
    ("Viper", viperagentselect),
    ("Phoenix", phoenixagentselect),
    ("Astra", astraagentselect),
    ("Brimstone", brimstoneagentselect),
    ("Iso", isoagentselect),
    ("Clove", cloveagentselect),
    ("Neon", neonagentselect),
    ("Yoru", yoruagentselect),
    ("Waylay", waylayagentselect),
    ("Sage", sageagentselect),
    ("Reyna", reynaagentselect),
    ("Omen", omenagentselect),
    ("Jett", jettagentselect),
]

for index, (name, func) in enumerate(buttons):
    row = index // 3
    col = index % 3
    btn = tk.Button(text=name, command=func, font="Verdana 20", width=15)
    btn.grid(row=row, column=col, padx=5, pady=5)



root.mainloop()

