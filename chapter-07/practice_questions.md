**1)**
re.compile()

**2)**
If normal strings are used then the backslash will be treated as escape chacter. So to 
avoid this issue raw strings are used.

**3)**
The search() returns the match object, span and the matched item.

**4)**
By using group(&nbsp;) or groups(&nbsp;) function.

**5)**
Here, the group(0) covers the entire string (\d\d\d)-(\d\d\d-\d\d\d\d), the group(1) covers
the first part of the string (\d\d\d) and the group(2) covers the second part of the string
(\d\d\d-\d\d\d\d).

**6)**
By using escape characters or backslash. Here, it can be give like \\( , \\..

**7)**
If the regex objects are enclosed or seperated by the parantheses then the findall() 
function return a list of tuples or else it return the list of strings.

**8)**
"|" symbol is generally used to reperesent "or".

**9)**
The first one is to declare a non-greedy match and the second one is to flag an optional 
group.

**10)**
→The + matches one or more of the preceding group.\
&ensp;&ensp;&ensp;&ensp;→The * matches zero or more of the preceding group.

**11)**
{3} tells that the preceding group repeats 3 time whereas {3,5} tells that the preceding
group can repeat any number of time between the range(inclusive) 3 to 5 ie, 3 or 4 or 5.

**12)**
\d&nbsp; -&nbsp; used to represent any numeric character.\
\w&nbsp; -&nbsp; used to represent any letter, numeric character, or the underscore.\
\s&nbsp; -&nbsp; used to represent any space, tab, or newline character.

**13)**
\D&nbsp; -&nbsp; used to represent any non numeric character.\
\W&nbsp; -&nbsp; used to represent any character that is not
 letter, numeric character, or the underscore.\
\S&nbsp; -&nbsp; used to represent any character that is not space, tab, or newline character.

**14)**
The dot-star(.*) is uses greedy mode: It will always try to match as much text as possible. 
where as the dot, star, and question mark(.*?) uses a non-greedy mode: It matchs any and all text in a non-greedy 
fashion. 

**15)**
[0-9a-z]

**16)**
By giving re.IGNORECASE or re.I as second argument to re.compile().

**17)**
The . character looks for any character except the newline character. If re.DOTALL is passed
 as the second argument, then the dot will also include the newline characters.

**18)**
X drummers, X pipers, five rings, X hens

**19)**
re.VERBOSE is used to ignore the whitespaces and is also used to add comments inside the 
regular expression string.

**20)**
re.compile(r'^\d{1,3}(,\d{3})*$')

**21)**
re.compile(r'[A-Z][a-z]*\sNakamoto')

**22)**
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', 
re.IGNORECASE)