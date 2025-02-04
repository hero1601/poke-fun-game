import random
from player import Player, AI

class Game:
    def __init__(self, players):
        self.players = players
        self.round_count = 0

    def assign_cards(self, cards):
        # Distribute the cards to the players
        random.shuffle(cards)
        for i, card in enumerate(cards):
            self.players[i % len(self.players)].add_cards(card)

    def play_round(self, stat_choice):
        self.round_count += 1

        print(f"Round {self.round_count} - {stat_choice} chosen")

        # Determine the winner based on the stat choice
        if stat_choice in ["HP", "Attack", "Defense", "Place"]:
            best_card = None
            winner = None
            cards_in_play = []
            stat_chosen = stat_choice.lower()
            for player in self.players:
                player_card = player.draw_card()
                cards_in_play.append(player_card)
                if stat_choice == "Place":
                    if best_card is None or getattr(player_card, stat_chosen) < getattr(best_card, stat_chosen):
                        best_card = player_card
                        winner = player
                else:
                    if best_card is None or getattr(player_card, stat_chosen) > getattr(best_card, stat_chosen):
                        best_card = player_card
                        winner = player
        else:
            raise ValueError("Invalid stat choice")
        
        
        for player, card in zip(self.players, cards_in_play):
            print(f"{player.name}: {card}")

        # Add the cards to the winner's deck
        winner.add_cards(cards_in_play)
        print(f"The winner of this round is {winner.name}!\n")
        return winner

    def start_game(self, player):
        # Start the game with each player choosing a stat for each round
        while True:
            if self.players[0].cards == [] or self.players[1].cards == []:
                break
            if isinstance(player, AI):  # AI plays automatically
                stat_choice = random.choice(["HP", "Attack", "Defense", "Place"])
                print(f"{player.name} (AI) chooses {stat_choice}")
            else:
                stat_choice = input(f"{player.name}, choose a stat (HP, Attack, Defense, Place): ")
            player = self.play_round(stat_choice)
        
        self.player_cards()
    

    def player_cards(self):
        for player in self.players:
            print(f"{player.name}: {player.cards}\n")
