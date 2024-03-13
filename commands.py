class OverwriteCommand:

    def __init__(self,original_information, information, information_type) -> None:
        self.original_information = original_information
        self.information = information
        self.information_type = information_type


    def execute(self) -> any:
        print(f"Insira o(a) novo(a) {self.information_type}")
        self.information = input("{} \r".format(self.original_information))
        
        if len(self.information) > 0:
            return self.information
        else:
            return self.original_information
        