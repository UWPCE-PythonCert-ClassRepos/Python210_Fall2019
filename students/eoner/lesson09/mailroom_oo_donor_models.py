

class donor():
    """Class that contains donor name and donations """
    def __init__(self, name, initial_donations=None):
        """Initialize classs with name and list of dantons"""
        self.name = name
        self.donations = initial_donations

    def __repr__(self):
        """returns representation of the donor name and list of donations"""
        return str(self.name + ", " + str(self.donations)) 

    def add_donation(self, donation):
        """append to donation list"""
        if type(self.donations) is not list:
            self.donations = []
        self.donations.append(donation)
    
    def average_donation(self):
        """calculates average of donations"""
        return sum(self.donations)/len(self.donations)

    def total_donations(self):
        """calculates total of donations"""
        return sum(self.donations)

    def send_last_donation_email(self):
        """returns a thank you string with donors name and last donation"""
        if type(self.donations) is not list:
            raise Exception( "no donations in the list")
        else:
            ty_dic = {"name": self.name, "last_donation": self.donations[-1]}
            ty_body = '\n'.join(('Heyyyy... {name},\n',
            'Thanks for the ${last_donation:.2f} sucka!\n'
            'Keep sending that money, though\n'
            '                  OK, BAIIII!'))
            output = ty_body.format(**ty_dic)
            return self.name,output

class charity():
    """ Chairty Object keeps track of donor objects ina dictionary"""
    
    def __init__(self,Name):
        """A charity that initiliazes with name and empty donor dic"""
        self.CharityName=Name
        self.Donors={}

    def __repr__(self):
        """returns representation of the donor name and list of donations"""
        return self.CharityName

    def add_donor(self, DonorName, DonationList):
        """add the donor to dictionary to track, create the donor via donor class"""
        self.Donors[DonorName] = donor(DonorName, DonationList)

    def list_donors(self):
        """return a list of donors"""
        return list(self.Donors.keys())
    
    def create_report(self):
        """Create a report for donations, return data as a list"""
        #sort db in order by total donation
        db = sorted(self.Donors.items(), key=lambda x: x[1].total_donations(), reverse=True)
        # build header line for report
        header = f'{"Donor Name":25}{"| Total Given":15}{"| Num Gifts":>15}{ "| Average Gift":>20}'
        underline = '-'*len(header)
        data = [(f'{(db[i][1].name):20} {(db[i][1].total_donations()):{17}.2f} {(len(db[i][1].donations)):15} {(db[i][1].average_donation()):{20}.2f}')for i in range(len(db))]  
        return (header,underline,data)

    def send_letter_all(self):
        """call the donor class method to write each person a letter"""
        #this seems easier to itate over for now"
        db = sorted(self.Donors.items(), key=lambda x: x[1].total_donations(), reverse=True)
        return [db[i][1].send_last_donation_email()for i in range(len(db))]  

#test
NewCharity=charity("Gates")
NewCharity.add_donor("DonaldDuck",[10,20,30])
NewCharity.add_donor("Mickey",[40])
