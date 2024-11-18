import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from PIL import ImageGrab, Image, ImageTk  # type: ignore # Para capturar a tela
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
import pandas as pd # type: ignore


class App:
    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("CalculaME")
        self.centralizar_janela(1100, 768)
        
        # Dados para gráficos
        self.resultados = []

        # Criação de um frame de container principal
        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # Chama a tela inicial
        self.tela_inicial()
    
    def centralizar_janela(self, largura, altura):
        """Centraliza a janela na tela."""
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def tela_inicial(self):
        """Tela inicial do aplicativo."""
        self.limpar_tela()
        
        logo_path = "logo.png"  # Substitua pelo caminho da sua logo
        try:
            img = Image.open(logo_path)
            img = img.resize((200, 150), Image.Resampling.LANCZOS)  # Redimensiona a imagem
            self.logo = ImageTk.PhotoImage(img)  # Mantém a referência
            label_logo = ttk.Label(self.container, image=self.logo)
            label_logo.pack(pady=20)
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo de logo não encontrado: {logo_path}")

        # Configuração da tela inicial
        label_inicio = ttk.Label(self.container, text="Escolha o tipo de cálculo:", font=("Arial", 18), bootstyle="primary")
        label_inicio.pack(pady=20)

        btn_escola = ttk.Button(self.container, text="Escola", command=self.menu_escola, width=20, bootstyle="primary")
        btn_escola.pack(pady=10)

        btn_faculdade = ttk.Button(self.container, text="Faculdade", command=self.menu_faculdade, width=20, bootstyle="secondary")
        btn_faculdade.pack(pady=10)

    def menu_escola(self):
        """Tela de cálculo para Escola."""
        self.limpar_tela()

        label_escola = ttk.Label(self.container, text="Adicionar Notas - Escola", font=("Arial", 18), bootstyle="primary")
        label_escola.pack(pady=20)

        entry_notas = ttk.Entry(self.container, width=50)
        entry_notas.pack(pady=10)
        entry_notas.insert(0, "Digite as notas separadas por vírgula")

        def calcular_media_escola():
            notas_str = entry_notas.get()
            try:
                notas = list(map(float, notas_str.split(',')))
                media = sum(notas) / len(notas)
                messagebox.showinfo("Média Simples", f"A média das notas é: {media:.2f}")
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira apenas números separados por vírgula.")

        btn_calcular_media = ttk.Button(self.container, text="Calcular Média Simples", command=calcular_media_escola, bootstyle="primary")
        btn_calcular_media.pack(pady=20)

        btn_voltar = ttk.Button(self.container, text="Voltar", command=self.tela_inicial, bootstyle="secondary")
        btn_voltar.pack(pady=10)

    def menu_faculdade(self):
        """Tela de escolha da Faculdade."""
        self.limpar_tela()

        label_faculdade = ttk.Label(self.container, text="Faculdade - Escolha a instituição", font=("Arial", 18), bootstyle="primary")
        label_faculdade.pack(pady=20)

        instituicoes = ["FIAP"]
        selecao_faculdade = tk.StringVar(self.root)
        selecao_faculdade.set(instituicoes[0])

        dropdown_faculdade = ttk.Combobox(self.container, textvariable=selecao_faculdade, values=instituicoes, width=30, font=("Arial", 14))
        dropdown_faculdade.pack(pady=10)

        def selecionar_faculdade():
            faculdade = selecao_faculdade.get()
            if faculdade == "FIAP":
                self.pagina_fiap()

        btn_selecionar = ttk.Button(self.container, text="Selecionar", command=selecionar_faculdade, bootstyle="secondary")
        btn_selecionar.pack(pady=20)

        btn_voltar = ttk.Button(self.container, text="Voltar", command=self.tela_inicial, bootstyle="secondary")
        btn_voltar.pack(pady=10)

    def pagina_fiap(self):
        """Tela de cálculo da FIAP."""
        self.limpar_tela()

        # Configuração do frame FIAP com rolagem
        frame_canvas = ttk.Frame(self.container)
        frame_canvas.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame_canvas)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.fiap_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.fiap_frame, anchor="nw")

        label_fiap = ttk.Label(self.fiap_frame, text="FIAP - Calcular Notas", font=("Arial", 18), bootstyle="primary")
        label_fiap.grid(row=0, column=0, columnspan=12, pady=10)

        headers = ["Matéria", "CP1", "CP2", "CP3", "SPRINT1", "SPRINT2", "GS", "Faltas", "Aulas", "Média Final", "PR", "Status"]
        for col, header in enumerate(headers):
            label = ttk.Label(self.fiap_frame, text=header, font=("Arial", 12, "bold"), bootstyle="secondary")
            label.grid(row=1, column=col, padx=5, pady=5)

        self.entries = []
        for row in range(12):
            row_entries = []
            materia_entry = ttk.Entry(self.fiap_frame, width=20)
            materia_entry.grid(row=row+2, column=0, padx=5, pady=5)
            row_entries.append(materia_entry)

            for col in range(1, 9):
                entry = ttk.Entry(self.fiap_frame, width=10)
                entry.grid(row=row+2, column=col, padx=5, pady=5)
                row_entries.append(entry)

            media_label = ttk.Label(self.fiap_frame, text="--", width=10, font=("Arial", 10), bootstyle="secondary")
            media_label.grid(row=row+2, column=9, padx=5, pady=5)
            row_entries.append(media_label)

            pr_label = ttk.Label(self.fiap_frame, text="--", width=10, font=("Arial", 10), bootstyle="secondary")
            pr_label.grid(row=row+2, column=10, padx=5, pady=5)
            row_entries.append(pr_label)

            status_label = ttk.Label(self.fiap_frame, text="--", width=10, font=("Arial", 10), bootstyle="secondary")
            status_label.grid(row=row+2, column=11, padx=5, pady=5)
            row_entries.append(status_label)

            self.entries.append(row_entries)

        def calcular_notas():
            for row_entries in self.entries:
                try:
                    cp1 = float(row_entries[1].get())
                    cp2 = float(row_entries[2].get())
                    cp3 = float(row_entries[3].get())
                    sprint1 = float(row_entries[4].get())
                    sprint2 = float(row_entries[5].get())
                    gs = float(row_entries[6].get())
                    faltas = float(row_entries[7].get())
                    aulas = float(row_entries[8].get())

                    cps = [cp1, cp2, cp3]
                    cps.remove(min(cps))
                    media_cp = sum(cps) / len(cps)
                    media_sprint = (sprint1 + sprint2) / 2
                    media_final = (media_cp * 0.2) + (media_sprint * 0.2) + (gs * 0.6)
                    pr = (aulas - faltas) / aulas * 100 if aulas > 0 else 0

                    if media_final >= 6 and pr >= 75:
                        row_entries[11].config(text="Aprovado", bootstyle="success")
                        row_entries[9].config(text=f"{media_final:.2f}", bootstyle="success")
                        row_entries[10].config(text=f"{pr:.2f}%", bootstyle="success")
                    elif media_final >= 4 and pr >= 75:
                        row_entries[11].config(text="Exame", bootstyle="warning")
                        row_entries[9].config(text=f"{media_final:.2f}", bootstyle="warning")
                        row_entries[10].config(text=f"{pr:.2f}%", bootstyle="warning")
                    else:
                        row_entries[11].config(text="Reprovado", bootstyle="danger")
                        row_entries[9].config(text=f"{media_final:.2f}", bootstyle="danger")
                        row_entries[10].config(text=f"{pr:.2f}%", bootstyle="danger")
                    
                    self.resultados.append({
                        "Matéria": row_entries[0].get(),
                        "Md_CP": media_cp*0.2,
                        "Md_Sprint": media_sprint*0.2,
                        "Gs": gs*0.6,
                        "Md_Final": media_final,
                        "Pr": pr,
                        "Status": row_entries[11].cget("text")
                    })
                        
                    btn_graficos = ttk.Button(self.fiap_frame, text="Mostrar Gráficos", command=self.graficos, bootstyle="secondary")
                    btn_graficos.grid(row=14, column=6, columnspan=3, pady=12)
                except ValueError:
                    row_entries[9].config(text="N/A")
                    row_entries[10].config(text="N/A")
            print(self.resultados)
        def exportar_resultados():
            x = self.fiap_frame.winfo_rootx()
            y = self.fiap_frame.winfo_rooty()
            width = x + self.fiap_frame.winfo_width()
            height = y + self.fiap_frame.winfo_height()
            img = ImageGrab.grab(bbox=(x, y, width, height))
            img.save("resultado_aluno.png")
            messagebox.showinfo("Resultados Salvos", "Os resultados foram exportados para 'resultado_aluno.png'")

        btn_calcular = ttk.Button(self.fiap_frame, text="Calcular Notas", command=calcular_notas, bootstyle="primary")
        btn_calcular.grid(row=14, column=0, columnspan=3, pady=12)

        btn_exportar = ttk.Button(self.fiap_frame, text="Exportar Resultados", command=exportar_resultados, bootstyle="secondary")
        btn_exportar.grid(row=14, column=3, columnspan=3, pady=12)

        btn_voltar = ttk.Button(self.fiap_frame, text="Voltar", command=self.tela_inicial, bootstyle="info")
        btn_voltar.grid(row=14, column=9, columnspan=3, pady=12)
        
        
    
    def graficos(self):
        # Tela de exibição de gráficos
        self.limpar_tela()
        label_graficos = ttk.Label(self.container, text="Gráficos de Composição da Média Final", font=("Arial", 18), bootstyle="primary")
        label_graficos.pack(pady=20)

        # Criar DataFrame para gráficos
        df = pd.DataFrame(self.resultados)

        # Criar um DataFrame para barras empilhadas
        df_composicao = df[['Matéria', 'Md_CP', 'Md_Sprint', 'Gs']].set_index('Matéria')

        # Gráfico de Barras Empilhadas
        fig, ax = plt.subplots(figsize=(12, 6))
        df_composicao.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)

        # Configurações do gráfico
        ax.set_title('Contribuição de Cada Componente na Média Final', fontsize=16)
        ax.set_ylabel('Nota', fontsize=12)
        ax.set_xlabel('Matéria', fontsize=12)
        ax.axhline(6, color='orange', linestyle='--', label='Aprovação', linewidth=2)
        ax.axhline(4, color='red', linestyle='--', label='Reprovação', linewidth=2)
        ax.legend(title='Componentes')

        # Adicionar gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, self.container)
        canvas.get_tk_widget().pack(pady=10)
        canvas.draw()

        def exportar_graficos():
            fig.savefig("composicao_media_final.png")
            messagebox.showinfo("Exportação Concluída", "O gráfico foi salvo como 'composicao_media_final.png'.")

        btn_exportar = ttk.Button(
            self.container, text="Exportar Gráficos", command=exportar_graficos, bootstyle="secondary"
        )
        btn_exportar.pack(pady=10)

        btn_voltar = ttk.Button(
            self.container, text="Voltar", command=self.pagina_fiap, bootstyle="info"
        )
        btn_voltar.pack(pady=10)
            
    def limpar_tela(self):
        """Remove todos os widgets do container."""
        for widget in self.container.winfo_children():
            widget.destroy()

# Inicialização da janela Tkinter com tema ttkbootstrap
root = ttk.Window(themename="simplex")
app = App(root)
root.mainloop()
