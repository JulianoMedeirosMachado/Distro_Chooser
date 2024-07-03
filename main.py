class Distribution:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def __str__(self):
        return f"{self.name}: {self.points} pontos"


def get_user_preferences():
    preferences = {}

    def print_question(question, options):
        print(f"\n\033[1m{question}\033[0m")
        for key, value in options.items():
            print(f"\033[94m{key}. {value}\033[0m")

    def get_valid_input(prompt, options):
        while True:
            choice = input(prompt).strip()
            if choice in options:
                return choice
            else:
                print(f"\033[91mOpção inválida. Por favor, escolha uma das seguintes opções: {', '.join(options)}\033[0m")

    print("\033[1;36m=== Bem-vindo ao Assistente de Escolha de Distribuição Linux ===\033[0m")
    print("Responda às perguntas a seguir para ajudar a escolher a melhor distribuição Linux para você.")

    print_question("1. Qual é o seu nível de experiência com Linux?", {
        '1': 'Iniciante',
        '2': 'Intermediário',
        '3': 'Avançado'
    })
    preferences['experience'] = get_valid_input("\033[92mEscolha uma opção (1/2/3): \033[0m", ['1', '2', '3'])

    print_question("2. Você prefere um ambiente de desktop leve ou completo?", {
        '1': 'Leve',
        '2': 'Completo'
    })
    preferences['desktop_environment'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("3. Para que você vai usar o sistema?", {
        '1': 'Uso diário',
        '2': 'Desenvolvimento',
        '3': 'Jogos',
        '4': 'Servidor'
    })
    preferences['purpose'] = get_valid_input("\033[92mEscolha uma opção (1/2/3/4): \033[0m", ['1', '2', '3', '4'])

    print_question("4. Qual é a configuração do seu hardware?", {
        '1': 'Baixo desempenho',
        '2': 'Médio desempenho',
        '3': 'Alto desempenho'
    })
    preferences['hardware'] = get_valid_input("\033[92mEscolha uma opção (1/2/3): \033[0m", ['1', '2', '3'])

    print_question("5. Você precisa de suporte comercial?", {
        '1': 'Sim',
        '2': 'Não'
    })
    preferences['support'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("6. Você prefere software de código aberto ou proprietário?", {
        '1': 'Código aberto',
        '2': 'Proprietário'
    })
    preferences['software'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("7. Você prefere versões estáveis ou as mais recentes?", {
        '1': 'Estável',
        '2': 'Recente'
    })
    preferences['release'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("8. Quão importante é uma comunidade ativa?", {
        '1': 'Muito',
        '2': 'Pouco'
    })
    preferences['community'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("9. Qual gerenciador de pacotes você prefere?", {
        '1': 'APT (Debian, Ubuntu, etc.)',
        '2': 'DNF (Fedora, RHEL, etc.)',
        '3': 'Pacman (Arch Linux, etc.)',
        '4': 'Zypper (openSUSE, etc.)',
        '5': 'Indiferente'
    })
    preferences['package_manager'] = get_valid_input("\033[92mEscolha uma opção (1/2/3/4/5): \033[0m", ['1', '2', '3', '4', '5'])

    print_question("10. Você precisa de suporte a hardware específico (e.g., placas de vídeo NVIDIA, impressoras, etc.)?", {
        '1': 'Sim',
        '2': 'Não'
    })
    preferences['hardware_support'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("11. Qual a sua preocupação com segurança e privacidade?", {
        '1': 'Alta',
        '2': 'Média',
        '3': 'Baixa'
    })
    preferences['security'] = get_valid_input("\033[92mEscolha uma opção (1/2/3): \033[0m", ['1', '2', '3'])

    print_question("12. Você precisa de software adicional específico (e.g., software de edição de vídeo, CAD, etc.)?", {
        '1': 'Sim',
        '2': 'Não'
    })
    preferences['software_additional'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    print_question("13. Qual é a sua preferência por personalização e flexibilidade no sistema operacional?", {
        '1': 'Baixa (Prefiro algo que funcione bem sem muitas modificações)',
        '2': 'Média (Gosto de fazer algumas personalizações)',
        '3': 'Alta (Quero ter total controle e flexibilidade sobre o sistema)'
    })
    preferences['customization'] = get_valid_input("\033[92mEscolha uma opção (1/2/3): \033[0m", ['1', '2', '3'])

    print_question("14. Com que frequência você está disposto a atualizar o seu sistema?", {
        '1': 'Raramente (Prefiro atualizações de longo prazo)',
        '2': 'Ocasionalmente (Estou disposto a fazer atualizações periódicas)',
        '3': 'Frequentemente (Quero sempre as últimas atualizações e recursos)'
    })
    preferences['update_frequency'] = get_valid_input("\033[92mEscolha uma opção (1/2/3): \033[0m", ['1', '2', '3'])

    print_question("15. Você tem preferência por uma distribuição que possua uma vasta quantidade de documentações e tutoriais disponíveis online?", {
        '1': 'Sim (Prefiro distribuições bem documentadas)',
        '2': 'Não (Não é um fator determinante para mim)'
    })
    preferences['documentation'] = get_valid_input("\033[92mEscolha uma opção (1/2): \033[0m", ['1', '2'])

    return preferences


def calculate_scores(preferences):
    distributions = [
        Distribution("Ubuntu"),
        Distribution("Lubuntu"),
        Distribution("Xubuntu"),
        Distribution("Fedora"),
        Distribution("CentOS"),
        Distribution("Debian"),
        Distribution("Red Hat Enterprise Linux"),
        Distribution("Arch Linux"),
        Distribution("Linux Mint"),
        Distribution("openSUSE"),
    ]

    for distro in distributions:
        if preferences['support'] == '1':
            if distro.name in ["Ubuntu", "Arch Linux"]:
                distro.add_points(2)
        elif preferences['support'] == '2':
            if distro.name in ["Debian", "Fedora"]:
                distro.add_points(2)
        elif preferences['support'] == '3':
            if distro.name in ["Red Hat Enterprise Linux", "SUSE Linux Enterprise"]:
                distro.add_points(3)
    
        if preferences['experience'] == '1':
            if distro.name in ["Ubuntu", "Linux Mint"]:
                distro.add_points(3)
 
        if preferences['experience'] == '2':
            if distro.name in ["Debian", "openSUSE"]:
                distro.add_points(2)

        if preferences['desktop_environment'] == '2':
            if distro.name in ["Ubuntu", "Linux Mint"]:
                distro.add_points(2)
        elif preferences['desktop_environment'] == '1':
            if distro.name in ["Lubuntu", "Xubuntu"]:
                distro.add_points(2)

        if preferences['purpose'] == '1':
            if distro.name in ["Ubuntu", "Linux Mint"]:
                distro.add_points(2)
        elif preferences['purpose'] == '2':
            if distro.name in ["Fedora", "Debian"]:
                distro.add_points(3)
        elif preferences['purpose'] == '3':
            if distro.name in ["Ubuntu", "Fedora"]:
                distro.add_points(2)
        elif preferences['purpose'] == '4':
            if distro.name in ["CentOS", "Debian"]:
                distro.add_points(3)

        if preferences['hardware'] == '1' and distro.name in ["Lubuntu", "Xubuntu"]:
            distro.add_points(3)
        elif preferences['hardware'] == '2' and distro.name in ["Ubuntu", "Linux Mint"]:
            distro.add_points(2)
        elif preferences['hardware'] == '3' and distro.name in ["Ubuntu", "Fedora", "Arch Linux"]:
            distro.add_points(3)

        if preferences['software'] == '1' and distro.name in ["Debian", "Fedora", "Arch Linux"]:
            distro.add_points(2)
        elif preferences['software'] == '2' and distro.name in ["Ubuntu", "Linux Mint"]:
            distro.add_points(2)

        if preferences['release'] == '1' and distro.name in ["Debian", "CentOS"]:
            distro.add_points(3)
        elif preferences['release'] == '2' and distro.name in ["Fedora", "Arch Linux"]:
            distro.add_points(3)

        if preferences['community'] == '1' and distro.name in ["Ubuntu", "Arch Linux", "Fedora"]:
            distro.add_points(2)
        elif preferences['community'] == '2' and distro.name in ["CentOS", "Red Hat Enterprise Linux"]:
            distro.add_points(2)

        if preferences['package_manager'] == '1' and distro.name in ["Ubuntu", "Linux Mint", "Debian"]:
            distro.add_points(2)
        elif preferences['package_manager'] == '2' and distro.name in ["Fedora", "Red Hat Enterprise Linux"]:
            distro.add_points(2)
        elif preferences['package_manager'] == '3' and distro.name == "Arch Linux":
            distro.add_points(2)
        elif preferences['package_manager'] == '4' and distro.name == "openSUSE":
            distro.add_points(2)
        elif preferences['package_manager'] == '5':
            distro.add_points(1)

        if preferences['hardware_support'] == '1' and distro.name in ["Ubuntu", "Linux Mint", "Fedora"]:
            distro.add_points(2)

        if preferences['security'] == '1' and distro.name in ["Debian", "Fedora", "Arch Linux"]:
            distro.add_points(3)
        elif preferences['security'] == '2' and distro.name in ["Ubuntu", "openSUSE"]:
            distro.add_points(2)
        elif preferences['security'] == '3' and distro.name in ["Linux Mint"]:
            distro.add_points(1)

        if preferences['software_additional'] == '1' and distro.name in ["Ubuntu", "Fedora", "Arch Linux"]:
            distro.add_points(2)

        if preferences['customization'] == '1' and distro.name in ["Ubuntu", "Linux Mint"]:
            distro.add_points(1)
        elif preferences['customization'] == '2' and distro.name in ["Fedora", "openSUSE"]:
            distro.add_points(2)
        elif preferences['customization'] == '3' and distro.name in ["Arch Linux", "Debian"]:
            distro.add_points(3)

        if preferences['update_frequency'] == '1' and distro.name in ["Debian", "CentOS"]:
            distro.add_points(3)
        elif preferences['update_frequency'] == '2' and distro.name in ["Ubuntu", "Fedora"]:
            distro.add_points(2)
        elif preferences['update_frequency'] == '3' and distro.name in ["Arch Linux", "Fedora"]:
            distro.add_points(1)

        if preferences['documentation'] == '1' and distro.name in ["Ubuntu", "Arch Linux", "Debian"]:
            distro.add_points(3)
        elif preferences['documentation'] == '2' and distro.name in ["CentOS", "Red Hat Enterprise Linux"]:
            distro.add_points(2)

    return distributions


def suggest_distribution(distributions):
    distributions.sort(key=lambda x: x.points, reverse=True)
    return distributions[0]


def main():
    preferences = get_user_preferences()
    distributions = calculate_scores(preferences)
    recommended_distro = suggest_distribution(distributions)
    print(f"\n\033[1;32mA distribuição Linux recomendada para você é: {recommended_distro.name} com {recommended_distro.points} pontos\033[0m")


if __name__ == "__main__":
    main()

