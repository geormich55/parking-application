# parking-application
A parking application in Python as a matter of a test for OTS company
Here I am listing the Python code I wrote and I will also attach it separately as one
excel file with the tables I ended up using for my solution.

As you will see it is simple and redundant with simple commands and few libraries.
I wanted to use pandas or Numpy but in the end I found those to be more useful when you have
a ready dataset and you want to break it into pieces and you want to extract tables from it.
So I just used two-dimensional arrays which are essentially dynamic lists
memory commitment.

I have an infinite while loop that ends when the user selects it with the corresponding option.
Also a while inside that only checks the day and if it changes it exits.
It's in as long as the day doesn't change..

I used the datetime function from which I got only the day for the comparison in the loop.
Also, as you will see, at the end I print out the cost and length of stay on the sign
minutes in the parking lot for all 3 types of vehicles (passenger, truck or bus) but only these
who come in and out on the same day because that's what I understood from the pronunciation that is being asked for.
That is, although the algorithm, as you will see, works even if vehicles enter and leave the parking lot any number of times. only one vehicle leaves I only print what is requested for vehicles entering and leaving on the same day. Also, since I'm only interested in each loop in the while where it's for each day separately, all the tables I use are emptied since I'm not interested in whether vehicles entered the previous days and left today, nor if vehicles entered today and exited in the following days.


So every day the tables are filled with the cars that entered, with the cars that left and with the
cars that entered and exited and I export license plate, cost and length of stay per passenger
in order, per truck in order and per bus in order only for those vehicles which
they were in and out the same day.

For the cost, the table proposed to us with the costs was clearly used.
I have also rounded the seconds to the dwell and calculate the dwell time in
minutes.

The board is also a few minutes old.
Of course this works depending on the length it gets from the datetime library which
I convert to string so it takes some time to increase the cost above 0.

Finally for the inside while-loop as I said I only see the day from the datetime while inside the inside
while-loop I only take the time and thus see which car entered first, which second, etc. and which
it came out first, second, etc., since it will be the same day, month, year, then
it is enough to compare only the hours, minutes and seconds to calculate output time - time
input so I can calculate the cost as well.

Finally, I would say that under normal circumstances I would pull from some API for each car the license plates and
the kind based on what I said in questions 1 and 2 or would I use some library like
the ones I mentioned above with some scripts that I would call for each car so that I have
license plate-number, type of car-type of vehicle, time of entry and time of exit.
In the example I implemented, however, I consider that the user enters them with an input that is requested
and I didn't call any API, for example, to get this data for each car and
use in my algorithm.

I have 7 tables with 2 columns and I rows for each type of vehicle passenger, truck or bus.
So it's 7*3=21 tables in total.

Car_plate_entry: in the first column is a pointer to the entry order of the vehicle, common to
all input tables by car type and in the second column its license plate

Car_date_entry: in the first column is a pointer to the entry order of the vehicle, common to
all entry tables by car type and in the second column the entry date
which finally as I said I kept the entry time of since the loop in while is per day for
reasons of simplicity

Car_plate_exit: in the first column is a pointer to the exit row of the vehicle, common to
all the cost tables by car type and in the second column its license plate

Cat_date_exit: in the first column is an index with the exit order of the vehicle, common to all
the exit tables by type of car and in the second column the exit date of which
finally as I said I kept the output time since the loop in while is per day for reasons
simplicity

Car_duration: in the first column is a pointer with the exit order of the vehicle, common to all
the expense tables by type of car and in the second column the length of stay of each
vehicle left the parking lot during the day in minutes

Car_cost: in the first column is an index with the output order of the vehicle, common to all of them
expense tables by type of car and in the second column the cost of staying for each vehicle
in the parking lot in euros

Car_plate_entry_exit: in the first column is an index with the exit row of the vehicle, common
in all cost tables by car type and in the second column the number plate of each
of a vehicle that entered and left the parking lot on the same day as these vehicles, their details
we are already looking

I loop through each day and see if the exit sign is equal to the exit sign and
the exit date is greater than the entry date (in case a car
entered and exited more than 1 time) then I enter in a table the cars that entered and exited,
the length of stay by subtracting exit time-entry time for each vehicle separately and the
cost.
Finally, I do this 3 times for the 3 types of vehicle.

Finally to say that I used Pycharm Editor 2020.2 to run the code and used
respectively some Python interpreter.
Since the code doesn't look good here, and for run purposes I will send it separately as I said
Python file.
In my code I used neither classes nor objects. Simply and only
arrays (two-dimensional lists) with dynamic memory allocation.
