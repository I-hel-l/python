class Giraffes:
    def left_foot_forward(self):
        print("Left_foot_forward!")
    def left_foot_back(self):
        print("Left_foot_back!")
    def right_foot_forward(self):
        print("Right_foot_forward!")
    def right_foot_back(self):
        print("Right_foot_back!")
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()

reginald = Giraffes()
reginald.dance()

