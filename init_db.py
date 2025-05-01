from app import db
from models import City, Service, Subservice, Company
import random

db.drop_all()
db.create_all()

city_names = [
    "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
    "Нижний Новгород", "Челябинск", "Самара", "Ростов-на-Дону", "Уфа"
]
service_names = [
    "Электрика", "Сантехника", "Уборка", "Ремонт техники", "Строительство",
    "Отделочные работы", "Окна и двери", "Малярные работы", "Мебель", "Вентиляция"
]
subservices_template = [
    "Установка", "Ремонт", "Диагностика", "Настройка", "Замена", "Консультация",
    "Демонтаж", "Сборка", "Обслуживание", "Профилактика"
]

for city_name in city_names:
    city = City(name=city_name)
    db.session.add(city)
    db.session.flush()

    for i in range(7):  # по 7 услуг на город
        service = Service(name=random.choice(service_names), city_id=city.id)
        db.session.add(service)
        db.session.flush()

        subservice_names = random.sample(subservices_template, k=7)
        for sub in subservice_names:
            db.session.add(Subservice(name=sub, service_id=service.id))

        for j in range(random.randint(10, 15)):
            company = Company(
                name=f"Компания {j+1} ({service.name})",
                image_url="https://via.placeholder.com/150",
                price=round(random.uniform(1000, 10000), 2),
                rating=round(random.uniform(1.0, 5.0), 1),
                service_id=service.id
            )
            db.session.add(company)

db.session.commit()
print("База успешно инициализирована и заполнена.")