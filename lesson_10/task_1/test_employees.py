# Завдання 1
#
# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді,
# якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

from employees import TeamLead

def test_teamlead_has_attr():
    lead = TeamLead(
        name="Tetiana",
        salary=1000,
        departament="QA",
        programming_language="Python",
        team_size=8
    )

    assert hasattr(lead, "departament")
    assert hasattr(lead, "programming_language")
    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")


if __name__ == "__main__":
    test_teamlead_has_attr()
    print("Test passed")

