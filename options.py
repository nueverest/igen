import uuid
from copy import deepcopy


class Options:
    def __init__(self):
        self.grid = {
            'Subject': [
                { 'id': 'subject1', 'name': 'Man', 'selected': 'False'}, 
                { 'id': 'subject2', 'name': 'Woman', 'selected': 'False'},
                { 'id': 'subject3', 'name': 'Animal', 'selected': 'False'},
                { 'id': 'subject4', 'name': 'Plant', 'selected': 'False'},
                { 'id': 'subject5', 'name': 'Vehicle', 'selected': 'False'},
            ],
            'Cinematic Vibe': [
                { 'id': 'vibe1', 'name': 'Star Wars', 'selected': 'False'}, 
                { 'id': 'vibe2', 'name': 'Barbie', 'selected': 'False'},
                { 'id': 'vibe3', 'name': 'Anime', 'selected': 'False'},
                { 'id': 'vibe4', 'name': 'Matrix', 'selected': 'False'},
                { 'id': 'vibe5', 'name': 'Avengers', 'selected': 'False'},
            ],
            'Medium': [
                { 'id': 'medium1', 'name': 'Photo', 'selected': 'False'}, 
                { 'id': 'medium2', 'name': 'Sculpture', 'selected': 'False'},
                { 'id': 'medium3', 'name': 'Painting', 'selected': 'False'},
                { 'id': 'medium4', 'name': 'Sketch', 'selected': 'False'},
                { 'id': 'medium5', 'name': 'Carving', 'selected': 'False'},
            ],
            'Video Game': [
                { 'id': 'game1', 'name': 'Minecraft', 'selected': 'False'}, 
                { 'id': 'game2', 'name': 'GTA', 'selected': 'False'},
                { 'id': 'game3', 'name': 'Fornite', 'selected': 'False'},
                { 'id': 'game4', 'name': 'League of Legends', 'selected': 'False'},
                { 'id': 'game5', 'name': 'World of Warcraft', 'selected': 'False'},    
            ],
            'Mood': [
                { 'id': 'mood1', 'name': 'Funny', 'selected': 'False'}, 
                { 'id': 'mood2', 'name': 'Somber', 'selected': 'False'},
                { 'id': 'mood3', 'name': 'Still', 'selected': 'False'},
                { 'id': 'mood4', 'name': 'Happy', 'selected': 'False'},
                { 'id': 'mood5', 'name': 'Relaxed', 'selected': 'False'},    
            ],
        }
        self.quick_grid = {
            'Subject': [
                'Man', 'Woman', 'Animal', 'Plant', 'Vehicle',
            ],
            'Cinematic Vibe': [
                'Star Wars', 'Barbie', 'Anime', 'Matrix', 'Avengers', 
            ],
            'Medium': [
                'Photo', 'Sculpture', 'Painting', 'Sketch', 'Carving',
            ],
            'Video Game': [
                'Minecraft', 'GTA', 'Fornite', 'League of Legends', 'World of Warcraft', 
            ],
            'Mood': [
                'Funny', 'Somber', 'Still', 'Happy', 'Relaxed', 
            ],
        }

    def process_key(self, key):
        switch={
            'Subject': "of a ",
            'Cinematic Vibe': "with a cinematic vibe influenced by ",
            'Medium': "using the medium of ",
            'Video Game': "that places you in the video game ",
            'Mood': "with a mood of ",
        }
        return switch.get(key, "Not a valid key!")

    def generate_prompt(self, user_request_form):
        prompt = 'create an image ' 

        # Loop through all names.
        for key, topics in self.quick_grid.items():
            # Reset temporary vars.
            key_contains_selection = False
            names = []

            for topic in range(len(topics)):
                print(topic)
                if user_request_form[topic] == 'True':
                    key_contains_selection = True 
                    names.append(topic)

            if key_contains_selection:
                # if a dictionary item is selected
                key_str = self.process_key(key)
                prompt += ' ' + key_str + ' '

                for name in range(len(names)):
                    prompt += name + ', '
        
        print(prompt)

        return prompt
            