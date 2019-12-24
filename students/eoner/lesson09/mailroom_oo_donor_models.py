

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
        header = f'{"Donor Name":25}{"| Total Given":15}{"| Num Gifts":>15}{ "| Average Gift":>20}'
        seperator = "_"*len(header)
        donor_list= [(f'{k:20} {sum(v):{17}.2f} {len(v):15} {(sum(v)/len(v)):{20}.2f}') for k,v in self.Donors.items()]
        return (header,seperator,donor_list)
    


#test
NewCharity=charity("Gates")
NewCharity.add_donor("DonaldDuck",[10,20,30])
NewCharity.add_donor("Mickey",[40])