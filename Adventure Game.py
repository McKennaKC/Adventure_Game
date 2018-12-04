# Starter code for an adventure type game.
# University of Utah, David Johnson, 2017.
# This code, or code derived from this code, may not be shared without permission.

# Changes date: 12/1

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

    screen_size = width, height = (700, 500)
    screen = pygame.display.set_mode(screen_size)

    # create the hero character
    # hero = load_piskell_sprite("hero",1)
    # hero_rect = hero[0].get_rect()
    # hero_rect.center = (350,250)

    # This function loads a series of sprite images stored in a folder with a
    # consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.

    def load_piskell_sprite(sprite_folder_name, number_of_frames):
        frame_counts = []
        padding = math.ceil(math.log(number_of_frames, 10))
        for frame in range(number_of_frames):
            folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
            frame_counts.append(pygame.image.load(folder_and_file_name).convert_alpha())

        return frame_counts

    hero_walk = load_piskell_sprite("hero_walk", 12)
    hero_walk_rect = hero_walk[0].get_rect()
    hero_walk_rect.center = (350, 250)



#Level 1 sprites:

    # add in a door
    door = pygame.image.load("door.png").convert_alpha()
    door_rect = door.get_rect()
    door_rect.center = 500, 400

    # add the mystical god
    mystical_god = pygame.image.load("mystical_god.png").convert_alpha()
    mystical_god_rect = mystical_god.get_rect()
    mystical_god_rect.center = 200, 200

    # add the button
    button = pygame.image.load("button.png").convert_alpha()
    button_rect = button.get_rect()
    button_rect.center = 400, 200

#Level 2 sprites:

    # add the 2nd level background assets
    floors_2 = pygame.image.load("floors_2.png").convert_alpha()
    floors_2_rect = floors_2.get_rect()
    floors_2_rect.center = 500, 400

    walls_2 = pygame.image.load("walls_2.png").convert_alpha()
    walls_2_rect = walls_2.get_rect()
    walls_2_rect.center = 500, 400

    stuff_2 = pygame.image.load("stuff_2.png").convert_alpha()
    stuff_2_rect = stuff_2.get_rect()
    stuff_2_rect.center = 500, 400

    foliage_2 = pygame.image.load("foliage_2.png").convert_alpha()
    foliage_2_rect = foliage_2.get_rect()
    foliage_2_rect.center = 500, 400

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
    sword_rect.center = 10, 400

    # add in a chest item
    chest = pygame.image.load("chest.png").convert_alpha()
    chest_rect = chest.get_rect()
    chest_rect.center = 500, 250

    # add in a door
    door = pygame.image.load("door.png").convert_alpha()
    door_rect = door.get_rect()
    door_rect.center = 500, 400

    # add the axe
    axe = pygame.image.load("axe.png").convert_alpha()
    axe_rect = axe.get_rect()
    axe_rect.center = 150, 400

    # add the axe icon
    axe_icon = pygame.image.load("axe_icon.png").convert_alpha()
    axe_icon_rect = axe_icon.get_rect()
    axe_icon_rect.center = 20, 50

    door_02 = pygame.image.load("door_02.png").convert_alpha()
    door_02_rect = door_02.get_rect()
    door_02_rect.center = 200, 300

    creature = pygame.image.load("creature.png").convert_alpha()
    creature_rect = creature.get_rect()
    creature_rect.center = 200, 500

    # add the creature icon
    creature_icon = pygame.image.load("creature_icon.png").convert_alpha()
    creature_icon_rect = creature_icon.get_rect()
    creature_icon_rect.center = 20, 50

    # add the coins icon
    coins_icon = pygame.image.load("coins_icon.png").convert_alpha()
    coins_icon_rect = coins_icon.get_rect()
    coins_icon_rect.center = 20, 80

    # add the key icon
    key_icon = pygame.image.load("key_icon.png").convert_alpha()
    key_icon_rect = key_icon.get_rect()
    key_icon_rect.center = 20, 80

    # add the sword icon
    sword_icon = pygame.image.load("sword_icon.png").convert_alpha()
    sword_icon_rect = sword_icon.get_rect()
    sword_icon_rect.center = 20, 80

    mystical_god = pygame.image.load("mystical_god.png").convert_alpha()
    mystical_god_rect = mystical_god.get_rect()
    mystical_god_rect.center = 200, 200

    # add the axe icon
    inventory_icon = pygame.image.load("inventory_icon.png").convert_alpha()
    inventory_icon_rect = inventory_icon.get_rect()
    inventory_icon_rect.center = 20, 20

    inventory_words = pygame.image.load("inventory_words.png").convert_alpha()
    inventory_words_rect = inventory_words.get_rect()
    inventory_words_rect.center = 22, 10

    # add 2nd door
    door_02 = pygame.image.load("door_02.png").convert_alpha()
    door_02_rect = door_02.get_rect()
    door_02_rect.center = 200, 300

    # add the creature
    # creature = pygame.image.load("creature.png").convert_alpha()
    # creature_rect = creature.get_rect()
    # creature_rect.center = 200, 500
    # creature = load_piskell_sprite("creature", 4)
    # creature_rect = creature[0].get_rect()
    # creature_rect.center = (200, 500)

    # add the first quest
    quest_01 = pygame.image.load("quest_01.png").convert_alpha()
    quest_01_rect = quest_01.get_rect()
    quest_01_rect.center = 400, 100

    # add the second quest
    quest_02 = pygame.image.load("quest_02.png").convert_alpha()
    quest_02_rect = quest_02.get_rect()
    quest_02_rect.center = 400, 200

