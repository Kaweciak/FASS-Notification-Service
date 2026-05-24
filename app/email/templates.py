def tourist_registered(payload):
    return (
        "Witamy w systemie",
        f"""
Cześć {payload['name']},

dziękujemy za rejestrację w systemie obsługi wycieczek.

Twoje konto zostało pomyślnie utworzone.

Życzymy miłego korzystania z platformy.
"""
    )


def employee_activation(payload):
    return (
        "Aktywacja konta",
        f"""
Dzień dobry,

aby aktywować konto, kliknij w poniższy link:

{payload['activation_link']}

Link aktywacyjny jest ważny przez ograniczony czas.
"""
    )


def assignment_created(payload):
    return (
        "Nowy przydział obszaru",
        f"""
Dzień dobry,

zostałeś przypisany do obszaru:

Nazwa obszaru: {payload['area_name']}
Poziom administracyjny: {payload['area_tier']}

Prosimy o zapoznanie się ze szczegółami w systemie.
"""
    )


def assignment_accepted(payload):
    return (
        "Przydział został zaakceptowany",
        f"""
Dzień dobry,

przydział obszaru został zaakceptowany.

Pracownik: {payload['employee_name']}
Obszar: {payload['area_name']}
Poziom administracyjny: {payload['area_tier']}
"""
    )


def assignment_rejected(payload):
    return (
        "Przydział został odrzucony",
        f"""
Dzień dobry,

przydział obszaru został odrzucony.

Pracownik: {payload['employee_name']}
Obszar: {payload['area_name']}
Poziom administracyjny: {payload['area_tier']}
"""
    )


def assignment_reminder(payload):
    return (
        "Przypomnienie o przydziale",
        f"""
Dzień dobry,

przypominamy o przypisanym obszarze administracyjnym.

Obszar: {payload['area_name']}
Poziom administracyjny: {payload['area_tier']}

Prosimy o potwierdzenie oraz zapoznanie się ze szczegółami.
"""
    )


def assignment_auto_accepted(payload):
    return (
        "Przydział został automatycznie zaakceptowany",
        f"""
Dzień dobry,

przydział został automatycznie zaakceptowany z powodu przekroczenia czasu odpowiedzi.

Obszar: {payload['area_name']}
Poziom administracyjny: {payload['area_tier']}
"""
    )


def patrol_created(payload):
    return (
        "Utworzono nowy patrol",
        f"""
Dzień dobry,

utworzono nowy patrol.

Nazwa patrolu: {payload['patrol_name']}
Obszar działania: {payload['area']}
"""
    )


def patrol_warning(payload):
    return (
        "Ostrzeżenie patrolu",
        f"""
UWAGA

Wygenerowano ostrzeżenie dla patrolu.

Poziom zagrożenia: {payload['severity']}
Treść komunikatu: {payload['message']}

Prosimy o podjęcie odpowiednich działań.
"""
    )


def trip_warning(payload):
    return (
        "Ważne ostrzeżenie dotyczące wycieczki",
        f"""
Dzień dobry,

dla wycieczki wygenerowano ostrzeżenie.

Wycieczka: {payload['trip_name']}
Treść ostrzeżenia: {payload['warning']}

Prosimy o zapoznanie się z informacją.
"""
    )


def participant_invited(payload):
    return (
        "Zaproszenie do udziału w wycieczce",
        f"""
Dzień dobry,

otrzymałeś zaproszenie do udziału w wycieczce.

Wycieczka: {payload['trip_name']}
Organizator: {payload['organizer']}

Szczegóły znajdziesz w systemie.
"""
    )


def trip_organizer_assigned(payload):
    return (
        "Przydzielono Ci rolę organizatora",
        f"""
Dzień dobry,

zostałeś przypisany jako organizator wycieczki.

Wycieczka: {payload['trip_name']}

Prosimy o zapoznanie się ze szczegółami organizacyjnymi.
"""
    )


def trip_cancelled(payload):
    return (
        "Wycieczka została odwołana",
        f"""
Dzień dobry,

wycieczka została odwołana.

Wycieczka: {payload['trip_name']}
Powód: {payload['reason']}

W razie pytań prosimy o kontakt z organizatorem.
"""
    )