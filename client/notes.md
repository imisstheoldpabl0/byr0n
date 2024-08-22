# To create a table with each component rendering a part of the table

How to:
1. ```<UserList>``` renders the whole table

2. UserList displays inside of ```<table>```:
    1.1: ```<UserTopComp>```:
        - Renders the top header of the table ```<thead>, <tr>, <th>```
    1.2: ```<UserCards paintCards={paintCards()}>```:
        - Renders the ```paintCards()``` function which returns the element ```<UserCard key={} user_id={} ...>```
        1.2.1 ```<UserCard {user_id, username, ...}>```:
            - Renders the top header of the table ```<tr>, <td>```

3. 
