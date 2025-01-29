from models import Automobilis, db
from app import app


with app.app_context():
    automobiliai = [
        Automobilis(gamintojas="Audi", modelis="A4", spalva="Juoda", kaina=30000),
        Automobilis(gamintojas="BMW", modelis="X5", spalva="Balta", kaina=50000),
        Automobilis(gamintojas="Mercedes", modelis="C-Class", spalva="Sidabrinė", kaina=45000),
        Automobilis(gamintojas="Volkswagen", modelis="Golf", spalva="Raudona", kaina=25000),
        Automobilis(gamintojas="Toyota", modelis="Corolla", spalva="Mėlyna", kaina=20000),
        Automobilis(gamintojas="Ford", modelis="Focus", spalva="Geltona", kaina=18000),
        Automobilis(gamintojas="Honda", modelis="Civic", spalva="Žalia", kaina=22000),
        Automobilis(gamintojas="Nissan", modelis="Leaf", spalva="Pilka", kaina=27000),
        Automobilis(gamintojas="Chevrolet", modelis="Cruze", spalva="Violetinė", kaina=23000),
        Automobilis(gamintojas="Kia", modelis="Ceed", spalva="Oranžinė", kaina=21000),
        Automobilis(gamintojas="Hyundai", modelis="i30", spalva="Tamsiai mėlyna", kaina=24000),
        Automobilis(gamintojas="Peugeot", modelis="308", spalva="Tamsiai žalia", kaina=26000),
        Automobilis(gamintojas="Renault", modelis="Megane", spalva="Bordo", kaina=25000),
        Automobilis(gamintojas="Mazda", modelis="CX-5", spalva="Sidabrinė", kaina=35000),
        Automobilis(gamintojas="Subaru", modelis="Outback", spalva="Mėlyna", kaina=37000),
        Automobilis(gamintojas="Tesla", modelis="Model 3", spalva="Balta", kaina=45000),
        Automobilis(gamintojas="Jaguar", modelis="F-Pace", spalva="Raudona", kaina=55000),
        Automobilis(gamintojas="Volvo", modelis="XC60", spalva="Tamsiai pilka", kaina=48000),
        Automobilis(gamintojas="Land Rover", modelis="Discovery", spalva="Žalia", kaina=60000),
        Automobilis(gamintojas="Porsche", modelis="Macan", spalva="Tamsiai mėlyna", kaina=70000),
        Automobilis(gamintojas="Lexus", modelis="RX", spalva="Sidabrinė", kaina=65000),
        Automobilis(gamintojas="Audi", modelis="Q7", spalva="Juoda", kaina=75000),
        Automobilis(gamintojas="BMW", modelis="X6", spalva="Pilka", kaina=80000),
        Automobilis(gamintojas="Mercedes", modelis="GLE", spalva="Aukso", kaina=85000),
        Automobilis(gamintojas="Volkswagen", modelis="Passat", spalva="Tamsiai raudona", kaina=32000),
        Automobilis(gamintojas="Toyota", modelis="RAV4", spalva="Šviesiai mėlyna", kaina=35000),
        Automobilis(gamintojas="Ford", modelis="Mustang", spalva="Raudona", kaina=60000),
        Automobilis(gamintojas="Honda", modelis="Accord", spalva="Pilka", kaina=37000),
        Automobilis(gamintojas="Nissan", modelis="Qashqai", spalva="Mėlyna", kaina=33000),
        Automobilis(gamintojas="Chevrolet", modelis="Equinox", spalva="Juoda", kaina=37000)
    ]

    db.session.add_all(automobiliai)
    db.session.commit()

    print("Duomenys užpildyti")

