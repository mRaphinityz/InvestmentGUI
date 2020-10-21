# Example from pages 276 - 277

# GUI based version of the investment.py application from Chapter 3

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
    # An investment calculator that demostrates the us of a multi-line text area
    def __init__(self):
        # Sets up the window and the widgets
        EasyFrame.__init__(self, title = "Investment Calculator")
        # Add the label components
        self.addLabel(text = "Initial amount", row = 0, column = 0)
        self.addLabel(text = "Number of years", row = 1, column = 0)
        self.addLabel(text = "Interest rate in %", row = 2, column = 0)
        #  Add the entry field components
        self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
        self.period = self.addIntegerField(value = 0, row = 1, column = 1)
        self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
        # Add the text area component
        self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
        # Add the button component
        self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
    
    # Event handling method
    def compute(self):
        # Computes the investment schedule based on the inputs and outputs the schedule
        startBalance = self.amount.getNumber()
        years = self.period.getNumber()
        rate = self.rate.getNumber() / 100

        # If any input is a zero, have the function do nothing
        if startBalance == 0 or rate == 0 or years == 0:
            return

        # initialize the acculator variable for the interset
        totalInterest = 0.0

        # set the header for the table
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")

        # compute and append the results for each year
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest
            # end of the for loop

            # display the totals for the entire investment period
            result += "Ending balance: $%0.2f\n" % endBalance
            result += "Total interest earned: $%0.2f\n" % totalInterest

            # Output the result variable while preserving read-only status
            self.outputArea["state"] = "normal"
            self.outputArea.setText(result)
            self.outputArea["state"] = "disabled"

# Definition
def main():
    TextAreaDemo().mainloop()


# Global call to the main() function
main()
