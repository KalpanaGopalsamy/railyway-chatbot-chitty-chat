from nltk.chat.util import Chat, reflections
pairs = [
        [
        r"hai|hi|hey|hello",
            ["hai frnd",]
        ],
        [
        r"how are you|hw r u|hru",
            ["I'm doing good?",]
        ],
        [
        r"my name is (.*)|i'm(.*)",
            ["tell me(.*), what is your doubt?",]
        ],
        [
        r"what is your name|how can i call you?",
            ["My name is chitty chat and I'm a chatbot?",]
        ],
        [
        r"(.*) tickets ?",
            ["Train ticket booking allows the travelers to seekers a confirmed birth a selected class of a train?",]
        ],
        [
        r"what are the source and destination?",
            ["There are many point to point trains are available are\nChennai-Bangalore\nCuddalore-Chennai\nPondicherry-Coimbatore\nMumbai-Chennai?",]
        ],
        [
        r"how many (.*) can be booked in a single ticket/transaction?",
            ["A maximum of 6 passenger for general and upto 4 passenger for tatkal?",]
        ],
        [
        r"can bulk booking be done through IRCTC?",
            ["No. Bulk booking cannot be done on the internet?",]
        ],
        [
        r"the name of the ticket is incorrect. How do i get it corrected?",
            ["It can’t be done once the ticket is reserved. You need to manually cancel the ticket and rebook again?",]
        ],
        [
        r"how are payment made for online reservation?",
            ["the payment modes are availabe are credit card, debit card, mobile/net banking, EMI/cash card?",]
        ],
        [
        r"what is a PNR?",
            ["PNR - Passenger Name Record is an unique number that recognizes your booking?",]
        ],
        [
        r"what is use of PNR|pnr?",
            ["PNR is utilized to get the Confirmed or Waitlisted status of your booking along with the coach and seat numbers?",]
        ], 
        [
        r"I would like to book tickets|whats the procedure to book tickets|what do you recommend?|could i get more information about booking",
        ["Train ticket booking allows the travelers to seek a confirmed berth in the selected class of a train.\nThere are two ways of booking train tickets: through railway station ticket counters or online train ticket booking.\nUnique PNR (Passenger Name Record) is generated against every ticket booked?",]
        ],
        [   
        r"when are you guys open|what are your hours|hours of operations?",
        ["we are open 7am-6pm monday-friday?",]
        ],
        [
        r"how to cancel my ticket|what are the procedure to cancel the ticket",
        ["E-Tickets can be cancelled on the internet at this website till Chart preparation of the train. Cancellations are not allowed at face to face Railway Counters.\nIf the user wishes to cancel his e-Ticket, he can do so till the time of chart preparation for the train?",]
        ],
        [
        r"what is the procedure to refund my payment|how can i refund my ticket amount|how many day before i need to",
        ["Go to www.irctc.co.in and go to 'Booked Tickets' link.\nSelect the ticket to be cancelled by selecting the passengers to be cancelled.\nThis cancellation will be confirmed online and the refund would be credited back to the account used for booking,\nafter deduction of applicable cancellation charges?",]
        ],
        [
        r"who are all having concessions|is there any special concession for booking tickets",
        ["These facilites are extended to men who are a minimum of 60yrs and women of minimum 58yrs of age.\nThere are granted concession in fares of all classes of train the concession is 40% of the fare for men and 50% \nof the fare for women?",]
        ],
        [
        r"bye",
            ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chitty():
        print("Hi, I'm Chitty chat and I chat a lot ;)\nPlease type lowercase English language to start a conversation. Type bye to leave ") #default message at the start
        chat = Chat(pairs, reflections)
        chat.converse()
if __name__ == "__main__":
    chitty()