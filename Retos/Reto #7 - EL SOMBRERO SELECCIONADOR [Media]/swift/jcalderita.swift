import Foundation

let questions: [String] = [
    "Moon or Stars?",
    "Left or Right?",
    "Black or White?",
    "Dawn or Dusk?",
    "Forest or River?",
    "If you were attending Hogwarts, which pet would you choose to take with you?",
    "Once every century, the Flutterby bush produces flowers that adopt their scent to attract the unwary. If it lured you, it would smell of",
    "How would you like to be known to history?",
    "Late at night, walking alone down the street, you hear a peculiar cry that you believe to have a magical source. Do you",
    "If you could have any power, which would you choose?",
    "A troll has gone berserk in the Headmaster’s study at Hogwarts. It is about to smash, crush and tear several irreplaceable items and treasures. In which order would you rescue these objects from the troll’s club, if you could?",
    "What kind of instrument most pleases your ear?",
    "What are you most looking forward to learning at Hogwarts?",
    "Which road tempts you most?",
    "Which of the following would you most hate people to call you?",
    "Which would you rather be",
    "After you have died, what would you most like people to do when they hear your name?",
    "A Muggle confronts you and says that they are sure you are a witch or wizard. Do you",
    "You enter an enchanted garden. What would you be most curious to examine first?",
    "Four boxes are placed before you. Which would you try and open?",
    "Given the choice, would you rather invent a potion that would guarantee you",
    "One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill. Now he has come top of the class in Charms, beating you into second place. Professor Flitwick is suspicious of what happened. He draws you to one side after his lesson and asks you whether or not your classmate used a forbidden quill. What do you do?",
    "Which of the following do you find most difficult to deal with?",
    "Which of the following would you most like to study?",
    "Which nightmare would frighten you most?",
    "You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. Do you",
    "Four goblets are placed before you. Which would you choose to drink?"
]

let gryffindorAnswers: [String] = [
    "Stars",
    "Right",
    "Tails",
    "Black",
    "Dawn",
    "Forest",
    "Tabby Cat",
    "A crackling log fire",
    "The Bold",
    "Draw your wand and try to discover the source of the noise?",
    "The power of invisibility.",
    "First, a mysterious handwritten book full of strange runes. Then student records going back 1000 years. Finally, a nearly perfected cure for dragon pox.",
    "The Drum",
    "Secrets about the castle.",
    "The twisting, leaf-strewn path through woods.",
    "Selfish",
    "Praised?",
    "Ask for more stories about your adventures.",
    "Agree, and walk away, leaving them to wonder whether you are bluffing?",
    "The statue of an old wizard with a strangely twinkling eye.",
    "The small pewter box, unassuming and plain, with a scratched message upon it that reads /“I open only for the worthy./”",
    "Glory?",
    "Tell Professor Flitwick that he ought to ask your classmate (and resolve to tell your classmate that if he doesn’t tell the truth, you will).",
    "Loneliness",
    "Ghosts",
    "An eye at the keyhole of the dark, windowless room in which you are locked.",
    "Volunteer to fight?",
    "The golden liquid so bright that it hurts the eye and which makes sunspots dance all around the room."
]

let slytherinAnswers: [String] = [
    "Moon",
    "Left",
    "Tails",
    "Black",
    "Dusk",
    "River",
    "Siamese Cat",
    "The sea",
    "The Great",
    "Draw your wand and stand your ground?",
    "The power to change the past.",
    "First, student records going back 1000 years.Then a mysterious handwritten book full of strange runes. Finally, a nearly perfected cure for dragon pox.",
    "The Violin",
    "Hexes and jinxes",
    "The narrow, dark, lantern-lit alley",
    "Ordinary",
    "Feared?",
    "I don’t care what people think of me after I’m dead; it’s what they think of me while I’m alive that counts.",
    "Agree, and ask whether they’d like a free sample of a jinx?",
    "The bubbling pool, in the depths of which something luminous is swirling.",
    "The gleaming jet black box with a silver lock and key, marked with a mysterious rune that you know to be the mark of Merlin.",
    "Power?",
    "You would not wait to be asked to tell Professor Flitwick the truth. If you knew that somebody was using a forbidden quill, you would tell the teacher before the exam started.",
    "Cold",
    "Vampires",
    "Being forced to speak in such a silly voice that hardly anyone can understand you, and everyone laughs at you.",
    "Suggest that all three of you should fight (without telling the troll)?",
    "The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions."
]

