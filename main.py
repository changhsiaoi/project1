def __init__(self):
    super().__init__()
    self.title("這是我的第一個觀窗")
    btn = tk.Button(self,text="請按我",padx=20,pady=20,font=('arial',16))
    btn.pack(padx=50,pady=30)
    tk.Button(self,text="請按我",padx=20,pady=20,font=('arial',16),command=self.userClick).pack(padx=50,pady=30)

def userClick(self):
        print("userClick")



def main():
