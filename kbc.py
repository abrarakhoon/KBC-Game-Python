from colorama import Fore,Style
question = [
    "Which is the capital city of India?",
    "Which is the largest planet in our solar system?",
    "Who is known as the 'Father of the Nation' in India?",
    "What is the square root of 144?",
    "Who wrote the Indian national anthem 'Jana Gana Mana'?",
    "Which planet is known as the 'Red Planet'?",
    "In which year did India gain independence?",
    "Who invented the light bulb?",
    "What is the chemical symbol for gold?",
    "Which Indian mathematician is known for his contributions to number theory and infinite series?"
]

options = [
    ["a) Mumbai", "b) New Delhi", "c) Kolkata", "d) Chennai"],
    ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
    ["a) Jawaharlal Nehru", "b) Subhas Chandra Bose", "c) Mahatma Gandhi", "d) Bhagat Singh"],
    ["a) 12", "b) 14", "c) 16", "d) 10"],
    ["a) Rabindranath Tagore", "b) Bankim Chandra Chatterjee", "c) Sarojini Naidu", "d) Lala Lajpat Rai"],
    ["a) Venus", "b) Mars", "c) Saturn", "d) Mercury"],
    ["a) 1945", "b) 1946", "c) 1947", "d) 1948"],
    ["a) Alexander Graham Bell", "b) Thomas Edison", "c) Nikola Tesla", "d) James Watt"],
    ["a) Ag", "b) Au", "c) Pb", "d) Go"],
    ["a) Satyendra Nath Bose", "b) Srinivasa Ramanujan", "c) C.V. Raman", "d) Homi Bhabha"]
]

answers = ['b', 'c', 'c', 'a', 'a', 'b', 'c', 'b', 'b', 'b']

def play_kbc():
    prize_money = 0
    levels = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 70000000]
    print("\nWelcome to KBC!\n")
    
    for i in range(len(question)):
        print(Fore.GREEN+f"Q{i + 1}: {question[i]}",Fore.RED+f"This Question is of ₹{levels[i]}"+Style.RESET_ALL)
        for option in options[i]:
            print(option)
        
        user_answer = input(Fore.YELLOW+"\nEnter your answer (a/b/c/d): "+Style.RESET_ALL)
        
        if user_answer == answers[i]:
            prize_money += levels[i]  # Use += to accumulate prize money
            print(f"Correct! You've won ₹{prize_money}\n")
        else:
            print(Fore.LIGHTRED_EX+"Incorrect answer!")
            print(Fore.RED+"Game over."+Style.RESET_ALL)
            break  # Exit the loop if the answer is incorrect
    else:
        print(f"Congratulations! You've won the jackpot of ₹{prize_money}\n")

    print(f"You take home ₹{prize_money}")

play_kbc()