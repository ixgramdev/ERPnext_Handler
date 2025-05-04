
import customtkinter as ctk
from modules.renamer import rename_fields

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class RenameApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Renombrador de Campos - ERPNext")
        self.geometry("700x500")

        self.entries = []

        self.frame = ctk.CTkScrollableFrame(self, width=680, height=400)
        self.frame.pack(padx=10, pady=10)

        header = ctk.CTkLabel(self.frame, text="Fieldname actual → Nuevo nombre", font=ctk.CTkFont(size=16))
        header.grid(row=0, column=0, columnspan=2, pady=5)

        self.add_row()

        self.add_button = ctk.CTkButton(self, text="+ Añadir campo", command=self.add_row)
        self.add_button.pack(pady=(0, 10))

        self.rename_button = ctk.CTkButton(self, text="Renombrar Campos", command=self.rename_all)
        self.rename_button.pack(pady=(0, 20))

        self.result_text = ctk.CTkTextbox(self, height=100)
        self.result_text.pack(padx=10, pady=10)

    def add_row(self):
        row = len(self.entries) + 1
        old_field = ctk.CTkEntry(self.frame, width=300, placeholder_text="Nombre actual")
        new_field = ctk.CTkEntry(self.frame, width=300, placeholder_text="Nuevo nombre")
        old_field.grid(row=row, column=0, padx=10, pady=5)
        new_field.grid(row=row, column=1, padx=10, pady=5)
        self.entries.append((old_field, new_field))

    def rename_all(self):
        self.result_text.delete("0.0", "end")

        fields = {}
        for old_entry, new_entry in self.entries:
            old_name = old_entry.get().strip()
            new_name = new_entry.get().strip()
            if old_name and new_name:
                fields[old_name] = new_name

        if not fields:
            self.result_text.insert("end", "⚠️ No hay campos válidos para renombrar.\n")
            return

        results = rename_fields(fields)

        for current, (status, result) in results.items():
            self.result_text.insert("end", f"{status} {current} → {result}\n")