#Level 3 sprites:

    # add the beast
    beast = pygame.image.load("beast.png").convert_alpha()
    beast_rect = beast.get_rect()
    beast_rect.center = 300, 400

    # add the beast running away
    beast_run = load_piskell_sprite("beast_run", 6)
    beast_run_rect = beast_run[0].get_rect()
    beast_run_rect.center = (350, 250)

#Level 4 sprites:

    # add the boss
    boss = load_piskell_sprite("boss", 6)
    boss_rect = boss[0].get_rect()
    boss_rect.center = (350, 250)

    boss_attack = load_piskell_sprite("boss_attack", 25)
    boss_attack_rect = boss_attack[0].get_rect()
    boss_attack_rect.center = (350, 250)



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
    rect_list = [key_rect, sword_rect, chest_rect, merchant_rect, door_rect, beast_rect, beast_run_rect, axe_rect, door_02_rect, mystical_god_rect, boss_rect, boss_attack_rect, creature_rect, quest_01_rect, quest_02_rect, button_rect, floors_2_rect, walls_2_rect, stuff_2_rect, foliage_2_rect]

    #Level 1 variables:
    level_1_over = False
    necklace = False
    fuckyou = False

    #Level 2 variables:
    level_2 = False
    quest1 = False
    quest2 = False

    #Level 3 variables:
    level_3 = False
    show_beast = False

    blockade_list = [mystical_god_rect]

    # blockade_list.add(mystical_god)

    inventory["creature"] = False
    inventory["axe"] = False
    inventory["coins"] = False
    inventory["sword"] = False
    inventory["key"] = False
    sword_display = False
    axe_display = False
    creature_display = True
    key_display = True
    chest_display = True


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

        if keys[pygame.K_LEFT] and hero_walk_rect.collidelist(blockade_list) > 0:
            is_facing_left = True
            movement_x = 0
            print(movement_x, movement_y)
        elif keys[pygame.K_LEFT] and hero_walk_rect.collidelist(blockade_list) < 0:
            is_facing_left = True
            movement_x += 10

        if keys[pygame.K_RIGHT] and hero_walk_rect.collidelist(blockade_list) > 0:
            is_facing_left = False
            movement_x = 0
            print(movement_x, movement_y)
        elif keys[pygame.K_RIGHT] and hero_walk_rect.collidelist(blockade_list) < 0:
            is_facing_left = False
            movement_x -= 10

        if keys[pygame.K_UP] and hero_walk_rect.collidelist(blockade_list) > 0:
            movement_y = 0
            print(movement_x, movement_y)
        elif keys[pygame.K_UP] and hero_walk_rect.collidelist(blockade_list) < 0:
            movement_y += 10

        if keys[pygame.K_DOWN] and hero_walk_rect.collidelist(blockade_list) > 0:
            movement_y = 0
            print(movement_x, movement_y)
        elif keys[pygame.K_DOWN] and hero_walk_rect.collidelist(blockade_list) < 0:
            movement_y -= 10



        # if keys[pygame.K_LEFT] and hero_walk_rect.colliderec:
        #     is_facing_left = True
        #     movement_x += 0
        # elif keys[pygame.K_LEFT]:
        #     is_facing_left = True
        #     movement_x += 10
        #
        # if keys[pygame.K_RIGHT] and pygame.sprite.spritecollideany(blockade_list):
        #     is_facing_left = False
        #     movement_x -= 0
        # elif keys[pygame.K_RIGHT]:
        #     is_facing_left = False
        #     movement_x -= 10
        #
        # if keys[pygame.K_UP] and pygame.sprite.spritecollideany(blockade_list):
        #     movement_y += 0
        # elif keys[pygame.K_UP]:
        #     movement_y += 10
        #
        # if keys[pygame.K_DOWN] and pygame.sprite.spritecollideany(blockade_list):
        #     movement_y -= 0
        # elif keys[pygame.K_DOWN]:
        #     movement_y -= 10



        # Move all the sprites in the scene by movement amount.
        # You can still move the rect of an individual sprite to make
        # it move around the landscape.
        for rect in rect_list:
            rect.move_ip(movement_x, movement_y)
        # for rect in blockade_list:

        screen.blit(inventory_icon, inventory_icon_rect)
        screen.blit(inventory_words, inventory_words_rect)

        if inventory["axe"] == True:
            inventory["creature"] = False
            screen.blit(axe_icon, axe_icon_rect)

        if inventory["creature"] == True:
            screen.blit(creature_icon, creature_icon_rect)

        if inventory["coins"] == True:
            screen.blit(coins_icon, coins_icon_rect)

        if inventory["sword"] == True:
            screen.blit(sword_icon, sword_icon_rect)

        if inventory["key"] == True:
            screen.blit(key_icon, key_icon_rect)

        # #
        #
        # if hero_rect.colliderect(mystical_god_rect):
        #     dialog = "Quest received!"
        #     dialog_counter = 30
        #
        #
        # if hero_rect.colliderect(beast_rect):
        #     if "axe" or "sword" in inventory:
        #         dead_beast = True
        #         dialog = "You killed me!"
        #         dialog_counter = 30
        #
        # # Check for touching door.
        # if hero_rect.colliderect(door_rect):
        #     dialog = "Teleporting!"
        #     dialog_counter = 30

        # This function loads a series of sprite images stored in a folder with a
        # consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.


