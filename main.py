import game  # Import game logic
import ui    # Import user interface
import logging  # Import logging for error tracking

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        ui.initialize()  # Initialize the UI
        logging.info("UI initialized successfully.")
        
        game_instance = game.Game()  # Create a game instance
        logging.info("Game instance created.")
        
        game_instance.start_game()  # Start the game loop
        logging.info("Game started successfully.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()  # Run the main function
