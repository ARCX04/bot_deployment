import subprocess
import logging

# Configure logging
def configure_logging():
    logging.basicConfig(filename='spotify_downloader.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

# Improved function to download Spotify song
def download_spotify_song(song_url):
    try:
        # Execute the spotdl command
        result = subprocess.run(['spotdl', song_url], capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            logging.info(f'Successfully downloaded: {song_url}')
        else:
            logging.error(f'Error downloading song: {result.stderr}')
            return f'Error: {result.stderr}'
    except Exception as e:
        logging.critical(f'An exception occurred: {str(e)}')
        return f'Critical Error: {str(e)}'\n
# Call this function to set up logging
configure_logging()