let ravenclawAnswers: [String] = [
    "Moon",
    "Left",
    "Heads",
    "White",
    "Dawn",
    "Forest",
    "Tawny owl",
    "Fresh parchment",
    "The Wise",
    "Withdraw into the shadows to await developments, while mentally reviewing the most appropriate defensive and offensive spells, should trouble occur?",
    "The power to change your appearance at will.",
    "First, a mysterious handwritten book full of strange runes. Then a nearly perfected cure for dragon pox. Finally, student records going back 1000 years.",
    "The Piano",
    "Every area of magic I can.",
    "The cobbled street lined with ancient buildings",
    "Ignorant",
    "Imitated?",
    "Think with admiration of your achievements.",
    "Ask what makes them think so?",
    "The silver-leafed tree bearing golden apples.",
    "The ornate golden casket, standing on clawed feet, whose inscription warns that both secret knowledge and unbearable temptation lie within.",
    "Wisdom?",
    "Tell Professor Flitwick the truth. If your classmate is prepared to win by cheating, he deserves to be found out. Also, as you are both in the same house, any points he loses will be regained by you, for coming first in his place.",
    "Hunger",
    "Goblins",
    "Standing on top of something very high and realizing suddenly that there are no hand- or footholds, nor any barrier to stop you falling.",
    "Attempt to confuse the troll into letting all three of you pass without fighting?",
    "The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds."
]

let hufflepuffAnswers: [String] = [
    "Stars",
    "Right",
    "Heads",
    "White",
    "Dusk",
    "River",
    "Common toad",
    "Home",
    "The Good",
    "Proceed with caution, keeping one hand on your concealed wand and an eye out for any disturbance?",
    "The power of superhuman strength.",
    "First, student records going back 1000 years. Then a nearly perfected cure for dragon pox. Finally, a mysterious handwritten book full of strange runes.",
    "The trumpet",
    "All about magical creatures, and how to befriend/care for them.",
    "The wide, sunny, grassy lane",
    "Cowardly",
    "Liked?",
    "Miss you, but smile.",
    "Tell them that you are worried about their mental health, and offer to call a doctor.",
    "The fat red toadstools that appear to be talking to each other.",
    "The small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking.",
    "Love?",
    "Lie and say you don’t know (but hope that somebody else tells Professor Flitwick the truth).",
    "Being ignored",
    "Trolls",
    "Waking up to find that neither your friends nor your family have any idea who you are.",
    "Suggest drawing lots to decide which of you will fight?",
    "The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums."
]


final class House {
    let name: String
    private(set) var score: Int = 0
    let answers: [String]
    
    init(name: String, answers: [String]) {
        self.name = name
        self.answers = answers
    }
    
    func correctAnswer(idx: Int, answer: String) {
        if answers[idx] == answer {
            score += 1
        }
    }
}

let gryffindor = House(name: "Gryffindor", answers: gryffindorAnswers)
let slytherin = House(name: "Slytherin", answers: slytherinAnswers)
let ravenclaw = House(name: "Ravenclaw", answers: ravenclawAnswers)
let hufflepuff = House(name: "Hufflepuff", answers: hufflepuffAnswers)

let houses = [gryffindor, slytherin, ravenclaw, hufflepuff]

questions.enumerated().forEach { (index, question) in
    let answer = houses.randomElement()!.answers[index]
    print("\(question) - \(answer)")
    houses.forEach { house in
        house.correctAnswer(idx: index, answer: answer)
    }
}

let selection = houses.sorted { first, second in
    first.score > second.score
}.first!.name

print("You are \(selection)")