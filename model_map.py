from models import *


db_map = {
    CardModel: ["name", "order", "description", "table"],
    TableModel: ["name", "board"],
    BoardModel: ["name", "team"],
    TeamModel: ["name"],
    UserModel: ["name", "username", "email", "password"]
}
