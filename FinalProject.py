user = [] 
user  


def intro():
    while True:
        print("Hello, Welcome to Mindfulness Right Now\n")
    
        user_name = input("What is your name? ").strip().capitalize()

        if user_name in user:
            print("Hello " + user_name) 
            question_prompt(intro) 
             
        else:
            add = input("Would you like to add your name to the list? (y/n) ").strip().lower()
        
            if add == "y":
                user.append(user_name)
                print("You are on the list!") 
                question_prompt(intro) 
            
            if add == "n":
             print("See you next time!") 
             break
             
            
            else: 
                print("invalid option") 
                
              


emotions = {"Happy":{"Prompt 1":"You are getting better and better everyday", "Prompt 2": "You are having a postive impact on the people you come in contact with", "Prompt 3": "You are successsful, strong, and confident" }, 
             "Sad":{"Prompt 1":"You are doing the best you can", "Prompt 2": "You are not pushed by your problems, you are led by your dreams", "Prompt 3": "You have made it through hard times before, and have come out stronger because of them. You are going to get through this"}, 
             "Mad":{"Prompt 1":"Breathe in and out and take a 10 minute walk", "Prompt 2": "Close your eyes, and count slowly to 10", "Prompt 3": "Listen to a song that reflects what you are feeling" }, 
             "Anxious":{"Prompt 1":"Stretch; shrug both shoulders, hold them up high for a little while, and then release them", "Prompt 2": "Close your eyes; vision a person, place, or thing you love. Take five slow breaths and with each one, imagine inhaling peace and comfort, and exhaling fear and worry", "Prompt 3": "Write down what you are feeling; what does your anxiety sound, look, and feel like?"}}


import random

def question_prompt(intro): 
    question = "" 
    while question != "q": 
        question = input("\nHow are you feeling right now? (pick a letter or \'q\' to quit)\n(a) Happy\n(b) Sad\n(c) Mad\n(d) Anxious\n") 
        answer_choices = 'abcd'
       
       
     
        if question in answer_choices: 
            print("Here is what I suggest you should do!\n") 
            if question == 'a': 
                chosen_emotion = "Happy" 
                chosen_prompt = random.choice(list(emotions[chosen_emotion].values())) 
                print(f"Emotion: {chosen_emotion}, Suggestion: {chosen_prompt}")
            elif question == 'b': 
                chosen_emotion = "Sad"  
                chosen_prompt = random.choice(list(emotions[chosen_emotion].values())) 
                print(f"Emotion: {chosen_emotion}, Suggestion: {chosen_prompt}") 
            elif question == 'c': 
                chosen_emotion = "Mad" 
                chosen_prompt = random.choice(list(emotions[chosen_emotion].values())) 
                print(f"Emotion: {chosen_emotion}, Suggestion: {chosen_prompt}")
            elif question == 'd':  
                chosen_emotion = "Anxious" 
                chosen_prompt = random.choice(list(emotions[chosen_emotion].values())) 
                print(f"Emotion: {chosen_emotion}, Suggestion: {chosen_prompt}")  
           
            
           
        else: 
            if question == "q": 
                break 
            else: 
                print("invalid option")
            

intro() 
        
  

