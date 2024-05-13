def main():
    '''set demo'''
    event1_attendees = {'Alice', 'Bob', 'Charlie'}
    event2_attendees = {'Charlie', 'Dave', 'Eve'}
    combined_attendees = event1_attendees | event2_attendees
    # event1_attendees.update(event2_attendees)
    # combined_attendees2 = event1_attendees
    combined_attendees.add('Frank')
    combined_attendees.remove('Bob')
    print(combined_attendees)


if __name__ == '__main__':
    main()
