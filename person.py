class OwnerPerson:
    """
    Information about the owner, including the name, city of residence,
    native language of speech, the language being studied (for text translations)
    """

    __name = ""
    __home_city = ""
    __native_language = ""
    __target_language = ""

    def set_name(self, string):
        '''
        This method will set name of person
        :param string: this variable will be name
        :return: __name
        '''

        self.__name = string
        return self.__name

    def set_home_city(self, string):
        '''
        This method will set home city of person
        :param string: this variable will be home city
        :return: __home_city
        '''

        self.__home_city = string
        return self.__home_city

    def set_native_language(self, string):
        '''
        This method will set native language of person.
        :param string: This variable will be native language
        :return: __native_language
        '''

        self.__native_language = string
        return self.__native_language

    def set_target_language(self, string):
        '''
        This method will set target language of person.
        :param string: This variable will be target language
        :return: __target_language
        '''

        self.__target_language = string
        return self.__target_language

    # getters
    def get_name(self):
        '''
        This method will get name of person.
        :return: __name
        '''

        return self.__name

    def get_home_city(self):
        '''
        This method will get home city of person.
        :return: __home_city
        '''

        return self.__home_city

    def get_native_language(self):
        '''
        This method will get native language of person.
        :return: __speech_language
        '''

        return self.__native_language

    def get_target_language(self):
        '''
        This method will get target language of person.
        :return: __recognition_language
        '''

        return self.__target_language
