# coffee-chatbot
I created a python chatbot that Starbucks users can text to place an order + help cut wait time of a normal coffee. 

intention: Current wait time @Starbucks is 4.5 minutes. With the chatbot, it can be ~ 1.5 minutes (2.4x faster). 

features(current): users can choose size, plastic or personal cup, type of drink, milk w/drink. 

features (future): users will order products other than coffee, leave a tip through chatbot, schedule a specific pick-up time, reserve a seat on location, etc. 

market-market scale (verticalization): e-commerce companies like amazon or brick-and-mortar like costco can add this offering. I can increase the feature possibilities on the chatbot so if an Amazon user wants to see an image/video of a product, that can be sent through text. 

# code-walkthrough-key-concepts
functions: I used nested + normal functions in this chatbot. Most of the functions had no parameters but had input, conditionals with calls/returns. 

conditionals: I used conditionals & dialog trees frequently in this chatbot. Line 3 - 11 is the first example. Users are making decisions based on the options available to them. If, else, elif are the computers way of taking their input "decision" data and feeding new options based on their choice. We can have a conversation with the user w/this method. 

input: I used the input command when I wanted the user to give me new information. Line 2 is one example. 

return: I used return when I wanted the code to give a response vs. running through its sub-routine of reviewing code + moving into following steps. 

recursion: I learned that this is when a function calls itself. Line 59 is an example of this. The function is calling itself. 

string concatenation: I used string concatenation to connect variables to strings, forming a sentence for the user. 
