# Starter code for an adventure type game.
# University of Utah, David Johnson, 2017.
# This code, or code derived from this code, may not be shared without permission.

# Changes date: 11/30/18 2:00pm

import sys, pygame, math

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_piskell_sprite(sprite_folder_name, number_of_frames):
    frame_counts = []
    padding = math.ceil(math.log(number_of_frames,10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding,'0') +".png"
        frame_counts.append(pygame.image.load(folder_and_file_name).convert_alpha())

    return frame_counts

# The main loop handles most of the game
def main():

    # Initialize pygame
    pygame.init()

    screen_size = height, width = (700, 500)
    screen = pygame.display.set_mode(screen_size)

    # create the hero character
    hero = load_piskell_sprite("hero",1)
    hero_rect = hero[0].get_rect()
    hero_rect.center = (350,250)

    # add in monster
    monster = pygame.image.load("monster.png").convert_alpha()
    monster_rect = monster.get_rect()
    monster_rect.center = 100, 200

    # add in Merchant
    merchant = pygame.image.load("merchant.png").convert_alpha()
    merchant_rect = merchant.get_rect()
    merchant_rect.center = 75, 395

    # add in a key item
    key = pygame.image.load("key.png").convert_alpha()
    key_rect = key.get_rect()
    key_rect.center = 250, 400

    # add in a sword item
    sword = pygame.image.load("sword.png").convert_alpha()
    sword_rect = sword.get_rect()
    sword_rect.center = 100, 400

    # add in a chest item
    chest = pygame.image.load("chest.png").convert_alpha()
    chest_rect = chest.get_rect()
    chest_rect.center = 500, 250

    # add in a door
    door = pygame.image.load("door.png").convert_alpha()
    door_rect = door.get_rect()
    door_rect.center = 500, 400

    # add the beast
    beast = pygame.image.load("beast.png").convert_alpha()
    beast_rect = beast.get_rect()
    beast_rect.center = 300, 400

    # add the axe
    axe = pygame.image.load("axe.png").convert_alpha()
    axe_rect = axe.get_rect()
    axe_rect.center = 200, 400

    door_02 = pygame.image.load("door_02.png").convert_alpha()
    door_02_rect = door_02.get_rect()
    door_02_rect.center = 200, 300

    creature = pygame.image.load("creature.png").convert_alpha()
    creature_rect = creature.get_rect()
    creature_rect.center = 200, 500

    mystical_god = pygame.image.load("mystical_god.png").convert_alpha()
    mystical_god_rect = mystical_god.get_rect()
    mystical_god_rect.center = 200, 200

    boss = pygame.image.load("boss.png").convert_alpha()
    boss_rect = boss.get_rect()
    boss_rect.center = 300, 400

    quest_01 = pygame.image.load("quest_01.png").convert_alpha()
    quest_01_rect = quest_01.get_rect()
    quest_01_rect.center = 400, 100

    quest_02 = pygame.image.load("quest_02.png").convert_alpha()
    quest_02_rect = quest_02.get_rect()
    quest_02_rect.center = 400, 200

    button = pygame.image.load("button.png").convert_alpha()
    button_rect = button.get_rect()
    button_rect.center = 400, 200

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Mostly used to cycle the animation of sprites
    frame_count = 0;

    # variable to show if we are still playing the game
    playing = True

    # variable for hero direction
    is_facing_left = True

    # Variable to track text on the screen. If you set the dialog string to something and set the position and the
    # counter, the text will show on the screen for dialog_counter number of frames.
    dialog_counter = 0
    dialog = ''
    dialog_position = (0,0)

    # Load font
    pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 20)


    # create the inventory and make it empty
    inventory = {}

    # This list should hold all the sprite rectangles that get shifted with a key press.
    rect_list = [monster_rect, key_rect, sword_rect, chest_rect, merchant_rect, door_rect, beast_rect, axe_rect, door_02_rect, mystical_god_rect, boss_rect, creature_rect, quest_01_rect, quest_02_rect, button_rect]

    level_3 = False
    level_2 = False
    show_beast = False
    quest1 = False
    quest2 = False

    #Level 1 variables:
    level_1_over = False
    necklace = False
    fuckyou = False

    # Loop while the player is still active
    while playing:
        # start the next frame
        screen.fill((0,150,25))

        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        # check for keys that are pressed
        # Note the indent makes it part of the while playing but not part of the for event loop.
        keys = pygame.key.get_pressed()
        # check for specific keys
        # movement says how the world should shift. Pressing keys changes the value in the movement variables.
        movement_x = 0
        movement_y = 0
        if keys[pygame.K_LEFT]:
            is_facing_left = True
            movement_x += 10
        if keys[pygame.K_RIGHT]:
            is_facing_left = False
            movement_x -= 10
        if keys[pygame.K_UP]:
            movement_y += 10
        if keys[pygame.K_DOWN]:
            movement_y -= 10

        # Move all the sprites in the scene by movement amount.
        # You can still move the rect of an individual sprite to make
        # it move around the landscape.
        for rect in rect_list:
            rect.move_ip(movement_x, movement_y)

        # Check for touching chest.
        if hero_rect.colliderect(chest_rect) and "coins" not in inventory and "key" in inventory:
            inventory["coins"] = True
            dialog = "Coins picked up!"
            dialog_counter = 30
        else:
            if hero_rect.colliderect(chest_rect) and "coins" not in inventory and "key" not in inventory:
                dialog = "Requires key!"
                dialog_counter = 30

        # Check for touching key.
        if hero_rect.colliderect(key_rect) and "key" not in inventory:
            inventory ["key"] = True
            dialog = "Key picked up!"
            dialog_counter = 30

        if hero_rect.colliderect(mystical_god_rect):
            dialog = "Quest received!"
            dialog_counter = 30

        if hero_rect.colliderect(axe_rect) and "creature" in inventory:
            inventory ["axe"] = True
            dialog = "Axe picked up!"
            dialog_counter = 30

        if hero_rect.colliderect(creature_rect) and "creature" not in inventory:
            inventory["creature"] = True
            dialog = "Creature picked up!"
            dialog_counter = 30

        if hero_rect.colliderect(beast_rect):
            if "axe" or "sword" in inventory:
                dead_beast = True
                dialog = "You killed me!"
                dialog_counter = 30

        # Check for touching door.
        if hero_rect.colliderect(door_rect):
            dialog = "Teleporting!"
            dialog_counter = 30

