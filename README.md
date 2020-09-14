# Ghost Invasion Game in Python [Completed]



### Preview : 

<p align="center">
	<img src="https://github.com/j471n/ghost-invasion-game-python/blob/master/Ghost%20Invasion%20Game/images/preview.gif">
</p>
<br>

## Table of Contents

- [Creating a Pygame Window and Responding to User Input](#1)

- [Setting the Background Color](#2)

- [Creating a Settings Class](#3)

- [Adding the Ship Image](#4)

- [Drawing the Ship to the Screen](#5)

- [Refactoring: The _check_events() and _update_screen() Methods](#6)

	- [The _check_events() Method](#6.1)

	- [The _update_screen() Method](#6.2)

- [Piloting the Ship](#7)

	- [Responding to a Keypress](#7.1)

	- [Allowing Continuous Movement](#7.2)

	- [Moving Both Left and Right](#7.3)

	- [Adjusting the Ship’s Speed](#7.4)

	- [Limiting the Ship’s Range](#7.5)

	- [Refactoring _check_events() and Pressing Q to Quit](#7.6)

	- [Running the Game in Fullscreen Mode](#7.7)

- [Shooting Bullets](#8)

	- [Adding the Bullet Settings](#8.1)

	- [Creating the Bullet Class](#8.2)

	- [Storing Bullets in a Group](#8.3)

	- [Firing Bullets](#8.4)

	- [Deleting Old Bullets](#8.5)

	- [Limiting the Number of Bullets](#8.6)

	- [Creating the _update_bullets() Method](#8.7)

- [Error : Occured](#9)

- [Creating a First Ghost](#10)

	- [Creating the Ghost Class](#10.1)

	- [Creating an Instance of the Ghost](#10.2)

- [Building the Ghost Fleet](#11)

	- [Determining How Many Ghosts Fit in a Row](#11.1)

	- [Creating a Row of Ghosts](#11.2)

	- [Refactoring _create_fleet()](#11.3)

	- [Adding Rows](#11.4)

- [Making the Fleet Move](#12)

	- [Moving the Ghosts Right](#12.1)

	- [Creating Settings for Fleet Direction](#12.2)

	- [Checking Whether an Ghost Has Hit the Edge](#12.3)

	- [Dropping the Fleet and Changing Direction](#12.4)

- [Shooting Ghosts](#13)

	- [Detecting Bullet Collisions](#13.1)

	- [Repopulating the Fleet](#13.2)

	- [Refactoring _update_bullets()](#13.3)

- [Ending the Game](#14)

	- [Detecting Ghost and Ship Collisions](#14.1)

	- [Responding to Ghost and Ship Collisions](#14.2)

	- [Ghosts that Reach the Bottom of the Screen](#14.3)

	- [Game Over!](#14.4)

	- [Identifying When Parts of the Game Should Run](#14.5)

- [Adding the Play Button](#15)

	- [Creating a Button Class](#15.1)

	- [Drawing the Button to the Screen](#15.2)

	- [Starting the Game](#15.3)

	- [Resetting the Game](#15.4)

	- [Deactivating the Play Button](#15.5)

	- [Hiding the Mouse Cursor](#15.6)


- [Leveling Up](#16)

	- [Modifying the Speed Settings](#16.1)

	- [Resetting the Speed](#16.1)

- [Scoring](#17)

	- [Displaying the Score](#17.1)

	- [Making a Scoreboard](#17.2)

	- [Updating the Score as Ghosts Are Shot Down](#17.3)

	- [Resetting the Score](#17.4)
	
	- [Making Sure to Score All Hits](#17.5)

	- [Increasing Point Values](#17.6)

	- [Rounding the Score](#17.7)

	- [High Scores](#17.8)

	- [Displaying the Level](#17.9)

	- [Displaying the Number of Ships](#17.10)



<h2 id = "1">Creating a Pygame Window and Responding to User Input</h2>

<!-- *********************************************part1************************************* -->

- First, we import the <code>sys</code> and `pygame` modules. The pygame module contains the functionality we need to make a game. We’ll use tools in the sys module to exit the game when the player quits.
       
- Ghost Invasion starts as a class called GhostInvasion. In the ```__init__()``` method, the <code>pygame.init()</code> function initializes the background settings that Pygame needs to work properly.

- We call <code>pygame.display.set_mode()</code> to create a display window, on which we’ll draw all the game’s graphical elements. The argument <code>(1200, 800)</code> is a tuple that defines the dimensions of the game window, which will be <code>1200 pixels</code> wide by <code>800 pixels</code> high.

- The object we assigned to <code>self.screen</code> is called a surface. A surface in Pygame is a part of the screen where a game element can be displayed.

- The surface returned by <code>display.set_mode()</code> represents the entire game window. When we activate the game’s animation loop, this surface will be redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.

- The game is controlled by the <code>run_game()</code> method. This method contains a <code>while</code> loop w that runs continually. The <code>while</code> loop contains an event loop and code that manages screen updates.

- To access the events that Pygame detects, we'll use the <code>pygame.event.get()</code> function. This function returns a list of events that have taken place since the last time this function was called. Any keyboard or mouse event will cause this <code>for</code> loop to run. Inside the loop, we’ll write a series of <code>if</code> statements to detect and respond to specific events.

- The call to <code>pygame.display.flip()</code> tells Pygame to make the most recently drawn screen visible. In this case, it simply draws an empty screen on each pass through the <code>while</code> loop, erasing the old screen so only the new screen is visible.

- At the end of the code, we create an instance of the game, and then call <code>run_game()</code>. We place <code>run_game()</code> in an if block that only runs if the file is called directly. When you run this <code>ghost_invasion.py</code> file, you should see an empty Pygame window.

<!-- *********************************************part2************************************* -->

<h2 id = "2">Setting the Background Color</h2>

  
- Pygame creates a <i>black screen</i> by default, but that’s boring. Let’s set a different background color. We’ll do this at the end of the <code>__init__()</code> method.

- Colors in Pygame are specified as RGB colors: a mix of red, green, and blue. Each color value can range from 0 to 255. The color value (255, 0, 0) is <i>red</i>, (0, 255, 0) is <i>green</i>, and (0, 0, 255) is <i>blue</i>. You can mix different RGB values to create up to 16 million colors. The color value (230, 230, 230) mixes equal amounts of red, blue, and green, which produces a light gray background color. We assign this color to <code>self.bg_color</code>. We fill the screen with the background color using the <code>fill()</code> method, which acts on a surface and takes only one <code>argument: a color</code>.
   

    <!-- *********************************************part3************************************* -->
<h2 id = "3">Creating a Settings Class</h2>

    
        
- Each time we introduce new functionality into the game, we’ll typically create some new settings as well. Instead of adding settings throughout the code, let’s write a module called <code>settings</code> that contains a class called <code>Settings</code>to store all these values in one place.
        
- This also makes it easier to modify the game’s appearance and behavior as our project grows: to modify the game, we’ll simply change some values in <code>settings.py</code>, which we’ll create next, instead of searching for different settings throughout the project.
        
- To make an instance of Settings in the project and use it to access our settings, we need to modify <code>ghost_invasion.py</code>

- We import Settings into the main program file. Then we create an instance of Settings and assign it to <code>self.settings</code>, after making the call to <code>pygame.init()</code>. When we create a screen, we use the <code>screen_width</code> and <code>screen_height</code> attributes of <code>self.settings</code>, and then we use <code>self.settings</code> to access the background color when filling the screen as well.
        
    

    <!-- *********************************************part4************************************* -->

<h2 id = "4">Adding the Ship Image</h2>
    
- Let’s add the ship to our game. To draw the player’s ship on the screen, we’ll load an image and then use the Pygame <code>blit()</code> method to draw the image.
        

- After choosing an image for the ship, we need to display it on the screen. To use our ship, we’ll create a new <code>ship</code> module that will contain the <code>class Ship</code>. This class will manage most of the behavior of the player’s ship.
        

- Pygame is efficient because it lets you treat all game elements like rectangles <i>(rects)</i> , even if they’re not exactly shaped like rectangles. Treating an element as a rectangle is efficient because rectangles are simple geometric shapes.
            We’ll treat the ship and the screen as rectangles in this class.
     

- We import the <code>pygame</code> module before defining the class. The <code>__init__()</code> method of
            <code>Ship</code> takes two parameters: the <code>self</code> reference and a reference to the current instance of the <code>GhostInvasion</code> class. This will give Ship access to all the game resources defined in <code>GhostInvasion</code>.

        
- we access the screen’s <code>rect</code> attribute using the <code>get_rect()</code> method and assign it to
            <code>self.screen_rect</code>. Doing so allows us to place the ship in the correct location on the screen.
        

- To load the image, we call <code>pygame.image.load()</code> and give it the location of our ship image. This function returns a surface representing the ship, which we assign to <code>self.image</code>. When the image is loaded, we call <code>get_rect()</code>            to access the ship surface’s <code>rect</code> attribute so we can later use it to place the ship.

- When you’re working with a <code>rect</code> object, you can use the x- and y-coordinates of the top, bottom, left, and right edges of the rectangle, as well as the center, to place the object. There are also attributes that combine these properties,
            such as midbottom, midtop, midleft, and midright. When you’re adjusting the horizontal or vertical placement of the rect, you can just use the x and y attributes, which are the x- and y-coordinates of its top-left corner.
        

- <b>Note: </b><u><i>In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
                    increase as you go down and to the right. On a 1200 by 800 screen, the origin is
                    at the top-left corner, and the bottom-right corner has the coordinates (1200, 800).
                    These coordinates refer to the game window, not the physical screen.</i></u>

- We’ll position the ship at the bottom center of the screen. To do so, make the value of
            <code>self.rect.midbottom</code> match the <code>midbottom</code> attribute of the screen’s
            <code>rect</code>. Pygame uses these rect attributes to position the ship image so it’s centered horizontally and aligned with the bottom of the screen. At y, we define the
            <code>blitme()</code> method, which draws the image to the screen at the position specified by
            <code>self.rect</code> 
           
<!-- *********************************************part5************************************* -->

<h2 id = "5">Drawing the Ship to the Screen</h2>

    
- We <code>import Ship</code> and then make an instance of <code>Ship</code> after the screen has been created. The call to <code>Ship()</code> requires one argument, an instance of <code></code>. The self argument here refers to the current instance
            of <code>GhostInvasion</code>. This is the parameter that gives <code>Ship</code> access to the game’s resources, such as the screen object. We assign this <code>Ship</code> instance to <code>self.ship</code>.
        

- After filling the background, we draw the ship on the screen by calling <code>ship.blitme()</code>, so the ship appears on top of the background. When you run <code>ghost_invasion.py</code> now, you should see an empty game screen with the rocket
            ship sitting at the bottom center.


    <!-- *********************************************part6************************************* -->

<h2 id = "6">Refactoring: The _check_events() and _update_screen() Methods</h2>


<p>In large projects, you’ll often refactor code you’ve written before adding more code. Refactoring simplifies the structure of the code you’ve already written, making it easier to build on. In this section, we’ll break the <code>run_game()</code>            method, which is getting lengthy, into two helper methods. A <i>helper
                method</i> does work inside a class but isn’t meant to be called through an instance. In Python, a single leading underscore indicates a helper method.</p>

- <h3 id = "6.1">The _check_events() Method</h3>
        
  - We’ll move the code that manages events to a separate method called <code>_check_events()</code>. This will simplify <code>run_game()</code> and isolate the event management loop. Isolating the event loop allows you to manage events separately
                from other aspects of the game, such as updating the screen.

  - We make a new <code>_check_events()</code> method and move the lines that check whether the player has clicked to close the window into this new method. To call a method from within a class, use dot notation with the variable <code>self</code>                and the name of the method. We call the method from inside the while loop in <code>run_game()</code>.
   
- <h3 id = "6.2">The _update_screen() Method</h3>
       
    - To further simplify <code>run_game()</code>, we’ll move the code for updating the screen to a separate method called <b><code>_update_screen()</code></b>

            
    - We moved the code that draws the background and the ship and flips the screen to
                <code>_update_screen()</code>. Now the body of the main loop in <code>run_game()</code> is much simpler. It’s easy to see that we’re looking for new events and updating the screen on each pass through the loop.
   
   
   

<!-- *********************************************part0.7************************************* -->
<h2 id = "7">Piloting the Ship</h2>

  
<p>We’ll give the player the ability to move the ship right and left. We’ll write code that responds when the player presses the right or left arrow key. We’ll focus on movement to the right first, and then we’ll apply the same principles to control movement to the left. As we add this code, you’ll learn how to control the movement of images on the screen and respond to user input</p>

<!-- *********************************************part7************************************* -->

- <h3 id = "7.1">Responding to a Keypress</h3>

        
    - Whenever the player presses a key, that keypress is registered in Pygame as an event. Each event is picked up by the
                <code>pygame.event.get()</code> method. We need to specify in our <code>_check_events()</code> method what kind of events we want the game to check for. Each keypress is registered as a <b>KEYDOWN</b> event. When Pygame detects a <b>KEYDOWN</b>                event, we need to check whether the key that was pressed is one that triggers a certain action. For example, if the player presses the right arrow key, we want to increase the ship’s <code>rect.x</code> value to move the ship to the right.
            

    - Inside <code>_check_events()</code> we add an elif block to the event loop to respond when Pygame detects a
                <b>KEYDOWN</b> event. We check whether the key pressed, <code>event.key</code>, is the right arrow key. The right arrow key is represented by <b>pygame.K_RIGHT</b>. If the right arrow key was pressed, we move the ship to the right by increasing
                the value of <code>self.ship.rect.x</code> by 1.

    <!-- *********************************************part8************************************* -->

    - <h3 id = "7.2">Allowing Continuous Movement</h3>

        
        - When the player holds down the right arrow key, we want the ship to continue moving right until the player releases the key. We’ll have the game detect a <b>pygame.KEYUP</b> event so we’ll know when the right arrow key is released; then
                we’ll use the <b>KEYDOWN</b> and <b>KEYUP</b> events together with a flag called
                <code>moving_right</code> to implement continuous motion.
          
        - When the <code>moving_right</code> flag is <i>False</i>, the ship will be motionless. When the player presses the right arrow key, we’ll set the flag to <i>True</i>, and when the player releases the key, we’ll set the flag to <i>False</i>                again. The <code>Ship</code> class controls all attributes of the ship, so we’ll give it an attribute called moving_right and an <code>update()</code> method to check the status of the <code>moving_right</code> flag. The <code>update()</code>                method will change the position of the ship if the flag is set to <i>True</i>. We’ll call this method once on each pass through the while loop to update the position of the ship.

        - We add a <code>self.moving_right</code> attribute in the <code>__init__()</code> method and set it to
                <i>False</i> initially. Then we add <code>update()</code>, which moves the ship right if the flag is
                <i>True</i>. The <code>update()</code> method will be called through an instance of <code>Ship</code>, so it’s not considered a helper method. Now we need to modify <code>_check_events()</code> so that
                <code>moving_right</code> is set to <i>True</i> when the right arrow key is pressed and <i>False</i> when the key is released.

        - We modify how the game responds when the player presses the right arrow key instead of changing the ship’s position directly, we merely set <code>moving_right</code> to <i>True</i>. we add a new
                <code>elif</code> block, which responds to
                <b>KEYUP</b> When the player releases the right arrow key <code>(K_RIGHT)</code>, we set
                <code>moving_right</code> to <i>False</i>. Next, we modify the <code>while</code> loop in
                <code>run_game()</code> so it calls the ship’s <code>update()</code> method on each pass through the loop
           

        - The ship’s position will be updated after we’ve checked for keyboard events and before we update the screen. This allows the ship’s position to be updated in response to player input and ensures the updated position will be used when drawing
                the ship to the screen.
        
    <!-- *********************************************part9************************************* -->

    - <h3 id = "7.3">Moving Both Left and Right</h3>

        
        - Now that the ship can move continuously to the right, adding movement to the left is straightforward. Again, we’ll modify the Ship class and the <code>_check _events()</code> method. Here are the relevant changes to <code>__init__()</code>                and <code>update()</code> in <code>Ship</code>

            
        - In <code>__init__()</code>, we add a <code>self.moving_left</code> flag. In <code>update()</code>, we use two separate if blocks rather than an elif to allow the ship’s <code>rect.x</code> value to be increased and then decreased when
                both arrow keys are held down. This results in the ship standing still. If we used <code>elif</code> for motion to the left, the right arrow key would always have priority. Doing it this way makes the movements more accurate when switching
                from right to left when the player might momentarily hold down both keys.
            
        - If a <b>KEYDOWN</b> event occurs for the <b>K_LEFT</b> key, we set <code>moving_left</code> to
                <i>True</i>. If a <b>KEYUP</b> event occurs for the <b>K_LEFT</b> key, we set <code>moving_left</code> to <i>False</i>. We can use <code>elif</code> blocks here because each event is connected to only one key. If the player presses both
                keys at once, two separate events will be detected. 


       

    <!-- *********************************************part10************************************* -->
    - <h3 id = "7.4">Adjusting the Ship’s Speed</h3>
       
       - Currently, the ship moves one pixel per cycle through the <code>while</code> loop, but we can take finer control of the ship’s speed by adding a <code>ship_speed</code> attribute to the <code>Settings</code> class. We’ll use this attribute
                to determine how far to move the ship on each pass through the loop. Here’s the new attribute in
                <code><i>settings.py</i></code>
            
        - We set the initial value of <code>ship_speed</code> to 2.0, When the ship moves now, its position is adjusted by 2.0 pixels rather than 1 pixel on each pass through the loop. We’re using decimal values for the speed setting to give us
                finer control of the ship’s speed when we increase the tempo of the game later on.
            
        - We create a settings attribute for <code>Ship</code>, so we can use it in <code>update()</code>. we’re adjusting the position of the ship by fractions of a pixel, we need to assign the position to a variable that can store a decimal value.
                You can use a decimal value to set an attribute of <code>rect</code>, but the <code>rect</code> will only keep the <i>integer</i> portion of that value. To keep track of the ship’s position accurately, we define a new <code>self.x</code>                attribute that can hold decimal values. We use the <code>float()</code> function to convert the value of <code>self.rect.x</code> to a decimal and assign this value to
                <code>self.x</code>

            
        - Now when we change the ship’s position in <code>update()</code>, the value of <code>self.x</code> is adjusted by the amount stored in <code>settings.ship_speed</code> After <code>self.x</code> has been updated, we use the new value to
                update <code>self.rect.x</code>, which controls the position of the ship Only the integer portion of
                <code>self.x</code> will be stored in <code>self.rect.x</code>, but that’s fine for displaying the ship. Now we can change the value of
                <code>ship_speed</code>, and any value greater than one will make the ship move faster. This will help make the ship respond quickly enough to shoot down ghosts, and it will let us change the tempo of the game as the player progresses
                in gameplay
            
        - <b>Note: </b><i><u>If you’re using macOS, you might notice that the ship moves very slowly, even with
                        a high speed setting. You can remedy this problem by running the game in fullscreen
                        mode, which we’ll implement shortly</u></i>
            

    <!-- *********************************************part11************************************* -->


    - <h3 id = "7.5">Limiting the Ship’s Range</h3>
        
        - At this point, the ship will disappear off either edge of the screen if you hold down an arrow key long enough. Let’s correct this so the ship stops moving when it reaches the screen’s edge. We do this by modifying the
                <code>update()</code> method in <code>Ship</code>.

        - This code checks the position of the ship before changing the value of <code>self.x</code> The code
                <code>self.rect.right</code> returns the x-coordinate of the right edge of the ship’s rect. If this value is less than the value returned by <code>self.screen_rect.right</code>, the ship hasn’t reached the right edge of the screen.

        - The same goes for the left edge: if the value of the left side of the <code>rect</code> is greater than zero, the ship hasn’t reached the left edge of the screen This ensures the ship is within these bounds before adjusting the value of
                <code>self.x</code>
        

    <!-- *********************************************part12************************************* -->

    - <h3 id = "7.6">Refactoring _check_events() and Pressing Q to Quit</h3>
        
        - The <code>_check_events()</code> method will increase in length as we continue to develop the game, so let’s break <code>_check_events()</code> into two more methods: one that handles <b>KEYDOWN</b> events and another that handles <b>KEYUP</b>                events.
            
        - We make two new helper methods: and <code>_check _keyup_events()</code> Each needs a self parameter and an event parameter. The bodies of these two methods are copied from <code>_check_events()</code>, and we’ve replaced the old code with
                calls to the new methods. The <code>_check_events()</code> method is simpler now with this cleaner code structure, which will make it easier to develop further responses to player input.

        - Now that we’re responding to keypresses efficiently, we can add another way to quit the game. It gets tedious to click the X at the top of the game window to end the game every time you test a new feature, so we’ll add a keyboard shortcut
                to end the game when the player presses <b>Q</b>

        - In <code>_check _keyup_events()</code>, we add a new block that ends the game when the player presses
                <b>Q</b>. Now, when testing, you can press <b>Q</b> to close the game rather than using your cursor to close the window.
        


    <!-- *********************************************part13************************************* -->

    - <h3 id = "7.7">Running the Game in Fullscreen Mode</h3>


        - Pygame has a fullscreen mode that you might like better than running the game in a regular window. Some games look better in fullscreen mode, and macOS users might see better performance in fullscreen mode.
           
        - When creating the screen surface, we pass a size of <code>(0, 0)</code> and the parameter
                <code>pygame.FULLSCREEN</code> This tells Pygame to figure out a window size that will fill the screen. Because we don’t know the width and height of the screen ahead of time, we update these settings after the screen is created. We use
                the
                <code>width</code> and <code>height</code> attributes of the screen’s rect to update the
                <code>settings</code> object. If you like how the game looks or behaves in fullscreen mode, keep these settings. If you liked the game better in its own window, you can revert back to the original approach where we set a specific screen
                size for the game.
            

        - <b>Note:</b><i><u>Make sure you can quit by pressing <b>Q</b> before running the game in fullscreen
                        mode;
                        Pygame offers no default way to quit a game while in fullscreen mode.</u></i>
       


<h2 id = "8">Shooting Bullets</h2>
    
<p>Now let’s add the ability to shoot bullets. We’ll write code that fires a bullet, which is represented by a small rectangle, when the player presses the spacebar. Bullets will then travel straight up the screen until they disappear off the top of the
            screen.</p>
        
<!-- *********************************************part13************************************* -->

- <h3 id = "8.1">Adding the Bullet Settings</h3>
        
    - At the end of the `__init__()` method, we’ll update settings.py to include the values we’ll need for a new Bullet class. 

    - These settings create dark gray bullets with a width of 3 pixels and a height of 15 pixels. The bullets will travel slightly slower than the ship.
        

<!-- *********************************************part14************************************* -->

- <h3 id = "8.2">Creating the Bullet Class</h3>

 
    - Now create a <code><i>bullet.py</i></code> file to store our <code>Bullet</code> class. Here’s the first part of bullet. py:
            
```
    import pygame
    from pygame.sprite import Sprite

    class Bullet(Sprite):
        #A Class to manage bullets fired from the ship

        def __init__(self, ai_game):

            #Create a bullet object at the ship's current position
            super().__init__()
            self.screen = ai_game.screen
            self.settings = ai_game.settings
            self.color = self.settings.bullet_color

            # Create a bullet rect at (0, 0) and then set correct position.
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
            self.rect.midtop = ai_game.ship.rect.midtop
            # Store the bullet's position as a decimal value.
            self.y = float(self.rect.y)
```
   - The <code>Bullet</code> class inherits from Sprite, which we import from the <code>pygame.sprite</code> module. When you use sprites, you can group related elements in your game and act on all the grouped elements at once. To create a bullet
                instance,
                `__init__()` needs the current instance of <i>GhostInvasion</i>, and we call
                <code>super()</code> to inherit properly from Sprite. We also set attributes for the screen and settings objects, and for the bullet’s color.

   - Then we create the bullet’s <code>rect</code> attribute. The bullet isn’t based on an image, so we have to build a rect from scratch using the <code>pygame.Rect()</code> class. This class requires the x- and y-coordinates of the top-left corner
                of the <code>rect</code>, and the width and height of the <code>rect</code>. We initialize the
                <code>rect</code> at (0, 0), but we’ll move it to the correct location in the next line, because the bullet’s position depends on the ship’s position. We get the width and height of the bullet from the values stored in <code>self.settings</code>
           

   - Then we set the bullet’s <code>midtop</code> attribute to match the ship’s <code>midtop</code> attribute. This will make the bullet emerge from the top of the ship, making it look like the bullet is fired from the ship. We store a decimal
                value for the bullet’s y-coordinate so we can make fine adjustments to the bullet’s speed.


 ```           
        def update(self):
        #"""Move the bullet up the screen."""
        #Update the decimal position of the bullets
        self.y -= self.settings.bullet_speed
        
        #update the rect position
        self.rect.y = self.y
        
        def draw_bullet(self):
        #"""Draw the bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

```




<!-- second part -->
   - The <code>update()</code> method manages the bullet’s position. When a bullet is fired, it moves up the screen, which corresponds to a decreasing y-coordinate value. To update the position, we subtract the amount stored in <code>settings.bullet_speed</code>                from <code>self.y</code>, We then use the value of
                <code>self.y</code> to set the value of <code>self.rect.y</code>

   - The <code>bullet_speed</code> setting allows us to increase the speed of the bullets as the game progresses or as needed to refine the game’s behavior. Once a bullet is fired, we never change the value of its x-coordinate, so it will travel
                vertically in a straight line even if the ship moves. When we want to draw a bullet, we call
                <code>draw_bullet().</code> The <code>draw.rect()</code> function fills the part of the screen defined by the bullet’s <code>rect</code> with the color stored in <code>self.color</code>.
    
<!-- *********************************************part15************************************* -->


- <h3 id = "8.3">Storing Bullets in a Group</h3>
    
    - Now that we have a <code>Bullet</code> class and the necessary settings defined, we can write code to fire a bullet each time the player presses the spacebar. We’ll create a group in <i>GhsotInvasion</i> to store all the live bullets so
                we can manage the bullets that have already been fired. This group will be an instance of the
                <code>pygame.sprite.Group</code> class, which behaves like a list with some extra functionality that’s helpful when building games. We’ll use this group to draw bullets to the screen on each pass through the main loop and to update each
                bullet’s position. Then we need to update the position of the bullets on each pass through the
                <code>whil</code> loop.
            
    - When you call <code>update()</code> on a group, group automatically calls <code>update()</code> for each sprite in the group. The line <code>self.bullets.update()</code> calls <code>bullet.update()</code> for each bullet we place in the group
                bullets
           
<!-- *********************************************part16************************************* -->

- <h3 id = "8.4">Firing Bullets</h3>
        
    - In <i>GhostInvasion</i>, we need to modify <code>_check_keydown_events()</code> to fire a bullet when the player presses the spacebar. We don’t need to change <code>_check_keyup _events()</code> because nothing happens when the spacebar
                is released. We also need to modify <code>_update_screen()</code> to make sure each bullet is drawn to the screen before we call <code>flip()</code>.
            
    - First, we <code>import Bullet</code> Then we call <code>_fire_bullet()</code> when the spacebar is pressed, In <code>_fire_bullet()</code>, we make an instance of Bullet and call it new_bullet We then add it to the group bullets using the
                <code>add()</code> method. The <code>add()</code> method is similar to <code>append()</code>, but it’s a method that’s written specifically for Pygame groups.
            
    - The <code>bullets.sprites()</code> method returns a list of all sprites in the group bullets. To draw all fired bullets to the screen, we loop through the sprites in bullets and call
                <code>draw_bullet()</code> on each one.
        


<!-- *********************************************part17************************************* -->

- <h3 id = "8.5">Deleting Old Bullets</h3>
        
    - At the moment, the bullets disappear when they reach the top, but only because Pygame can’t draw them above the top of the screen. The bullets actually continue to exist; their y-coordinate values just grow increasingly negative. This is a problem, because
                they continue to consume memory and processing power.
            

    - We need to get rid of these old bullets, or the game will slow down from doing so much unnecessary work. To do this, we need to detect when the <code>bottom</code> value of a bullet’s <code>rect</code> has a value of 0, which indicates
                the bullet has passed off the top of the screen.
           

```       
    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
        print(len(self.bullets))
```         

   - When you use a <code>for</code> loop with a list (or a group in Pygame), Python expects that the list will stay the same length as long as the loop is running. Because we can’t remove items from a list or group within a <code>for</code> loop,
                we have to loop over a copy of the group. We use the <code>copy()</code> method to set up the
                <code>for</code> loop. which enables us to modify <code>bullets</code> inside the loop. We check each bullet to see whether it has disappeared off the top of the screen, If it has, we remove it from
                <code>bullets</code> then we insert a
                <code>print()</code> call to show how many bullets currently exist in the game and verify that they’re being deleted when they reach the top of the screen.

   - If this code works correctly, we can watch the terminal output while firing bullets and see that the number of bullets decreases to zero after each series of bullets has cleared the top of the screen. After you run the game and verify that
                bullets are being deleted properly, remove the <code>print()</code> call. If you leave it in, the game will slow down significantly because it takes more time to write output to the terminal than it does to draw graphics to the game window.
        

<!-- *********************************************part18************************************* -->


- <h3 id = "8.6">Limiting the Number of Bullets</h3>

        
    - Many shooting games limit the number of bullets a player can have on the screen at one time; doing so encourages players to shoot accurately. We’ll do the same in <i>GhostInvasion</i> , First, store the number of bullets allowed in <code>settings.py</code>,
                This limits the player to three bullets at a time. We’ll use this<i>GhostInvasion</i> to check how many bullets exist before creating a new bullet in <code>_fire_bullet()</code>
    
    - When the player presses the spacebar, we check the length of bullets. If <code>len(self.bullets)</code> is less than three, we create a new bullet. But if three bullets are already active, nothing happens when the spacebar is pressed. When
                you run the game now, you should be able to fire bullets only in groups of three.
    

<!-- *********************************************part19************************************* -->

- <h3 id = "8.7">Creating the _update_bullets() Method</h3>

        
    - We want to keep the <i>GhostInvasion</i> class reasonably well organized, so now that we’ve written and checked the bullet management code, we can move it to a separate method. We’ll create a new method called <code>_update_bullets()</code>                and add it just before _update_screen()
            
    - The code for <code>_update_bullets()</code> is cut and pasted from <code>run_game()</code>, all we’ve done here is clarify the comments. Now our main loop contains only minimal code, so we can quickly read the method names and understand what’s
                happening in the game. The main loop checks for player input, and then updates the position of the ship and any bullets that have been fired. We then use the updated positions to draw a new screen. <i>Run
                    ghost_invasion.py one more time, and make sure you can still fire
                    bullets without errors.</i>
   

<h2 id = "9" align="center">Error : Occured</h2>

<p>Removing some extra whitespaces and there was an error of bullets iin which bullets were blinking while firing, reason for that I repeted the code accidentally from <code>_update_screen()</code> to
            <code>run_game()</code>, which I was mistaken in the start of the program. So Now it is fixed. <br><b>Now
                You can check the fromat of commit from which
                you can understand better.</b></p>


<h2 id="10" >Creating a First Ghost</h2>

  
<p>Placing one ghost on the screen is like placing a ship on the screen. Each ghost’s behavior is controlled by a class called ghost, which we’ll structure like the Ship class </p>

<!-- *********************************************part21************************************* -->

- <h3 id = "10.1">Creating the Ghost Class</h3>

        
    - Now we’ll write the <i>Ghost</i> class and save it as <code>ghost.py</code> Most of this class is like the <code>Ship</code> class except for the ghosts’ placement on the screen. We initially place each ghost near the top-left corner of
                the screen; we add a space to the left of it that’s equal to the ghost’s width and a space above it equal to its height, so it’s easy to see. We’re mainly concerned with the ghosts’ horizontal speed, so we’ll track the horizontal position
                of each ghost precisely This <code>Ghost</code> class doesn’t need a method for drawing it to the screen; instead, we’ll use a Pygame group method that automatically draws all the elements of a group to the screen.
            

```           
    -----------------------------------ghost.py--------------------------------------
    import pygame
    from pygame.sprite import Sprite
    
    class Ghost(Sprite):
        # """A class to represent a single ghost in the fleet."""
        
        def __init__(self, ai_game):
            # """Initialize the ghost and set its starting position."""
            super().__init__()
            self.screen = ai_game.screen
            # Load the ghost image and set its rect attribute.
            self.image = pygame.image.load('images/ghost.png')
            self.rect = self.image.get_rect()
            # Start each new ghost near the top left of the screen.
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            # Store the ghost's exact horizontal position.
            self.x = float(self.rect.x)
```            
       

<!-- *********************************************part22************************************* -->

- <h3 id = "10.2">Creating an Instance of the Ghost</h3>
        
    - We want to create an instance of <code>Ghost</code> so we can see the first ghost on the screen. Because it’s part of our setup work, we’ll add the code for this instance at the end of the
                <code>__init__()</code> method in <b>GhostInvasion</b>. Eventually, we’ll create an entire fleet of ghosts, which will be quite a bit of work, so we’ll make a new helper method called <code>_create_fleet()</code>.
            

    - The order of methods in a class doesn’t matter, as long as there’s some consistency to how they’re placed. I’ll place <code>_create_fleet()</code> just before the <code>_update_screen()</code> method, but anywhere in <b>GhostInvasion</b> will
                work. First, we’ll import the <code>Ghost</code> class.


    - We create a group to hold the fleet of ghosts, and we call <code>_create_fleet()</code> In this method, we’re creating one instance of <i>Ghost</i>, and then adding it to the group that will hold the fleet. The ghost will be placed in the
                default upper-left area of the screen, which is perfect for the first ghost. To make the ghost appear, we need to call the group’s <code>draw()</code> method in <code>_update_screen()</code>
            

    - When you call <code>draw()</code> on a group, <code>Pygame</code> draws each element in the group at the position defined by its <code>rect</code> attribute. The <code>draw()</code> method requires one argument; a surface on which to draw
                the elements from the group. Now that the first ghost appears correctly, we’ll write the code to draw an entire fleet.
       

<h2 id = "11">Building the Ghost Fleet</h2>

    
<p>To draw a fleet, we need to figure out how many ghosts can fit across the screen and how many rows of ghosts can fit down the screen. We’ll first figure out the horizontal spacing between ghosts and create a row; then we’ll determine the vertical
            spacing and create an entire fleet.</p>

<!-- *********************************************part23************************************* -->


- <h3 id = "11.1">Determining How Many Ghosts Fit in a Row</h3>
        
    <p>To figure out how many ghosts fit in a row, let’s look at how much horizontal space we have. The screen width is stored in settings.screen_width, but we need an empty margin on either side of the screen. We’ll make this margin the width of
                one ghost. Because we have two margins, the available space for ghosts is the screen width minus two ghost widths: <br>
                
                
    <code>available_space_x = settings.screen_width – (2 * ghost_width)</code>
                    
    We also need to set the spacing between ghosts; we’ll make it one ghost width. The space needed to display one ghost is twice its width: one width for the ghost and one width for the empty space to its right. To find the number
                of ghosts that fit across the screen, we divide the available space by two times the width of an ghost. We use floor division (//), which divides two numbers and drops any remainder, so we’ll get an integer number of ghosts: <br>
                
                    
    <code>number_ghosts_x = available_space_x // (2 * ghost_width)</code>
                    
    We’ll use these calculations when we create the fleet</p>

    - <b>Note:</b><u><i>One great aspect of calculations in programming is that you don’t have to be sure
                        your formulas are correct when you first write them. You can try them out and see if
                        they work. At worst, you’ll have a screen that’s overcrowded with ghosts or has too few
                        ghosts. You can then revise your calculations based on what you see on the screen.</i></u>
       

<!-- *********************************************part24************************************* -->


- <h3 id = "11.2">Creating a Row of Ghosts</h3>

    
    - We’re ready to generate a full row of ghosts. Because our code for making a single ghost works, we’ll rewrite <code>_create_fleet()</code> to make a whole row of ghosts.
            

    - We’ve already thought through most of this code. We need to know the ghost’s width and height to place ghosts, so we create an ghost, before we perform calculations. This ghost won’t be part of the fleet, so don’t add it to the group <i>ghosts</i>.
                code we get the ghost’s width from its <code>rect</code> attribute and store this value in <code>ghost_width</code> so we don’t have to keep working through the <code>rect</code> attribute. We calculate the horizontal space available for
                ghosts and the number of ghosts that can fit into that space.
            

    - Next, we set up a loop that counts from 0 to the number of ghosts we need to make In the main body of the loop, we create a new ghost and then set its x-coordinate value to place it in the row, Each ghost is pushed to the right one ghost width
                from the left margin. Next, we multiply the ghost width by 2 to account for the space each ghost takes up, including the empty space to its right, and we multiply this amount by the ghost’s position in the row. We use the ghost’s x attribute
                to set the position of its <code>rect</code>. Then we add each new ghost to the group <i>ghosts</i>. When you run <b>GhostInvasion</b> now, you should see the first row of ghosts appear.
            

    - The first row is offset to the left, which is actually good for gameplay. The reason is that we want the fleet to move right until it hits the edge of the screen, then drop down a bit, then move left, and so forth. Like the classic game Space
                Invaders, this movement is more interesting than having the fleet drop straight down. We’ll continue this motion until all ghosts are shot down or until an ghost hits the ship or the bottom of the screen.


        - <b>Note:</b><i><u>Depending on the screen width you’ve chosen, the alignment of the first row of ghosts
            might look slightly different on your system.</u></i>
        

<!-- *********************************************part25************************************* -->


<h3 id = "11.3">Refactoring _create_fleet()</h3>


   - If the code we’ve written so far was all we need to create a fleet, we’d probably leave <code>_create_fleet()</code> as is. But we have more work to do, so let’s clean up the method a bit. We’ll add a new helper method,
                <code>_create_ghost()</code>, and call it from <code>_create_fleet()</code>


   - The method <code>_create_fleet()</code> requires one parameter in addition to self: it needs the ghost number that’s currently being created. We use the same body we made for <code>_create_fleet()</code> except that we get the width of an
                ghost inside the method instead of passing it as an argument. This refactoring will make it easier to add new rows and create an entire fleet.

<!-- *********************************************part26************************************* -->

- <h3 id = "11.4">Adding Rows</h3>

    - To finish the fleet, we’ll determine the number of rows that fit on the screen and then repeat the loop for creating the ghosts in one row until we have the correct number of rows. To determine the number of rows, we find the available vertical
                space by subtracting the ghost height from the top, the ship height from the bottom, and two ghost heights from the bottom of the screen: <br>
                
                    
        <code>available_space_y = settings.screen_height – (3 * ghost_height) – ship_height</code>
               
            
    - The result will create some empty space above the ship, so the player has some time to start shooting ghosts at the beginning of each level. Each row needs some empty space below it, which we’ll make equal to the height of one ghost. To find the number
                of rows, we divide the available space by two times the height of an ghost. We use floor division because we can only make an integer number of rows. (Again, if these calculations are off, we’ll see it right away and adjust our approach
                until we have reasonable spacing.) <br>
                
                    
        <code>number_rows = available_height_y // (2 * ghost_height)</code>
                  

        Now that we know how many rows fit in a fleet, we can repeat the code for creating a row.
            
    - We need the width and height of an ghost, so we use the attribute size, which contains a tuple with the width and height of a <code>rect</code> object. To calculate the number of rows we can fit on the screen, we write our <code>available_space_y</code>                    calculation right after the calculation for <code>available_space_x</code>, The calculation is wrapped in parentheses so the outcome can be split over two lines, which results in lines of 79 characters or less, as is recommended.


    - To create multiple rows, we use two nested loops: one outer and one inner loop The inner loop creates the ghosts in one row. The outer loop counts from 0 to the number of rows we want; Python uses the code for making a single row and repeats
                    it <code>number_rows</code> times.


    - To nest the loops, write the new <code>for</code> loop and indent the code you want to repeat. (Most text editors make it easy to indent and unindent blocks of code, but for help see Appendix B.) Now when we call <code>_create_ghost()</code>,
                    we include an argument for the row number so each row can be placed farther down the screen.

    
    - The definition of <code>_create_ghost()</code> needs a parameter to hold the row number. Within <code>_create_ghost()</code>, we change an ghost’s y-coordinate value when it’s not in the first row by starting with one ghost’s height
                    to create empty space at the top of the screen. Each row starts two ghost heights below the previous row, so we multiply the ghost height by two and then by the row number. The first row number is 0, so the vertical placement of the
                    first row is unchanged. All subsequent rows are placed farther down the screen. When you run the game now, you should see a full fleet of <i>ghosts</i>.


<h2 id = "12">Making the Fleet Move</h2>
    
<p>Now let’s make the fleet of ghosts move to the right across the screen until it hits the edge, and then make it drop a set amount and move in the other direction. We’ll continue this movement until all ghosts have been shot down, one collides
            with the ship, or one reaches the bottom of the screen. Let’s begin by making the fleet move to the right.
        </p>

<!-- *********************************************part27************************************* -->

- <h3 id = "12.1">Moving the Ghosts Right</h3>

    - To move the ghosts, we’ll use an <code>update()</code> method in ghost.py, which we’ll call for each ghost in the group of ghosts. First, add a setting to control the speed of each ghost, Then use this setting to implement <code>update()</code>                We create a settings parameter in `__init__()` so we can access the ghost’s speed in <code>update()</code>. Each time we update an ghost’s position, we move it to the right by the amount stored in <code>ghost_speed</code>. We
                track the ghost’s exact position with the <code>self.x</code> attribute, which can hold decimal values, We then use the value of <code>self.x</code> to update the position of the ghost’s <code>rect</code>, In the main <code>while</code>                loop, we already have calls to update the ship and bullet positions. Now we’ll add a call to update the position of each ghost as well
            
    
    - We’re about to write some code to manage the movement of the fleet, so we create a new method called <code>_update_ghosts()</code>. We set the ghosts’ positions to update after the bullets have been updated, because we’ll soon be checking
                to see whether any bullets hit any ghosts
            

    - Where you place this method in the module is not critical. But to keep the code organized, I’ll place it just after <code>_update_bullets()</code> to match the order of method calls in the <code>while</code> loop. Here’s the first version
                of <code>_update_ghosts()</code>
            

    - We use the <code>update()</code> method on the ghosts group, which calls each ghost’s <code>update()</code> method. When you run <b>GhostInvasion</b> now, you should see the fleet move right and disappear off the side of the screen.
        

<!-- *********************************************part28************************************* -->


- <h3 id = "12.2">Creating Settings for Fleet Direction</h3>

        
    - Now we’ll create the settings that will make the fleet move down the screen and to the left when it hits the right edge of the screen. Here’s how to implement this behavior.
            
    - The setting <code>fleet_drop_speed</code> controls how quickly the fleet drops down the screen each time an ghost reaches either edge. It’s helpful to separate this speed from the ghosts’ horizontal speed so you can adjust the two speeds independently.

    - To implement the setting <code>fleet_direction</code>, we could use a text value, such as <code>'left'</code> or <code>'right'</code>, but we’d end up with <code>if-elif</code> statements testing for the fleet direction. Instead, because we
                have only two directions to deal with, let’s use the values 1 and −1, and switch between them each time the fleet changes direction. (Using numbers also makes sense because moving right involves adding to each ghost’s x-coordinate value,
                and moving left involves subtracting from each ghost’s x-coordinate value.)
        

<!-- *********************************************part29************************************* -->

- <h3 id = "12.3">Checking Whether an Ghost Has Hit the Edge</h3>

    
    - We need a method to check whether an ghost is at either edge, and we need to modify <code>update()</code> to allow each ghost to move in the appropriate direction.
            
    - We can call the new method <code>check_edges()</code> on any ghost to see whether it’s at the left or right edge. The ghost is at the right edge if the <code>right</code> attribute of its <code>rect</code> is greater than or equal to the
                <code>right</code> attribute of the screen’s <code>rect</code>. It’s at the left edge if its <code>left</code> value is less than or equal to 0.

    - We modify the method <code>update()</code> to allow motion to the left or right by multiplying the ghost’s speed by the value of <code>fleet_direction</code>. If <code>fleet _direction</code> is 1, the value of ghost_speed will be added to
                the ghost’s current position, moving the ghost to the right; if <code>fleet_direction</code> is −1, the value will be subtracted from the ghost’s position, moving the ghost to the left.
    

<!-- *********************************************part30************************************* -->


- <h3 id = "12.4">Dropping the Fleet and Changing Direction</h3>
        
    - When an ghost reaches the edge, the entire fleet needs to drop down and change direction. Therefore, we need to add some code to <b>GhostInvasion</b> because that’s where we’ll check whether any ghosts are at the left or right edge. We’ll
                make this happen by writing the methods <code>_check_fleet_edges()</code> and <code>_change_fleet_direction()</code>, and then modifying <code>_update_ghosts()</code>. I’ll put these new methods after <code>_create_ghost()</code>, but
                again the placement of these methods in the class isn’t critical.
            

          
    - In <code>_check_fleet_edges()</code>, we loop through the fleet and call <code>check_edges()</code> on each ghost, If <code>check_edges()</code> returns <code>True</code>, we know an ghost is at an edge and the whole fleet needs to change
                direction; so we call <code>_change_fleet _direction()</code> and break out of the loop In <code>_change_fleet _direction()</code>, we loop through all the ghosts and drop each one using the setting fleet_drop _speed. then we change the
                value of <code>fleet_direction</code> by multiplying its current value by −1. The line that changes the fleet’s direction isn’t part of the for loop. We want to change each ghost’s vertical position, but we only want to change the direction
                of the fleet once.
            

    - We’ve modified the method by calling <code>_check_fleet_edges()</code> before updating each ghost’s position. When you run the game now, the fleet should move back and forth between the edges of the screen and drop down every time it hits
                an edge.


<h2 id = "13">Shooting Ghosts</h2>

    
<p>We’ve built our ship and a fleet of ghosts, but when the bullets reach the ghosts, they simply pass through because we aren’t checking for collisions. In game programming, collisions happen when game elements overlap. To make the bullets shoot
            down ghosts, we’ll use the method <code>sprite.groupcollide()</code> to look for collisions between members of two groups.</p>

<!-- *********************************************part31************************************* -->

- <h3 id = "13.1">Detecting Bullet Collisions</h3>

        
    - We want to know right away when a bullet hits an ghost so we can make an ghost disappear as soon as it’s hit. To do this, we’ll look for collisions immediately after updating the position of all the bullets

            

    - The <code>sprite.groupcollide()</code> function compares the rects of each element in one group with the rects of each element in another group. In this case, it compares each bullet’s <code>rect</code> with each ghost’s <code>rect</code>                and returns a dictionary containing the bullets and ghosts that have collided. Each key in the dictionary will be a bullet, and the corresponding value will be the ghost that was hit.
            

    - The new code we added compares the positions of all the bullets in <code>self.bullets</code> and all the ghosts in <code>self.ghosts</code>, and identifies any that overlap. Whenever the rects of a bullet and ghost overlap, <code>groupcollide()</code>                adds a keyvalue pair to the dictionary it returns. The two True arguments tell Pygame to delete the bullets and ghosts that have collided. (To make a high-powered bullet that can travel to the top of the screen, destroying every ghost
                in its path, you could set the first Boolean argument to <code>False</code> and keep the second Boolean argument set to <code>True</code>. The ghosts hit would disappear, but all bullets would stay active until they disappeared off the
                top of the screen.)
                <b>When you run <i>GhostInvasion</i> now, ghosts you hit should disappear.</b>
          

<!-- *********************************************part32************************************* -->

- <h3 id = "13.2">Repopulating the Fleet</h3>

      
    - One key feature of <i>GhostInvasion</i> is that the ghosts are relentless: every time the fleet is destroyed, a new fleet should appear. To make a new fleet of ghosts appear after a fleet has been destroyed, we first check whether the
                <code>ghosts</code> group is empty. If it is, we make a call to <code>_create_fleet()</code>. We’ll perform this check at the end of <code>_update_bullets()</code>, because that’s where individual ghosts are destroyed.
           
    
    - We check whether the <code>ghosts</code> group is empty. An empty group evaluates to False, so this is a simple way to check whether the group is empty. If it is, we get rid of any existing bullets by using the <code>empty()</code> method,
                which removes all the remaining sprites from a group. We also call <code>_create _fleet()</code>, which fills the screen with ghosts again. Now a new fleet appears as soon as you destroy the current fleet.
      

<!-- *********************************************part33************************************* -->

<h3 id = "13.3">Refactoring <i>_update_bullets()</i></h3>

   - Let’s refactor <code>_update_bullets()</code> so it’s not doing so many different tasks. We’ll move the code for dealing with bullet and ghost collisions to a separate method.

   - We’ve created a new method, <code>_check_bullet_ghost_collisions()</code>, to look for collisions between bullets and ghosts, and to respond appropriately if the entire fleet has been destroyed. Doing so keeps <code>_update_bullets()</code>                from growing too long and simplifies further development.
        

<h2 id="14">Ending the Game</h2>

    
<p>
            What’s the fun and challenge in a game if you can’t lose? If the player doesn’t shoot down the fleet quickly enough, we’ll have the ghosts destroy the ship when they make contact. At the same time, we’ll limit the number of ships a player can use, and
            we’ll destroy the ship when an ghost reaches the bottom of the screen. The game will end when the player has used up all their ships.
        </p>

<!-- *********************************************part34************************************* -->

- <h3 id = "14.1">Detecting Ghost and Ship Collisions</h3>

    - We’ll start by checking for collisions between ghosts and the ship so we can respond appropriately when an ghost hits it. We’ll check for ghost and ship collisions immediately after updating the position of each ghost in <i>GhostInvasion</i>.
            

    
    - The <code>spritecollideany()</code> function takes two arguments: a sprite and a group. The function looks for any member of the group that has collided with the sprite and stops looping through the group as soon as it finds one member
                that has collided with the sprite. Here, it loops through the group <code>ghosts</code> and returns the first ghost it finds that has collided with ship.
            
    - If no collisions occur, <code>spritecollideany()</code> returns <code>None</code> and the <code>if</code> block won’t execute. If it finds an ghost that has collided with the ship, it returns that ghost and the <code>if</code> block executes:
                it prints Ship hit!!!. When an ghost hits the ship, we’ll need to do a number of tasks: we’ll need to delete all remaining ghosts and bullets, recenter the ship, and create a new fleet. Before we write code to do all this, we need to know
                that our approach for detecting ghost and ship collisions works correctly. Writing a <code>print()</code> call is a simple way to ensure we’re detecting these collisions properly. Now when you run <i>GhostInvasion</i>, the message <i>Ship
                hit!!!</i> should appear in the terminal whenever an ghost runs into the ship.
           

<!-- *********************************************part35************************************* -->

- <h3 id = "14.2">Responding to Ghost and Ship Collisions</h3>

      
    - Now we need to figure out exactly what will happen when an ghost collides with the ship. Instead of destroying the <code>ship</code> instance and creating a new one, we’ll count how many times the ship has been hit by tracking statistics
                for the game. Tracking statistics will also be useful for scoring. Let’s write a new class, GameStats, to track game statistics, and save it as <code>game_stats.py</code>
            
```            
    ------------------------------game_stats.py----------------------------------

    class GameStats:
        """Track statistics for Ghost Invasion."""
        def __init__(self, ai_game):
            """Initialize statistics."""
            self.settings = ai_game.settings
            self.reset_stats()

        def reset_stats(self):
            """Initialize statistics that can change during the game."""
            self.ships_left = self.settings.ship_limit

```
    
   - We’ll make one GameStats instance for the entire time <i>GhostInvasion</i> is running. But we’ll need to reset some statistics each time the player starts a new game. To do this, we’ll initialize most of the statistics in the <code>reset _stats()</code>                method instead of directly in `__init()__`. We’ll call this method from `__init()__` so the statistics are set properly when the GameStats instance is first created But we’ll also be able to call <code>reset_stats()</code>                any time the player starts a new game.
          

   
   - Right now we have only one statistic, <code>ships_left</code>, the value of which will change throughout the game. The number of ships the player starts with should be stored in <code>settings.py</code> as <code>ship_limit</code>
            

   - We also need to make a few changes in <code>ghost_invasion.py</code> to create an instance of GameStats. We <code>import</code> the <code>sleep()</code> function from the time module in the Python standard library so we can pause the game
                for a moment when the ship is hit. We also <code>import GameStats</code>. We’ll create an instance of GameStats in `__init()__`:

```
    # Create an instance to store game statistics.
    self.stats = GameStats(self)
```

    
   - We make the instance after creating the game window but before defining other game elements, such as the ship. When an ghost hits the ship, we’ll subtract one from the number of ships left, destroy all existing ghosts and bullets, create a new fleet,
                and reposition the ship in the middle of the screen. We’ll also pause the game for a moment so the player can notice the collision and regroup before a new fleet appears
            

   - Let’s put most of this code in a new method called <code>_ship_hit()</code>. We’ll call this method from <code>_update_ghosts()</code> when an ghost hits the ship:
    

   - The new method <code>_ship_hit()</code> coordinates the response when an ghost hits a ship. Inside <code>_ship_hit()</code>, the number of ships left is reduced by 1 , after which we empty the groups ghosts and bullets. Next, we create
                a new fleet and center the ship. (We’ll add the method <code>center_ship()</code> to Ship in a moment.) Then we add a pause after the updates have been made to all the game elements but before any changes have been drawn to the screen,
                so the player can see that their ship has been hit. The <code>sleep()</code> call pauses program execution for half a second, long enough for the player to see that the ghost has hit the ship. When the <code>sleep()</code> function ends,
                code execution moves on to the <code>_update_screen()</code> method, which draws the new fleet to the screen
    

   - In <code>_update_ghosts()</code>, we replace the <code>print()</code> call with a call to <code>_ship_hit()</code> when an ghost hits the ship. Here’s the new method <code>center_ship()</code> add it to the end of <code>ship.py</code>:

```
    ------------------------ship.py---------------------------
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

```

   - We center the ship the same way we did in `__init()__`. After centering it, we reset the <code>self.x</code> attribute, which allows us to track the ship’s exact position.
           
        - <b>Note:</b><i><u>Notice that we never make more than one ship; we make only one ship instance for the
            whole game and recenter it whenever the ship has been hit. The statistic <code>ships_left</code>
            will tell us when the player has run out of</u></i>
        

<!-- *********************************************part36************************************* -->

- <h3 id = "14.3">Ghosts that Reach the Bottom of the Screen</h3>

        
    - If an ghost reaches the bottom of the screen, we’ll have the game respond the same way it does when an ghost hits the ship. To check when this happens, add a new method in <code>ghost_invasion.py</code>:

```               
    def _check_ghosts_bottom(self):
        #"""Check if any ghosts have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for ghost in self.ghosts.sprites():
            if ghost.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

```
            

   
   - The method <code>_check_ghosts_bottom()</code> checks whether any ghosts have reached the bottom of the screen. An ghost reaches the bottom when its rect.bottom value is greater than or equal to the screen’s <code>rect.bottom</code> attribute.
                If an ghost reaches the bottom, we call <code>_ship_hit()</code>. If one ghost hits the bottom, there’s no need to check the rest, so we break out of the loop after calling <code>_ship_hit()</code>. We’ll call this method from <code>_update_ghosts()</code>
            
        
   - We call <code>_check_ghosts_bottom()</code> after updating the positions of all the ghosts and after looking for ghost and ship collisions. Now a new fleet will appear every time the ship is hit by an ghost or an ghost reaches the bottom
                of the screen.
          

<!-- *********************************************part37************************************* -->

<h3 id = "14.4">Game Over!</h3>

   - Ghost Invasion feels more complete now, but the game never ends. The value of <code>ships_left</code> just grows increasingly negative. Let’s add a <code>game_active</code> flag as an attribute to <code>GameStats</code> to end the game
                when the player runs out of ships. We’ll set this flag at the end of the `__init()__` method in GameStats:

```
    ------------------------------game_stats.py----------------------------
    # Start Ghost Invasion in an active state.
    self.game_active = True
```

   - Now we add code to <code>_ship_hit()</code> that sets <code>game_active</code> to False when the player has used up all their ships.
           

   
   - Most of <code>_ship_hit()</code> is unchanged. We’ve moved all the existing code into an <code>if</code> block, which tests to make sure the player has at least one ship remaining. If so, we create a new fleet, pause, and move on. If the
                player has no ships left, we set <code>game_active</code> to False.
           

<!-- *********************************************part38************************************* -->

- <h3 id = "14.5">Identifying When Parts of the Game Should Run</h3>

    - We need to identify the parts of the game that should always run and the parts that should run only when the game is active.
            
    - In the main loop, we always need to call <code>_check_events()</code>, even if the game is inactive. For example, we still need to know if the user presses <b>Q</b> to quit the game or clicks the button to close the window. We also continue
                updating the screen so we can make changes to the screen while waiting to see whether the player chooses to start a new game. The rest of the function calls only need to happen when the game is active, because when the game is inactive,
                we don’t need to update the positions of game elements.


    - Now when you play Ghost Invasion, the game should freeze when you’ve used up all your ships.
        


<h2 id="15">Adding the Play Button</h2>

<p>In this section, we’ll add a Play button that appears before a game begins
and reappears when the game ends so the player can play again.
Right now the game begins as soon as you run `ghost_invasion.py` Let’s
start the game in an inactive state and then prompt the player to click a Play
button to begin. To do this, modify the `__init__()` method of GameStats</p>

```
------------------------game_stats.py--------------------------

	# Start game in an inactive state.
	self.game_active = False
```
<p>Now the game should start in an inactive state with no way for the
player to start it until we make a Play button.</p>

<!-- *********************************************part39************************************* -->


- <h3 id = "15.1">Creating a Button Class</h3>

	- Because Pygame doesn’t have a built-in method for making buttons, we’ll
	write a `Button` class to create a filled rectangle with a label. You can use this
	code to make any button in a game. Here’s the first part of the `Button` class;
	save it as `button.py`:

	```
	--------------------------button.py--------------------------------

	import pygame.font      #importing pygame_font

	class Button:
	    def __init__(self, ai_game, msg):

	        # """Initialize button attributes."""
	        self.screen = ai_game.screen
	        self.screen_rect = self.screen.get_rect()

	        # Set the dimensions and properties of the button.
	        self.width, self.height = 200, 50
	        self.button_color = (0, 255, 0)
	        self.text_color = (255, 255, 255)
	        self.font = pygame.font.SysFont(None, 48)
	        
	        # Build the button's rect object and center it.
	        self.rect = pygame.Rect(0, 0, self.width, self.height)
	        self.rect.center = self.screen_rect.center
	        
	        # The button message needs to be prepped only once.
	        self._prep_msg(msg)

	```

    - First, we `import` the `pygame.font` module, which lets Pygame render text
	to the screen. The `__init__()` method takes the parameters self, the `ai_game` object, and msg, which contains the button’s text. We set the button dimensions, and then set `button_color` to color the button’s `rect` object bright
	green and set `text_color` to render the text in white.

	 - We prepare a `font` attribute for rendering text. The `None` argument
	tells Pygame to use the default font, and `48` specifies the size of the text. To
	center the button on the screen, we create a `rect` for the button and set its
	`center` attribute to match that of the screen.


	 - Pygame works with text by rendering the string you want to display as
	an image. We call `_prep_msg()`to handle this rendering.
	Here’s the code for `_prep_msg()`:

```
------------------------------------button.py-----------------------------------

	def _prep_msg(self, msg):
		#"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
```
	
  - The `_prep_msg()` method needs a `self` parameter and the text to be rendered
	as an image (msg). The call to `font.render()` turns the text stored in
	`msg` into an image, which we then store in `self.msg_image`. The `font.render()`
	method also takes a Boolean value to turn antialiasing on or off (antialiasing
	makes the edges of the text smoother). The remaining arguments are
	the specified font color and background color. We set antialiasing to True
	and set the text background to the same color as the button.

  - We center the text image on the button by creating a `rect` from
	the image and setting its `center` attribute to match that of the button.
	Finally, we create a `draw_button()` method that we can call to display the
	button onscreen:

```
--------------------------button.py--------------------------------

	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
```

  - We call `screen.fill()`to draw the rectangular portion of the button.
	Then we call `screen.blit()` to draw the text image to the screen, passing it
	an image and the `rect` object associated with the image. This completes the
	`Button`class.


  
<!-- *********************************************part40************************************* -->


- <h3 id="15.2">Drawing the Button to the Screen</h3>



	- We’ll use the Button class to create a Play button in GhostInvasion.
	Because we need only one Play button, we’ll create the button in the
	`__init__()` method of `GhostInvasion`. We can place this code at the very end
	of `__init__()`:

	```
	-------------ghost_invasion.py---------------

	# Make the Play button.
	self.play_button = Button(self, "Play")
	```


	- This code creates an instance of `Button` with the label Play, but it doesn’t
draw the button to the screen. We’ll call the button’s `draw_button()` method
in `_update_screen()`:

	```
	-------------ghost_invasion.py---------------

	# Draw the play button if the game is inactive.
	if not self.stats.game_active:
		self.play_button.draw_button()
	```

	- To make the Play button visible above all other elements on the screen,
	we draw it after all the other elements have been drawn but before flipping
	to a new screen. We include it in an if block, so the button only appears
	when the game is inactive. Now when you run Ghost Invasion, you should see a Play button in the
	center of the screen.

<!-- *********************************************part41************************************* -->


- <h3 id = "15.3">Starting the Game</h3>

	- To start a new game when the player clicks Play, add the following `elif`
block to the end of `_check_events()` to monitor mouse events over the button:


	```
	-------------ghost_invasion.py---------------

	elif event.type == pygame.MOUSEBUTTONDOWN:
		mouse_pos = pygame.mouse.get_pos()
		self._check_play_button(mouse_pos)
	```

	- Pygame detects a `MOUSEBUTTONDOWN` event when the player clicks anywhere
	on the screen, but we want to restrict our game to respond to mouse clicks
	only on the `Play` button. To accomplish this, we use `pygame.mouse.get_pos()`,
	which returns a tuple containing the mouse cursor’s x- and y-coordinates
	when the mouse button is clicked. We send these values to the new
	method `_check_play_button()`.
	Here’s `_check_play_button()`, which I chose to place after `_check_events()`:

	```
	-----------------------ghost_invasion.py-----------------------

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		if self.play_button.rect.collidepoint(mouse_pos):
			self.stats.game_active = True
	```

	- We use the rect method `collidepoint()` to check whether the point of the
	mouse click overlaps the region defined by the Play button’s `rect`. If so, we
	set `game_active` to `True`, and the game begins!
	At this point, you should be able to start and play a full game. When
	the game ends, the value of `game_active` should become `False` and the `Play`
	button should reappear.

<!-- *********************************************part42************************************* -->


- <h3 id = "15.4">Resetting the Game</h3>

	- The Play button code we just wrote works the first time the player clicks
	`Play`. But it doesn’t work after the first game ends, because the conditions
	that caused the game to end haven’t been reset.
	To reset the game each time the player clicks Play, we need to `reset` the
	game statistics, clear out the old ghosts and bullets, build a new fleet, and
	center the ship, as shown here:

	```
	-------------------ghost_invasion.py----------------

	# Reset the game statistics.
	self.stats.reset_stats()

	--------------------------------------------------

	# Get rid of any remaining ghosts and bullets.
	self.ghosts.empty()
	self.bullets.empty()

	# Create a new fleet and center the ship.
	self._create_fleet()
	self.ship.center_ship()

	```

	- We reset the game statistics, which gives the player three new
	ships. Then we set `game_active` to `True` so the game will begin as soon as the
	code in this function finishes running. We empty the `ghosts` and `bullets`
	groups, and then create a new fleet and center the ship. Now the game will reset properly each time you click Play, allowing you to play it as many times as you want!


<!-- *********************************************part43************************************* -->


- <h3 id= "15.5">Deactivating the Play Button</h3>

	- One issue with our Play button is that the button region on the screen will
	continue to respond to clicks even when the Play button isn’t visible. If you
	click the Play button area by accident after a game begins, the game will
	restart. To fix this, set the game to start only when `game_active` is `False`:

	```
	-------------------ghost_invasion.py----------------

	button_clicked = self.play_button.rect.collidepoint(mouse_pos)
	if button_clicked and not self.stats.game_active:

	```

	-  The flag button_clicked stores a True or False value. and the game
will restart only if Play is clicked and the game is not currently active. To test this behavior, start a new game and repeatedly click where the Play
button should be. If everything works as expected, clicking the Play button
area should have no effect on the gameplay.

<!-- *********************************************part44************************************* -->


- <h3 id= "15.6">Hiding the Mouse Cursor</h3>

	- We want the mouse cursor to be visible to begin play, but once play begins, it
just gets in the way. To fix this, we’ll make it invisible when the game becomes
active. We can do this at the end of the `if` block in `_check_play_button()`:

	```
	-----------------ghost_invasion.py---------------

	# Hide the mouse cursor.
	pygame.mouse.set_visible(False)

	```

	- Passing `False` to `set_visible()` tells Pygame to hide the cursor when the
mouse is over the game window.
`
	- We’ll make the cursor reappear once the game ends so the player can
click Play again to begin a new game. Here’s the code to do that:


	```pygame.mouse.set_visible(True)```

	- We make the cursor visible again as soon as the game becomes inactive,
which happens in `_ship_hit()`. Attention to details like this makes your game
more professional looking and allows the player to focus on playing rather
than figuring out the user interface.



<h2 id="16">Leveling Up</h2>

<p>In our current game, once a player shoots down the entire ghost fleet, the
player reaches a new level, but the game difficulty doesn’t change. Let’s
liven things up a bit and make the game more challenging by increasing
the game’s speed each time a player clears the Screen.</p>


<!-- *********************************************part45************************************* -->

- <h3 id="16.1">Modifying the Speed Settings</h3>

	- We’ll first reorganize the `Settings` class to group the game settings into
	static and changing ones. We’ll also make sure that settings that change, during the game reset when we start a new game. Here’s the `__init__()`
	method for `settings.py`:

	```
	--------------settings.py--------------------

	# How quickly the game speeds up
	self.speedup_scale = 1.5
	self.initialize_dynamic_settings()
	
	```

	- We continue to initialize those settings that stay constant in the __init__()
	method. We add a `speedup_scale` setting to control how quickly the game
	speeds up: a value of 2 will double the game speed every time the player
	reaches a new level; a value of 1 will keep the speed constant. A value like
	1.1 should increase the speed enough to make the game challenging but not
	impossible. Finally, we call the `initialize_dynamic_settings()` method to initialize
	the values for attributes that need to change throughout the game.
	Here’s the code for `initialize_dynamic_settings()`:

	```
	--------------settings.py--------------------

	def initialize_dynamic_settings(self):
		#"""Initialize settings that change throughout the game."""
		self.ship_speed = 2.0
		self.bullet_speed = 3.0
		self.ghost_speed = 2.0
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

	```

	- This method sets the initial values for the ship, bullet, and ghost
speeds. We’ll increase these speeds as the player progresses in the game
and reset them each time the player starts a new game. We include `fleet
_direction` in this method so the ghosts always move right at the beginning
of a new game. We don’t need to increase the value of `fleet_drop_speed`,
because when the ghosts move faster across the screen, they’ll also come
down the screen faster.


	- To increase the speeds of the ship, bullets, and ghosts each
time the player reaches a new level, we’ll write a new method called
increase_speed():

	```
	--------------settings.py--------------------

	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.ghost_speed *= self.speedup_scale
	```

	- To increase the speed of these game elements, we multiply each speed
	setting by the value of `speedup_scale`.
	We increase the game’s tempo by calling `increase_speed()` in `_check
	_bullet_ghost_collisions()` when the last ghost in a fleet has been shot down:

	```self.settings.increase_speed()```

	- Changing the values of the speed settings `ship_speed`, `ghost_speed`, and
`bullet_speed` is enough to speed up the entire game!



<!-- *********************************************part46************************************* -->

- <h3 id="16.2">Resetting the Speed</h3>


	- Now we need to return any changed settings to their initial values each
time the player starts a new game; otherwise, each new game would start
with the increased speed settings of the previous game:

	```
	-------------------ghost_invasion.py----------------	

	# Reset the game settings.
	self.settings.initialize_dynamic_settings()

	```

	- Playing Ghost Invasion should be more fun and challenging now. Each
time you clear the screen, the game should speed up and become slightly
more difficult. If the game becomes too difficult too quickly, decrease the
value of `settings.speedup_scale`. Or if the game isn’t challenging enough,
increase the value slightly. Find a sweet spot by ramping up the difficulty in
a reasonable amount of time. The first couple of screens should be easy, the
next few challenging but double, and subsequent screens almost impossibly
difficult.



<h2 id="17">Scoring</h2>

<p>Let’s implement a scoring system to track the game’s score in real time and
display the high score, level, and number of ships remaining.
The score is a game statistic, so we’ll add a `score` attribute to `GameStats`:<p>

```self.score = 0 ```

<p>To reset the score each time a new game starts, we initialize score in
`reset_stats()` rather than `__init__()`.</p>

<!-- *********************************************part47************************************* -->

- <h3 id="17.1">Displaying the Score</h3>

	- To display the score on the screen, we first create a new class, Scoreboard. For
now, this class will just display the current score, but eventually we’ll use
it to report the high score, level, and number of ships remaining as well.
Here’s the first part of the class; save it as `scoreboard.py`:


	```
  ----------------------scoreboard.py--------------------------

	import pygame.font
	
	class Scoreboard:
		
		"""A class to report scoring information."""
		def __init__(self, ai_game):
		
		#"""Initialize scorekeeping attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		
		# Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# Prepare the initial score image.
		self.prep_score()

  ```

  - Because Scoreboard writes text to the screen, we begin by importing the
pygame.font module. Next, we give `__init__()` the `ai_game` parameter so it can
access the settings, screen, and stats objects, which it will need to report the
values we’re tracking, Then we set a text color. and instantiate a font
object.

  - To turn the text to be displayed into an image, we call `prep_score()`,
which we define here:

```
  ----------------------scoreboard.py--------------------------

	def prep_score(self):
		
		"""Turn the score into a rendered image."""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True,
		self.text_color, self.settings.bg_color)
		
		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

```
  
   - In `prep_score()`, we turn the numerical value `stats.score` into a string,
and then pass this string to `render()`, which creates the image. To display
the score clearly onscreen, we pass the screen’s background color and the
text color to `render()`.

   - We’ll position the score in the upper-right corner of the screen and
have it expand to the left as the score increases and the width of the number
grows. To make sure the score always lines up with the right side of the
screen, we create a `rect` called `score_rect` and set its right edge 20 pixels
from the right edge of the screen. We then place the top edge 20 pixels
down from the top of the screen.

   - Then we create a show_score() method to display the rendered score
image, This method draws the score image onscreen at the location score_rect
specifies.

```
----------------------scoreboard.py--------------------------

	def show_score(self):  
	
		#"""Draw score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)

```




<!-- *********************************************part48************************************* -->


- <h3 id="17.2">Making a Scoreboard</h3>

	- To display the score, we’ll create a Scoreboard instance in `GhostInvasion`.
	- Next, we make an instance of Scoreboard in `__init__()`:

	```
	-------------------ghost_invasion.py----------------	

	# Create an instance to store game statistics,and create a scoreboard.
	self.stats = GameStats(self)
	self.sb = Scoreboard(self)

	```

	- Then we draw the scoreboard onscreen in `_update_screen()`:

	```
	-------------------ghost_invasion.py----------------	

	# Draw the score information.
	self.sb.show_score()
	```

	- We call show_score() just before we draw the Play button.
When you run Ghost Invasion now, a 0 should appear at the top right
of the screen. (At this point, we just want to make sure the score appears in
the right place before developing the scoring system further.)




<!-- *********************************************part49************************************* -->

- <h3 id="17.3">Updating the Score as Ghosts Are Shot Down</h3>

	- To write a live score onscreen, we update the value of `stats.score` whenever
an ghost is hit, and then call `prep_score()` to update the score image. But
first, let’s determine how many points a player gets each time they shoot
down an ghost.

	```
  -----------------settings.py--------------------

	# Scoring
	self.ghost_points = 50

	```

	- We’ll increase each ghost’s point value as the game progresses. To make
sure this point value is reset each time a new game starts, we set the value in
`initialize_dynamic_settings()`.

	- Let’s update the score each time an ghost is shot down in `_check_bullet
_ghost_collisions()`:

	```
  -----------------------ghost_invasion.py----------------------

	if collisions:
		self.stats.score += self.settings.ghost_points
		self.sb.prep_score()

	```

	- When a bullet hits an ghost, Pygame returns a collisions dictionary.
We check whether the dictionary exists, and if it does, the ghost’s value is
added to the score. We then call prep_score() to create a new image for the
updated score.
Now when you play Ghost Invasion, you should be able to rack up points!



<!-- *********************************************part50************************************* -->

- <h3 id="17.4">Resetting the Score</h3>

	- Right now, we’re only prepping a new score after an ghost has been hit,
which works for most of the game. But we still see the old score when a new
game starts until the first ghost is hit in the new game.
We can fix this by prepping the score when starting a new game:

	```self.sb.prep_score()```

	- We call `prep_score()` after resetting the game stats when starting a new
game. This preps the scoreboard with a 0 score.



<!-- *********************************************part51************************************* -->

- <h3 id="17.5">Making Sure to Score All Hits</h3>


	- As currently written, our code could miss scoring for some ghosts. For
example,
if two bullets collide with ghosts during the same pass through
the loop or if we make an extra-wide bullet to hit multiple ghosts, the
player will only receive points for hitting one of the ghosts. To fix this,
let’s refine the way that bullet and ghost collisions are detected.

	- In `_check_bullet_ghost_collisions()`, any bullet that collides with an ghost
becomes a key in the `collisions` dictionary. The value associated with each
bullet is a list of ghosts it has collided with. We loop through the values in
the `collisions` dictionary to make sure we award points for each ghost hit.


	```
  ----------------------------ghost_invasion.py---------------------------

	for ghosts in collisions.values():
		self.stats.score += self.settings.ghost_points * len(ghosts)
	
	```


	- If the collisions dictionary has been defined, we loop through all values
in the dictionary. Remember that each value is a list of ghosts hit by a single
bullet. We multiply the value of each ghost by the number of ghosts in each
list and add this amount to the current score. To test this, change the width
of a bullet to 300 pixels and verify that you receive points for each ghost you
hit with your extra-wide bullets; then return the bullet width to its normal
value.


<!-- *********************************************part52************************************* -->

- <h3 id="17.6">Increasing Point Values</h3>

	- Because the game gets more difficult each time a player reaches a new level,
ghosts in later levels should be worth more points. To implement this functionality,
we’ll add code to increase the point value when the game’s speed
increases:

	```
  -----------------settings.py------------------------

	# How quickly the ghost point values increase
	self.score_scale = 1.5

	```



<!-- *********************************************part53************************************* -->

- <h3 id="17.7">Rounding the Score</h3>


	- Most arcade-style shooting games report scores as multiples of 10, so let’s
follow that lead with our scores. Also, let’s format the score to include
comma separators in large numbers. We’ll make this change in `Scoreboard`:

	```
  ------------------scoreboard.py------------------------

	rounded_score = round(self.stats.score, -1)
	score_str = "{:,}".format(rounded_score)

	```

	- The `round()` function normally rounds a decimal number to a set number
of decimal places given as the second argument. However, when you
pass a negative number as the second argument, `round()` will round the
value to the nearest 10, 100, 1000, and so on. The code tells Python to
round the value of `stats.score` to the nearest 10 and store it in `rounded_score`.

	- a string formatting directive tells Python to insert commas into
numbers when converting a numerical value to a string: for example, to
output `1,000,000` instead of 1000000. Now when you run the game, you should
see a neatly formatted, rounded score even when you rack up lots of points.


<!-- *********************************************part54************************************* -->

- <h3 id="17.8">High Scores</h3>

	- Every player wants to beat a game’s high score, so let’s track and report high
scores to give players something to work toward. We’ll store high scores in
`GameStats`:

	```
  -----------------game_stats.py---------------------

	# High score should never be reset.
	self.high_score = 0

	```
	- Because the high score should never be reset, we initialize high_score in
`__init__()` rather than in `reset_stats()`. Next, we’ll modify Scoreboard to display the high score. Let’s start with
the `__init__()` method:
	
	```
  -----------------scoreboard.py-----------------------

	self.prep_high_score()
	```

	- The high score will be displayed separately from the score, so we need a
new method, `prep_high_score()`, to prepare the high score image. Here’s the `prep_high_score()` method:

	```
  ----------------------scoreboard.py-------------------------

	def prep_high_score(self):
		
		"""Turn the high score into a rendered image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
		
		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	```

	- We round the high score to the nearest 10 and format it with commas.
We then generate an image from the high score, center the high score
rect horizontally, and set its top attribute to match the top of the score
image.

	- The `show_score()` method now draws the current score at the top right
and the high score at the top center of the screen:


	```
  ----------------------scoreboard.py---------------------------------

	self.screen.blit(self.high_score_image, self.high_score_rect)
	```

	- To check for high scores, we’ll write a new method, `check_high_score()`,
in `Scoreboard`:

	```
  ----------------------scoreboard.py---------------------------------

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	```

	- The method `check_high_score()` checks the current score against the
high score. If the current score is greater, we update the value of `high_score`
and call `prep_high_score()` to update the high score’s image.


	- We need to call `check_high_score()` each time an ghost is hit after updating
the score in `_check_bullet_ghost_collisions()`:

	```self.sb.check_high_score()```

	- We call `check_high_score()` when the collisions dictionary is present, and
we do so after updating the score for all the ghosts that have been hit.

	


<!-- *********************************************part55************************************* -->

- <h3 id="17.9">Displaying the Level</h3>

	- To display the player’s level in the game, we first need an attribute in
`GameStats` representing the current level. To reset the level at the start of
each new game, initialize it in `reset_stats()`:

	```
  ----------------game_stats.py----------------

	self.level = 1
	
	```

	- To have Scoreboard display the current level, we call a new method, `prep
_level()`, from `__init__()`:

	```
  ----------------scoreboard.py----------------

	self.prep_level()
	
	```

	- Here’s `prep_level()`:

	```
  ----------------scoreboard.py----------------

	def prep_level(self):
		
		#"""Turn the level into a rendered image."""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
		
		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	```

	- The `prep_level()` method creates an image from the value stored in
`stats.level`  and sets the image’s `right` attribute to match the score’s `right`
attribute. It then sets the `top` attribute `10 pixels` beneath the bottom of
the score image to leave space between the score and the level. We also need to update `show_score()`:


	```
  ----------------scoreboard.py----------------

	self.screen.blit(self.level_image, self.level_rect)

	```

	- This new line draws the level image to the screen.
We’ll increment `stats.level` and update the level image in `_check_bullet
_ghost_collisions()`:

	```
  ----------------ghost_invasion.py----------------

	# Increase level.
	self.stats.level += 1
	self.sb.prep_level()

	```

	- If a fleet is destroyed, we increment the value of stats.level and call
`prep_level()` to make sure the new level displays correctly.
To ensure the level image updates properly at the start of a new game,
we also call `prep_level()` when the player clicks the Play button:


	```
  ----------------ghost_invasion.py----------------

	self.sb.prep_level()

	```

	- <b>Note:</b> <i>In some classic games, the scores have labels, such as Score, High Score, and Level.
We’ve omitted these labels because the meaning of each number becomes clear once
you’ve played the game. To include these labels, add them to the score strings just
before the calls to `font.render()` in Scoreboard.</i>


<!-- *********************************************part56************************************* -->

- <h3 id="17.10">High Scores</h3>


	- Finally, let’s display the number of ships the player has left, but this time,
let’s use a graphic. To do so, we’ll draw ships in the upper-left corner of the screen to represent how many ships are left, just as many classic arcade
games do.


	- First, we need to make `Ship` inherit from `Sprite` so we can create a group
of ships:


	```
  ---------------ship.py------------------------

	from pygame.sprite import Sprite

	```
	- Here we `import Sprite`, make sure Ship inherits from `Sprite`, and call
`super()` at the beginning of `__init__()`. Next, we need to modify `Scoreboard` to create a group of ships we can
display. Here are the import statements for `Scoreboard`:


	```
  ---------------scoreboard.py------------------------

	from pygame.sprite import Group
	from ship import Ship

	```

	- Because we’re making a group of ships, we import the `Group` and `Ship`
classes.
Here’s `__init__()`:


	```
  ---------------scoreboard.py------------------------

	self.ai_game = ai_game
	self.prep_ships()

	```

	- We assign the game instance to an attribute, because we’ll need it to
create some ships. We call `prep_ships()` after the call to `prep_level()`.
Here’s `prep_ships()`:

	```
  ---------------scoreboard.py------------------------

	def prep_ships(self):
		#"""Show how many ships are left."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
		ship = Ship(self.ai_game)
		ship.rect.x = 10 + ship_number * ship.rect.width
		ship.rect.y = 10
		self.ships.add(ship)

	```

	- The `prep_ships()` method creates an empty group, `self.ships`, to hold
	the ship instances. To fill this group, a loop runs once for every ship the
	player has left. Inside the loop, we create a new ship and set each ship’s
	x-coordinate value so the ships appear next to each other with a 10-pixel
	margin on the left side of the group of ships. We set the y-coordinate
	value 10 pixels down from the top of the screen so the ships appear in the
	upper-left corner of the screen. Then we add each new ship to the group
	ships.

	- Now we need to draw the ships to the screen.

	```
  ---------------scoreboard.py------------------------

	self.ships.draw(self.screen)

	```

	- To display the ships on the screen, we call `draw()` on the group, and
Pygame draws each ship.
	
	- To show the player how many ships they have to start with, we call
	`prep_ships()` when a new game starts. We do this in `_check_play_button()` in
	`GhostInvasion`:


	```
  ---------------ghost_invasion.py------------------------

	self.sb.prep_ships()

	```



  
