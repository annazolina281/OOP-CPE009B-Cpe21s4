import random
from Character import Character
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

class Game:
    def __init__(self):
        self.single_player_wins = 0
        self.current_role = Novice
        self.roles = {
            0: Novice,      # 0 wins: Novice
            1: Swordsman,   # 1 win: Swordsman
            2: Archer,      # 2 wins: Archer
            3: Magician     # 3 wins: Magician
        }
        self.mode = None

    def start_game(self):
        print("Welcome to the game!")
        self.select_mode()  # Select mode at the start

    def select_mode(self):
        while self.mode not in ["1", "2"]:
            self.mode = input("Select game mode (1 for Single Player, 2 for Player vs Player): ")
            if self.mode not in ["1", "2"]:
                print("Invalid mode. Please select a valid mode.")
        
        if self.mode == "1":
            self.single_player_mode()
        elif self.mode == "2":
            self.player_vs_player_mode()

    def single_player_mode(self):
        while True:
            player = self.current_role("Player")
            boss = Boss("Monster")
            self.set_boss_stats(boss)
            self.play_match(player, boss)
            if player.getHp() > 0:  # Only allow role change if player won
                self.single_player_wins += 1
                self.change_role()

            if not self.play_again():
                break  # Exit single player mode

        self.reset_game()

    def player_vs_player_mode(self):
        while True:
            player1 = self.select_role("Player 1")
            player2 = self.select_role("Player 2")
            self.play_match(player1, player2)

            if not self.play_again():
                break  # Exit player vs player mode

        self.reset_game()

    def change_role(self):
        if self.single_player_wins in self.roles:
            self.current_role = self.roles[self.single_player_wins]
            print(f"You have upgraded to {self.current_role.__name__}!")
        else:
            print("You are already at the highest level (Magician).")

    def select_role(self, player_name):
        print(f"Select a role for {player_name}:")
        for num, role in self.roles.items():
            print(f"{num}: {role.__name__}")
        role_choice = input("Enter the number of your chosen role: ")
        return self.roles.get(int(role_choice), Novice)(player_name)

    def play_match(self, player1, player2):
        print(f"\n{player1.getUsername()} vs {player2.getUsername()}")
        while player1.getHp() > 0 and player2.getHp() > 0:
            for player in [player1, player2]:
                print(f"\n{player.getUsername()}'s turn")
                action = input("Enter 'a' to attack or 'h' to heal: ").strip().lower()

                if action == 'a':
                    player.basicAttack(player2 if player == player1 else player1)
                elif action == 'h' and isinstance(player, Magician):
                    player.heal()
                else:
                    if action == 'h':
                        print("Only Magician can heal.")
                    else:
                        print("Invalid action. Please enter 'a' or 'h'.")
                    continue

                # Display HP after action
                print(f"{player1.getUsername()} HP: {player1.getHp()}")
                print(f"{player2.getUsername()} HP: {player2.getHp()}")

        if player1.getHp() <= 0:
            print(f"{player2.getUsername()} wins!")
        else:
            print(f"{player1.getUsername()} wins!")

    def set_boss_stats(self, boss):
        # Set Boss stats based on player's win count
        if self.single_player_wins < 2:
            boss.setHp(50)  # Easy level Boss HP
            boss.setDamage(5)  # Easy level Boss Damage
        elif self.single_player_wins < 5:
            boss.setHp(75)  # Medium level Boss HP
            boss.setDamage(10)  # Medium level Boss Damage
        else:
            boss.setHp(100)  # Hard level Boss HP
            boss.setDamage(15)  # Hard level Boss Damage

    def play_again(self):
        return input("Do you want to play again? (y/n): ").strip().lower() == 'y'

    def reset_game(self):
        # Reset for a new game session
        self.single_player_wins = 0
        self.current_role = Novice
        self.mode = None  # Reset mode selection

if __name__ == "__main__":
    game = Game()
    game.start_game()
