class StaticMethods():
    @staticmethod
    def ValidInteger(prompt:str,max:int,min=0,notify=False,notify_message="Out Limits",notify_Exception=False,notify_message_Exception="Only Integer Accepted."):
        """
        Prompts a input that only returns integer, if user doesn't input an integer this method will only notify if notify is True.
        """
        while True:
            try:
                Response = int(input(prompt))
                if Response >= min and Response <= max : return Response
                else: 
                    if notify: print(notify_message)
            except ValueError:
                if notify_Exception: print(notify_message_Exception)
    @staticmethod
    def Centered(phrase):
        """
        Returns a phrase in the middle of the shell.
        """
        return "{:^50}".format(phrase)
    def CustomPosition(position:int,phrase):
        """
        Returns a phrase in any X position given.
        """
        return "{:^{}}".format(phrase,position)
