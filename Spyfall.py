import discord
import random
import asyncio
import math
import os
from PIL import Image

# Setting bot intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize Discord client
client = discord.Client(intents=intents)

# Store the reference to the timer task
timer_task = None

# Put locations below, sync position with captioned image (0.png - Airport Terminal | 1.png - Avenegers Movie | etc.)
locations = ["Airport Terminal", "Avengers Movie", "Bioweapons Lab", "Bowling Alley", "Cafeteria", "City Park", "Concert Venue", "Corporate Office", "Gameshow", "Gym", "High-Stakes Poker Game", "Hogwarts Castle", "Hospital Waiting Room", "International Harbor", "Laboratory", "MI-6", "Movie Theater", "Mountain Cabin", "Polling Place", "Soap Opera", "Spy Convention", "Street Market", "Thrift Shop", "Wild West Town", "YouTuber Mansion", "Zoo", "Campsite"]

# Notifies user in Heroku that bot is ready
@client.event
async def on_ready():
    print('Bot is ready')

# Detects messages from users
@client.event
async def on_message(message):
    # Starts Game
    if message.content.startswith('!start_game'):
        await start_game(message)

    # Stops game
    elif message.content.startswith("!stop_game") or message.content.startswith("!end_game"):
        await end_game(message.channel)

# Starts timer
async def start_timer(channel):
    print("Starting Timer")

    timeRaw = 540
    message = await channel.send("Minutes Remaining: 9")

    # Count down timer
    while timeRaw != 0:
        timeRaw -= 1

        minutes = math.ceil(timeRaw / 60)

        ## Apply only when minute changes
        if(timeRaw % 60 == 0):
            await message.edit(content="Minutes Remaining: " + str(minutes))

        ## Wait on second
        await asyncio.sleep(1)

    # Timer completed
    await message.edit(content='Time Up!')
    await end_game(channel)

# Ends Timer
async def end_timer(channel):
    if(timer_task):
        timer_task.cancel()
        await channel.send("Game Ended")

# Starts game
async def start_game(message):
        global timer_task

        # End previous game
        await end_game(message.channel)

        users = message.mentions
        spy = random.choice(users)
        
        result = pickLocs(locations)
        location = random.choice(list(result.keys()))

        # Path to the images folder
        images_folder = "images"
        # List image filenames based on selected numbers
        selected_image_files = [os.path.join(images_folder, f"Captioned_{num}.jpg") for num in result.values()]

        # Load selected images
        images = [Image.open(image_file) for image_file in selected_image_files]
        # Create a 6x4 grid
        grid_image = create_image_grid(images, rows=4, cols=6)
        # Save the grid as a PNG file
        grid_image_path = "grid_image.png"
        grid_image.save(grid_image_path)

        # Send a message to the spy
        await spy.send(f"You are the spy, guess the location!")
        
        # Send a message to the rest of the players with the location
        for user in users:
            
            if user != spy:
                await user.send(f"You are not the spy, the location is: {location}. Guess the spy and win!")
            with open(grid_image_path, "rb") as file:
                await user.send(file=discord.File(file))

        # Start timer
        timer_task = asyncio.create_task(start_timer(message.channel))

# Ends game
async def end_game(channel):
    print("Ending Game")

    await end_timer(channel)


def pickLocs(array):
    if len(array) < 24:
        raise ValueError("Array length should be at least 24")

    result_dict = {}
    while (len(result_dict) < 24):
        temp = random.choice(array);
        if temp not in result_dict.keys():
            result_dict[temp] = array.index(temp)
    return result_dict

def create_image_grid(images, rows, cols, grid_size=(200, 200), background_color=(255, 255, 0)):
    grid_width = cols * grid_size[0]
    grid_height = rows * grid_size[1]
    grid = Image.new('RGB', (grid_width, grid_height), color=background_color)
    

    for i, img in enumerate(images):
        img = img.resize(grid_size)
        x = (i % cols) * grid_size[0]
        y = (i // cols) * grid_size[1]
        grid.paste(img, (x, y))

    return grid

# Run the bot with your Discord bot token
client.run('INPUT SECRET HERE')