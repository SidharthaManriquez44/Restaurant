# Restaurant Menu Manager 🍽️

This project is a menu management system for a restaurant.  
It allows you to define different menus (Brunch, Dinner, Kids, etc.) with associated times and dishes.

### 🚀 Features

- Create and organize menus with name, time and items.
- Check which menus are available according to the current time.
- Manage reservations and guest eligibility for a welcome drink.
- Clean project structure with classes and packages.
- CLI interface and ready for future GUI implementation.

### 📦 Project structure

restaurant_project/
├── cli/ # Command-line interface
│ ├── init.py
│ └── menu_interface.py
├── data/ # Static data, configs
│ ├── init.py
│ └── menu_data.py
├── src/ # Source code
│ ├── booking/
│ │ ├── init.py
│ │ └── booking.py
│ └── restaurant/
│ ├── init.py
│ ├── menu.py
│ └── restaurant.py
├── tests/ # Unit tests
│ ├── init.py
│ └── test_restaurant.py
├── main.py # Entry point
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE


### How to run

``` bash
    python main.py
```
## 🧪 Tests

The unittest includes custom tests that validate:
* Menu creation
* Add Menu to Restaurant
* Items Format
* Available Menus

This project uses pytest for testing.
```bash
  # From the project root
  pytest -v
```
Or run a specific test file:
```bash
  pytest tests/test_restaurant.py -v
```

## ⚙️ Requirements
* Python 3.10+
* No external dependencies

Does not require external dependencies

##  ‍🧑‍💻 Author
Developed by `Sidhartha Manriquez`.

## 📄 License

This project is under the [License MIT](LICENSE).