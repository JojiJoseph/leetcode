class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.n_big = big
        self.n_medium = medium
        self.n_small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.n_big:
                self.n_big -= 1
                return True
        if carType == 2 and self.n_medium:
                self.n_medium -= 1
                return True
        if carType == 3 and self.n_small:
                self.n_small -= 1
                return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)