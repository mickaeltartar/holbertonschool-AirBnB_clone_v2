![hbnb-logo](https://i.imgur.com/GM1iQ0P.png)

# <p align = "center">HolbertonBnB</p>

# <p align = "center">AirBnB Clone - MySQL</p>

This is the second step towards building our first full web application : the **AirBnB clone**

For this project, we have focused on implementing an additional storage option, which, as you can see from the diagram below, is the second step of the Airbnb Clone projects to follow in the coming weeks

![hbnb-diag-step2](https://i.imgur.com/keAoFFG.png)

🚨 You can find the very first step of this project **[here](https://github.com/ValPumpkins/holbertonschool-AirBnB_clone)**, all info about the cobsole can be find in this [repository](https://github.com/ValPumpkins/holbertonschool-AirBnB_clone) **[README](https://github.com/ValPumpkins/holbertonschool-AirBnB_clone/blob/main/README.md)**


## 🛠️ Console Setup
1. Clone this git repository

```bash
git clone https://github.com/ValPumpkins/holbertonschool-AirBnB_clone_v2.git
cd holbertonschool-AirBnB_clone_v2
```
2. You can now use the command interpreter

```bash
./console
```
3. If all goes well, the following prompt should appear

```bash
(hbtn)
```
4. You can now use it as you wish. The commands available are detailed below, in the "*Commands*" category.

### 💡 Bonus

This shell can also work in non-interactive mode :

```bash
echo "help" | ./console.py
```

## 🖲️ Commands
Once the console is open, you can type `help` to see all the commands available:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

* **create** - Creates an instance based on given class

* **destroy** - Destroys an object based on class and UUID

* **show** - Shows an object based on class and UUID

* **all** - Shows all objects the program has access to, or all objects of a given class

* **update** - Updates existing attributes an object based on class name and UUID

* **quit** - Exits the program (EOF will as well)


### 💡 Alt syntax
You can also used every commands like that :
```bash
(hbnb) <class_name>.cmd(<optional arg>)
```
```bash
(hbnb) User.create()
1337
(hbnb) User.update(1337, name, Bernard)
```

### 📺 Outputs

- **create** :
```bash
(hbnb) create BaseModel
```
output ⤵️
```bash
bf68a684-6994-41cc-82f2-2d1341e711b3
```
- **show**
```bash
(hbnb) show BaseModel bf68a684-6994-41cc-82f2-2d1341e711b3
```
output ⤵️
```bash
[BaseModel] (bf68a684-6994-41cc-82f2-2d1341e711b3) {'id': 'bf68a684-6994-41cc-82f2-2d1341e711b3', 'created_at': datetime.datetime(2023, 11, 1, 17, 44, 6, 792332), 'updated_at': datetime.datetime(2023, 11, 1, 17, 44, 6, 792371)}
```
- **count**
```bash
(hbnb) count User
```
output ⤵️
```bash
2
```
- **update**
```bash
(hbnb) update BaseModel bf68a684-6994-41cc-82f2-2d1341e711b3 name "Roger"
```
output ⤵️
```bash
no output
```
but `file.json` is updated :
```json
{
	"BaseModel.bf68a684-6994-41cc-82f2-2d1341e711b3": {
        "id": "bf68a684-6994-41cc-82f2-2d1341e711b3",
        "created_at": "2023-11-01T17:44:06.792332",
        "updated_at": "2023-11-01T17:48:32.407856",
        "name": "Roger",
        "__class__": "BaseModel"
    }
}
```
- **destroy**
```bash
(hbnb) destroy BaseModel bf68a684-6994-41cc-82f2-2d1341e711b3
```
output ⤵️
```bash
no output
```
but `file.json` is updated :
```json
{}
```

## 🗃️ Classes
### 👑 BaseModel
The **BaseModel class** is the base class for this project and defines all the attributes for the other classes

`Base = declarative_base()` : declaration that creates a base class for model definitions (in SQLAlchemy)

| Class attributes | Public instance methods |
| -------- | -------- | -------- |
| `id`    | `save`   |
| `created_at`    | `to_dict`    |
| `updated_at`    | `delete`   |

### 👶 Others Classes
#### 🚨 Inherits  from `BaseModel`

| Class names | `__tablename__` | Class Attributes |
| -------- | -------- | -------- |
| User   |  `users`   | `email`  / `password` / `first_name` / `last_name`      |
| State    | `states`   | `name`   |
| City    |   `cities`  | `state_id` / `name`    |
| Amenity    |  `amenities`   | `name`    |
| Place    |   `places`  | `city_id`  / `user_id` / `name` / `description` / `number_rooms` / `number_bathrooms` / `max_guest` / `price_by_night` / `latitude` / `longitude` / `amenity_ids`    |
| Review    |  `reviews`  | `place_id` / `user_id` / `text`    |

<br>
<br>

# 📦 Storage
## 🚨 Our main focus here
### 1️⃣ FileStorage mode
The `FileStorage` class is used to save and load data from a JSON file.

It acts as a bridge between the application's objects and a file, ensuring data persistence, it allows the application to store and retrieve instances of various classes efficiently.

Environmental variable : `HBNB_TYPE_STORAGE=file`.

In `FileStorage` mode, each time the backend is initialized, an instance of FileStorage named storage is created. This object is loaded or reloaded with the class instances that are stored in the JSON file. The storage is responsible for tracking these changes and updating the `file.json` accordingly. It ensures that the data in the JSON file accurately reflects the current state of the class instances.

| Public instance methods | Private class attributes |
| -------- | -------- |
| `all`    | `file_path`    |
| `new`   | `objects`   |
| `save`    | -    |
| `reload`    | -    |
| `delete`    | -    |

### 2️⃣ DBStorage mode
The `DBStorage` mode is the new engine we added in this step and is run by setting the environmental variables `HBNB_TYPE_STORAGE=db`.

| Public instance methods | Private class attributes |
| -------- | -------- |
| `all`    | `__engine`    |
| `new`   | `__session`   |
| `save`    | -    |
| `reload`    | -    |
| `delete`    | -    |

The object created after each initialization is loaded or reloaded from the MySQL database specified in this environmental variables :
- `HBNB_ENV` : running environment ("dev" or "test")
- `HBNB_MYSQL_USER` : username of MySQL
- `HBNB_MYSQL_PWD` : password of MySQL
- `HBNB_MYSQL_HOST` : hostname of MySQL
- `HBNB_MYSQL_DB`: database name of MySQL

The connection and querying processes are facilitated through SQLAlchemy.

You will find in this repository, this two scripts :
- `setup_mysql_dev.sql` : for database `hbnb_dev_db`
- `setup_mysql_test.sql` : for database `hbnb_test_db`

to configure `hbnb_dev_db` and `hbnb_test_db` databases on a MySQL server.

These two scripts enable you to set up the databases you need for the DBStorage mode to work properly.

#### 📺 Output example for DBStorage
- To create a user :
```bash
echo 'create User email="tetris@dog.go" password="dogpwd" first_name="Tetris" last_name="Pumpkins"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```
output ⤵️
```bash
(hbnb)
76a239c3-b5fd-4302-bed0-11b5fe05afe0
(hbnb)
```
- Check if everything has been entered correctly :
```bash
echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```
output ⤵️
```bash
(hbnb)
[[User] (76a239c3-b5fd-4302-bed0-11b5fe05afe0) {'first_name': 'Tetris', 'last_name': 'Pumpkins', 'created_at': datetime.datetime(2023, 12, 1, 11, 1, 6), 'updated_at': datetime.datetime(2023, 12, 1, 11, 1, 6), 'email': 'tetris@dog.go', 'password': 'dogpwd', 'id': '76a239c3-b5fd-4302-bed0-11b5fe05afe0'}]
(hbnb)
```
```bash
echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password:
```
output ⤵️
```bash
*************************** 1. row ***************************
     email: tetris@dog.go
  password: dogpwd
first_name: Tetris
 last_name: Pumpkins
        id: 76a239c3-b5fd-4302-bed0-11b5fe05afe0
created_at: 2023-12-01 11:01:06
updated_at: 2023-12-01 11:01:06
```

## 💪 Testing
Unittests for this project are defined in the `tests` folder.
You can run the entire test suite by using the following command :
```bash
python3 -m unittest discover tests
```

## 👥 Team
### V1 :
- Justin Majetich
- Ezra Nobrega

### V2 :
- 👨‍💻 Mickaël Tartar aka [mickaeltartar](https://github.com/mickaeltartar)
- 🥦 Valentine Quignon aka [ValPumpkins](https://github.com/ValPumpkins)
