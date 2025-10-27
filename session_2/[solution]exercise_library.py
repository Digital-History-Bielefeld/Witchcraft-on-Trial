# Now we want to use a library to get information from Wikipedia. The library is called `wikipedia`. 

# First you need to install the library. Go to the terminal below (the spooky part where you can type commands) and type the following command:
# pip install wikipedia

# When the installation is done, you can use the library in your code. 
# First you need to import the library with the command `import wikipedia`. Write this below.

import wikipedia

# Now you can use the library to get information from Wikipedia.
# Use the function `wikipedia.summary("witch hunts")` to get a summary of the Wikipedia article about witch hunts. Save the result in a variable called `summary`.
# Print the result to see the output.

# your code here:
summary = wikipedia.summary("witch hunts")
print(summary)


# Now run your script with the run button in the top right corner of this window or by typing `python3 session_2/exercise_library.py` in the terminal.
