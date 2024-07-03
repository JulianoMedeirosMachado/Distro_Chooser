class Distribution:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def __str__(self):
        return f"{self.name}: {self.points} pontos"


def get_user_preferences():
    questions = [
        ("Qual é o seu nível de experiência com Linux?", ['Iniciante', 'Intermediário', 'Avançado']),
        ("Você prefere um ambiente de desktop leve ou completo?", ['Leve', 'Completo']),
        ("Para que você vai usar o sistema?", ['Uso diário', 'Desenvolvimento', 'Jogos', 'Servidor']),
        ("Qual é a configuração do seu hardware?", ['Baixo desempenho', 'Médio desempenho', 'Alto desempenho']),
        ("Você precisa de suporte comercial?", ['Sim', 'Não']),
        ("Você prefere software de código aberto ou proprietário?", ['Código aberto', 'Proprietário']),
        ("Você prefere versões estáveis ou as mais recentes?", ['Estável', 'Recente']),
        ("Quão importante é uma comunidade ativa?", ['Muito', 'Pouco']),
        ("Qual gerenciador de pacotes você prefere?", ['APT (Debian, Ubuntu, etc.)', 'DNF (Fedora, RHEL, etc.)', 'Pacman (Arch Linux, etc.)', 'Zypper (openSUSE, etc.)', 'Indiferente']),
        ("Você precisa de suporte a hardware específico?", ['Sim', 'Não']),
        ("Qual a sua preocupação com segurança e privacidade?", ['Alta', 'Média', 'Baixa']),
        ("Você precisa de software adicional específico?", ['Sim', 'Não']),
        ("Qual é a sua preferência por personalização e flexibilidade no sistema operacional?", ['Baixa', 'Média', 'Alta']),
        ("Com que frequência você está disposto a atualizar o seu sistema?", ['Raramente', 'Ocasionalmente', 'Frequentemente']),
        ("Você tem preferência por uma distribuição que possua uma vasta quantidade de documentações e tutoriais disponíveis online?", ['Sim', 'Não']),
        ("De qual sistema operacional você está migrando?", ['Windows', 'macOS', 'Chrome OS', 'Nunca usei um computador'])
    ]

    preferences = {}
    for i, (question, options) in enumerate(questions, 1):
        print(f"\n\033[1m{i}. {question}\033[0m")
        for idx, option in enumerate(options, 1):
            print(f"\033[94m{idx}. {option}\033[0m")
        preferences[i] = input("\033[92mEscolha uma opção: \033[0m").strip()

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
        Distribution("Zorin OS"),
        Distribution("Pop!_OS"),
        Distribution("elementary OS"),
        Distribution("Manjaro")
    ]

    points_map = {
        1: {
            "1": [("Linux Mint", 3), ("Zorin OS", 3), ("Ubuntu", 2), ("Fedora", 1), ("openSUSE", 1), ("Arch Linux", 1), ("CentOS", 1), ("Debian", 1), ("Red Hat Enterprise Linux", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Manjaro", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Ubuntu", 3), ("Fedora", 3), ("openSUSE", 2), ("Linux Mint", 2), ("Debian", 2), ("Arch Linux", 2), ("Zorin OS", 2), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Manjaro", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Arch Linux", 3), ("Fedora", 2), ("Ubuntu", 2), ("Debian", 2), ("openSUSE", 2), ("Manjaro", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        2: {
            "1": [("Lubuntu", 3), ("Xubuntu", 3), ("Linux Mint", 2), ("Debian", 2), ("Ubuntu", 2), ("Fedora", 1), ("openSUSE", 1), ("Arch Linux", 1), ("Zorin OS", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Manjaro", 1)],
            "2": [("Ubuntu", 3), ("Fedora", 3), ("Pop!_OS", 2), ("Manjaro", 2), ("Linux Mint", 2), ("Debian", 2), ("openSUSE", 2), ("Arch Linux", 2), ("Zorin OS", 2), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        3: {
            "1": [("Linux Mint", 3), ("Zorin OS", 3), ("Ubuntu", 2), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("Arch Linux", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Fedora", 3), ("openSUSE", 3), ("Ubuntu", 2), ("Debian", 2), ("Arch Linux", 2), ("Linux Mint", 2), ("Pop!_OS", 2), ("Manjaro", 2), ("Zorin OS", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Pop!_OS", 3), ("Manjaro", 3), ("Fedora", 2), ("Arch Linux", 2), ("Ubuntu", 2), ("Debian", 1), ("openSUSE", 1), ("Linux Mint", 1), ("Zorin OS", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "4": [("CentOS", 3), ("Debian", 3), ("Red Hat Enterprise Linux", 2), ("Fedora", 2), ("openSUSE", 2), ("Ubuntu", 1), ("Linux Mint", 1), ("Arch Linux", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("Zorin OS", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        4: {
            "1": [("Lubuntu", 3), ("Xubuntu", 3), ("Linux Mint", 2), ("Debian", 2), ("Ubuntu", 2), ("Fedora", 1), ("openSUSE", 1), ("Arch Linux", 1), ("Zorin OS", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Manjaro", 1)],
            "2": [("Ubuntu", 3), ("Linux Mint", 3), ("Zorin OS", 2), ("Fedora", 2), ("openSUSE", 2), ("Debian", 2), ("Pop!_OS", 2), ("Manjaro", 2), ("Arch Linux", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Fedora", 2), ("Arch Linux", 3), ("Debian", 2), ("openSUSE", 2), ("Ubuntu", 1), ("Linux Mint", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("Zorin OS", 1), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        5: {
            "1": [("Red Hat Enterprise Linux", 3), ("Ubuntu", 2), ("SUSE Linux Enterprise", 2), ("CentOS", 2), ("Debian", 2), ("Fedora", 1), ("openSUSE", 1), ("Arch Linux", 1), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Debian", 3), ("Arch Linux", 2), ("Fedora", 2), ("openSUSE", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 1), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        6: {
            "1": [("Debian", 3), ("Fedora", 3), ("Arch Linux", 2), ("openSUSE", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Ubuntu", 2), ("Linux Mint", 3), ("Fedora", 2), ("openSUSE", 2), ("Debian", 2), ("Arch Linux", 2), ("CentOS", 1), ("Red Hat Enterprise Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        7: {
            "1": [("Debian", 3), ("CentOS", 3), ("Ubuntu", 2), ("openSUSE", 2), ("Red Hat Enterprise Linux", 2), ("Fedora", 2), ("Linux Mint", 1), ("Arch Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Fedora", 3), ("Arch Linux", 2), ("openSUSE", 2), ("Debian", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        8: {
            "1": [("Ubuntu", 2), ("Arch Linux", 3), ("Fedora", 3), ("Debian", 2), ("openSUSE", 2), ("Linux Mint", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("CentOS", 3), ("Red Hat Enterprise Linux", 3), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("Ubuntu", 2), ("Linux Mint", 1), ("Arch Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        9: {
            "1": [("Debian", 3), ("Ubuntu", 3), ("Linux Mint", 2), ("openSUSE", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 2), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Fedora", 3), ("Red Hat Enterprise Linux", 3), ("openSUSE", 2), ("Debian", 2), ("Ubuntu", 2), ("CentOS", 2), ("Arch Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Arch Linux", 3), ("Manjaro", 3), ("Fedora", 2), ("Debian", 2), ("openSUSE", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "4": [("openSUSE", 3), ("Debian", 2), ("Fedora", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "5": [("Linux Mint", 2), ("Pop!_OS", 2), ("Ubuntu", 2), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 1), ("Zorin OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        10: {
            "1": [("Ubuntu", 3), ("Fedora", 3), ("openSUSE", 2), ("Linux Mint", 2), ("Debian", 2), ("Arch Linux", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Debian", 3), ("Arch Linux", 3), ("openSUSE", 2), ("Fedora", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        11: {
            "1": [("Debian", 3), ("Fedora", 3), ("Arch Linux", 3), ("openSUSE", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("openSUSE", 3), ("Pop!_OS", 2), ("Fedora", 2), ("Debian", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 1), ("Linux Mint", 1), ("Zorin OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Linux Mint", 2), ("Ubuntu", 2), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        12: {
            "1": [("Ubuntu", 3), ("Fedora", 3), ("Pop!_OS", 2), ("Debian", 2), ("openSUSE", 2), ("Arch Linux", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Debian", 2), ("Arch Linux", 2), ("openSUSE", 2), ("Fedora", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        13: {
            "1": [("Linux Mint", 3), ("Zorin OS", 3), ("Ubuntu", 2), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("Pop!_OS", 2), ("Manjaro", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Fedora", 3), ("openSUSE", 3), ("Debian", 2), ("Arch Linux", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Arch Linux", 3), ("Manjaro", 3), ("Fedora", 2), ("Debian", 2), ("openSUSE", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        14: {
            "1": [("Debian", 3), ("CentOS", 3), ("Ubuntu", 2), ("openSUSE", 2), ("Red Hat Enterprise Linux", 2), ("Fedora", 2), ("Linux Mint", 1), ("Arch Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("Fedora", 3), ("openSUSE", 2), ("Debian", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Arch Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Arch Linux", 3), ("Fedora", 3), ("Debian", 2), ("openSUSE", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        15: {
            "1": [("Debian", 3), ("Arch Linux", 3), ("openSUSE", 2), ("Fedora", 2), ("Ubuntu", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("CentOS", 3), ("Red Hat Enterprise Linux", 3), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("Ubuntu", 2), ("Linux Mint", 1), ("Arch Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        },
        16: {
            "1": [("Linux Mint", 3), ("Zorin OS", 3), ("Ubuntu", 2), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Pop!_OS", 2), ("Manjaro", 2), ("elementary OS", 2), ("Arch Linux", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "2": [("elementary OS", 3), ("Ubuntu", 3), ("Zorin OS", 2), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 2), ("Arch Linux", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "3": [("Ubuntu", 3), ("openSUSE", 2), ("Debian", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 2), ("Arch Linux", 1), ("Zorin OS", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)],
            "4": [("Ubuntu", 3), ("Zorin OS", 3), ("Debian", 2), ("openSUSE", 2), ("Fedora", 2), ("CentOS", 2), ("Red Hat Enterprise Linux", 2), ("Linux Mint", 2), ("Arch Linux", 1), ("Pop!_OS", 1), ("Manjaro", 1), ("elementary OS", 1), ("Lubuntu", 1), ("Xubuntu", 1)]
        }
    }

    for idx, response in preferences.items():
        if response in points_map[idx]:
            for distro_name, points in points_map[idx][response]:
                for distro in distributions:
                    if distro.name == distro_name:
                        distro.add_points(points)

    return distributions


def determine_user_type(preferences):
    user_type = "Usuário"
    
    if preferences[1] == '1':
        user_type = "Iniciante"
    elif preferences[1] == '2':
        user_type = "Intermediário"
    elif preferences[1] == '3':
        user_type = "Avançado"
    
    if preferences[3] == '3':
        user_type = "Gamer"
    elif preferences[3] == '4':
        user_type = "Profissional"
    
    return user_type


def suggest_distribution(distributions):
    distributions.sort(key=lambda x: x.points, reverse=True)
    return distributions


def main():
    preferences = get_user_preferences()
    distributions = calculate_scores(preferences)
    ranked_distributions = suggest_distribution(distributions)
    user_type = determine_user_type(preferences)

    print(f"\n\033[1;32mVocê é classificado como: {user_type}\033[0m")
    print("\n\033[1;32mRanking das distribuições Linux recomendadas:\033[0m")
    for distro in ranked_distributions:
        print(distro)


if __name__ == "__main__":
    main()
