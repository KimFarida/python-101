class Workout:
    def __init__(self, activity_type):
        self.activity_type = activity_type
        self.duration = 0
        self.calories = 0
        self.is_completed = False

    def start_workout(self, duration):
        self.duration = duration
        if self.activity_type == "running":
            self.calories = duration * 10
        elif self.activity_type == "swimming":
            self.calories = duration * 15
        print(f"Started {self.activity_type} workout for {duration} minutes")

    def complete_workout(self):
        self.is_completed = True
        print(f"Completed! Burned {self.calories} calories")


# Usage
morning_run = Workout("running")
morning_run.start_workout(30)
morning_run.complete_workout()