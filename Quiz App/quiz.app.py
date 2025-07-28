def run_quiz(questions):
    """
    Runs a quiz, asking questions and tracking the user's score.
    """
    score = 0
    # Enumerate through the questions to get both index and the question object
    for i, question in enumerate(questions):
        # Print the question number and the prompt
        print(f"\nQuestion {i + 1}: {question['prompt']}")
        # Loop through the options for the current question
        for j, option in enumerate(question["options"]):
            # Print the option letter (A, B, C, etc.) and the option text
            print(f"  {chr(ord('A') + j)}) {option}")

        # Get user's answer
        while True:
            answer = input("Enter your answer (A, B, C, etc.): ").upper()
            # Validate if the user's input is one of the valid options
            if answer in [chr(ord('A') + k) for k in range(len(question["options"]))]:
                break
            else:
                print("Invalid input. Please enter a valid option.")

        # Check if the submitted answer is the correct one
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            # If incorrect, show the correct answer
            print(f"Incorrect. The correct answer was {question['answer']}.")

    # After the quiz is over, print the final score
    print(f"\nQuiz Finished! You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    # A list of dictionary objects, where each dictionary is a question
    india_gk_questions = [
        # Existing 20 Questions
        {
            "prompt": "What is the capital of India?",
            "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
            "answer": "B"
        },
        {
            "prompt": "In which year did India gain independence from British rule?",
            "options": ["1942", "1945", "1947", "1950"],
            "answer": "C"
        },
        {
            "prompt": "What is the national animal of India?",
            "options": ["Lion", "Bengal Tiger", "Elephant", "Leopard"],
            "answer": "B"
        },
        {
            "prompt": "Which monument, built by Emperor Shah Jahan, is one of the Seven Wonders of the World?",
            "options": ["Qutub Minar", "Red Fort", "Taj Mahal", "Hawa Mahal"],
            "answer": "C"
        },
        {
            "prompt": "Who is known as the 'Father of the Nation' in India?",
            "options": ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose", "Mahatma Gandhi"],
            "answer": "D"
        },
        {
            "prompt": "What is the name of the Indian space agency?",
            "options": ["NASA", "Roscosmos", "ISRO", "ESA"],
            "answer": "C"
        },
        {
            "prompt": "Which river is considered the holiest in Hinduism and is also the longest river within India?",
            "options": ["Yamuna", "Brahmaputra", "Godavari", "Ganges (Ganga)"],
            "answer": "D"
        },
        {
            "prompt": "Who was the first Prime Minister of India?",
            "options": ["Indira Gandhi", "Jawaharlal Nehru", "Lal Bahadur Shastri", "Rajiv Gandhi"],
            "answer": "B"
        },
        {
            "prompt": "Which is the largest state in India by area?",
            "options": ["Uttar Pradesh", "Maharashtra", "Rajasthan", "Madhya Pradesh"],
            "answer": "C"
        },
        {
            "prompt": "The classical dance form 'Kathakali' originated from which state?",
            "options": ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh"],
            "answer": "B"
        },
        {
            "prompt": "Who wrote the Indian National Anthem, 'Jana Gana Mana'?",
            "options": ["Bankim Chandra Chatterjee", "Muhammad Iqbal", "Rabindranath Tagore", "Sarojini Naidu"],
            "answer": "C"
        },
        {
            "prompt": "What is the highest civilian award in India?",
            "options": ["Padma Vibhushan", "Bharat Ratna", "Padma Bhushan", "Param Vir Chakra"],
            "answer": "B"
        },
        {
            "prompt": "Which mountain range separates the Indian subcontinent from the Tibetan Plateau?",
            "options": ["The Andes", "The Rockies", "The Alps", "The Himalayas"],
            "answer": "D"
        },
        {
            "prompt": "The festival of lights, celebrated by Hindus, Jains, and Sikhs, is called?",
            "options": ["Holi", "Eid", "Diwali", "Christmas"],
            "answer": "C"
        },
        {
            "prompt": "Which city is famously known as the 'Silicon Valley of India'?",
            "options": ["Hyderabad", "Pune", "Bengaluru", "Mumbai"],
            "answer": "C"
        },
        {
            "prompt": "What is the national flower of India?",
            "options": ["Rose", "Lotus", "Marigold", "Jasmine"],
            "answer": "B"
        },
        {
            "prompt": "Who was the first woman Prime Minister of India?",
            "options": ["Pratibha Patil", "Sonia Gandhi", "Indira Gandhi", "Sushma Swaraj"],
            "answer": "C"
        },
        {
            "prompt": "The Ajanta and Ellora Caves, famous for their rock-cut sculptures, are located in which state?",
            "options": ["Maharashtra", "Karnataka", "Madhya Pradesh", "Gujarat"],
            "answer": "A"
        },
        {
            "prompt": "What is the official currency of India?",
            "options": ["Indian Rupee", "Taka", "Indian Dollar", "Rupiah"],
            "answer": "A"
        },
        {
            "prompt": "According to the census, which is the most populous state in India?",
            "options": ["Maharashtra", "Bihar", "West Bengal", "Uttar Pradesh"],
            "answer": "D"
        },
        # --- Additional 80 Questions Start Here ---
        {
            "prompt": "Who was the first President of India?",
            "options": ["Dr. S. Radhakrishnan", "Dr. Rajendra Prasad", "Zakir Hussain", "V. V. Giri"],
            "answer": "B"
        },
        {
            "prompt": "Which state is known as the 'Spice Garden of India'?",
            "options": ["Karnataka", "Kerala", "Assam", "Tamil Nadu"],
            "answer": "B"
        },
        {
            "prompt": "What is the name of the border line between India and Pakistan?",
            "options": ["Durand Line", "McMahon Line", "Radcliffe Line", "Line of Control"],
            "answer": "C"
        },
        {
            "prompt": "Who composed the national song of India, 'Vande Mataram'?",
            "options": ["Rabindranath Tagore", "Sarojini Naidu", "Bankim Chandra Chatterjee", "Subramania Bharati"],
            "answer": "C"
        },
        {
            "prompt": "What does the 'Tricolour' in the Indian flag represent?",
            "options": ["Saffron for sacrifice, white for peace, green for prosperity", "Red for revolution, white for purity, blue for justice", "Yellow for wisdom, white for truth, green for nature", "Orange for courage, blue for sky, green for earth"],
            "answer": "A"
        },
        {
            "prompt": "Where is the headquarters of the Indian Space Research Organisation (ISRO) located?",
            "options": ["Chennai", "Mumbai", "Hyderabad", "Bengaluru"],
            "answer": "D"
        },
        {
            "prompt": "The 'Green Revolution' in India was primarily associated with the production of?",
            "options": ["Milk", "Pulses", "Wheat", "Cotton"],
            "answer": "C"
        },
        {
            "prompt": "Which Indian city is known as the 'Pink City'?",
            "options": ["Jodhpur", "Udaipur", "Jaipur", "Agra"],
            "answer": "C"
        },
        {
            "prompt": "Who was the first Indian to win a Nobel Prize?",
            "options": ["C. V. Raman", "Mother Teresa", "Rabindranath Tagore", "Amartya Sen"],
            "answer": "C"
        },
        {
            "prompt": "The classical dance 'Bharatanatyam' originated from which state?",
            "options": ["Kerala", "Andhra Pradesh", "Tamil Nadu", "Karnataka"],
            "answer": "C"
        },
        {
            "prompt": "Which is the highest mountain peak in India?",
            "options": ["K2 (Godwin Austen)", "Nanda Devi", "Kangchenjunga", "Mount Everest"],
            "answer": "C"
        },
        {
            "prompt": "The 'White Revolution' is associated with an increase in the production of?",
            "options": ["Fish", "Eggs", "Cotton", "Milk"],
            "answer": "D"
        },
        {
            "prompt": "Who is known as the 'Iron Man of India'?",
            "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose"],
            "answer": "C"
        },
        {
            "prompt": "The Parliament of India consists of the President and which two houses?",
            "options": ["Lok Sabha and Rajya Sabha", "Vidhan Sabha and Vidhan Parishad", "House of Commons and House of Lords", "Senate and House of Representatives"],
            "answer": "A"
        },
        {
            "prompt": "Which is the largest freshwater lake in India?",
            "options": ["Dal Lake", "Wular Lake", "Chilika Lake", "Vembanad Lake"],
            "answer": "B"
        },
        {
            "prompt": "The Harappan civilization flourished along the banks of which river?",
            "options": ["Ganges", "Yamuna", "Indus", "Brahmaputra"],
            "answer": "C"
        },
        {
            "prompt": "What is the national bird of India?",
            "options": ["Peacock", "Parrot", "Pigeon", "Crow"],
            "answer": "A"
        },
        {
            "prompt": "Which state has the longest coastline in India?",
            "options": ["Maharashtra", "Kerala", "Gujarat", "Andhra Pradesh"],
            "answer": "C"
        },
        {
            "prompt": "Who was the architect of the Indian Constitution?",
            "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Dr. B. R. Ambedkar", "Sardar Patel"],
            "answer": "C"
        },
        {
            "prompt": "When is National Science Day celebrated in India?",
            "options": ["28th February", "15th August", "26th January", "2nd October"],
            "answer": "A"
        },
        {
            "prompt": "The famous Sun Temple is located in which state?",
            "options": ["Gujarat", "Odisha", "Tamil Nadu", "Rajasthan"],
            "answer": "B"
        },
        {
            "prompt": "Who was the last Mughal emperor of India?",
            "options": ["Akbar", "Aurangzeb", "Shah Jahan", "Bahadur Shah Zafar"],
            "answer": "D"
        },
        {
            "prompt": "What is the national tree of India?",
            "options": ["Neem Tree", "Banyan Tree", "Mango Tree", "Peepal Tree"],
            "answer": "B"
        },
        {
            "prompt": "The 'Chipko movement' was a social movement aimed at:",
            "options": ["Protecting women's rights", "Promoting literacy", "Protecting trees and forests", "Eradicating poverty"],
            "answer": "C"

        },
        {
            "prompt": "Which Indian state is famous for its backwaters?",
            "options": ["Goa", "Kerala", "Tamil Nadu", "Karnataka"],
            "answer": "B"
        },
        {
            "prompt": "Who gave the slogan 'Jai Jawan Jai Kisan'?",
            "options": ["Atal Bihari Vajpayee", "Indira Gandhi", "Lal Bahadur Shastri", "Jawaharlal Nehru"],
            "answer": "C"
        },
        {
            "prompt": "The ruins of Hampi, a UNESCO World Heritage Site, are located in which state?",
            "options": ["Andhra Pradesh", "Telangana", "Karnataka", "Tamil Nadu"],
            "answer": "C"
        },
        {
            "prompt": "How many states are there in India?",
            "options": ["27", "28", "29", "30"],
            "answer": "B"
        },
        {
            "prompt": "Which is the southern-most tip of mainland India?",
            "options": ["Indira Point", "Kanyakumari", "Rameswaram", "Point Calimere"],
            "answer": "B"
        },
        {
            "prompt": "The sport of 'Polo' is said to have originated in which Indian state?",
            "options": ["Rajasthan", "Manipur", "Punjab", "Haryana"],
            "answer": "B"
        },
        {
            "prompt": "What is the minimum age to be the President of India?",
            "options": ["25 years", "30 years", "35 years", "40 years"],
            "answer": "C"
        },
        {
            "prompt": "The Khajuraho temples are located in which state?",
            "options": ["Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Maharashtra"],
            "answer": "B"
        },
        {
            "prompt": "Who was the first Indian woman to climb Mount Everest?",
            "options": ["Arunima Sinha", "Premlata Agarwal", "Bachendri Pal", "Santosh Yadav"],
            "answer": "C"
        },
        {
            "prompt": "Which is the largest river island in the world, located in India?",
            "options": ["Majuli", "Havelock Island", "Diu Island", "Munroe Island"],
            "answer": "A"
        },
        {
            "prompt": "The film 'Lagaan' was nominated for an Oscar in which category?",
            "options": ["Best Director", "Best Actor", "Best Foreign Language Film", "Best Picture"],
            "answer": "C"
        },
        {
            "prompt": "The 'Valley of Flowers' National Park is located in which state?",
            "options": ["Himachal Pradesh", "Jammu and Kashmir", "Uttarakhand", "Sikkim"],
            "answer": "C"
        },
        {
            "prompt": "Who is known as the 'Nightingale of India'?",
            "options": ["Lata Mangeshkar", "Sarojini Naidu", "M. S. Subbulakshmi", "Asha Bhosle"],
            "answer": "B"
        },
        {
            "prompt": "The Indian Premier League (IPL) is a professional league for which sport?",
            "options": ["Hockey", "Football", "Kabaddi", "Cricket"],
            "answer": "D"
        },
        {
            "prompt": "What is the name of India's first mission to Mars?",
            "options": ["Chandrayaan-1", "Gaganyaan", "Mangalyaan", "Aditya-L1"],
            "answer": "C"
        },
        {
            "prompt": "In which city is the Golden Temple located?",
            "options": ["Ludhiana", "Chandigarh", "Amritsar", "Patiala"],
            "answer": "C"
        },
        {
            "prompt": "Which of these languages is NOT listed in the Eighth Schedule of the Indian Constitution?",
            "options": ["Sanskrit", "Nepali", "English", "Konkani"],
            "answer": "C"
        },
        {
            "prompt": "Who was the first Indian in space?",
            "options": ["Kalpana Chawla", "Sunita Williams", "Rakesh Sharma", "Ravish Malhotra"],
            "answer": "C"
        },
        {
            "prompt": "The Gir National Park in Gujarat is famous for which animal?",
            "options": ["Bengal Tiger", "One-horned Rhinoceros", "Asiatic Lion", "Elephant"],
            "answer": "C"
        },
        {
            "prompt": "Who was the founder of the Maurya Empire?",
            "options": ["Ashoka", "Bindusara", "Chandragupta Maurya", "Samudragupta"],
            "answer": "C"
        },
        {
            "prompt": "The festival of 'Bihu' is predominantly celebrated in which state?",
            "options": ["West Bengal", "Odisha", "Assam", "Mizoram"],
            "answer": "C"
        },
        {
            "prompt": "The historic 'Dandi March' led by Mahatma Gandhi was a protest against:",
            "options": ["Salt Tax", "Jallianwala Bagh Massacre", "Rowlatt Act", "Partition of Bengal"],
            "answer": "A"
        },
        {
            "prompt": "Which city is home to the headquarters of the Reserve Bank of India (RBI)?",
            "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
            "answer": "B"
        },
        {
            "prompt": "The 'Charminar' is a famous monument located in which city?",
            "options": ["Delhi", "Agra", "Hyderabad", "Lucknow"],
            "answer": "C"
        },
        {
            "prompt": "Who was the first Indian to win an individual Olympic gold medal?",
            "options": ["Leander Paes", "Karnam Malleswari", "Abhinav Bindra", "Neeraj Chopra"],
            "answer": "C"
        },
        {
            "prompt": "Which country shares the longest land border with India?",
            "options": ["China", "Pakistan", "Bangladesh", "Nepal"],
            "answer": "C"
        },
        {
            "prompt": "What is the national motto of India?",
            "options": ["Vande Mataram", "Jai Hind", "Satyameva Jayate", "Inquilab Zindabad"],
            "answer": "C"
        },
        {
            "prompt": "The 'Kuchipudi' dance form originated in which state?",
            "options": ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
            "answer": "D"
        },
        {
            "prompt": "Who directed the critically acclaimed film 'Pather Panchali'?",
            "options": ["Raj Kapoor", "Guru Dutt", "Satyajit Ray", "Bimal Roy"],
            "answer": "C"
        },
        {
            "prompt": "Where is the Indian Military Academy (IMA) located?",
            "options": ["Pune", "Dehradun", "Delhi", "Hyderabad"],
            "answer": "B"
        },
        {
            "prompt": "The tropic of cancer passes through how many Indian states?",
            "options": ["6", "7", "8", "9"],
            "answer": "C"
        },
        {
            "prompt": "What is the national fruit of India?",
            "options": ["Banana", "Apple", "Guava", "Mango"],
            "answer": "D"
        },
        {
            "prompt": "Who wrote the famous book 'The Discovery of India'?",
            "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "A. P. J. Abdul Kalam"],
            "answer": "B"
        },
        {
            "prompt": "The 'Nalanda University', an ancient center of learning, was located in which modern-day state?",
            "options": ["Uttar Pradesh", "Bihar", "Odisha", "West Bengal"],
            "answer": "B"
        },
        {
            "prompt": "Who was the first Sikh Prime Minister of India?",
            "options": ["Giani Zail Singh", "Manmohan Singh", "Harkishan Singh Surjeet", "Parkash Singh Badal"],
            "answer": "B"
        },
        {
            "prompt": "The 'Gateway of India' is located in which city?",
            "options": ["New Delhi", "Kolkata", "Chennai", "Mumbai"],
            "answer": "D"
        },
        {
            "prompt": "Which state is the largest producer of tea in India?",
            "options": ["Kerala", "Karnataka", "West Bengal", "Assam"],
            "answer": "D"
        },
        {
            "prompt": "Who is known as the 'Missile Man of India'?",
            "options": ["C. V. Raman", "Homi J. Bhabha", "A. P. J. Abdul Kalam", "Vikram Sarabhai"],
            "answer": "C"
        },
        {
            "prompt": "In which year was the first general election held in India?",
            "options": ["1947", "1950", "1952", "1955"],
            "answer": "C"
        },
        {
            "prompt": "The 'Hornbill Festival' is celebrated in which state?",
            "options": ["Mizoram", "Meghalaya", "Nagaland", "Arunachal Pradesh"],
            "answer": "C"
        },
        {
            "prompt": "Which planet is India's 'Mangalyaan' mission studying?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "B"
        },
        {
            "prompt": "The language 'Dogri' is primarily spoken in which region?",
            "options": ["Sikkim", "Goa", "Lakshadweep", "Jammu"],
            "answer": "D"
        },
        {
            "prompt": "Who was the first woman President of India?",
            "options": ["Indira Gandhi", "Sonia Gandhi", "Pratibha Patil", "Droupadi Murmu"],
            "answer": "C"
        },
        {
            "prompt": "The Jallianwala Bagh massacre took place in which city?",
            "options": ["Lahore", "Delhi", "Amritsar", "Meerut"],
            "answer": "C"
        },
        
        {
            "prompt": "Who is the Father Of Nation?",
            "options": ["Lahore", "Delhi", "Mahatama Gaundhi", "Meerut"],
            "answer": "C"
        }, 
        {
            "prompt": "The 'Odissi' classical dance originated from which state?",
            "options": ["West Bengal", "Andhra Pradesh", "Odisha", "Bihar"],
            "answer": "C"
        },
        {
            "prompt": "Which Indian cricketer was the first to score 10,000 runs in Test cricket?",
            "options": ["Sachin Tendulkar", "Kapil Dev", "Sunil Gavaskar", "Rahul Dravid"],
            "answer": "C"
        },
        {
            "prompt": "What is the national aquatic animal of India?",
            "options": ["Shark", "River Dolphin", "Crocodile", "Blue Whale"],
            "answer": "B"
        },
        {
            "prompt": "The 'Konark Sun Temple' is dedicated to which deity?",
            "options": ["Vishnu", "Shiva", "Brahma", "Surya (The Sun God)"],
            "answer": "D"
        },
        {
            "prompt": "Who was the first female ruler of the Delhi Sultanate?",
            "options": ["Noor Jahan", "Chand Bibi", "Razia Sultan", "Mumtaz Mahal"],
            "answer": "C"
        },
        {
            "prompt": "Which Indian state is known as the 'Land of Five Rivers'?",
            "options": ["Haryana", "Punjab", "Gujarat", "Uttar Pradesh"],
            "answer": "B"
        },
        {
            "prompt": "In which year did India win its first Cricket World Cup?",
            "options": ["1979", "1983", "1987", "2011"],
            "answer": "B"
        },
        {
            "prompt": "The 'Elephanta Caves' are located near which major city?",
            "options": ["Chennai", "Kolkata", "Delhi", "Mumbai"],
            "answer": "D"
        },
        {
            "prompt": "Who founded the 'Brahmo Samaj' in 1828?",
            "options": ["Swami Vivekananda", "Dayananda Saraswati", "Raja Ram Mohan Roy", "Ishwar Chandra Vidyasagar"],
            "answer": "C"
        },
        {
            "prompt": "Which is the smallest state in India by area?",
            "options": ["Sikkim", "Goa", "Tripura", "Nagaland"],
            "answer": "B"
        },
        {
            "prompt": "What is the name of India's highest military decoration for valour?",
            "options": ["Ashok Chakra", "Maha Vir Chakra", "Param Vir Chakra", "Kirti Chakra"],
            "answer": "C"
        }
    ]

    # Call the function to run the quiz with the new set of questions
    run_quiz(india_gk_questions)