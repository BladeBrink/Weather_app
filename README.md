# Weather_app
This app is designed to give the user current weather information for specific areas

Requirements: 
Requestes
Tkinter 
Json
Pycountry 

Report:

Line 1 - 5: imports the necessary Requirements 

Line 7 - 15: This creates a function which takes in a string as an argument in order to convert a country to country code using the Pycountry Library. It checks if the input is empty to which it notifies the user of the error. Otherwise if not empty it tries to return a country code for the country given. If no country code is able to be give, an error message is shown to the user to notify the user that the country can not be found. 

Line 18 - 37: This code creates the main function to get the weather information. It takes in two arguments, the city searched (from the user) and the country code (from the country code function above). It uses the requests Library to to call an API using an API key given by https://openweathermap.org/. The api takes the city, country code and the api key in order to return results. The results are returned, ordered and assigned accordingly. The function then returns a final list containing the city, country, temperature in Celsius, temperature in Fahrenheit, the icon code (used to fetch the correct image representing the weather) and the description of the weather (eg:cloudy). If it can not execute the code for any reason, the user is notified of an error. 

Line 40 -  47: This creates the search function which is run when the user clicks the search button in the GUI. It gets the user inputs from the entry box for city and country. A country code is assigned by calling the country_to_code() function above. It calls the get weather function to get the weather Information. The last 4 lines is used to display the weather to the user. It assigns the location label, the weather image, the temp labels and the weather labels. All of this is assigned from the final list created above. The image is assigned by using the codes that are received from the API and loading the image with matching code to the bitmap. 

Line 52 -83: This lines simply create the GUI using Tkinter. It creates all the labels, buttons and entry boxes necessary for the app. 

Line 85: Creates the maintop to run the app.
