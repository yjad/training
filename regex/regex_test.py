import re

"""
------------------------------------------------------------------------------------------------------------------
Identifiers	                Modifiers	                        White space characters	        Escape required
------------------------------------------------------------------------------------------------------------------
\d= any number (a digit)	\d represents a digit.Ex: \d{1,5}   \n = new line	                . + * ? [] $ ^ () {} | \
                            it will declare any number in a row 
                            with length between 1 to 5 like 424,444,545 34567 etc.	  
                            matching a number from 0 to 255. The regex [0-9] matches single-digit numbers 0 to 9. [1-9][0-9] matches double-digit numbers 10 to 99. That’s the easy part. Matching the three-digit numbers is a little more complicated, since we need to exclude numbers 256 through 999. 1[0-9][0-9] takes care of 100 to 199. 2[0-4][0-9] matches 200 through 249.
                            \d[0]: any digit followed by zero
\D= anything but a number 
(a non-digit)	            + = matches 1 or more	            \s= space	
\s = space (tab,space,newline etc.)	
                            ? = matches 0 or 1	                \t =tab	
\S= anything but a space	* = 0 or more	                    \e = escape	
\w = letters ( Match alphanumeric character, including "_")	
                            $ match end of a string	            \r = carriage return	
\W =anything but letters ( Matches a non-alphanumeric character excluding "_")	
                            ^ match start of a string	        \f= form feed	
. = anything but letters (periods)	
                            | matches either or x/y	            -----------------	
\b = any character except for new line	
                            [] = range or "variance"	        ----------------	
\.	                        {x} = this amount of preceding code	-----------------	
                            ^ matches only at the beginning of the string, and $ matches only at the end of the string
"""

p = re.compile("Yahia Jad")
print (p.match('Y')
