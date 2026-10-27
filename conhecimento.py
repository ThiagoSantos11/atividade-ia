
import re
import unicodedata


def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    texto = re.sub(r"[^\w\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


CONHECIMENTO = [
    {
        "tema": "python",
        "palavras": ["python", "linguagem python", "programar em python"],
        "resposta": (
            "Python é uma linguagem de programação conhecida "
            "pela sintaxe simples e legível. É utilizada em "
            "desenvolvimento web, automação, análise de dados e IA."
        )
    },
    {
        "tema": "logica",
        "palavras": ["logica de programacao", "algoritmo", "pseudocodigo"],
        "resposta": (
            "Lógica de programação é a organização dos passos "
            "necessários para resolver um problema por meio de "
            "um programa. Algoritmos representam esses passos."
        )
    },
    {
        "tema": "html",
        "palavras": ["html", "linguagem html", "tag html"],
        "resposta": (
            "HTML é uma linguagem de marcação usada para estruturar "
            "páginas web. Suas tags definem elementos como títulos, "
            "parágrafos, imagens e links."
        )
    },
    {
        "tema": "css",
        "palavras": ["css", "folha de estilo", "estilizar pagina"],
        "resposta": (
            "CSS é utilizado para definir a aparência de páginas web, "
            "incluindo cores, fontes, espaçamentos, tamanhos e layouts."
        )
    },
    {
        "tema": "javascript",
        "palavras": ["javascript", "js", "linguagem javascript"],
        "resposta": (
            "JavaScript é uma linguagem de programação muito usada "
            "para adicionar interatividade às páginas web, validar "
            "formulários e manipular elementos HTML."
        )
    },
    {
        "tema": "php",
        "palavras": ["php", "linguagem php"],
        "resposta": (
            "PHP é uma linguagem executada principalmente no servidor. "
            "É usada para criar páginas dinâmicas, processar formulários "
            "e trabalhar com bancos de dados."
        )
    },
    {
        "tema": "sql",
        "palavras": ["sql", "consulta sql", "comando select"],
        "resposta": (
            "SQL é uma linguagem usada para consultar e manipular "
            "bancos de dados relacionais. SELECT consulta registros, "
            "INSERT adiciona, UPDATE altera e DELETE remove registros."
        )
    },
    {
        "tema": "banco",
        "palavras": ["banco de dados", "bancos de dados", "database"],
        "resposta": (
            "Um banco de dados organiza informações para que possam "
            "ser armazenadas, consultadas e atualizadas. MySQL e "
            "PostgreSQL são exemplos de sistemas de banco de dados."
        )
    },
    {
        "tema": "mysql",
        "palavras": ["mysql"],
        "resposta": (
            "MySQL é um sistema de gerenciamento de banco de dados "
            "relacional que utiliza SQL para consultar e manipular dados."
        )
    },
    {
        "tema": "api",
        "palavras": ["api", "apis", "interface de programacao"],
        "resposta": (
            "Uma API define como sistemas ou programas podem se "
            "comunicar. Uma API web permite, por exemplo, solicitar "
            "dados de um servidor usando requisições HTTP."
        )
    },
    {
        "tema": "http",
        "palavras": ["http", "https", "protocolo http"],
        "resposta": (
            "HTTP é um protocolo usado na comunicação entre clientes "
            "e servidores web. HTTPS adiciona proteção por criptografia "
            "TLS durante a comunicação."
        )
    },
    {
        "tema": "dns",
        "palavras": ["dns", "servidor dns", "resolucao de nomes"],
        "resposta": (
            "DNS traduz nomes de domínio, como exemplo.com, em "
            "informações usadas para localizar serviços na rede, "
            "como endereços IP."
        )
    },
    {
        "tema": "ip",
        "palavras": ["endereco ip", "ipv4", "ipv6"],
        "resposta": (
            "Um endereço IP identifica uma interface de rede para "
            "a comunicação usando o protocolo IP. IPv4 utiliza "
            "endereços de 32 bits; IPv6 utiliza 128 bits."
        )
    },
    {
        "tema": "redes",
        "palavras": ["rede de computadores", "redes de computadores", "rede lan", "lan", "wan"],
        "resposta": (
            "Uma rede de computadores conecta dispositivos para "
            "permitir comunicação e compartilhamento de recursos. "
            "LAN costuma cobrir uma área local; WAN conecta áreas "
            "geográficas maiores."
        )
    },
    {
        "tema": "internet",
        "palavras": ["internet", "como funciona a internet"],
        "resposta": (
            "A internet é uma rede mundial de redes interconectadas. "
            "Dispositivos trocam dados usando protocolos como IP, "
            "TCP e HTTP."
        )
    },
    {
        "tema": "wifi",
        "palavras": ["wifi", "wi fi", "rede sem fio"],
        "resposta": (
            "Wi-Fi é uma tecnologia de comunicação sem fio que conecta "
            "dispositivos a uma rede local. Um roteador ou ponto de "
            "acesso transmite o sinal de rádio."
        )
    },
    {
        "tema": "seguranca",
        "palavras": ["seguranca da informacao", "ciberseguranca", "seguranca digital"],
        "resposta": (
            "Segurança da informação busca proteger dados e sistemas. "
            "Boas práticas incluem senhas fortes, atualizações, "
            "autenticação multifator e cópias de segurança."
        )
    },
    {
        "tema": "sql_injection",
        "palavras": ["sql injection", "injecao sql"],
        "resposta": (
            "SQL Injection é uma vulnerabilidade em que entradas "
            "controladas pelo usuário alteram indevidamente uma "
            "consulta SQL. Consultas preparadas com parâmetros "
            "ajudam a prevenir esse problema."
        )
    },
    {
        "tema": "xss",
        "palavras": ["xss", "cross site scripting"],
        "resposta": (
            "XSS é uma vulnerabilidade que permite executar scripts "
            "indevidos no navegador de outra pessoa. A prevenção "
            "inclui escapar a saída conforme o contexto e tratar "
            "corretamente dados fornecidos pelos usuários."
        )
    },
    {
        "tema": "csrf",
        "palavras": ["csrf", "cross site request forgery"],
        "resposta": (
            "CSRF ocorre quando um site induz o navegador de uma "
            "pessoa autenticada a enviar uma ação não desejada. "
            "Tokens CSRF e cookies configurados corretamente ajudam "
            "a reduzir esse risco."
        )
    },
    {
        "tema": "git",
        "palavras": ["git", "controle de versao"],
        "resposta": (
            "Git é um sistema de controle de versão que registra "
            "alterações nos arquivos de um projeto. Ele permite "
            "comparar versões e recuperar mudanças anteriores."
        )
    },
    {
        "tema": "github",
        "palavras": ["github"],
        "resposta": (
            "GitHub é uma plataforma para hospedar repositórios Git, "
            "colaborar em projetos, revisar código e acompanhar "
            "problemas e alterações."
        )
    },
    {
        "tema": "docker",
        "palavras": ["docker", "container", "containers", "contêiner"],
        "resposta": (
            "Docker é uma plataforma usada para criar e executar "
            "contêineres. Eles empacotam uma aplicação com suas "
            "dependências, ajudando a manter ambientes consistentes."
        )
    },
    {
        "tema": "kubernetes",
        "palavras": ["kubernetes", "k8s"],
        "resposta": (
            "Kubernetes automatiza a implantação, a escala e a "
            "manutenção de aplicações em contêineres distribuídos "
            "por diferentes máquinas."
        )
    },
    {
        "tema": "nuvem",
        "palavras": ["computacao em nuvem", "cloud computing", "nuvem"],
        "resposta": (
            "Computação em nuvem permite utilizar recursos de "
            "computação, armazenamento e serviços pela rede, "
            "sem precisar manter toda a infraestrutura localmente."
        )
    },
    {
        "tema": "ia",
        "palavras": ["inteligencia artificial", "ia", "machine learning", "aprendizado de maquina"],
        "resposta": (
            "Inteligência artificial é uma área da computação que "
            "desenvolve sistemas capazes de realizar tarefas como "
            "reconhecer padrões, interpretar linguagem e fazer "
            "previsões. Machine learning é uma de suas áreas."
        )
    },
    {
        "tema": "poo",
        "palavras": ["programacao orientada a objetos", "poo", "classe em programacao"],
        "resposta": (
            "Programação orientada a objetos organiza o código em "
            "classes e objetos. Conceitos importantes incluem "
            "encapsulamento, herança, abstração e polimorfismo."
        )
    },
    {
        "tema": "hardware",
        "palavras": ["hardware", "pecas do computador"],
        "resposta": (
            "Hardware é a parte física de um computador, como "
            "processador, memória RAM, placa-mãe, armazenamento "
            "e periféricos."
        )
    },
    {
        "tema": "software",
        "palavras": ["software", "programa de computador"],
        "resposta": (
            "Software é o conjunto de programas e instruções que "
            "fazem um computador executar tarefas. Sistemas "
            "operacionais e aplicativos são exemplos."
        )
    },
    {
        "tema": "sistema_operacional",
        "palavras": ["sistema operacional", "windows", "linux"],
        "resposta": (
            "Um sistema operacional gerencia os recursos do "
            "computador e permite executar programas. Windows e "
            "Linux são exemplos de sistemas operacionais."
        )
    },
    {
        "tema": "estrutura_dados",
        "palavras": ["estrutura de dados", "lista ligada", "pilha", "fila"],
        "resposta": (
            "Estruturas de dados organizam informações para facilitar "
            "operações. Listas, pilhas, filas, árvores e tabelas "
            "hash são exemplos com características diferentes."
        )
    },
    {
        "tema": "teste",
        "palavras": ["teste de software", "testes de software", "teste unitario"],
        "resposta": (
            "Testes de software verificam se um programa funciona "
            "como esperado. Testes unitários verificam partes "
            "pequenas do código; testes de integração verificam "
            "a interação entre componentes."
        )
    },
    {
        "tema": "lgpd",
        "palavras": ["lgpd", "lei geral de protecao de dados", "protecao de dados"],
        "resposta": (
            "A LGPD é a Lei Geral de Proteção de Dados Pessoais "
            "do Brasil. Ela estabelece regras para o tratamento "
            "de dados pessoais e prevê direitos para seus titulares."
        )
    },
    {
        "tema": "backup",
        "palavras": ["backup", "copia de seguranca", "copias de seguranca"],
        "resposta": (
            "Backup é uma cópia de dados que pode ser usada para "
            "recuperar informações perdidas ou danificadas. É "
            "importante testar periodicamente a restauração."
        )
    },
    {
        "tema": "excel",
        "palavras": ["excel", "planilha", "planilhas"],
        "resposta": (
            "Excel é um aplicativo de planilhas usado para organizar "
            "dados, realizar cálculos com fórmulas, criar gráficos "
            "e analisar informações."
        )
    },
    {
        "tema": "eletronica",
        "palavras": ["arduino", "eletronica", "circuito eletrico"],
        "resposta": (
            "Eletrônica estuda circuitos que controlam sinais "
            "elétricos. Arduino é uma plataforma popular para "
            "projetos com sensores, componentes e programação."
        )
    },
    {
        "tema": "acessibilidade",
        "palavras": ["acessibilidade digital", "acessibilidade web"],
        "resposta": (
            "Acessibilidade digital busca tornar sites e aplicativos "
            "utilizáveis por pessoas com diferentes capacidades. "
            "Contraste adequado, navegação por teclado e textos "
            "alternativos são exemplos de boas práticas."
        )
    }
]


def responder(pergunta):
    texto = normalizar(pergunta)

    if not texto:
        return "Digite uma pergunta para eu poder responder."

    if texto in {
        "oi", "ola", "bom dia", "boa tarde", "boa noite",
        "e ai", "tudo bem", "como vai"
    }:
        return (
            "Olá! Posso responder perguntas sobre programação, "
            "bancos de dados, redes, segurança e outros assuntos de TI. "
            "O que você gostaria de saber?"
        )

    if texto in {"obrigado", "obrigada", "valeu", "muito obrigado", "muito obrigada"}:
        return "Por nada! Pode mandar outra pergunta sobre TI."

    if texto in {"tchau", "ate mais", "adeus"}:
        return "Até mais! Espero ter ajudado nos seus estudos de TI."

    melhores = []
    palavras_pergunta = set(texto.split())

    for item in CONHECIMENTO:
        pontos = 0

        for palavra in item["palavras"]:
            termo = normalizar(palavra)

            if " " in termo:
                if termo in texto:
                    pontos = max(pontos, len(termo.split()) + 1)
            elif termo in palavras_pergunta:
                pontos = max(pontos, 1)

        if pontos > 0:
            melhores.append((pontos, item))

    if not melhores:
        return (
            "Não encontrei uma resposta específica para essa pergunta "
            "na minha base de conhecimento. Tente perguntar sobre um "
            "assunto de TI, como Python, HTML, SQL, redes ou segurança."
        )

    melhores.sort(key=lambda item: item[0], reverse=True)
    maior_pontuacao = melhores[0][0]
    candidatos = [
        item for pontos, item in melhores
        if pontos == maior_pontuacao
    ]

    if len(candidatos) > 1:
        temas = ", ".join(item["tema"] for item in candidatos[:3])
        return (
            "Sua pergunta pode se referir a mais de um assunto: "
            f"{temas}. Pode especificar qual deles você quer conhecer?"
        )

    return melhores[0][1]["resposta"]
