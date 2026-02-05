# Updated spotdl command in main.py to include better error handling and output format specification

# Code before line 215

try:
    spotdl_command = 'spotdl --format mp3 --output "{output}"'
    # Add logic for output template improvement
    # For instance, changing output to include artist and title.
    output_template = 'Output to: {artist} - {title} (Download Complete)'
    # Assuming a function that runs this command
    run_command(spotdl_command.format(output=output_template))
except Exception as e:
    print(f'An error occurred: {e}')
    # Include additional logging or error handling

# Code after line 215