# Mad Libs Project: Tragic and Hilarious Stories

def get_input(prompt):
    """Function to get user input with a prompt."""
    return input(prompt)

def create_tragic_story(elderly_woman_name, grandson_name):
    """Generate the tragic story using provided names."""
    tragic_story_template = """
    In a quiet hospital room, an elderly woman named {elderly_woman_name} lay in bed, her memories fading. 
    Every day, her grandson {grandson_name} visited, hoping to spark recognition. 
    One day, he brought a photo of their last vacation together, but she only stared blankly. 
    As he held her hand, he whispered, 'I love you,' knowing this might be their final moment together.
    """
    
    return tragic_story_template.format(
        elderly_woman_name=elderly_woman_name,
        grandson_name=grandson_name
    )

def create_hilarious_story(owner_name, cat_name, adjective, cat_action, dog_action, noun):
    """Generate the hilarious story using provided inputs."""
    hilarious_story_template = """
    One sunny afternoon, {owner_name} decided to train their cat {cat_name} to fetch. 
    Armed with a {adjective} toy, they threw it across the yard. 
    To their surprise, the cat {cat_action} instead of fetching! 
    The neighbor's dog {dog_action} in confusion as the cat proudly strutted back with a {noun} instead!
    """
    
    return hilarious_story_template.format(
        owner_name=owner_name,
        cat_name=cat_name,
        adjective=adjective,
        cat_action=cat_action,
        dog_action=dog_action,
        noun=noun
    )

def main():
    """Main function to run the Mad Libs project."""
    
    # Gather user input for the tragic story
    print("Let's create a tragic story!")
    elderly_woman_name = get_input("Enter the name of the elderly woman: ")
    grandson_name = get_input("Enter the name of the grandson: ")

    # Generate and display the tragic story
    tragic_story = create_tragic_story(elderly_woman_name, grandson_name)
    print("\nHere is your tragic Mad Libs story:")
    print(tragic_story)

    # Gather user input for the hilarious story
    print("Now, let's create a hilarious story!")
    owner_name = get_input("Enter the name of the cat owner: ")
    cat_name = get_input("Enter the name of the cat: ")
    adjective = get_input("Enter an adjective: ")
    cat_action = get_input("Enter a verb (what the cat does): ")
    dog_action = get_input("Enter a verb (what the dog does): ")
    noun = get_input("Enter a noun: ")

    # Generate and display the hilarious story
    hilarious_story = create_hilarious_story(owner_name, cat_name, adjective, cat_action, dog_action, noun)
    print("\nHere is your hilarious Mad Libs story:")
    print(hilarious_story)

# Entry point for the program
if __name__ == "__main__":
    main()