import sys
import time


data = [
    {
        "Username": "@instagram",
        "Owner": "Instagram",
        "Followers (millions)": 697,
        "Description": "Social media platform",
        "Country": "United States"
    },
    {
        "Username": "@cristiano",
        "Owner": "Cristiano Ronaldo",
        "Followers (millions)": 668,
        "Description": "Footballer",
        "Country": "Portugal"
    },
    {
        "Username": "@leomessi",
        "Owner": "Lionel Messi",
        "Followers (millions)": 510,
        "Description": "Footballer",
        "Country": "Argentina"
    },
    {
        "Username": "@selenagomez",
        "Owner": "Selena Gomez",
        "Followers (millions)": 416,
        "Description": "Musician and actress",
        "Country": "United States"
    },
    {
        "Username": "@kyliejenner",
        "Owner": "Kylie Jenner",
        "Followers (millions)": 392,
        "Description": "Media personality",
        "Country": "United States"
    },
    {
        "Username": "@therock",
        "Owner": "Dwayne Johnson",
        "Followers (millions)": 391,
        "Description": "Actor and professional wrestler",
        "Country": "United States"
    },
    {
        "Username": "@arianagrande",
        "Owner": "Ariana Grande",
        "Followers (millions)": 373,
        "Description": "Musician and actress",
        "Country": "United States"
    },
    {
        "Username": "@kimkardashian",
        "Owner": "Kim Kardashian",
        "Followers (millions)": 354,
        "Description": "Media personality",
        "Country": "United States"
    },
    {
        "Username": "@beyonce",
        "Owner": "Beyoncé",
        "Followers (millions)": 308,
        "Description": "Musician and actress",
        "Country": "United States"
    },
    {
        "Username": "@khloekardashian",
        "Owner": "Khloé Kardashian",
        "Followers (millions)": 300,
        "Description": "Media personality",
        "Country": "United States"
    },
    {
        "Username": "@nike",
        "Owner": "Nike",
        "Followers (millions)": 298,
        "Description": "Sportswear multinational",
        "Country": "United States"
    },
    {
        "Username": "@lilbieber",
        "Owner": "Justin Bieber",
        "Followers (millions)": 292,
        "Description": "Musician",
        "Country": "Canada"
    },
    {
        "Username": "@kendalljenner",
        "Owner": "Kendall Jenner",
        "Followers (millions)": 285,
        "Description": "Media personality",
        "Country": "United States"
    },
    {
        "Username": "@taylorswift",
        "Owner": "Taylor Swift",
        "Followers (millions)": 281,
        "Description": "Musician",
        "Country": "United States"
    },
    {
        "Username": "@natgeo",
        "Owner": "National Geographic",
        "Followers (millions)": 276,
        "Description": "Magazine",
        "Country": "United States"
    }
]


def main():
    score = 0
    animated_print("Welcome to the Higher Lower Game!", delay=0.04)
    animated_print("Guess which Instagram account has more followers.", delay=0.04)
    animated_print("Let's begin!😊", delay=0.04)
    for i, entry in enumerate(data):
        if i == len(data) - 1:
            print(f"game ends here your score is {score}")
            break
        owner = entry.get("Owner", "<unknown>")
        description = entry.get("Description", "")
        location = entry.get("Country", "")
        print(f"Compare A: {owner}, a {description}, from {location}.")
        animated_print("VS", delay=0.1)
        next_entry = data[i+1] if i < len(data) else print(f"game ends here your score is {score}")
        owner2 = next_entry.get("Owner", "<unknown>")
        description2 = next_entry.get("Description", "")
        location2 = next_entry.get("Country", "")
        print(f"Against B: {owner2}, a {description2}, from {location2}.")
        user_choice = input("Who do you think has more followers? Type 'A' or 'B':").strip().upper()

        followers_a = entry.get("Followers (millions)", 0)
        followers_b = next_entry.get("Followers (millions)", 0)
        if user_choice == "A":
            if followers_a > followers_b:
                print("You're right!")
                score += 1
                continue
            else:
                print("You're wrong!")
                print(f"Final score: {score}")
                break
        elif user_choice == "B":
            if followers_b > followers_a:
                print("You're right!")
                score += 1
                continue
            else:
                print("You're wrong!")
                print(f"Final score: {score}")
                break
        else:
            print("Invalid choice. Please type 'A' or 'B'.")
            break   



def animated_print(text, delay=0.05):
    """Print `text` one character at a time with `delay` seconds between characters."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

main()
# def main():
#     """Iterate through `data` and print a concise summary for each entry."""
#     for i, entry in enumerate(data, start=1):
#         owner = entry.get("Owner", "<unknown>")
#         username = entry.get("Username", "")
#         followers = entry.get("Followers (millions)", "?")
#         desc = entry.get("Description", "")
#         country = entry.get("Country", "")
#         print(f"{i}. {owner} ({username}) — {followers}M followers — {desc}, {country}")


# if __name__ == "__main__":
#     main()

