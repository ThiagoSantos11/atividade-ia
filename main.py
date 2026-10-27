
import tkinter as tk
from tkinter import messagebox
from conhecimento import responder


class ChatbotTI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot TI")
        self.root.geometry("1000x680")
        self.root.minsize(750, 500)

        self.usuario = "thiago"
        self.tema_escuro = True

        self.cores = {
            "escuro": {
                "fundo": "#111827",
                "painel": "#1F2937",
                "campo": "#374151",
                "texto": "#F9FAFB",
                "secundario": "#9CA3AF",
                "usuario": "#164E63",
                "bot": "#273449",
                "botao": "#2563EB",
                "hover": "#1D4ED8"
            },
            "claro": {
                "fundo": "#F3F4F6",
                "painel": "#FFFFFF",
                "campo": "#F9FAFB",
                "texto": "#111827",
                "secundario": "#6B7280",
                "usuario": "#DBEAFE",
                "bot": "#E5E7EB",
                "botao": "#2563EB",
                "hover": "#1D4ED8"
            }
        }

        self.mostrar_login()

    def cor(self, nome):
        tema = "escuro" if self.tema_escuro else "claro"
        return self.cores[tema][nome]

    def mostrar_login(self):
        self.tela_login = tk.Frame(
            self.root,
            bg=self.cor("fundo")
        )
        self.tela_login.pack(fill="both", expand=True)

        caixa = tk.Frame(
            self.tela_login,
            bg=self.cor("painel"),
            padx=40,
            pady=35
        )
        caixa.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            caixa,
            text="Chatbot TI",
            font=("Arial", 25, "bold"),
            bg=self.cor("painel"),
            fg=self.cor("texto")
        ).pack(pady=(0, 8))

        tk.Label(
            caixa,
            text="Seu assistente de tecnologia",
            font=("Arial", 11),
            bg=self.cor("painel"),
            fg=self.cor("secundario")
        ).pack(pady=(0, 25))

        tk.Label(
            caixa,
            text="Usuário",
            font=("Arial", 11, "bold"),
            bg=self.cor("painel"),
            fg=self.cor("texto")
        ).pack(anchor="w")

        self.campo_usuario = tk.Entry(
            caixa,
            font=("Arial", 12),
            width=30
        )
        self.campo_usuario.pack(pady=(6, 15), ipady=7)

        tk.Label(
            caixa,
            text="Senha",
            font=("Arial", 11, "bold"),
            bg=self.cor("painel"),
            fg=self.cor("texto")
        ).pack(anchor="w")

        self.campo_senha = tk.Entry(
            caixa,
            font=("Arial", 12),
            width=30,
            show="*"
        )
        self.campo_senha.pack(pady=(6, 20), ipady=7)

        tk.Button(
            caixa,
            text="Entrar",
            command=self.validar_login,
            font=("Arial", 12, "bold"),
            bg=self.cor("botao"),
            fg="white",
            activebackground=self.cor("hover"),
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=27,
            pady=9
        ).pack()

        self.campo_senha.bind(
            "<Return>",
            lambda evento: self.validar_login()
        )
        self.campo_usuario.focus_set()

    def validar_login(self):
        usuario = self.campo_usuario.get().strip()
        senha = self.campo_senha.get()

        if usuario == "thiago" and senha == "12345678":
            self.usuario = usuario
            self.tela_login.destroy()
            self.mostrar_chat()
        else:
            messagebox.showerror(
                "Erro de login",
                "Usuário ou senha incorretos."
            )

    def mostrar_chat(self):
        self.tela_chat = tk.Frame(
            self.root,
            bg=self.cor("fundo")
        )
        self.tela_chat.pack(fill="both", expand=True)

        cabecalho = tk.Frame(
            self.tela_chat,
            bg=self.cor("painel"),
            padx=20,
            pady=15
        )
        cabecalho.pack(fill="x")

        tk.Label(
            cabecalho,
            text="Chatbot TI",
            font=("Arial", 19, "bold"),
            bg=self.cor("painel"),
            fg=self.cor("texto")
        ).pack(side="left")

        tk.Button(
            cabecalho,
            text="Limpar conversa",
            command=self.limpar_conversa,
            bg=self.cor("campo"),
            fg=self.cor("texto"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=7
        ).pack(side="right", padx=(5, 0))

        self.botao_tema = tk.Button(
            cabecalho,
            text="☀️ Tema claro",
            command=self.alternar_tema,
            bg=self.cor("campo"),
            fg=self.cor("texto"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=7
        )
        self.botao_tema.pack(side="right")

        area = tk.Frame(
            self.tela_chat,
            bg=self.cor("fundo"),
            padx=20,
            pady=15
        )
        area.pack(fill="both", expand=True)

        self.chat = tk.Text(
            area,
            wrap="word",
            font=("Arial", 11),
            bg=self.cor("fundo"),
            fg=self.cor("texto"),
            insertbackground=self.cor("texto"),
            relief="flat",
            borderwidth=0,
            padx=12,
            pady=12,
            state="disabled"
        )
        self.chat.pack(side="left", fill="both", expand=True)

        barra = tk.Scrollbar(
            area,
            command=self.chat.yview
        )
        barra.pack(side="right", fill="y")
        self.chat.configure(yscrollcommand=barra.set)

        self.configurar_estilos()

        self.frame_inferior = tk.Frame(
            self.tela_chat,
            bg=self.cor("painel"),
            padx=15,
            pady=15
        )
        self.frame_inferior.pack(fill="x")

        self.entrada = tk.Entry(
            self.frame_inferior,
            font=("Arial", 12),
            bg=self.cor("campo"),
            fg=self.cor("texto"),
            insertbackground=self.cor("texto"),
            relief="flat"
        )
        self.entrada.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10),
            ipady=12
        )

        self.entrada.bind(
            "<Return>",
            lambda evento: self.enviar_mensagem()
        )

        self.botao_enviar = tk.Button(
            self.frame_inferior,
            text="Enviar ➤",
            command=self.enviar_mensagem,
            font=("Arial", 11, "bold"),
            bg=self.cor("botao"),
            fg="white",
            activebackground=self.cor("hover"),
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=22,
            pady=10
        )
        self.botao_enviar.pack(side="right")

        self.adicionar_mensagem(
            "Chatbot TI",
            "Olá! Faça uma pergunta sobre tecnologia. "
            "Por exemplo: O que é Python? Ou: Para que serve o DNS?",
            "bot"
        )
        self.entrada.focus_set()

    def configurar_estilos(self):
        self.chat.tag_configure(
            "nome_usuario",
            foreground="#38BDF8",
            font=("Arial", 10, "bold")
        )
        self.chat.tag_configure(
            "nome_bot",
            foreground="#34D399",
            font=("Arial", 10, "bold")
        )
        self.chat.tag_configure(
            "texto_usuario",
            background=self.cor("usuario"),
            foreground=self.cor("texto"),
            lmargin1=12,
            lmargin2=12,
            rmargin=12,
            spacing1=5,
            spacing3=12
        )
        self.chat.tag_configure(
            "texto_bot",
            background=self.cor("bot"),
            foreground=self.cor("texto"),
            lmargin1=12,
            lmargin2=12,
            rmargin=12,
            spacing1=5,
            spacing3=12
        )

    def adicionar_mensagem(self, nome, mensagem, tipo):
        self.chat.config(state="normal")

        if tipo == "usuario":
            icone = ""
            tag_nome = "nome_usuario"
            tag_texto = "texto_usuario"
        else:
            icone = ""
            tag_nome = "nome_bot"
            tag_texto = "texto_bot"

        self.chat.insert("end", f"{icone} {nome}\n", tag_nome)
        self.chat.insert("end", mensagem.strip() + "\n\n", tag_texto)

        self.chat.config(state="disabled")
        self.chat.see("end")

    def enviar_mensagem(self):
        pergunta = self.entrada.get().strip()

        if not pergunta:
            return

        self.adicionar_mensagem(
            self.usuario,
            pergunta,
            "usuario"
        )

        self.entrada.delete(0, "end")
        self.botao_enviar.config(state="disabled")

        self.chat.config(state="normal")
        self.chat.mark_set("inicio_status", "end-1c")

        self.adicionar_mensagem(
            "Chatbot TI",
            "Pensando...",
            "bot"
        )

        self.root.after(
            500,
            lambda: self.processar_resposta(pergunta)
        )

    def processar_resposta(self, pergunta):
        try:
            resposta = responder(pergunta)
        except Exception:
            resposta = (
                "Não consegui processar sua pergunta. "
                "Confira o arquivo conhecimento.py."
            )

        self.chat.config(state="normal")
        self.chat.delete("inicio_status", "end")
        self.chat.mark_unset("inicio_status")
        self.chat.config(state="disabled")

        self.adicionar_mensagem(
            "Chatbot TI",
            resposta,
            "bot"
        )

        self.botao_enviar.config(state="normal")
        self.entrada.focus_set()

    def limpar_conversa(self):
        if messagebox.askyesno(
            "Limpar conversa",
            "Deseja apagar todas as mensagens?"
        ):
            self.chat.config(state="normal")
            self.chat.delete("1.0", "end")
            self.chat.config(state="disabled")

            self.adicionar_mensagem(
                "Chatbot TI",
                "Conversa limpa! Faça sua próxima pergunta.",
                "bot"
            )

    def alternar_tema(self):
        self.tema_escuro = not self.tema_escuro
        self.tela_chat.destroy()
        self.mostrar_chat()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotTI(root)
    root.mainloop()
""