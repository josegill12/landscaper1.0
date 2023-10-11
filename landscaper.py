class Player:
    def __init__(self):
        self.money = 0
        self.tool = "teeth"
        self.efficiency = 1  # Amount of grass you can cut at once with your current tool

    def earn_money(self, amount):
        self.money += amount
        print(f"You earned ${amount}! You now have ${self.money}.")

    def buy_tool(self, tool, cost, efficiency):
        if self.money >= cost:
            self.money -= cost
            self.tool = tool
            self.efficiency = efficiency
            print(f"You bought a {tool}! Your efficiency is now {efficiency}x.")
        else:
            print(f"You don't have enough money to buy the {tool}!")

    def cut_grass(self):
        grass_cut = self.efficiency * 10
        earnings = grass_cut // 10
        self.earn_money(earnings)
        print(f"You cut {grass_cut} square meters of grass with your {self.tool} and earned ${earnings}.")

def main():
    player = Player()
    while True:
        print("\nOptions:")
        print("1. Cut grass")
        print("2. Shop for tools")
        print("3. Check balance and tool")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.cut_grass()
        elif choice == "2":
            print("\nShop:")
            print("1. Scissors - $50 (2x efficiency)")
            print("2. Lawnmower - $200 (5x efficiency)")
            print("3. Super Lawnmower - $500 (10x efficiency)")
            tool_choice = input("Choose a tool or press any key to exit: ")

            if tool_choice == "1":
                player.buy_tool("Scissors", 50, 2)
            elif tool_choice == "2":
                player.buy_tool("Lawnmower", 200, 5)
            elif tool_choice == "3":
                player.buy_tool("Super Lawnmower", 500, 10)
            else:
                print("Exiting shop.")
        elif choice == "3":
            print(f"\nYou have ${player.money} and your current tool is {player.tool} with {player.efficiency}x efficiency.")
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()
