staff_training_history = {
    "Yon": {
        "Training 1": {
            "Date": "2023-09-10",
            "Duration": "4 days",
            "Trainer": "Trainer C"
        },
        "Training 2": {
            "Date": "2023-10-20",
            "Duration": "11 days",
            "Trainer": "Trainer D"
        }
    },
    "Yogesh Raja":{
        "Training 1":{
            "Date" : "2023-11-08",
            "Duration": "8 days",
            "Trainer": "Trainer A"
        }
    },
    "Arularasu": {
        "Training 1": {
            "Date": "2023-08-15",
            "Duration": "2 weeeks",
            "Trainer": "Trainer A"
        },
        "Training 2": {
            "Date": "2023-10-25",
            "Duration": "25 days",
            "Trainer": "Trainer B"
        }
    },
    "shyam": {
        "Training 1": {
            "Date": "2023-10-10",
            "Duration": "10 days",
             "Trainer": "Trainer E"
        },
        "Training 2": {
            "Date": "2023-10-20",
            "Duration": "11 days",
            "Trainer": "Trainer F"
        },
        "Training 3": {
            "Date": "2023-10-20",
            "Duration": "11 days",
            "Trainer": "Trainer G"
        }
    }
}

def generate_training_history_report(staff_name):
    if staff_name in staff_training_history:
        print(f"Training history for {staff_name}:")
        for index, (training_name, training_info) in enumerate(staff_training_history[staff_name].items(), start=1):
            print(f"\nTraining {index}: {training_name}")
            print(f"Date: {training_info['Date']}")
            print(f"Duration: {training_info['Duration']}")
            print(f"Trainer: {training_info['Trainer']}")
    else:
        print(f"No training history found for {staff_name}.")

flow=1
while flow==1:
    print("""
Name of the staffs:
    1. Yon
    2. Yogesh Raja
    3. Arularasu
    4. Shyam 
""")
    staff_name = input("Enter the name : ")
    generate_training_history_report(staff_name)
    print("""
Do you want to see history for anyother else?
    if yes enter "1" else any other key to exit the program.
          """)
    if int(input()) != 1:
        flow = 0
    else:
        print()