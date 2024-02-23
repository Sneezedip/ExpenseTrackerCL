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
