class TowersOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.rods = {
            'A': list(range(num_disks, 0, -1)),
            'B': [],
            'C': []
        }
        self.move_count = 0
    
    def display(self):
        print("A:", self.rods['A'])
        print("B:", self.rods['B'])
        print("C:", self.rods['C'])
        print()
        
    def move_disk(self, from_rod, to_rod):
        if self.rods[from_rod] and (not self.rods[to_rod] or self.rods[from_rod][-1] < self.rods[to_rod][-1]):
            disk = self.rods[from_rod].pop()
            self.rods[to_rod].append(disk)
            self.move_count += 1
            return True
        return False
    
    def is_solved(self):
        return len(self.rods['C']) == self.num_disks
    
    def play(self):
        while not self.is_solved():
            self.display()
            move = input("Enter your move (e.g., A C to move from A to C) or type 'exit' to quit:")
            if move.lower() == 'exit':
                print("Exiting the game.")
                return
            try:
                from_rod, to_rod = move.split()
                if self.move_disk(from_rod.upper(), to_rod.upper()):
                    continue
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input format. Please enter ywo rod names (e.g., A C).")
            print("You Win! Total moves:", self.move_count)
            
if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))
    game = TowersOfHanoi(num_disks)
    game.play()
    