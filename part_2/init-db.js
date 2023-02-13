db = db.getSiblingDB("animal_db");
db.animal_tb.drop();

db.animal_tb.insertMany([
    {
        "id": 1,
        "CPU_Info": "10",
        "Memory_Info": "500"
    },
    {
        "id": 2,
        "CPU_Info": "7.8",
        "Memory_Info": "350"
    },
    {
        "id": 3,
        "CPU_Info": "4.5",
        "Memory_Info": "150"
    },
]);