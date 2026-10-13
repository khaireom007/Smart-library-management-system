# 06. Pseudocode

## Add a Book
START  
READ all book fields  
REMOVE surrounding spaces from text fields  
VALIDATE required fields, ISBN, and price  
IF any value is invalid THEN  
&nbsp;&nbsp;DISPLAY validation message  
ELSE IF Book ID already exists THEN  
&nbsp;&nbsp;DISPLAY duplicate message  
ELSE  
&nbsp;&nbsp;CREATE book record as a dictionary  
&nbsp;&nbsp;STORE ISBN components as a tuple  
&nbsp;&nbsp;SET availability to TRUE  
&nbsp;&nbsp;APPEND record to catalogue list  
&nbsp;&nbsp;DISPLAY success message  
END IF  
STOP

## Search by Title
START  
READ search title  
CREATE empty results list  
FOR EACH book in catalogue  
&nbsp;&nbsp;IF title matches without case sensitivity THEN  
&nbsp;&nbsp;&nbsp;&nbsp;APPEND book to results  
&nbsp;&nbsp;END IF  
END FOR  
IF results is empty THEN DISPLAY not-found message  
ELSE DISPLAY every result  
END IF  
STOP

## Display All Records
START  
IF catalogue is empty THEN  
&nbsp;&nbsp;DISPLAY empty-catalogue message  
ELSE  
&nbsp;&nbsp;FOR EACH book in catalogue  
&nbsp;&nbsp;&nbsp;&nbsp;DISPLAY book details  
&nbsp;&nbsp;END FOR  
END IF  
STOP

## Update a Book
START  
READ Book ID  
FIND matching record  
IF record does not exist THEN  
&nbsp;&nbsp;DISPLAY not-found message  
ELSE  
&nbsp;&nbsp;DISPLAY allowed fields  
&nbsp;&nbsp;READ field and new value  
&nbsp;&nbsp;VALIDATE new value  
&nbsp;&nbsp;IF valid THEN update selected field and confirm  
&nbsp;&nbsp;ELSE display validation message  
&nbsp;&nbsp;END IF  
END IF  
STOP

## Unique Categories
START  
CREATE empty category list  
FOR EACH book in catalogue  
&nbsp;&nbsp;APPEND category to list  
END FOR  
CONVERT category list to a set  
SORT unique categories for display  
DISPLAY unique categories  
STOP

## Count Available Books
START  
SET count to zero  
FOR EACH book in catalogue  
&nbsp;&nbsp;IF book is available THEN  
&nbsp;&nbsp;&nbsp;&nbsp;INCREASE count by one  
&nbsp;&nbsp;END IF  
END FOR  
DISPLAY count  
STOP

## Find by Author
START  
READ author name  
CREATE empty matches list  
FOR EACH book in catalogue  
&nbsp;&nbsp;IF author matches without case sensitivity THEN  
&nbsp;&nbsp;&nbsp;&nbsp;APPEND book to matches  
&nbsp;&nbsp;END IF  
END FOR  
IF matches is empty THEN DISPLAY no-match message  
ELSE DISPLAY matches  
END IF  
STOP

## Sort Titles
START  
COPY all titles into a new list  
SORT titles alphabetically without changing catalogue  
DISPLAY sorted titles  
STOP

## Available Books
START  
CREATE empty available list  
FOR EACH book in catalogue  
&nbsp;&nbsp;IF availability is TRUE THEN APPEND book  
END FOR  
IF available list is empty THEN DISPLAY no-available-books message  
ELSE DISPLAY available list  
END IF  
STOP

## Borrow or Return
START  
READ Book ID and action  
FIND book  
IF book is not found THEN DISPLAY not-found message  
ELSE IF action is BORROW THEN  
&nbsp;&nbsp;IF book is already unavailable THEN DISPLAY already borrowed  
&nbsp;&nbsp;ELSE SET availability to FALSE and confirm  
&nbsp;&nbsp;END IF  
ELSE IF action is RETURN THEN  
&nbsp;&nbsp;IF book is already available THEN DISPLAY already available  
&nbsp;&nbsp;ELSE SET availability to TRUE and confirm  
&nbsp;&nbsp;END IF  
END IF  
STOP

## Menu Loop
START  
REPEAT  
&nbsp;&nbsp;DISPLAY menu  
&nbsp;&nbsp;READ choice  
&nbsp;&nbsp;IF choice is valid operation THEN perform operation  
&nbsp;&nbsp;ELSE IF choice is EXIT THEN stop repeating  
&nbsp;&nbsp;ELSE DISPLAY invalid-choice message  
UNTIL choice is EXIT  
DISPLAY closing message  
STOP
