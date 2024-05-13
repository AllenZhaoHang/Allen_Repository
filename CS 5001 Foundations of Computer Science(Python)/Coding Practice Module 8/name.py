'''
    Write a class called Name that represents
    a person's full name consisting of a first name
    and a last name. Your class should also store a
    nick name for the person
    Hang Zhao
    10/22/2023
'''


class Name:
    '''
    class Name
    Attributes: first name, last name, nick name
    Methods: get_first_name(), get_last_name(), get_full_name(),
    set_nick_name(nick_name), get_nick_name()
    '''

    def __init__(self, first_name, last_name):
        # if not isinstance(first_name, str) or not isinstance(last_name, str):
        #     raise ValueError("First name and last name must be strings.")
        # if not first_name or not last_name:
        #     raise ValueError("First name and last name must not be empty.")
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = first_name

    def get_first_name(self):
        '''get first name'''
        return self.first_name

    def get_last_name(self):
        ''' get last name '''
        return self.last_name

    def get_full_name(self):
        ''' get full name '''
        return f"{self.first_name} {self.last_name}"

    def set_nick_name(self, nick_name):
        '''set nick name'''
        if not isinstance(nick_name, str):
            raise ValueError("Nick name must be a string.")
        if not nick_name:
            raise ValueError("Nick name must not be empty.")
        self.nick_name = nick_name

    def get_nick_name(self):
        '''get nick name'''
        return self.nick_name

    def __str__(self):
        '''
        Method -- returns a string that represents this coffee
        Parameters:
           self -- the current object
        '''
        output = self.first_name + ' "' + self.nick_name + \
            '" ' + self.last_name
        return output
