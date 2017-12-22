import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton

class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('Simple example 1')
        self.mainmenu = [
            {'File': [
                {'Open': self.__openEvent}
            ]}]

                #Definition of the forms fields
        self._firstname     = ControlText('First name', 'Default value')
        self._middlename    = ControlText('Middle name')
        self._lastname      = ControlText('Lastname name')
        self._fullname      = ControlText('Full name')
        self._button        = ControlButton('Press this button')

    def __openEvent(self):
        pass

#Execute the application
if __name__ == "__main__":   pyforms.start_app(SimpleExample1 )
