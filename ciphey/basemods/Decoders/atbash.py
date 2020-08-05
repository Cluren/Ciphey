# community

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry


@registry.register
class Atbash(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        '''
        Takes an encoded string and attempts to decode it according to the Atbash cipher.

            The Atbash cipher is a very simple substitution cipher without a key.
            It operates by replacing every letter in the input by its 'counterpoint'
            in the alphabet. Example: A -> Z, B -> Y, ... , M -> N and vice versa.
        '''
        
        dec = ''
        letters = list('abcdefghijklmnopqrstuvwxyz')
        atbash_dict = {letters[i]:letters[::-1][i] for i in range(26)}

        # Ensure that ciphertext is a string 
        if type(ctext) == str:
            # Normalize the string to all-lowercase letters
            ctext = ctext.lower()
        else:
            return None

        for l in ctext:
            if l in atbash_dict.keys():
                # Match every letter of the input to its atbash counterpoint
                dec += atbash_dict[l]
            else:
                # If the current character is not in the defined alphabet, 
                # just accept it as-is (useful for numbers, punctuation,...)
                dec += l
        return dec

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.1

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return 'atbash'
