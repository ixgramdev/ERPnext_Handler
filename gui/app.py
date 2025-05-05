import customtkinter as ctk
from gui.gui_renamer import RenamerFrame
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ERPNextHandler(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ERPnext Handler")
        self.geometry("900x600")

        # Top Bar (con ícono y título)
        top_frame = ctk.CTkFrame(self, height=60)
        top_frame.pack(fill="x")

        icon = ctk.CTkLabel(top_frame, text="", image=ctk.CTkImage(light_image=Image.open("assets/icon.png"), size=(40, 40)))
        icon.pack(side="left", padx=10, pady=10)

        title = ctk.CTkLabel(top_frame, text="ERPnext Handler", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(side="left", padx=5)

        # Divider
        divider = ctk.CTkFrame(self, height=2)
        divider.pack(fill="x")

        # Body: Sidebar + Content Area
        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True)

        self.sidebar = ctk.CTkFrame(body, width=200)
        self.sidebar.pack(side="left", fill="y", padx=(10, 5), pady=10)

        self.content = ctk.CTkFrame(body)
        self.content.pack(side="left", fill="both", expand=True, padx=(5, 10), pady=10)

        # Botón de módulo Renamer
        renamer_btn = ctk.CTkButton(self.sidebar, text="Renamer", command=self.show_renamer)
        renamer_btn.pack(pady=10, fill="x")

        self.module_frame = None
        self.show_renamer()

    def show_renamer(self):
        if self.module_frame:
            self.module_frame.destroy()
        self.module_frame = RenamerFrame(self.content)
        self.module_frame.pack(fill="both", expand=True)
