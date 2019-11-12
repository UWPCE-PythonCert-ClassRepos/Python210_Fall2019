'''
Script: mailroom
Date: 10/28/2019
Dev: Kory Shaffer
'''


donors = {'William Gates, III': (653784.49, 2),  'Mark Zuckerberg': (16396.10, 3), 'Jeff Bezos': (877.33, 1),
          'Paul Allen': (708.42, 3)}

def main(donors):
    user_input(donors)


def user_input(donors):
    selection = ''
    while selection != '3':
        selection = input('\nPlease select type one of following commands: \n' 
                          '1 : Send a single Thank You\n' 
                          '2 : Create a Report\n'
                          '3 : Send letters to all donors\n'
                          '4 : QUIT\n ')
        if selection == '1':
            send_thank_you(donors)
        elif selection == '2':
            create_report(donors)
        elif selection == '3':
            send_all_thank_yous(donors)
        elif selection == '4':
            print('QUITTING')
        else:
            print('INVALID SELECTION')


def send_thank_you(donors):
    donor = ''
    done = False
    while not done:
        donor = input('\n type \'list\' to show list of names or enter donor\'s name: ')
        if donor == 'list':
            for entry in donors:
                print(entry)
        else:
            donation = float(input('How much did %s donate?' % donor))
            if donor not in donors:
                donors[donor] = (donation, 1)
            else:
                donors[donor] = {donor: (donors[donor][0] + donation, donors[donor][1] + 1)}
            print('\n Dear {:s},\n \n Thank you for your generous donation of ${:.2f}. \n \n Kind Regards, \n'
                  ' Local Non-Profit \n'.format(donor, donation))
            done = True

def create_report(donors):
    print('{:<20}|{:^13}|{:^11}|{:^14}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*60)
    for donor in donors:
        print('{:<20} ${:>12.2f}{:>11}  ${:>12.2f}'.format(donor, donors[donor][0], donors[donor][1],
                                                      donors[donor][0]/donors[donor][1]))
def send_all_thank_yous(donors):
            for donor in donors:
                f = open(donor+'_letter.txt', 'w+')
                donation = donors[donor][0]
                f.write('\n Dear {:s},\n \n Thank you for your generous donation of ${:.2f}. \n \n Kind Regards, \n'
                    ' Local Non-Profit \n'.format(donor, donation))

if __name__ == '__main__':
    main(donors)