# 1st level stuff
        if level_1_over == False:

            # Draw Hero
            hero_walk_sprite = hero_walk[frame_count % len(hero_walk)]
            if not is_facing_left:
                hero_walk_sprite = pygame.transform.flip(hero_walk_sprite, True, False)
            screen.blit(hero_walk_sprite, hero_walk_rect)

            #Mystical God appears
            screen.blit(mystical_god, mystical_god_rect)

            #Gives necklace
            if hero_walk_rect.colliderect(mystical_god_rect):
                necklace = True
                dialog = "Now you may travel through the portal"
                dialog_counter = 30

                print(movement_x)
                print(movement_y)

            if necklace == True:
                screen.blit(button, button_rect)

            #Picks up necklace
            if hero_walk_rect.colliderect(button_rect):
                inventory["necklace"] = True
                dialog = "You picked up the magic necklace!"
                dialog_counter = 30
                necklace = False
                fuckyou = True

            #Portal appears
            if fuckyou == True:
                screen.blit(door, door_rect)




# Add 2nd level stuff
        if hero_walk_rect.colliderect(door_rect):
            level_1_over = True
            level_2 = True
            quest1 = True
            quest2 = True

        # Draw level 2 background
        if level_2 == True:
            # screen.blit(level2, level2_rect)

            screen.blit(floors_2, floors_2_rect)
            screen.blit(walls_2, walls_2_rect)
            screen.blit(stuff_2, stuff_2_rect)
            screen.blit(foliage_2, foliage_2_rect)

        # if hero_walk_rect.colliderect(walls_2_rect):
        #     if keys[pygame.K_LEFT]:
        #         is_facing_left = True
        #         movement_x -= 10
        #     if keys[pygame.K_RIGHT]:
        #         is_facing_left = False
        #         movement_x += 10
        #     if keys[pygame.K_UP]:
        #         movement_y -= 10
        #     if keys[pygame.K_DOWN]:
        #         movement_y += 10

        # Draw hero
        hero_walk_sprite = hero_walk[frame_count % len(hero_walk)]
        if not is_facing_left:
            hero_walk_sprite = pygame.transform.flip(hero_walk_sprite, True, False)
        screen.blit(hero_walk_sprite, hero_walk_rect)

        if quest1 == True:
            screen.blit(quest_01, quest_01_rect)
        if quest2 == True:
            screen.blit(quest_02, quest_02_rect)

            # Draw sprites
            screen.blit(merchant, merchant_rect)
            screen.blit(door_02, door_02_rect)

            if hero_walk_rect.colliderect(quest_01_rect):
                quest1 = False
                quest2 = False

                dialog = "New Quest: Get coins to buy the sword from the merchant"
                dialog_counter = 30


            if inventory["key"] == False and key_display == True:
                screen.blit(key, key_rect)

            if inventory["coins"] == False and chest_display == True:
                screen.blit(chest, chest_rect)

            # Check for touching chest.
            if hero_walk_rect.colliderect(chest_rect) and inventory["coins"] == False and inventory["key"] == True and chest_display == True:
                inventory["coins"] = True
                inventory["key"] = False
                key_display = False
                chest_display = False
                dialog = "Coins picked up!"
                dialog_counter = 30
            else:
                if hero_walk_rect.colliderect(chest_rect) and inventory["coins"] == False and inventory["key"] == False and chest_display == True:
                    dialog = "Requires key!"
                    dialog_counter = 30

            # Check for touching key.
            if hero_walk_rect.colliderect(key_rect) and inventory["key"] == False and key_display == True:
                inventory["key"] = True
                dialog = "Key picked up!"
                dialog_counter = 30

            if hero_walk_rect.colliderect(merchant_rect) and inventory["coins"] == True and inventory["sword"] == False:
                inventory["coins"] = False
                sword_display = True
                dialog = "Here is your sword!"
                dialog_counter = 30
            else:
                if hero_walk_rect.colliderect(merchant_rect) and inventory["coins"] == False and inventory["sword"] == False:
                    dialog = "I need coins in exchange for the sword!"
                    dialog_counter = 30

            if sword_display == True:
                screen.blit(sword, sword_rect)

            if hero_walk_rect.colliderect(sword_rect) and inventory["sword"] == False and sword_display == True:
                inventory["sword"] = True
                sword_display = False
                dialog = "Sword picked up!"
                dialog_counter = 30

            # if inventory["creature"] == False and inventory["axe"] == False and creature_display == True:
            #     screen.blit(creature, creature_rect)

            if hero_walk_rect.colliderect(creature_rect) and inventory["creature"] == False and creature_display == True:
                inventory["creature"] = True
                dialog = "Creature picked up!"
                dialog_counter = 30

            if hero_walk_rect.colliderect(merchant_rect) and inventory["creature"] == True and inventory["axe"] == False:
                inventory["creature"] = False
                creature_display = False
                axe_display = True
                dialog = "Thank you! Here is the axe."
                dialog_counter = 30
            else:
                if hero_walk_rect.colliderect(merchant_rect) and inventory["creature"] == False and creature_display == True:
                    dialog = "Catch that creature for me!"
                    dialog_counter = 30

            if axe_display == True and inventory["axe"] == False:
                screen.blit(axe, axe_rect)

            if hero_walk_rect.colliderect(axe_rect) and inventory["axe"] == False and inventory["creature"] == False and axe_display == True and creature_display == False:
                inventory["axe"] = True
                axe_display = False
                dialog = "You picked up the axe!"
                dialog_counter = 30




