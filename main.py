from card import Card, read_cards
from player import Player, AI
from game import Game


def main():
    # Create cards for the game
    cards = read_cards("poke-cards.csv")

    # Create players
    player1 = Player("Player 1")
    ai_player = AI("AI")

    # Initialize the game
    game = Game([player1, ai_player])

    # Distribute the cards to the players
    game.assign_cards(cards)

    # Start the game
    game.start_game(player1)

if __name__ == "__main__":
    main()