# 1st level stuff
        if level_1_over == False:

            #Mystical God appears
            screen.blit(mystical_god, mystical_god_rect)

            if hero_rect.colliderect(mystical_god_rect):
                necklace = True
                dialog = "Now you may travel through the portal"
                dialog_counter = 30

            if necklace == True:
                screen.blit(button, button_rect)

            if hero_rect.colliderect(button_rect):
                inventory["necklace"] = True
                dialog = "You picked up the magic necklace!"
                dialog_counter = 30
                necklace = False
                fuckyou = True

            if fuckyou == True:
                screen.blit(door, door_rect)

# Add 2nd level stuff
        if hero_rect.colliderect(door_rect):
            level_1_over = True
            level_2 = True
            quest1 = True
            quest2 = True

        if quest1 == True:
            screen.blit(quest_01, quest_01_rect)
        if quest2 == True:
            screen.blit(quest_02, quest_02_rect)
        if level_2 == True:

            # Draw the characters
            screen.blit(merchant, merchant_rect)
            screen.blit(door_02, door_02_rect)

            if hero_rect.colliderect(quest_01_rect):
                quest1 = False
                quest2 = False

                dialog = "New Quest: Get coins to buy the sword from the merchant"
                dialog_counter = 30

            if "key" not in inventory:
                screen.blit(key, key_rect)

            if "coins" not in inventory:
                screen.blit(chest, chest_rect)

            if hero_rect.colliderect(merchant_rect) and "coins" in inventory:
                screen.blit(sword, sword_rect)
                inventory["sword"] = True
                dialog = "Here is your sword!"
                dialog_counter = 30
            else:
                if hero_rect.colliderect(merchant_rect) and "coins" not in inventory:
                    dialog = "I need coins in exchange for the sword!"
                    dialog_counter = 30

            if hero_rect.colliderect(quest_02_rect):
                quest1 = False
                quest2 = False

                dialog = "New Quest: Catch the creature for the merchant to get the axe"
                dialog_counter = 30

            if "creature" not in inventory:
                screen.blit(creature, creature_rect)

            if "creature" in inventory:
                screen.blit(axe, axe_rect)
                dialog = "Thank you! Here is the axe."
                dialog_counter = 30
            else:
                if hero_rect.colliderect(merchant_rect) and "creature" not in inventory:
                    dialog = "Catch that creature for me!"
                    dialog_counter = 30

            if hero_rect.colliderect(axe_rect):
                inventory["axe"] = True
                dialog = "You picked up the axe!"
                dialog_counter = 30
# Add 3nd level stuff.
        if hero_rect.colliderect(door_02_rect):
            level_2 = False
            level_3 = True
            show_beast = True

        if level_3 == True:
            if show_beast == True:
                screen.blit(beast, beast_rect)
            if hero_rect.colliderect(beast_rect):
                show_beast = False
                dialog = "You killed me!"
                dialog_counter = 20
                dialog = "YOU WIN!"
                dialog_counter = 50


        # Pick the sprite frame to draw
        hero_sprite = hero[frame_count%len(hero)]
        # Flip the sprite depending on direction
        if not is_facing_left:
            hero_sprite = pygame.transform.flip(hero_sprite, True, False)
        screen.blit(hero_sprite, hero_rect)

        # draw any dialog
        if dialog:
            pygame.draw.rect(screen, (200,220,220), (50,425, 600, 50))
            textsurface = myfont.render(dialog, False, (0, 0, 0))
            screen.blit(textsurface, (75, 430,))

            # Track how long the dialog is on screen
            dialog_counter -= 1
            if dialog_counter == 0:
                dialog = ''

        # Bring drawn changes to the front
        pygame.display.update()

        frame_count += 1

        # 30 fps
        clock.tick(30)

    # loop is over
    pygame.quit()
    sys.exit()

# Start the program
main()
