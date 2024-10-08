# Experiências Profissionais de Henrique Constantino

experiencias = [
    {
        "cargo": "Scrum Master",
        "empresa": "Localiza",
        "periodo": "10/2022 - 05/2024",
        "local": "Belo Horizonte/São Paulo",
        "descricao": (
            "Liderei iniciativas de transformação ágil, promovendo uma cultura de melhoria "
            "baseado nas entregas da sprint. Conduzi sessões de treinamento para processos ágeis "
            "dentro de um time que tratava integrações dentro da AWS e GCP. "
            "Participei de uma iniciativa de alfabetização em dados que trazia a proposta de "
            "nivelar o conhecimento dentro de todas as áreas da empresa."
        )
    },
    {
        "cargo": "Business Intelligence Analyst",
        "empresa": "Unidas",
        "periodo": "03/2022 - 10/2022",
        "local": "São Paulo, SP",
        "descricao": (
            "Atuei gerindo times de BI, estruturando processos de Data Lake, ingestão e limpeza "
            "de dados, e garantindo a governança de dados. Isso possibilitou a criação de dashboards "
            "corporativos e relatórios estratégicos que deram suporte a decisões críticas."
        )
    },
    {
        "cargo": "Marketing Team Leader",
        "empresa": "Facebook 3rd/TP",
        "periodo": "06/2021 - 02/2022",
        "local": "São Paulo",
        "descricao": (
            "Gestão de equipes bilíngues e relatórios estratégicos da carteira de clientes. "
            "Acompanhamento da evolução do time e implementação de estratégias de retenção de clientes."
        )
    },
    {
        "cargo": "CS Team Leader",
        "empresa": "Concentrix",
        "periodo": "06/2018 - 06/2021",
        "local": "São Paulo",
        "descricao": (
            "Experiência sólida em Customer Care e Suporte Técnico, atuando como Team Lead e "
            "liderando times de larga escala, focando na gestão de qualidade e implementação de melhorias contínuas."
        )
    },
    {
        "cargo": "Estagiário ISOC - Network Assurance",
        "empresa": "TIM",
        "periodo": "03/2017 - 12/2017",
        "local": "São Paulo",
        "descricao": (
            "Estagiário na rede de criação, desenvolvimento e manutenção de relatórios e dashboards "
            "para gestão administrativa."
        )
    }
]

def mostrar_experiencias(experiencias):
    for exp in experiencias:
        print(f"Cargo: {exp['cargo']}")
        print(f"Empresa: {exp['empresa']}")
        print(f"Período: {exp['periodo']}")
        print(f"Local: {exp['local']}")
        print(f"Descrição: {exp['descricao']}")
        print("-" * 50)

if __name__ == "__main__":
    mostrar_experiencias(experiencias)