# Add 3nd level stuff.
#         if hero_rect.colliderect(door_02_rect):
#             level_2 = False
#             level_3 = True
#             show_beast = True
#
#         if level_3 == True:
#             if show_beast == True:
#                 screen.blit(beast, beast_rect)
#             if hero_rect.colliderect(beast_rect):
#                 show_beast = False
#                 dialog = "You killed me!"
#                 dialog_counter = 20
#                 dialog = "YOU WIN!"
#                 dialog_counter = 50

            # beast_run_sprite = beast_run[frame_count % len(beast_run)]
            # if not is_facing_left:
            #     beast_run_sprite = pygame.transform.flip(beast_run_sprite, True, False)
            # screen.blit(beast_run_sprite, beast_run_rect)




# Add 4th level stuff.
#         boss_sprite = boss[frame_count % len(boss)]
#         screen.blit(boss_sprite, boss_rect)
#
#         boss_attack_sprite = boss_attack[frame_count % len(boss_attack)]
#         screen.blit(boss_attack_sprite, boss_attack_rect)





        # Pick the sprite frame to draw
        # hero_sprite = hero[frame_count%len(hero)]
        # # Flip the sprite depending on direction
        # if not is_facing_left:
        #     hero_sprite = pygame.transform.flip(hero_sprite, True, False)
        # screen.blit(hero_sprite, hero_rect)

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
